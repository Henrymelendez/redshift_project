import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drop all created tables in sparkify db
 
    Parameters:
    conn(psycopg2.connect): Postgres connection to RedShift sparkify db
    cur(psycopg2.cursor): Postgres cursor to RedShift sparkify db
 
    Returns:
    None
    """

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create all tables in sparkify db
 
    Parameters:
    conn(psycopg2.connect): Postgres connection to RedShift sparkify db
    cur(psycopg2.cursor): Postgres cursor to RedShift sparkify db
 
    Returns:
    None
    """

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Drop & create all tables in sparkify db
 
    Parameters:
    None
 
    Returns:
    None
    """

    # Obtain RedShift cluster & db login information
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    DWH_HOST = config.get("DWH", "DWH_HOST")
    DWH_DB= config.get("DWH","DWH_DB")
    DWH_DB_USER= config.get("DWH","DWH_DB_USER")
    DWH_DB_PASSWORD= config.get("DWH","DWH_DB_PASSWORD")
    DWH_PORT = config.get("DWH","DWH_PORT")

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(DWH_HOST, DWH_DB, DWH_DB_USER, DWH_DB_PASSWORD, DWH_PORT))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()