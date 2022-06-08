import cx_Oracle

def abc():
    try:
        conn=cx_Oracle.connect('scott/tiger@orclpdb')
        return conn
    except Exception as e:
        print('Exception is ',e)
        return 'conn'


