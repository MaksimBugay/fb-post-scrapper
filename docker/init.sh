#!/bin/bash
docker service rm backend-local_fb-scrapper
(docker stack deploy --with-registry-auth -c backend.yml backend-local)

docker service logs -f backend-local_fb-scrapper

read -p "Press any key..."