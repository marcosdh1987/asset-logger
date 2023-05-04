from contants import DOLAR_URL, HOST, DB, USER, PASS, PORT, create_table_query, insert
import requests
import pandas as pd
import psycopg2


def db_connect():
    conn = psycopg2.connect(
    host=HOST,
    database=DB,
    user=USER,
    password=PASS,
    port=PORT)
    cur = conn.cursor()
    return conn, cur


def main():
    dolar_json = requests.get(DOLAR_URL).json()
    #create a series with the json to put as a row in the dataframe
    dolar_row = {}

    for i in dolar_json:
        if i == 'last_update':
            dolar_row["last_update"] = dolar_json[i]
        else:
            for j in dolar_json[i]:
                dolar_row[f"dolar_{i}_{j}"] = dolar_json[i][j]

    series = pd.DataFrame(dolar_row, index=[0]).iloc[0]

    #create a connection to the database
    conn, cur = db_connect()
    print("connected to the database")
    #create the table if it doesn't exist
    cur.execute(create_table_query)
    conn.commit()
    print("table created")
    #insert the data into the table
    cur.execute(insert, series)
    conn.commit()
    print("data inserted")
    #close the connection
    cur.close()
    conn.close()
    print("connection closed")


if __name__ == "__main__":
    print("getting data from the dolar API...")
    main()
    print("App finished.")