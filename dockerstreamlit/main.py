import os
import mysql.connector
import streamlit as st
import pandas as pd

PATH_IMAGES = "./Images/"

MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
MYSQL_DB = os.environ["MYSQL_DB"]


try:
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        buffered=True,
    )

    query = "SELECT * FROM summaries ORDER BY date DESC LIMIT 4"
    df = pd.read_sql(query, con=conn)

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d %H:%M:%S")
    df["day"] = df["date"].dt.strftime("%d/%m/%Y")
    df["hour"] = df["date"].dt.strftime("%Hh%Mm%Ss")

    # Close database connection
    conn.close()
except Exception as e:
    df = pd.DataFrame()
    print(str(e))

# The used image (FastFoot.jpeg) was created using Generative AI and is free-to-use.
st.image(PATH_IMAGES + "FastFoot.jpeg", caption="Welcome to FastFoot !")

st.text("\n" * 2)


if df.empty:
    st.success("No summary of your football news is currently available...", icon="❔")
else:
    most_recent_summary = df.iloc[0].squeeze()

    container = st.container(border=True)
    container.markdown(
        "⚽️"
        + " "
        + "_News created on the "
        + most_recent_summary["day"]
        + " at "
        + most_recent_summary["hour"]
        + "_."
        + "  \n"
        + " "
        + most_recent_summary["summary"]
    )

    st.text("\n" * 2)

    df_historique = df.iloc[1:]
    if df_historique.empty:
        pass
    else:
        sentence = "See the history of previous news"

        with st.expander(sentence):
            for i, row in df_historique.iterrows():
                st.markdown(
                    "📖"
                    + " "
                    + "_News created on the "
                    + row["day"]
                    + " at "
                    + row["hour"]
                    + "_."
                    + "  \n"
                    + " "
                    + row["summary"]
                )
