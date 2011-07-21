import psycopg2
from datetime import datetime

def connect():
    from settings import dbname, user, host, password
    if password:
        conn_template = "dbname='%s' user='%s' host='%s' password='%s'"
        conn_str = conn_template % (dbname, user, host, password)
    else:
        conn_template = "dbname='%s' user='%s' host='%s'"
        conn_str = conn_template % (dbname, user, host)
    return psycopg2.connect(conn_str)

def execute(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    cur.close()

def fetch(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    return result

def get_tables(conn):
    query="SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    return fetch(conn, query)

def get_columns(conn, table_name):
    query="SELECT column_name FROM information_schema.columns WHERE table_name = '%s'" % table_name
    return fetch(conn, query)

def get_rows(conn, table_name, limit):
    query = "SELECT * FROM %(table_name)s LIMIT %(limit)s" % locals()
    return fetch(conn, query)

def insert(conn, table_name, fields, values):
    fields = list_to_fields(fields)
    values = list_to_fields(values)
    query = "INSERT INTO %(table_name)s (%(fields)s) VALUES (%(values)s)" % locals()
    execute(conn, query)

def print_rows(rows):
    for row in rows:
        print row

def list_to_fields(fields):
    fields = map(str, fields)
    return ','.join(fields)

def load(conn, count):
    fields = ['category', 'title', 'actor', 'price', 'special', 'common_prod_id']
    for i in xrange(count):
        time =  datetime.now().isoformat()
        values = ['4', "'ACADEMY ALABAMA'",  "'%s'" % time, 20.01, 0,  3343]
        insert(conn, 'products', fields, values)

def main():
    try:
        conn = connect()
    except Exception, e:
        print e
        raise
    #print get_tables(conn)
    #print get_columns(conn, 'products')
    #print_rows(get_rows(conn, 'products', 20))
    print "##LOADING##"
    load(conn, 20000)
    print "##LOADED##"
    print "##COMMITING##"
    conn.commit()
    print "##COMMITED##"
    conn.close()


if __name__ == "__main__":
    main()