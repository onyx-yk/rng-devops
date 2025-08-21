This is a simple program I've made that is used to demonstrate DevOps practices.

Tech Stack:
1) Flask in Python for the RNG Generation.
2) HTML/JS is used for Frontend for the webpage using NGINX as the api and fetching the number from backend.
3) Docker and Docker Compose for containerization and deployment.
4) CI/CD with Github Actions that create an image in Docker Compose.

Features:
1) Random number generated from Backend API and frontend fetches directly from backend.
2) Frontend and backend have their separate container in docker 
3) Nginx used are reverse proxy for API requests.
4) Github actions used for automated building and testing. 

How to Use:
1) Clone this repo and enter the deploy file and run 'docker compose -f docker-compose.prod.yml up -d'
2) Frontend and backend API will be created at http://localhost:8080/ and http://localhost:5000/ (http://localhost:5000/random for the json output)
3) Close it by "docker compose -f docker-compose.prod.yml down"
