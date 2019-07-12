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
# 关闭游标
cursor.close()
# 关闭连接
conn.close()