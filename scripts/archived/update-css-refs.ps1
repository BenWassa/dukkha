# Update HTML files to use new CSS structure
$basePath = "c:\Users\benjamin.haddon\Documents\dukkha\docs"

# Files in docs/site/ directory (use ../ for CSS paths)
$siteFiles = @(
    "site\recovery.html",
    "site\protocols.html", 
    "site\model.html",
    "site\library.html"
)

# Files in docs/site/protocols/ directory (use ../../ for CSS paths)
$protocolFiles = @(
    "site\protocols\stress-management-protocol.html",
    "site\protocols\sleep-optimization-protocol.html",
    "site\protocols\nutrition-supplementation-protocol.html",
    "site\protocols\mindfulness-awareness-protocol.html",
    "site\protocols\digital-detox-protocol.html"
)

# Update site files
foreach ($file in $siteFiles) {
    $fullPath = Join-Path $basePath $file
    if (Test-Path $fullPath) {
        Write-Host "Updating $file..."
        $content = Get-Content $fullPath -Raw
        $content = $content -replace 'href="../styles\.css"', 'href="../variables.css">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../utilities.css">
    <link rel="stylesheet" href="../print.css" media="print"'
        Set-Content $fullPath $content -NoNewline
    }
}

# Update protocol files
foreach ($file in $protocolFiles) {
    $fullPath = Join-Path $basePath $file
    if (Test-Path $fullPath) {
        Write-Host "Updating $file..."
        $content = Get-Content $fullPath -Raw
        $content = $content -replace 'href="../../styles\.css"', 'href="../../variables.css">
    <link rel="stylesheet" href="../../styles.css">
    <link rel="stylesheet" href="../../utilities.css">
    <link rel="stylesheet" href="../../print.css" media="print"'
        Set-Content $fullPath $content -NoNewline
    }
}

Write-Host "HTML files updated with new CSS structure!"
