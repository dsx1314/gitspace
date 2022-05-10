# encoding=gbk
import psycopg2

config= {'host':'192.168.12.203','port':'5432','user':'postgres','passwd':'postgres','db':'parkingos_V3'}

try:
    conn = psycopg2.connect(database="parkingos_V3",user="postgres",password="postgres",host="192.168.12.203",port="5432")
    print("成功连接")
except psycopg2.Error as e:
    print("连接失败")

cur = conn.cursor()

cur.execute("SELECT sum(temp_pay) 临停电子支付,SUM(temp_cash) 临停现金,SUM(month_pay) 月租电子支付,SUM(month_cash) 月租现金,SUM(store_pay) 储值电子支付,SUM(store_cash) 储值现金,SUM(shop_pay) 商户电子支付,SUM(shop_cash) 商户现金,SUM(store_use) 储值抵扣,SUM(discount_money) 优惠金额,SUM(total_money) 收入总金额,SUM(refunds_money) 退款金额,SUM(service_charge) 手续费,SUM(out_money) 支出金额,SUM(temp_total) 临停收费合计,SUM(month_total) 月租收费合计,SUM(shop_total) 商户充值合计,SUM(other_total) 其他支付合计,SUM(store_total) 储值支付合计,sum(free_money) 免费金额 FROM zhtc_report_month_total;")
rows = cur.fetchall()


f = open('dsx.txt','w')
f.write(f'{rows}')




