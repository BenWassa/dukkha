<#
.SYNOPSIS
    QA script for Project Dukkha.
.DESCRIPTION
    - Checks that every href="#fnN" in docs/site/*.html has a matching id="fnN" in the same file.
    - Optionally validates URLs listed in docs/references_extracted.csv.
.PARAMETER CheckUrls
    If specified, the script will perform network requests to validate all unique URLs in the references CSV.
.EXAMPLE
    # Run anchor/id checks only
    .\scripts\qa_check.ps1
.EXAMPLE
    # Run both anchor/id checks and URL validation
    .\scripts\qa_check.ps1 -CheckUrls
#>
param(
    [switch]$CheckUrls
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop' # Exit on terminating errors

# --- CONFIGURATION ---
$baseDir = $PSScriptRoot
$sitePath = Join-Path $baseDir "..\docs\site"
$csvPath = Join-Path $baseDir "..\docs\references_extracted.csv"
$totalErrors = 0

# --- FUNCTIONS ---
function Write-Color([string]$Message, [string]$Color) {
    if ($Color -eq 'None') {
        Write-Host $Message
    } else {
        Write-Host $Message -ForegroundColor $Color
    }
}

# --- SCRIPT ---
Write-Color 'Project Dukkha — QA Check' 'Cyan'
Write-Color "Checking footnote anchor/id parity in '$($sitePath)'..." 'None'

$siteFiles = Get-ChildItem -Path $sitePath -Filter *.html -File
$anchorErrors = @()

foreach ($f in $siteFiles) {
    $fileName = $f.Name
    $fileContent = Get-Content $f.FullName -Raw
    
    $hrefs = [regex]::Matches($fileContent, 'href="#(fn\d+)"') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique
    $ids = [regex]::Matches($fileContent, 'id="(fn\d+)"') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique
    
    $missingIds = $hrefs | Where-Object { $_ -notin $ids }
    
    if ($missingIds) {
        $anchorErrors += [pscustomobject]@{ File = $fileName; MissingIds = ($missingIds -join ', ') }
        $msg = "[FAIL] '$($fileName)': Missing IDs for -> " + ($missingIds -join ', ')
        Write-Color $msg 'Red'
    } else {
        $msg = "[OK]   '$($fileName)': All footnote anchors match."
        Write-Color $msg 'Green'
    }
}

if ($CheckUrls) {
    Write-Color "`nValidating URLs from '$($csvPath)'..." 'Cyan'
    if (-not (Test-Path $csvPath)) {
        Write-Color "Error: References CSV not found at '$($csvPath)'" 'Red'
        exit 1
    }

    $rows = Import-Csv -Path $csvPath
    $urls = $rows | Where-Object { $_.url -and ($_.url.Trim() -ne '') } | Select-Object -ExpandProperty url -Unique
    $httpErrors = @()
    $checkedCount = 0

    foreach ($u in $urls) {
        $checkedCount++
        $progressMsg = "Checking ({0}/{1}): {2}" -f $checkedCount, $urls.Count, $u
        Write-Host $progressMsg
        
        $status = ''
        try {
            $response = Invoke-WebRequest -Uri $u -Method Head -TimeoutSec 15 -UseBasicParsing
            $status = $response.StatusCode
        } catch [System.Net.WebException] {
            try {
                $response = Invoke-WebRequest -Uri $u -Method Get -TimeoutSec 20 -UseBasicParsing
                $status = $response.StatusCode
            } catch {
                $status = $_.Exception.Message
            }
        } catch {
            $status = $_.Exception.Message
        }

        if (($status -is [int] -and $status -ge 200 -and $status -lt 400) -or ($status -is [string] -and $status -match '200')) {
            Write-Color "  -> OK ($status)" 'Green'
        } else {
            Write-Color "  -> FAIL ($status)" 'Red'
            $httpErrors += [pscustomobject]@{ URL = $u; Status = $status }
        }
        Start-Sleep -Milliseconds 200 # Be polite
    }
} else {
    Write-Color "`nURL checks skipped. Use -CheckUrls to validate." 'Yellow'
}

# --- SUMMARY ---
Write-Color "`n--- Summary ---" 'Cyan'

if ($anchorErrors.Count -gt 0) {
    $totalErrors += $anchorErrors.Count
    Write-Color "Anchor/ID Mismatches: $($anchorErrors.Count) file(s) failed." 'Red'
    $anchorErrors | Format-Table -AutoSize
} else {
    Write-Color 'Anchor/ID Checks: OK' 'Green'
}

if ($CheckUrls) {
    if ($httpErrors.Count -gt 0) {
        $totalErrors += $httpErrors.Count
        Write-Color "URL Validation: $($httpErrors.Count) URL(s) failed." 'Red'
        $httpErrors | Format-Table -AutoSize
    } else {
        Write-Color 'URL Validation: OK' 'Green'
    }
}

if ($totalErrors -gt 0) {
    Write-Color "`nQA check finished with $totalErrors error(s)." 'Red'
    exit 1
} else {
    Write-Color "`nQA check finished successfully." 'Green'
    exit 0
}
