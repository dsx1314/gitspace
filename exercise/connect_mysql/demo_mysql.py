# encoding=gbk
import psycopg2

config= {'host':'192.168.12.203','port':'5432','user':'postgres','passwd':'postgres','db':'parkingos_V3'}

try:
    conn = psycopg2.connect(database="parkingos_V3",user="postgres",password="postgres",host="192.168.12.203",port="5432")
    print("�ɹ�����")
except psycopg2.Error as e:
    print("����ʧ��")

cur = conn.cursor()

cur.execute("SELECT sum(temp_pay) ��ͣ����֧��,SUM(temp_cash) ��ͣ�ֽ�,SUM(month_pay) �������֧��,SUM(month_cash) �����ֽ�,SUM(store_pay) ��ֵ����֧��,SUM(store_cash) ��ֵ�ֽ�,SUM(shop_pay) �̻�����֧��,SUM(shop_cash) �̻��ֽ�,SUM(store_use) ��ֵ�ֿ�,SUM(discount_money) �Żݽ��,SUM(total_money) �����ܽ��,SUM(refunds_money) �˿���,SUM(service_charge) ������,SUM(out_money) ֧�����,SUM(temp_total) ��ͣ�շѺϼ�,SUM(month_total) �����շѺϼ�,SUM(shop_total) �̻���ֵ�ϼ�,SUM(other_total) ����֧���ϼ�,SUM(store_total) ��ֵ֧���ϼ�,sum(free_money) ��ѽ�� FROM zhtc_report_month_total;")
rows = cur.fetchall()


f = open('dsx.txt','w')
f.write(f'{rows}')




