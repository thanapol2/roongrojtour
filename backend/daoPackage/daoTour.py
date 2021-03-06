import configparser
import cx_Oracle
import os
from backend.daoPackage import daoAbstact as db


class daoTour():
    def __init__(self):
        return 'hello world'

        def searchTour():
            conn = cx_Oracle.connect(db.dao.USER, db.dao.PASS, db.dao.DB_URL)
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

    def createUpdateTour(data):
        conn = cx_Oracle.connect(db.dao.USER, db.dao.PASS, db.dao.DB_URL)
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
        conn = cx_Oracle.connect(db.dao.USER, db.dao.PASS, db.dao.DB_URL)
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
        conn = cx_Oracle.connect(db.dao.USER, db.dao.PASS, db.dao.DB_URL)
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
        conn = cx_Oracle.connect(db.dao.USER, db.dao.PASS, db.dao.DB_URL)
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