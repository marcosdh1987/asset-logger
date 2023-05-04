DOLAR_URL = 'https://api.bluelytics.com.ar/v2/latest'
HOST="192.168.0.47"
DB="assets"
USER="postgres"
PASS="postgres"
PORT=5431
create_table_query = '''CREATE TABLE IF NOT EXISTS dollar
            (id SERIAL PRIMARY KEY,
            last_update timestamp,
            dolar_oficial_value_avg float,
            dolar_oficial_value_sell float,
            dolar_oficial_value_buy float,
            dolar_blue_value_avg float,
            dolar_blue_value_sell float,
            dolar_blue_value_buy float,
            dolar_oficial_euro_value_avg float,
            dolar_oficial_euro_value_sell float,
            dolar_oficial_euro_value_buy float,
            dolar_blue_euro_value_avg float,
            dolar_blue_euro_value_sell float,
            dolar_blue_euro_value_buy float); '''
#query to insert the series in the table dollar
insert = """INSERT 
            INTO dollar(dolar_oficial_value_avg, dolar_oficial_value_sell, dolar_oficial_value_buy, dolar_blue_value_avg, dolar_blue_value_sell, dolar_blue_value_buy, dolar_oficial_euro_value_avg, dolar_oficial_euro_value_sell, dolar_oficial_euro_value_buy, dolar_blue_euro_value_avg, dolar_blue_euro_value_sell, dolar_blue_euro_value_buy,last_update)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s);"""