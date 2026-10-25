import sqlite3
from sqlite3 import Error

db_file = "21"

def create_connection():
    conn = None
    try:
        #print('Connecting to..'+db_file)
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(sql):
    ok = False
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(sql)
            ok = True
        except Error as e:
            print(e)
        finally:
            conn.close()
    return ok

def insert_record(sql, record_data):
    rec_id = -1
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(sql, record_data)
            conn.commit()
            rec_id = cur.lastrowid
        except Error as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()
    return rec_id

def update_record(sql, record_data):
    ok = False
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(sql, record_data)
            conn.commit()
            ok = True
        except Error as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()
    return ok

def execute_sql(sql, data):  #used for deleting records
    ok = False
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if not data == (): cur.execute(sql, data)
            else: cur.execute(sql)
            conn.commit()
            ok = True
        except Error as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()
    return ok


def query_table(sql):
    rows = None
    conn = create_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall();
        conn.close()
        #for row in rows:
        #    print(row)
    return rows

def run_query(sql):
    print('')
    print('Query:',sql.strip())
    records = query_table(sql)
    if not records == None:
        for record in records:
            print(record)
