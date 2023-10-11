import os
import pymssql


cnxn = pymssql.connect(
    server=os.environ['test_db_host'],
    user="sa",
    password=os.environ['sa_PWD'],
    autocommit=True,
    conn_properties=""
)


with cnxn.cursor() as crsr:
    db_name = "[sqla_test]"
    print(f"Re-creating database {db_name}")
    crsr.execute("USE master")
    crsr.execute(f"DROP DATABASE {db_name}")
    crsr.execute(f"CREATE DATABASE {db_name}")
