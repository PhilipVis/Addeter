cd addeter || exit

rm -rf dist
rm -rf build
rm -f addeter.spec

pyinstaller addeter.py \
    --onefile \
    --add-data "*:ui" \
    --add-data "*:config"