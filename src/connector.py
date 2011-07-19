import psycopg2

def connect():
    from settings import dbname, user, host, password
    conn_template = "dbname='%s' user='%s' host='%s' password='%s'"
    conn_str = conn_template % (dbname, user, host, password)
    return psycopg2.connect(conn_str)

def get_tables(conn):
    cur = conn.cursor()
    query="SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    cur.execute(query)
    return cur.fetchall()

def get_columns(conn, table_name):
    cur = conn.cursor()
    query="SELECT column_name FROM information_schema.columns WHERE table_name = '%s'" % table_name
    cur.execute(query)
    return cur.fetchall()

def get_rows(conn, table_name, limit):
    cur = conn.cursor()
    query = "SELECT * FROM %(table_name)s LIMIT %(limit)s" % locals()
    cur.execute(query)
    return cur.fetchall()

def print_rows(rows):
    for row in rows:
        print row

def main():
    try:
        conn = connect()
    except Exception, e:
        print e
        raise
    print get_tables(conn)
    print get_columns(conn, 'products')
    print_rows(get_rows(conn, 'products', 20))


if __name__ == "__main__":
    main()