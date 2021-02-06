import pymysql

def connection():
    try:
        connect = pymysql.connect('127.0.0.1', 'root', '', 'loginoop')
        if connect:
            print("Database is connected.")
        return connect
    except Exception as e:
        return "Something was wrong! : " + str(e)