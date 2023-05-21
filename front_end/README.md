# To run this file
## using docker compose
- docker-compose build
- docker-compose up

## normal docker run
- docker build -t streamlit .
- docker run -p 8501:8501 streamlit

## only streamlit
- go to /src, streamlit run home.py

# To upload this image and run in instance
- build package
    - docker build -t streamlit .
- push image to docker hub
    - docker tag streamlit USERNAME/REPO_NAME
    - docker push USERNAME/REPO_NAME
- go to instance server & make sure it can login docker
    - sudo chmod 666 /var/run/docker.sock
- pull and keep it running in the background
    - docker login -u USERNAME
    - docker pull USERNAME/REPO_NAME
    - docker run -t -d -p 8501:8501 USERNAME/REPO_NAME
    - docker logout

for current package available in chinatipk/frontend

