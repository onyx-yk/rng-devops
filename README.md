This is a simple program I've made that is used to demonstrate DevOps practices.

Tech Stack:
-Flask in Python for the RNG Generation.

-HTML/JS is used for Frontend for the webpage using NGINX as the api and fetching the number from backend.

-Docker and Docker Compose for containerization and deployment.

-CI/CD with Github Actions that create an image in Docker Compose.

Features:
-Random number generated from Backend API and frontend fetches directly from backend.

-Frontend and backend have their separate container in docker 

-Nginx used are reverse proxy for API requests.

-Github actions used for automated building and testing. 

How to Use:
1) Clone this repo and enter the deploy file and run 'docker compose -f docker-compose.prod.yml up -d'
2) Frontend and backend API will be created at http://localhost:8080/ and http://localhost:5000/ (http://localhost:5000/random for the json output)
3) Close it by "docker compose -f docker-compose.prod.yml down"
