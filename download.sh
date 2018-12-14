sudo apt-get update
sudo apt-get install zip
pushd ~
find ./ztdl-5-day-bootcamp -name "*.ipynb" | tar -czvf to_download.tgz -T -
popd
