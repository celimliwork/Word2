@echo off
chcp 65001 >nul
echo ========================================
echo 🎓 YDS Kelime Öğrenme Sistemi
echo ========================================
echo.

:menu
echo [1] Oyunu Başlat (1. Set)
echo [2] Yeni Set İşle
echo [3] Proje Dokümantasyonu
echo [4] Çıkış
echo.
set /p choice="Seçiminiz (1-4): "

if "%choice%"=="1" goto start_game
if "%choice%"=="2" goto process_set
if "%choice%"=="3" goto show_docs
if "%choice%"=="4" goto exit

echo ❌ Geçersiz seçim!
goto menu

:start_game
echo.
echo 🎮 Oyun başlatılıyor...
start "" "game.html"
echo ✅ Tarayıcınızda açıldı!
timeout /t 2 >nul
goto menu

:process_set
echo.
echo 📝 Yeni set işleme...
python process_vocabulary.py
pause
goto menu

:show_docs
echo.
echo 📖 Dokümantasyon açılıyor...
start "" "README.md"
timeout /t 2 >nul
goto menu

:exit
echo.
echo 👋 Görüşmek üzere! Başarılar!
timeout /t 2 >nul
exit
