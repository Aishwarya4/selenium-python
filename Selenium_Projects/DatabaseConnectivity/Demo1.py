import cx_Oracle
import os

os.environ['PATH']='E:\Software_Testing\instantclient_19_10'
con=cx_Oracle.connect("system","aishu","localhost/pdborcl")
print("connected")
con.close()

