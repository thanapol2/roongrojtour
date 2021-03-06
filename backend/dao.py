import configparser
import cx_Oracle
import os
import backend.Tools as Tools

# db_connect = create_engine('oracle://tong:tong@127.0.0.1:1521/xe',coerce_to_unicode=True)
os.environ["NLS_LANG"] = ".UTF8"
config = configparser.ConfigParser()
config.sections()
config.read('./backend/data/database.ini')
USER = config['CONFIG']['USER']
PASS = config['CONFIG']['PASS']
DB_URL = config['CONFIG']['DB_URL']


def checkTourName(name,surname):
    canInsert = False
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    # conn = db_connect.connect()
    sql = 	"SELECT count(*) numb	"\
		    "FROM tour_master		"\
		    "Where  THAI_NAME = 	"\
		    "'"+name+"' and"\
		    "	  THAI_SURNAME = 	"\
		    "'"+surname+"'"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        number = row[0]
    cur.close()
    conn.close()
    if(number>0):
        canInsert = False
    else:
        canInsert = True
    return canInsert

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
    "       , NVL(PATH_PIC,'no_pic.jpg') PATH_PIC           "\
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
        result['PATH_PIC'] = 'image/tour_picture/'+row[22]

    sql = "select TOUR_ID									"\
		"		,NO_PIG 									"\
		"		,NO_MEAT									"\
		"		,NO_CHICKEN									"\
		"		,HALAL										"\
		"		,MANGSA 									"\
		"		,VEGETARIAN									"\
		"		,ISLAM										"\
		"		,NO_SEAFOOD									"\
		"		,NO_SHRIMP									"\
		"		,NO_FISH									"\
		"from EAT											"\
	    "where tour_id =  '" + tourID +"'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        result['NO_PIG'] = row[0]
        result['NO_MEAT'] = row[1]
        result['NO_CHICKEN'] = row[2]
        result['HALAL'] = row[3]
        result['MANGSA'] = row[4]
        result['VEGETARIAN'] = row[5]
        result['ISLAM'] = row[6]
        result['NO_SEAFOOD'] = row[7]
        result['NO_SHRIMP'] = row[8]
        result['NO_FISH'] = row[9]
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

