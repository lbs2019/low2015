
from tool.mysql_until import MysqlUntil
# 获取mysqluntil对象
mysql = MysqlUntil()

# 调用查询方法
# sql_select = "select * from t_book"
# result = mysql.get_fetchall(sql_select)
# print(result)

# 删除方法
sql_delete = "delete from t_book where id=9999"
result = mysql.alert_sql(sql_delete)
print(result)