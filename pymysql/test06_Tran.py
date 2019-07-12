# 导包
import pymysql
"""
    目标：基于mysql 事务的操作
"""

# 获取连接对象
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="",
                       database="books",
                       charset="utf8",
                       port=3306)
# 获取游标对象
cursor = conn.cursor()
try:
    # 事务开始
    conn.begin()
    # 新增图书
    sql = "insert into t_book values(3,'东游记','1990-11-11',30,50,0)"
    cursor.execute(sql)

    # 更新图书
    sql = "UPDATE t_boo set `read`=`read`+1 where title='东游记'"
    cursor.execute(sql)
    # 手动提交事务
    conn.commit()
except Exception as e:
    print(e)
    # 回滚事务
    conn.rollback()
finally:
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

# 自动提交事务
# conn.autocommit(True)


