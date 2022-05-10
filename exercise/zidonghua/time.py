import time,datetime
class TimeMysql:
    def in_time (cur_time):
        try:
            print(f"正在将{cur_time}转换为%Y-%m-%d %H:%M:%S格式时间")
            loc_time = time.localtime(cur_time)
            now = time.strftime("%Y-%m-%d %H:%M:%S",loc_time)
            print(f"转换时间{now}成功")
        except:
            print(f"转换时间{cur_time}失败")
            raise

    def now_time ():
            cur_time = time.time()
            print(f"正在获取当前时间戳{cur_time}")
            loc_time = time.localtime(cur_time)
            now = time.strftime("%Y-%m-%d %H:%M:%S",loc_time)
            print(f"转换当前时间戳{now}成功")





if __name__ == '__main__':
    in_time = TimeMysql.in_time(int(input("请输入10位时间戳: ")))
    now_time = TimeMysql.now_time()
