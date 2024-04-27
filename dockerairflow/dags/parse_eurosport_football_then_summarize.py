import os
import datetime
import json
import mysql.connector
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from data.parse.parse_eurosport_football import get_articles_eurosport_football
from data.summarize.summarize import summarize_football


# Definition of tasks
def get_parsing_eurosport_football(ti):
    main_articles = get_articles_eurosport_football()

    ti.xcom_push(key="main_articles", value=json.dumps(main_articles))


def get_summary(ti):
    main_articles = ti.xcom_pull(
        key="main_articles", task_ids="task_parse_eurosport_football"
    )
    main_articles = json.loads(main_articles)

    summary = summarize_football(articles=main_articles)

    ti.xcom_push(key="summary", value=json.dumps(summary))


def write_into_db(ti):
    summary = ti.xcom_pull(key="summary", task_ids="task_summarize")
    summary = json.loads(summary)

    now = datetime.datetime.now().strftime(format="%Y-%m-%d %H:%M:%S")

    MYSQL_HOST = os.environ["MYSQL_HOST"]
    MYSQL_USER = os.environ["MYSQL_USER"]
    MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
    MYSQL_DB = os.environ["MYSQL_DB"]

    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        buffered=True,
    )
    cursor = conn.cursor()

    summary = summary.replace('"', "'")

    query = f'INSERT INTO summaries(summary, date) VALUES ("{summary}", "{now}")'

    cursor.execute(query)
    conn.commit()

    # Close database connection
    conn.close()


# DAG default arguments
default_args = {
    "owner": "your_name",
    "start_date": datetime.datetime(2023, 9, 29),
    "retries": 0,
}


# DAG creation
with DAG(
    "parse_eurosport_football_then_summarize",
    default_args=default_args,
    schedule_interval=datetime.timedelta(minutes=2),
    catchup=False,
) as dag:
    task_parse_eurosport_football = PythonOperator(
        task_id="task_parse_eurosport_football",
        python_callable=get_parsing_eurosport_football,
        dag=dag,
    )

    task_summarize = PythonOperator(
        task_id="task_summarize",
        python_callable=get_summary,
        dag=dag,
    )

    task_into_db = PythonOperator(
        task_id="task_into_db",
        python_callable=write_into_db,
        dag=dag,
    )

    # Task dependencies
    task_parse_eurosport_football >> task_summarize >> task_into_db
