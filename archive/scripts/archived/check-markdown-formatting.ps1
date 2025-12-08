# Markdown Formatting Check Script
# Scans HTML files for common Markdown formatting that should be converted to HTML

$htmlFiles = Get-ChildItem "docs\site" -Include "*.html" -Recurse

Write-Host "Checking HTML files for Markdown formatting remnants..." -ForegroundColor Yellow

$issues = @()

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw
    $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "")
    
    # Check for *italic* formatting
    if ($content -match '\*[^*\s][^*]*[^*\s]\*') {
        $issues += "❌ $relativePath : Found *italic* formatting (should be <i>text</i>)"
    }
    
    # Check for **bold** formatting
    if ($content -match '\*\*[^*\s][^*]*[^*\s]\*\*') {
        $issues += "❌ $relativePath : Found **bold** formatting (should be <strong>text</strong>)"
    }
    
    # Check for `code` formatting
    if ($content -match '`[^`\s][^`]*[^`\s]`') {
        $issues += "❌ $relativePath : Found `code` formatting (should be <code>text</code>)"
    }
    
    # Check for markdown headers
    if ($content -match '^[\s]*#{1,6}[\s]') {
        $issues += "❌ $relativePath : Found markdown headers (should be <h1>, <h2>, etc.)"
    }
    
    # Check for markdown bullet points
    if ($content -match '^[\s]*[-*+][\s]') {
        $issues += "❌ $relativePath : Found markdown bullet points (should be <ul><li> structure)"
    }
}

if ($issues.Count -eq 0) {
    Write-Host "✅ All HTML files look good! No Markdown formatting remnants found." -ForegroundColor Green
} else {
    Write-Host "Found $($issues.Count) formatting issue(s):" -ForegroundColor Red
    $issues | ForEach-Object { Write-Host $_ }
    Write-Host "`nPlease convert these to proper HTML formatting." -ForegroundColor Yellow
}

Write-Host "`nFormatting guide:" -ForegroundColor Cyan
Write-Host "*text* → <i>text</i> (italic)"
Write-Host "**text** → <strong>text</strong> (bold)"
Write-Host "`text` → <code>text</code> (inline code)"
Write-Host "# Header → <h1>Header</h1> (heading)"
Write-Host "- Item → <li>Item</li> (list item)"
