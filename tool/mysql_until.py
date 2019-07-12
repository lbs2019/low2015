import pymysql


class MysqlUntil:
    conn = None
    cursor = None

    # 获取连接对象方法
    def get_conn(self):
        self.conn = pymysql.connect(host="localhost",
                               user="root",
                               password="",
                               database="books",
                               charset="utf8",
                               autocommit=True,
                               port=3306)
        return self.conn

    # 获取游标对象对方法
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标对象方法
    def close_cursor(self, cursor):
        cursor.close()

    # 关闭连接对象方法
    def close_conn(self):
        self.conn.close()

    # 查询sql方法
    def get_fetchall(self, sql):
        try:
            self.cursor = self.get_cursor()
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            # 关闭游标
            self.close_cursor(self.cursor)
            # 关闭连接
            self.close_conn()

    # 增删改 sql方法
    def alert_sql(self, sql):
        try:
            self.cursor = self.get_cursor()
            self.cursor.execute(sql)
            # 提交事务
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            # 回滚事务
            self.conn.rollback()
        finally:
            # 关闭游标
            self.close_cursor(self.cursor)
            # 关闭连接
            self.close_conn()