def newCompany(data):
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    cur = conn.cursor()
    sql = "INSERT INTO COMPANY_MASTER 	"\
			"		(THAI_NAME,			"\
			"		ENG_NAME,			"\
			"		ADDRESS,			"\
			"		POST_NO,			"\
			"		PROVINCE,			"\
			"		TAX_ID,				"\
			"		EMAIL,				"\
			"		TEL_NO,				"\
			"		COMPANY_TYPE,		"\
			"		REMARK)				"\
			"		VALUES (			"\
			"'"+data['THAI_NAME']+"',   "\
			"'"+data['ENG_NAME']+"',    "\
			"'"+data['ADDRESS']+"',     "\
			"'"+data['POST_NO']+"',     "\
			"'"+data['PROVINCE']+"',    "\
			"'"+data['TAX_ID']+"',      "\
			"'"+data['EMAIL']+"',           "\
			"'"+data['TEL_NO']+"',          "\
			"'"+data['COMPANY_TYPE']+"',    "\
			"'"+data['REMARK']+"'           "\
			")"
    try:
        cur.execute(sql)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def updateCompany(data):
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    cur = conn.cursor()
    sql = 	"UPDATE COMPANY_MASTER		    "\
			"SET		THAI_NAME    =		"\
			"'"+data['THAI_NAME']+"',       "\
			"		ENG_NAME	 =		    "\
			"'"+data['ENG_NAME']+"',        "\
			"		ADDRESS		 =		    "\
			"'"+data['ADDRESS']+"',         "\
			"		POST_NO		 =		    "\
			"'"+data['POST_NO']+"',         "\
			"		PROVINCE	 =		    "\
			"'"+data['PROVINCE']+"',        "\
			"		TAX_ID		 =		    "\
			"'"+data['TAX_ID']+"',          "\
			"		EMAIL		 =		    "\
			"'"+data['EMAIL']+"',           "\
			"		TEL_NO		 =		    "\
			"'"+data['TEL_NO']+"',          "\
			"		COMPANY_TYPE =		    "\
			"'"+data['COMPANY_TYPE']+"',    "\
			"		REMARK		 =		    "\
			"'"+data['REMARK']+"'           "\
			"WHERE COMPANY_ID	 =		    "\
			"'"+data['COMPANY_ID']+"'       "
    print(sql)
    try:
        cur.execute(sql)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def newTour(data):
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    cur = conn.cursor()
    try:
        sql = "INSERT INTO TOUR_MASTER 	    "\
				"		(THAI_TITLE,		"\
				"		THAI_NAME,			"\
				"		THAI_SURNAME,		"\
				"		ENG_TITLE,			"\
				"		ENG_NAME,			"\
				"		ENG_SURNAME,		"\
				"		SEX,				"\
				"		PERSON_ID,			"\
				"		PASSPORT_ID,		"\
				"		EMAIL,				"\
				"		COUNTRY,			"\
				"		NATIONALITY,		"\
				"		BIRTH_DAY,			"\
				"		ISSUE_DATE,			"\
				"		EXPIRE_DATE,		"\
				"		DETAIL,				"\
				"		TEL,				"\
				"		ADDRESS,			"\
				"		POST_NO,			"\
				"		PROVINCE			"\
				"		)					"\
				"		VALUES (			"\
				"'"+data['THAI_TITLE']+"',       "\
				"'"+data['THAI_NAME']+"',        "\
				"'"+data['THAI_SURNAME']+"',      "\
				"'"+data['ENG_TITLE']+"',        "\
				"'"+data['ENG_NAME']+"',        "\
				"'"+data['ENG_SURNAME']+"',      "\
				"'"+data['SEX']+"',           "\
				"'"+data['PERSON_ID']+"',      "\
				"'"+data['PASSPORT_ID']+"',    "\
				"'"+data['EMAIL']+"',         "\
				"'"+data['COUNTRY']+"',       "\
				"'"+data['NATIONALITY']+"',   " \
                + Tools.genToDateSQL(data['BIRTH_DAY']) + ",      " \
                + Tools.genToDateSQL(data['ISSUE_DATE']) + ",     " \
                + Tools.genToDateSQL(data['EXPIRE_DATE']) + ",    " \
                "'"+data['DETAIL']+"',        "\
				"'"+data['TEL']+"',         "\
				"'"+data['ADDRESS']+"',       "\
				"'"+data['POST_NO']+"',        "\
				"'"+data['PROVINCE']+"'     "\
                ")"
        cur.execute(sql)
        sql = "INSERT INTO EAT	( TOUR_ID						"\
				    "	,NO_PIG										"\
				    "	,NO_MEAT									"\
				    "	,NO_CHICKEN									"\
				    "	,HALAL										"\
				    "	,MANGSA										"\
				    "	,VEGETARIAN									"\
				    "	,ISLAM										"\
				    "	,NO_SEAFOOD									"\
				    "	,NO_SHRIMP									"\
				    "	,NO_FISH									"\
				    ") (SELECT tour_id,								"\
                    "	,'"+data['NO_PIG']+"'		    "\
                    "	,'"+data['NO_MEAT']+"'		"\
                    "	,'"+data['NO_CHICKEN']+"'		"\
                    "	,'"+data['HALAL']+"'		    "\
                    "	,'"+data['MANGSA']+"'		"\
                    "	,'"+data['VEGETARIAN']+"'		    "\
                    "	,'"+data['ISLAM']+"'		    "\
                    "	,'"+data['NO_SEAFOOD']+"'	    "\
                    "	,'"+data['NO_SHRIMP']+"'	    "\
                    "	,'"+data['NO_FISH']+"'		"\
				    "	FROM tour_master							"\
				    "	WHERE THAI_NAME||' '||THAI_SURNAME	=		"\
				    "	'"+data['THAI_NAME']+" " \
                    + data['THAI_SURNAME'] +"')					"
        cur.execute(sql)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def updateTour(data):
    conn = cx_Oracle.connect(USER, PASS, DB_URL)
    cur = conn.cursor()
    try:
        sql = 	"UPDATE   TOUR_MASTER		 	    "\
				"SET		THAI_TITLE    =		    "\
				"'"+data['THAI_TITLE']+"',       "\
				"		THAI_NAME     =		        "\
				"'"+data['THAI_NAME']+"',        "\
				"		THAI_SURNAME  =		        "\
				"'"+data['THAI_SURNAME']+"',      "\
				"		ENG_TITLE	  =		        "\
				"'"+data['ENG_TITLE']+"',        "\
				"		ENG_NAME	  =		        "\
				"'"+data['ENG_NAME']+"',        "\
				"		ENG_SURNAME	  =		        "\
				"'"+data['ENG_SURNAME']+"',      "\
				"		SEX	 		  =		        "\
				"'"+data['SEX']+"',           "\
				"		PERSON_ID	  =		        "\
				"'"+data['PERSON_ID']+"',      "\
				"		PASSPORT_ID	  =		        "\
				"'"+data['PASSPORT_ID']+"',    "\
				"		EMAIL		  =		        "\
				"'"+data['EMAIL']+"',         "\
				"		COUNTRY	  	  =		        "\
				"'"+data['COUNTRY']+"',       "\
				"		NATIONALITY	  =		        "\
				"'"+data['NATIONALITY']+"',   "\
				"		BIRTH_DAY	  =		        "\
                + Tools.genToDateSQL(data['BIRTH_DAY'])+",      "\
				"		ISSUE_DATE	  =		        "\
                + Tools.genToDateSQL(data['ISSUE_DATE'])+",     "\
				"		EXPIRE_DATE	  =		        "\
                + Tools.genToDateSQL(data['EXPIRE_DATE'])+",    "\
				"		DETAIL	  	  =		        "\
				"'"+data['DETAIL']+"',        "\
				"		TEL	  		  =		        "\
				"'"+data['TEL']+"',         "\
				"		ADDRESS	  	  =		        "\
				"'"+data['ADDRESS']+"',       "\
				"		POST_NO	      =		        "\
				"'"+data['POST_NO']+"',        "\
				"		PROVINCE	  =		        "\
				"'"+data['PROVINCE']+"'     "\
				"WHERE TOUR_ID  =           "\
				"'"+data['TOUR_ID']+"'      "
        print(sql)
        cur.execute(sql)

        sql =   "merge INTO EAT a USING					       "\
                "     (SELECT count(tour_id) cid FROM eat		"\
                "      where TOUR_ID = 				        "\
                "'"+data['TOUR_ID']+"')		                "\
                "   b ON (b.cid > 0)						"\
                "WHEN MATCHED THEN							"\
                "UPDATE  		 							"\
                "SET		 NO_PIG =						"\
                "'"+data['NO_PIG']+"',		            "\
                "		NO_MEAT	=							"\
                "'"+data['NO_MEAT']+"',		            "\
                "		NO_CHICKEN	=						"\
                "'"+data['NO_CHICKEN']+"',		            "\
                "		HALAL	=							"\
                "'"+data['HALAL']+"',		            "\
                "		MANGSA 	=							"\
                "'"+data['MANGSA']+"',		"\
                "		VEGETARIAN	=						"\
                "'"+data['VEGETARIAN']+"',		"\
                "		ISLAM		=						"\
                "'"+data['ISLAM']+"',		"\
                "		NO_SEAFOOD	=						"\
                "'"+data['NO_SEAFOOD']+"',	"\
                "		NO_SHRIMP	=						"\
                "'"+data['NO_SHRIMP']+"',	"\
                "		NO_FISH		=						"\
                "'"+data['NO_FISH']+"' 		"\
                " where TOUR_ID = 							"\
                "'"+data['TOUR_ID']+"'		                "\
                "WHEN NOT MATCHED THEN						"\
                "INSERT ( TOUR_ID						    "\
                "	,NO_PIG									"\
                "	,NO_MEAT								"\
                "	,NO_CHICKEN								"\
                "	,HALAL									"\
                "	,MANGSA									"\
                "	,VEGETARIAN								"\
                "	,ISLAM									"\
                "	,NO_SEAFOOD								"\
                "	,NO_SHRIMP								"\
                "	,NO_FISH								"\
                ") values ( '"+data['TOUR_ID']+"'         "\
                "	,'"+data['NO_PIG']+"'		    "\
                "	,'"+data['NO_MEAT']+"'		"\
                "	,'"+data['NO_CHICKEN']+"'		"\
                "	,'"+data['HALAL']+"'		    "\
                "	,'"+data['MANGSA']+"'		"\
                "	,'"+data['VEGETARIAN']+"'		    "\
                "	,'"+data['ISLAM']+"'		    "\
                "	,'"+data['NO_SEAFOOD']+"'	    "\
                "	,'"+data['NO_SHRIMP']+"'	    "\
                "	,'"+data['NO_FISH']+"'		"\
                ")									"
        print(sql)
        cur.execute(sql)
        conn.commit()
    except cx_Oracle.DatabaseError as e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()

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
		"  ph.payment_type,              						" \
		"  ph.payment_date,										" \
		"  ph.CHEQUE_BANK,										" \
		"  ph.CHEQUE_DATE,										" \
		"  ph.CHEQUE_NO,										" \
		"  ph.SALES_ID,											" \
		"  s.TH_NAME||' '||s.TH_SURNAME as sales_name,			" \
        "  ph.invoice_no,                                       " \
        "  ph.REVISED,                           				" \
        "  ph.invoice_type,                                     " \
        "  ph.TOTAL_ALL+ph.VAT as TOTAL_VAT                     " \
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
		"		    TO_CHAR(p.PAYMENT_DATE,'YYYY-MM-DD') payment_date,	    " \
		"		    p.CHEQUE_BANK,								            " \
		"		    TO_CHAR(p.CHEQUE_DATE,'YYYY-MM-DD') CHEQUE_DATE,	    " \
		"		    p.SALES_ID,									            " \
        "		    p.CHEQUE_NO,								            " \
        "           h.invoice_no,                                           " \
        "           h.REVISED,                           				    " \
        "           h.invoice_type                                          " \
        "	FROM payment_detail p								            " \
		"	LEFT JOIN invoice_head h							" \
		"		  ON p.invoice_no    = h.invoice_no				" \
		"		  AND p.REVISED      = h.REVISED				" \
		"		  AND p.invoice_type = h.invoice_type			" \
		"		  WHERE p.PAYMENT_NO = '" + paymentNo +"'       " \
		"		  AND   p.ISVAT = '" +isVat +"'                 " \
		"		  ) ph,											" \
		" SALES s												" \
		" WHERE  S.SALES_ID = ph.SALES_ID                       "
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
        result['INVOICE_NO'] = row[17]
        result['REVISED'] = row[18]
        result['INVOICE_TYPE'] = row[19]
        result['TOTAL_VAT'] = row[20]
    cur.close()
    conn.close()
    return result

