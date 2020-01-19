import psycopg2
import sqlite3
import sys
 
#Change these values as needed
 
sqdb='testmydb5.db'
sqlike='table'
pgdb='testmydb5'
pguser='postgres'
pgpswd='1234'
pghost='127.0.0.1'
pgport='5432'
pgschema='testmydb5.sql'
 
consq=sqlite3.connect(sqdb)
cursq=consq.cursor()
 
tabnames=[]
 
cursq.execute("SELECT name FROM sqlite_master WHERE type='table'"# AND name LIKE '%s'" (%table))
tabgrab = cursq.fetchall()
for item in tabgrab:
    tabnames.append(item[0])
 
for table in tabnames:
    cursq.execute("SELECT sql FROM sqlite_master WHERE type='table'"# AND name = ?;", (table,))
    create = cursq.fetchone()[0]
    cursq.execute("SELECT * FROM %s;" %table)
    rows=cursq.fetchall()
    colcount=len(rows[0])
    pholder='%s,'*colcount
    newholder=pholder[:-1]
 
    try:
 
        conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                               host=pghost, port=pgport)
        curpg = conpg.cursor()
        curpg.execute("SET search_path TO %s;" %pgschema)
        curpg.execute("DROP TABLE IF EXISTS %s;" %table)
        curpg.execute(create)
        curpg.executemany("INSERT INTO %s VALUES (%s);" % (table, newholder),rows)
        conpg.commit()
        print('Created', table)
 
    except psycopg2.DatabaseError as e:
        print ('Error %s' % e) 
        sys.exit(1)
 
    finally:
 
        if conpg:
            conpg.close()
 
consq.close()