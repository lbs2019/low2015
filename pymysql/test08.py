def test_003():
    try:
        print("我是try主体，被执行")
        return True
    except:
        print("出现异常啦")
    finally:
        print("我是finally！")

r = test_003()
print("执行结果：",r )


sql = "select * from t_book"
print(sql.split(" ")[0])