def getInvoiceDetail(invoiceNo,rev):
    headInvoice = {}
    conn = cx_Oracle.connect(USER,PASS,DB_URL)
    cur = conn.cursor()
    sql = "SELECT I.INVOICE_TYPE,							" \
        "		I.INVOICE_NO,									" \
        "		I.REVISED, 										" \
        "		I.CREATE_USER, 									" \
        "		S.TH_NAME||' '||S.TH_SURNAME SALES_NAME,		" \
        "		to_char(I.issue_date,'YYYY-MM-DD') issue_date, 	" \
        "		to_char(I.DUE_DATE,'YYYY-MM-DD') DUE_DATE,		" \
        "		I.due_date - I.issue_date DUE_DAY, 				" \
        "		I.CUSTOMER_ID,									" \
        "		I.CUSTOMER_NAME,								" \
        "		I.ATTN,	 										" \
        "		I.TAX_ID,	 									" \
        "		I.ADDRESS,	 									" \
        "		I.TEL_NO,	 									" \
        "		I.EMAIL,	 									" \
        "		I.VAT,											" \
        "		I.TOTAL_ALL,									" \
        "		I.PAYMENT_TYPE,									" \
        "		I.REF,											" \
        "		I.SUBJECT										" \
        "   FROM  invoice_head	i	                            " \
        "   LEFT JOIN SALES	s									" \
        "   ON i.CREATE_USER = s.SALES_ID						" \
        "   WHERE I.INVOICE_Type								" \
        "	    ||I.INVOICE_NO = '"+invoiceNo+"'	            " \
        "	    AND I.REVISED    = '" +rev+"'		            "
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        headInvoice['INVOICE_TYPE'] = row[0]
        headInvoice['INVOICE_NO'] = row[1]
        if(row[2]=="0"):
            headInvoice['REVISED'] = ""
        else:
            headInvoice['REVISED'] = " (REV"+row[2]+")"
        headInvoice['SALES_ID'] = row[3]
        headInvoice['SALES_NAME'] = row[4]
        headInvoice['ISSUE_DATE'] = row[5]
        headInvoice['DUE_DATE'] = row[6]
        headInvoice['DUE_DAY'] = row[7]
        headInvoice['CUSTOMER_ID'] = row[8]
        headInvoice['CUSTOMER_NAME'] = row[9]
        headInvoice['ATTN'] = row[10]
        headInvoice['TAX_ID'] = row[11]
        headInvoice['ADDRESS'] = row[12]
        headInvoice['TEL'] = row[13]
        headInvoice['EMAIL'] = row[14]
        headInvoice['VAT'] = row[15]
        headInvoice['TOTAL_ALL'] = row[16]
        headInvoice['PAYMENT_TYPE'] = row[17]
        headInvoice['REF'] = row[18]
        headInvoice['SUBJECT'] = row[19]

    sql =  "SELECT  SERVICE_NAME, 						" \
            "		SERVICE_TYPE,					 	" \
            "		QTY_AD,								" \
            "		PRICE,								" \
            "		TOTAL								" \
            "FROM  invoice_DETAIL	                    " \
            "WHERE INVOICE_Type	                		" \
            "	||INVOICE_NO = '"+invoiceNo+"'		    " \
            "	AND REVISED    = '"+rev+"'		    	" \
            "ORDER BY SEQ_NO							"
    cur.execute(sql)
    detailInvoice = cur.fetchall()

    cur.close()
    conn.close()

    return headInvoice,detailInvoice

