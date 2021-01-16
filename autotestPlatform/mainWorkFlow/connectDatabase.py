import os
import cx_Oracle

def multiExcuteSql(sqls):
    # 解决 Oracle 乱码问题
    # 或 os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect("ECT_OWNER/Mm*cuN7V/U='fZVd@172.32.231.249/oraods")
    cursor = conn.cursor()
    for sql in sqls:
        cursor.execute(sql)
        print("执行的sql"+sql)
        print(cursor.execute(sql))
    cursor.close()
    conn.close()

def DBReturnRows(sql):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    conn = cx_Oracle.connect("ECT_OWNER/Mm*cuN7V/U='fZVd@172.32.231.249/oraods")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    rows = str(rows[0][0])
    cursor.close()
    conn.close()
    return rows

# if __name__ == '__main__':
#     print(DBReturnRows("SELECT count(*) FROM COUPON c2 WHERE c2.COUPON_RULE_UUID='8aaade2a73b702f80173b87e13ca00cc' AND COMPANY_UUID ='8aaa614a6aaf570e016aafc997cc0001' AND CREATE_TIME > SYSDATE-1"))