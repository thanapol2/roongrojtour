import cx_Oracle
# from sqlalchemy import create_engine
import os

# db_connect = create_engine('oracle://tong:tong@127.0.0.1:1521/xe',coerce_to_unicode=True)
os.environ["NLS_LANG"] = ".UTF8"

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
    cur.close()
    conn.close()
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
    cur.close()
    conn.close()
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
    cur.close()
    conn.close()
    return rows

def createUpdateTour(data):
    conn = cx_Oracle.connect('tong', 'tong', 'localhost:1521/XE')
    cur = conn.cursor()
    msg = ''
    try:
        sql = "insert into table1 (column1) values ('1') "
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        msg = "error in insert operation"

    finally:
        cur.close()
        conn.close()

    return msg
def getTour(tourID):
    conn = cx_Oracle.connect('tong', 'tong', 'localhost:1521/XE')
    cur = conn.cursor()
    # conn = db_connect.connect()
    result = {}
    sql = "select TOUR_ID									"\
    "		,THAI_TITLE 									"\
    "		, THAI_NAME 									"\
    "		, THAI_SURNAME 									"\
    "		, ENG_TITLE 									"\
    "		, ENG_NAME 										"\
    "		, ENG_SURNAME 									"\
    "		, SEX 											"\
    "		, PERSON_ID 									"\
    "		, PASSPORT_ID 									"\
    "		, EMAIL 										"\
    "		, COUNTRY 										"\
    "		, NATIONALITY 									"\
    "		,to_char(BIRTH_DAY,'YYYY-MM-DD') BIRTH_DAY		"\
    "		,to_char(ISSUE_DATE,'YYYY-MM-DD') ISSUE_DATE	"\
    "		,to_char(EXPIRE_DATE,'YYYY-MM-DD') EXPIRE_DATE	"\
    "		, DETAIL 										"\
    "		, PATH_PIC 										"\
    "		, ADDRESS 										"\
    "		, PROVINCE 										"\
    "		, POST_NO 										"\
    "		, TEL											"\
    "from tour_Master										"\
    "where tour_id =  " + tourID
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        result['TOUR_ID'] = row[0]
        result['THAI_TITLE'] = row[1]
        result['THAI_NAME'] = row[2]
        result['THAI_SURNAME'] = row[3]
        result['ENG_TITLE'] = row[4]
        result['ENG_NAME'] = row[5]
        result['ENG_SURNAME'] = row[6]
        result['SEX'] = row[7]
        result['PERSON_ID'] = row[8]
        result['PASSPORT_ID'] = row[9]
        result['EMAIL'] = row[10]
        result['COUNTRY'] = row[11]
        result['NATIONALITY'] = row[12]
        result['BIRTH_DAY'] = row[13]
        result['ISSUE_DATE'] = row[14]
        result['EXPIRE_DATE'] = row[15]
        result['DETAIL'] = row[16]
        result['PATH_PIC'] = row[17]
        result['ADDRESS'] = row[18]
        result['PROVINCE'] = row[19]
        result['POST_NO'] = row[20]
        result['TEL'] = row[21]
    cur.close()
    conn.close()
    return result



