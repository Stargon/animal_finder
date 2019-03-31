import pymysql
import config

def mysql_connection():
    return pymysql.connect(host=config.MYSQL_HOST,user=config.MYSQL_USER,db=config.MYSQL_DATABASE, cursorclass=pymysql.cursors.DictCursor)
