# 导包
import pymysql
# 获取连接对象
conn = pymysql.Connect(host="192.168.35.44",
                       user="root",
                       password="",
                       database="books",
                       port=3306,
                       charset="utf8")
# 获取游标
cursor = conn.cursor()
# 执行sql语句 提示：默认返回的不是结果，而是受影响的行数
row = cursor.execute("select * from t_book")
print("受影响的行数为：", row)
# 拿取第一条数据
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# 拿取指定条数数据
# print(cursor.fetchmany(2))
print("受影响的行数2：", cursor.rowcount)
print("---"* 30)

# 拿取所有数据
# print(cursor.fetchall())

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

"""
    注意：
        1. fetchone：拿取1条数据，拿走以后，就永远少1条；
        2. fetchall：拿取剩余的数据；
        3. fetchmany：拿取指定条数数据；
"""