import os
import mysql.connector

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

# Database creation
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS summaries (id INT AUTO_INCREMENT PRIMARY KEY, summary VARCHAR(2500), date DATETIME)"
)
conn.commit()


# Close connection
conn.close()
