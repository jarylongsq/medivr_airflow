# MediVR Airflow Pipeline

## Steps to getting started
- Clone this repo
- Install the prerequisites
- Run the service
- Check http://localhost:8080

### Prerequisites

- Install [Docker](https://www.docker.com/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)
- Following the Airflow release from [Python Package Index](https://pypi.python.org/pypi/apache-airflow)

### Usage

Limit the memory usage for Docker
```
Open Windows Terminal/CMD/PowerShell
# turn off all wsl instances such as docker-desktop
wsl --shutdownnotepad "$env:USERPROFILE/.wslconfig"

Edit the .wsconfig file and paste this command
[wsl2]
memory=3GB   # Limits VM memory in WSL 2 up to 3GB
processors=4 # Makes the WSL 2 VM use two virtual processors
```

Build the web service with Docker first
```
# Build the image
# docker-compose up -d --build
```

Run the webservice 
```
docker-compose up -d
```

Check http://localhost:8080/

- `docker-compose logs` - Displays log output
- `docker-compose ps` - List containers
- `docker-compose down` - Stop containers

Connecting to database:
username: airflow
password: airflow
