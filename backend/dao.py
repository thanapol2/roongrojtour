import configparser
import cx_Oracle
import os

# db_connect = create_engine('oracle://tong:tong@127.0.0.1:1521/xe',coerce_to_unicode=True)
os.environ["NLS_LANG"] = ".UTF8"
config = configparser.ConfigParser()
config.sections()
config.read('./backend/data/database.ini')
USER = config['CONFIG']['USER']
PASS = config['CONFIG']['PASS']
DB_URL = config['CONFIG']['DB_URL']


def searchTour():
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
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
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
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
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
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
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
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
def getTourDetail(tourID):
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
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
    "where tour_id =  '" + tourID +"'"
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


def getCompanyDetail(tourID):
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    cur = conn.cursor()
    # conn = db_connect.connect()
    result = {}
    sql = "select COMPANY_ID								"\
    "		, THAI_NAME 									"\
    "		, ENG_NAME	 									"\
    "		, ADDRESS 										"\
    "		, PROVINCE 										"\
    "		, POST_NO 										"\
    "		, TEL_NO										"\
    "		, EMAIL											"\
    "		, TAX_ID										"\
    "		, COMPANY_TYPE									"\
    "		, REMARK										"\
    "FROM  COMPANY_Master		                            "\
    "where company_id =  '" + tourID +"'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        result['COMPANY_ID'] = row[0]
        result['THAI_NAME'] = row[1]
        result['ENG_NAME'] = row[2]
        result['ADDRESS'] = row[3]
        result['PROVINCE'] = row[4]
        result['POST_NO'] = row[5]
        result['TEL_NO'] = row[6]
        result['EMAIL'] = row[7]
        result['TAX_ID'] = row[8]
        result['COMPANY_TYPE'] = row[9]
        result['REMARK'] = row[10]
    cur.close()
    conn.close()
    return result

def getCompanyMeeting(tourID):
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    cur = conn.cursor()
    sql = "select m.SEQ_NO									"\
    "		, m.company_id									"\
    "		, m.Contact_Day									"\
    "		, m.Detail	 									"\
    "		, m.CONTACT_NAME								"\
    "		, m.Phone										"\
    "		, s.TH_NAME || ' ' || s.TH_SURNAME name			"\
    "FROM  meeting_log m	                                "\
    "inner join sales s		                                "\
    "on s.SALES_ID = m.SALE_ID								"\
    "where m.company_id =  '" + tourID + "'					"\
    "	  AND m.STATUS = 'Y'								"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def getPaymentType():
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    cur = conn.cursor()
    sql = "select PAYMENT_TYPE          " \
          "       ,NAME                 " \
          "from payment_type            "
    cur = conn.cursor()
    cur.execute(sql)
    list = cur.fetchall()
    cur.close()
    conn.close()

    rows = []
    for temp in list:
        row = {}
        row['VALUE'] = temp[0]
        row['PAYMENT_NAME'] = temp[1]
        rows.append(row)
    return rows

def getPaymentDetail(paymentNo,isVat):
    result = {}
    conn = cx_Oracle.connect(USER,PASS,DB_URL)
    cur = conn.cursor()
    sql = "SELECT  CASE                                         " \
        "  WHEN ph.isvat = 'Y'                                  " \
        "  THEN 'ใบกำกับภาษี'                                    " \
        "  ELSE 'ใบรับเงิน' end AS PAYMENT_TYPE,                  " \
        "  ph.payment_no,								        " \
		"  ph.customer_id,										" \
		"  ph.customer_name,									" \
		"  ph.address,											" \
		"  ph.detail ,											" \
		"  ph.TOTAL_ALL,										" \
		"  ph.VAT,												" \
		"  ph.TAX_ID,											" \
		"  ph.ISVAT,											" \
		"  pt.NAME as payment_name,								" \
		"  ph.payment_date,										" \
		"  ph.CHEQUE_BANK,										" \
		"  ph.CHEQUE_DATE,										" \
		"  ph.CHEQUE_NO,										" \
		"  ph.SALES_ID,											" \
		"  s.TH_NAME||' '||s.TH_SURNAME as sales_name			" \
		"FROM 													" \
		"  (SELECT p.payment_no,								" \
		"		    h.customer_id,								            " \
		"		    h.customer_name, 							            " \
		"		    h.address,									            " \
		"		    p.detail ,									            " \
		"		    TO_CHAR(h.TOTAL_ALL-h.VAT,'FM999999999.00') TOTAL_ALL,	" \
		"		    h.payment_type,								            " \
		"		    h.VAT,										            " \
		"		    h.TAX_ID,									            " \
		"			p.ISVAT,										        " \
		"		    TO_CHAR(p.PAYMENT_DATE,'DD/MM/YYYY') payment_date,	    " \
		"		    p.CHEQUE_BANK,								            " \
		"		    TO_CHAR(p.CHEQUE_DATE,'DD/MM/YYYY') CHEQUE_DATE,	    " \
		"		    p.SALES_ID,									            " \
        "		    p.CHEQUE_NO									            " \
        "	FROM payment_detail p								            " \
		"	LEFT JOIN invoice_head h							" \
		"		  ON p.invoice_no    = h.invoice_no				" \
		"		  AND p.REVISED      = h.REVISED				" \
		"		  AND p.invoice_type = h.invoice_type			" \
		"		  WHERE p.PAYMENT_NO = '" + paymentNo +"'       " \
		"		  AND   p.ISVAT = '" +isVat +"'                 " \
		"		  ) ph,											" \
		" PAYMENT_TYPE pt,		    							" \
		" SALES s												" \
		" WHERE pt.PAYMENT_TYPE = ph.PAYMENT_TYPE				" \
		" AND S.SALES_ID = ph.SALES_ID                          "
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        result['PAYMENT_TYPE'] = row[0]
        result['PAYMENT_NO'] = row[1]
        result['CUSTOMER_ID'] = row[2]
        result['CUSTOMER_NAME'] = row[3]
        result['ADDRESS'] = row[4]
        result['DETAIL'] = row[5]
        result['TOTAL_ALL'] = row[6]
        result['VAT'] = row[7]
        result['TAX_ID'] = row[8]
        result['IS_VAT'] = row[9]
        result['PAYMENT_NAME'] = row[10]
        result['PAYMENT_DATE'] = row[11]
        result['CHEQUE_BANK'] = row[12]
        result['CHEQUE_DATE'] = row[13]
        result['CHEQUE_NO'] = row[14]
        result['SALES_ID'] = row[15]
        result['SALES_NAME'] = row[16]
    cur.close()
    conn.close()
    return result