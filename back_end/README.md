# To run this file
## using docker compose
- docker-compose build
- docker-compose up

## normal docker run
- docker build -t backend .
- docker run -p 8296:8296 backend

## run in local
- python run.py

# To upload this image and run in instance
- build package
    - docker build -t backend .
- push image to docker hub
    - docker tag backend USERNAME/REPO_NAME
    - docker push USERNAME/REPO_NAME
- go to instance server & make sure it can login docker
    - sudo chmod 666 /var/run/docker.sock
- pull and keep it running in the background
    - docker login -u USERNAME
    - docker pull USERNAME/REPO_NAME
    - docker run -t -d -p 8296:8296 USERNAME/REPO_NAME
    - docker logout

for current package available in chinatipk/backend

## Acknowledgement and Reference
- For flask template, https://github.com/iliasmansouri/flask-swagger-template
- For swagger format, https://swagger.io/docs/specification/2-0/basic-structure/