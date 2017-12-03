import cx_Oracle
from sqlalchemy import create_engine
import os

# db_connect = create_engine('oracle://tong:tong@127.0.0.1:1521/xe',coerce_to_unicode=True)
os.environ["NLS_LANG"] = ".UTF8"
def getTour():
    db_connect = create_engine('oracle://tong:tong@127.0.0.1:1521/xe')
    conn = db_connect.connect()
    sql = "SELECT 	ID,				" \
          "		NAME,			    " \
          "		TYPE,			    " \
          "		EN_NAME			    " \
          "FROM  com_tour	        "
    # cur = conn.cursor()
    query = conn.execute(sql)
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    # row = cur.fetchall()
    # print(row)
    rows = query.fetchall()
    # cur.close()
    conn.close()
    return result


def searchTour():
    conn = cx_Oracle.connect('tong', 'tong', 'localhost:1521/XE')
    # conn = db_connect.connect()
    sql = "SELECT 	ID,				" \
          "		NAME,			    " \
          "		EN_NAME,		    " \
          "		TYPE			    " \
          "FROM  com_tour	        "
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    # print(row)
    # cur.close()
    # conn.close()
    # cx_Oracle.disconnect()
    return rows

def searchInvoice():
    conn = cx_Oracle.connect('tong', 'tong', 'localhost:1521/XE')
    # conn = db_connect.connect()
    sql = "select INVOICE_NO,			                        " \
          "		  CUSTOMER_NAME,		                        " \
          "		  PAYMENT_TYPE,			                        " \
          "		  to_char(ISSUE_DATE,'YYYY/MM/DD') issue_date,	" \
          "		  CREATE_USER									" \
          "FROM  search_invoice	                                " \
          "order by invoice_no	desc,ISSUE_DATE	desc            "
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    # print(row)
    # cur.close()
    # conn.close()
    # cx_Oracle.disconnect()
    return rows

def searchPayment():
    conn = cx_Oracle.connect('tong', 'tong', 'localhost:1521/XE')
    # conn = db_connect.connect()
    sql = "select PAYMENT_TYPE,									"\
		"	PAYMENT_NO,											"\
		"	INVOICE_NO, 										"\
        "	REJECT,												"\
        "	to_char(PAYMENT_DATE,'YYYY/MM/DD') PAYMENT_DATE,	"\
        "	CUSTOMER_NAME,										"\
        "	to_char(ISSUE_DATE,'YYYY/MM/DD') issue_date		    "\
		"from Search_PAYMENT									"\
		"order by PAYMENT_NO							        "
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    # print(row)
    # cur.close()
    # conn.close()
    # cx_Oracle.disconnect()
    return rows



