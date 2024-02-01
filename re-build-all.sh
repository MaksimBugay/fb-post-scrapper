docker service rm backend-local_fb-scrapper

sleep 5s

docker image rm --force n7fr846yfa6ohlhe/mbugai:fb-scrapper-1000

docker build -t n7fr846yfa6ohlhe/mbugai:fb-scrapper-1000 -f Dockerfile .

read -p "Press any key..."
