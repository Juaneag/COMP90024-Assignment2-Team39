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

## Acknowledgement and Reference
- For charts visualizations
    - For setup, https://docs.streamlit.io/library/get-started
  - Chart visualization
    - https://docs.streamlit.io/library/api-reference/charts
    - https://echarts.streamlit.app/
  - Calling API inside Streamlit
    - https://discuss.streamlit.io/t/using-an-api-from-inside-streamlit-app/37477/22
    - each request should have code running under main functions otherwise it will not working