pushd ~
zip -R to_download "*.ipynb" "*.py" -i "ztdl-5-day-bootcamp/*" -x "*/.ipynb_checkpoints/*"
# find ./ztdl-5-day-bootcamp -name "*.ipynb" | tar -czvf to_download.tgz -T -
mv to_download.zip ./ztdl-5-day-bootcamp/
popd
