import sys import pymysql 
import logger conn = None 
def openConnection(): 
    global conn try: 
        if(conn is None): conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5) 
        elif (not conn.open): conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5) 
   except: logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
sys.exit()

def getRecords(): 
    try: 
        openConnection() with conn.cursor() as cur: 
            sql = "SELECT * FROM table" 
            cur.execute(sql) 
            result = cur.fetchall() 
            print(result) 
            cur.close() 
            conn.close() 
    except Exception as e: 
            print(e) 
    finally: 
            print('Query Successful') getRecords()


def getRecords(table): 
    try: 
        openConnection() with conn.cursor() as cur: 
        sql = "SELECT * FROM %s" 
        cur.execute(sql, table)
        result = cur.fetchall()
        for row in result: 
             record = { 
               'id': row[0], 
               'name': row[1], 
               'email': row[2], 
               'phone': row[3]
             } 
        cur.close() 
        conn.close() 
     except Exception as e: 
          print(e) 
     finally: 
          print('Query Successful')
getRecords('table_name')

sql = "SELECT * FROM %s WHERE column_name = `somevalue`"

#Updating Rows of Data
def getRecords(table, data): 
    try: 
        openConnection() with conn.cursor() as cur: 
        sql = "UPDATE %s SET date=%s, numsent=%s WHERE email = %s"
        cur.execute(sql, (table, data['date_sent'], data['status'],   
        data['email'])) 
        conn.commit() 
        cur.close() 
        conn.close() 
     except Exception as e: 
        print(e) 
     finally: 
        print('Query Successful') 
        data = { 
          'date_sent': '12/01/2018', 
          'email': 'fakeemail@example.com', 
          'status': 'Confirmed' 
        } 

getRecords('table_name', data)

#-----------------------------------------------------------------------------------------------
#For Dessert: Usage in AWS Lambda

import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = "rdsName.dfsd834mire.us-west-3.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
logger = logging.getLogger()
logger.setLevel(logging.INFO)
conn = None
def openConnection():
    global conn
    try:
        if(conn is None):
            conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=10)
        elif (not conn.open):
            conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=10)
    except:
        logger.error("ERROR: Could not connect to MySql instance.")
        sys.exit()
logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
















