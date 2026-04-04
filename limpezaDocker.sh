# Parar todos os cotainer

docker stop $(docker ps -aq)

# Limpeza profunda no docker

docker system prune -a --volumes

# Verificar o uso do disco do docker

docker system df
