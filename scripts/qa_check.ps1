<#
QA script for Project Dukkha
- Checks that every href="#fnN" in docs/site/*.html has a matching id="fnN" in the same file.
- Optionally validates URLs listed in docs/references_extracted.csv.

Usage:
powershell -ExecutionPolicy Bypass -File .\scripts\qa_check.ps1           # run anchor/id checks only
powershell -ExecutionPolicy Bypass -File .\scripts\qa_check.ps1 -CheckUrls # also validate URLs from docs/references_extracted.csv

This script is safe to run in PowerShell 5.1 (Windows). Network URL checks use Invoke-WebRequest and will be rate-limited.
#>

param(
    [switch]$CheckUrls
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

Write-Host "Project Dukkha — QA check" -ForegroundColor Cyan
Write-Host "Checking footnote anchor/id parity in docs/site/*.html...`n"

$sitePath = Join-Path $PSScriptRoot "..\docs\site"
$siteFiles = Get-ChildItem -Path $sitePath -Filter *.html -File -ErrorAction Stop
$anchorErrors = @()

foreach ($f in $siteFiles) {
    $text = Get-Content $f.FullName -Raw
    $hrefs = [regex]::Matches($text,'href="#(fn\d+)"') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique
    $ids = [regex]::Matches($text,'id="(fn\d+)"') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique

    $missing = $hrefs | Where-Object { $_ -notin $ids }
    if ($missing) {
        $anchorErrors += [pscustomobject]@{
            File = $f.Name
            MissingIds = ($missing -join ', ')
        }
        Write-Host "[FAIL] $($f.Name): missing footnote ids for -> $($missing -join ', ')" -ForegroundColor Red
    }
    else {
        Write-Host "[OK]   $($f.Name): all hrefs matched" -ForegroundColor Green
    }
}

if (-not $CheckUrls) {
    Write-Host "`nURL checks skipped. To run URL validation, re-run with -CheckUrls." -ForegroundColor Yellow
    if ($anchorErrors.Count -gt 0) { exit 2 } else { exit 0 }
}

# URL validation
Write-Host "`nValidating URLs from docs/references_extracted.csv (de-duplicated)..." -ForegroundColor Cyan
$csvPath = Join-Path $PSScriptRoot "..\docs\references_extracted.csv"
if (-not (Test-Path $csvPath)) {
    Write-Host "References CSV not found at $csvPath" -ForegroundColor Red
    if ($anchorErrors.Count -gt 0) { exit 3 } else { exit 4 }
}

$rows = Import-Csv -Path $csvPath
$urls = $rows | Where-Object { $_.url -and ($_.url.Trim() -ne '') } | Select-Object -ExpandProperty url -Unique

$httpErrors = @()
$checked = 0
foreach ($u in $urls) {
    $checked++
    Write-Host "Checking ($checked/$($urls.Count)): $u"
    try {
        # Prefer HEAD to reduce payload, fall back to GET if server rejects HEAD
        $resp = Invoke-WebRequest -Uri $u -Method Head -TimeoutSec 15 -UseBasicParsing -ErrorAction Stop
        $status = $resp.StatusCode
    }
    catch [System.Net.WebException] {
        # Try GET if HEAD failed
        try {
            $resp = Invoke-WebRequest -Uri $u -Method Get -TimeoutSec 20 -UseBasicParsing -ErrorAction Stop
            $status = $resp.StatusCode
        }
        catch {
            $status = $_.Exception.Message
        }
    }
    catch {
        $status = $_.Exception.Message
    }

    if (($status -is [int] -and ($status -ge 200 -and $status -lt 400)) -or ($status -is [string] -and $status -match '200')) {
        Write-Host "  -> OK ($status)" -ForegroundColor Green
    }
    else {
        Write-Host "  -> FAIL ($status)" -ForegroundColor Red
        $httpErrors += [pscustomobject]@{ url = $u; status = $status }
    }

    Start-Sleep -Milliseconds 200 # polite rate-limit
}

Write-Host "`nSummary:" -ForegroundColor Cyan
if ($anchorErrors.Count -gt 0) {
    Write-Host "Anchor/id mismatches: $($anchorErrors.Count) file(s)" -ForegroundColor Red
    $anchorErrors | Format-Table -AutoSize
}
else { Write-Host "Anchor/id checks: OK" -ForegroundColor Green }

if ($httpErrors.Count -gt 0) {
    Write-Host "URL validation failed for $($httpErrors.Count) URL(s):" -ForegroundColor Red
    $httpErrors | Format-Table -AutoSize
    exit 5
}
else { Write-Host "URL checks: OK (all reachable)" -ForegroundColor Green }

exit 0
