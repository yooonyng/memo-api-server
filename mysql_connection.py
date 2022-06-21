import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host = 'yh-db.c5ixbhe6phsg.ap-northeast-2.rds.amazonaws.com',
        database = 'memo_db',
        user = 'memo_user',
        password = 'node1234test'
    )
    return connection