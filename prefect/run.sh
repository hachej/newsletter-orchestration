docker build -t prefect-docker-guide-image .
docker run --network="host" -e PREFECT_API_URL=http://localhost:4200/api prefect-docker-guide-image