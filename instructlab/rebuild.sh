docker-compose down #--volumes
docker-compose up --watch #--build 



# --watch ensures the container builds and monitors for changes
# --build forces a rebuild of the Docker image if any of the files change