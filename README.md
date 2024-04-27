![FastFoot](./dockerstreamlit/Images/FastFoot.jpeg)

# 👋 Welcome to the FastFoot app !

FastFoot is a **tutorial** to build an all-in app combining **webscraping** tools, **Generative AI** (Large Language Model), **task scheduler** (Apache Airflow), **database** (MySQL), **web interface** (Streamlit) and **easy deploiement** tool (Docker) to automatically get and summarize the freshest football news !

📰 A **blogpost on Medium called _All-in AI app for news summarizer_** is available as well : **https://medium.com/@jb.excoffier/all-in-ai-app-for-news-summarizer-4e3ff1dc06d6**.

The app is written in Python 🐍 and is easily deployable with Docker 🚢 !

### To deploy and play with this app locally, you need to :
1. have [Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) installed (version 26.1.0 was used to built this app).
2. create [your own paying OpenAI API key through their website](https://openai.com/product), and copy-paste it to the `.env` file (`OPENAI_APIKEY`, which is by default set to a non-working key).
3. open a terminal and execute Docker compose command `docker compose up -d`. 
    - access the Airflow webserver to activate DAG and its tasks at : https://0.0.0.0:8080/ (credentials are in the `.env` file). Tasks are then automatically executed on a regular basis, thus results are continuously updated as well 👌
    - access the **web interface page at http://0.0.0.0:8501/FastFoot/** to see the latest summary of the breaking football news !

⭐ Give a star if you like this project, and read the related blogpost !


