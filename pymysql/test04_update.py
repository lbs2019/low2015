# 导包
import pymysql
"""
    目标：基于mysql 更新操作
"""

# 获取连接对象
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="",
                       database="books",
                       charset="utf8",
                       autocommit=True,
                       port=3306)
# 获取游标对象
cursor = conn.cursor()
# 执行sql语句
sql = "UPDATE t_book set `read`=`read`+1 where id=3"
row = cursor.execute(sql)
print("受影响的行数：", row)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()