Write-Host "=" * 50 -ForegroundColor Yellow
Write-Host "23 KOD DEBUG MODE" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Yellow

Write-Host "`n[1] Checking Python..." -ForegroundColor Green
python --version

Write-Host "`n[2] Running debug.py..." -ForegroundColor Green
python debug.py

Write-Host "`n[3] Running main.py..." -ForegroundColor Green
python main.py

Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
