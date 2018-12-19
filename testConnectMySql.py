# -*- coding:utf-8 -*


import pymysql,time




def core_code(index):
    print(str(i)+"连接到mysql...")
    db = pymysql.connect(host="40.73.102.21",user="root",passwd="Passw0rdVmw@re!",db="shxh2",charset="utf8")
    cursor =db.cursor()

    sql ="""select count(DISTINCT item_id) FROM tbl_zjly_yuanju WHERE online='0' ;"""
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        print("执行返回的结果")
        print(res)
        db.commit()
    except:
        print(str(index)+"sql插入错误")
    cursor.close()
    db.close()

if __name__=='__main__':
    for i in range(1,100):
        start_time=time.clock()
        core_code(i)
        end_time=time.clock()
        print("一次连接花费的时间%f"%(end_time - start_time))




