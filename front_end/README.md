# To run this file
## using docker compose
- docker-compose build
- docker-compose up

## normal docker run
- docker build -t streamlit .
- docker run -p 8501:8501 streamlit

## only streamlit
- go to /src, streamlit run home.py