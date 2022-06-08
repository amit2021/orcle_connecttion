import dbconnect

conn1 = dbconnect.abc()

print('amit ',conn1)

cur=conn1.cursor()
print(cur)

sql='select * from emp where rownum=1'

a=cur.execute(sql)

print(a.fetchone())