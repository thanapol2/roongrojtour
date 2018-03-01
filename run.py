import os
from flask import Flask, render_template,jsonify,request,json
from flask_cors import CORS
import backend.dao as dao
import backend.config_data as config_data
from werkzeug import utils
import backend.Tools as Tools

# Config flask
UPLOAD_FOLDER = './dist/static/image/tour_picture'
app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist/templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#  Config get data
config = config_data.config_data()
NATIONS = config.NATIONS
COUNTRYS = config.COUNTRYS
PROVINCES = config.PROVINCES
COMPANY_TYPES = config.COMPANY_TYPES
BANKS = config.BANKS
PAYMENT_TYPES = config.PAYMENT_TYPES
RT_TYPE = config.RT_TYPE
RTS_TYPE = config.RTS_TYPE


@app.route('/api/tour_list')
def searchTour():
    rows = dao.searchTour()
    return render_template("tour_search.html", rows=rows)

@app.route('/api/tour/<tourID>')
def getMember(tourID):
    # data = []
    if("C" in tourID):
        data = dao.getCompanyDetail(tourID)
        return render_template("company_detail.html", data=data, provinces=PROVINCES,types=COMPANY_TYPES)
    else:
        data = dao.getTourDetail(tourID)
        print(data)
        return render_template("tour_detail.html", data=data,countrys=COUNTRYS, nations=NATIONS, provinces=PROVINCES)

@app.route('/api/checked_name/<nameSurname>')
def checkName(nameSurname):
    data = nameSurname.split("_")
    if(dao.checkTourName(data[0],data[1])):
        return "<p style='color:green;'><b>OK</b></p>"
    else:
        return "<p style='color:red;'><b>" + data[0]+" "+data[1] + "</b> is already created.</p>"

@app.route('/api/tour', methods=['GET'])
def newTour():
    # if request.method == 'GET':
    data = []
    return render_template("tour_detail.html", data=data, countrys=COUNTRYS, nations=NATIONS, provinces=PROVINCES)
    # else: # post

@app.route('/api/tour', methods=['POST'])
def createupdate_tour():
    data = request.get_json()
    # issueDate = request.form['password']
    # print(data)
    if ("" == data["TOUR_ID"]):
        dao.newTour(data)
    else:
        dao.updateTour(data)
    return json.dumps({'status': 'OK'})

@app.route('/api/company', methods=['GET'])
def newCompany():
    data = []
    return render_template("company_detail.html", data=data, provinces=PROVINCES, types=COMPANY_TYPES)

@app.route('/api/company',methods = ['POST'])
def createupdate_company():
    data = request.get_json()
    if(data["COMPANY_ID"]==""):
        dao.newCompany(data)
    else:
        dao.updateCompany(data)
    return json.dumps({'status':'OK'})

#  Tour member ------------------------

@app.route('/api/invoice_list')
def searchInvoice():
    rows = dao.searchInvoice()
    return render_template("invoice_search.html", rows=rows)

@app.route('/api/payment_list')
def searchPayment():
    rows = dao.searchPayment()
    return render_template("payment_search.html", rows=rows)

@app.route('/api/invoice/<invoiceNo>' ,methods=['GET'])
def getInvoice(invoiceNo):
    invoiceNo = invoiceNo.replace("(", "")
    invoiceNo = invoiceNo.replace(")", "")
    invoiceTypes = []
    rev = "0"
    if("REV" in invoiceNo):
        temp = invoiceNo.split("REV")
        invoiceNo = temp[0]
        rev = temp[1]
    else:
        rev = "0"
    if("RTS" in invoiceNo):
        invoiceTypes = RTS_TYPE
    else:
        invoiceTypes = RT_TYPE
    data,rows = dao.getInvoiceDetail(invoiceNo,rev)
    return render_template("invoice_detail.html",data=data,rows=rows,invoiceTypes=invoiceTypes)

@app.route('/api/rtinvoice' ,methods=['GET'])
def newRTInvoice():
    invoiceTypes = RT_TYPE
    return render_template("invoice_detail.html",data=None,rows=[],invoiceTypes=invoiceTypes)

@app.route('/api/rtsinvoice' ,methods=['GET'])
def newRTSInvoice():
    invoiceTypes = RTS_TYPE
    return render_template("invoice_detail.html",data=None,rows=[],invoiceTypes=invoiceTypes)

#  payment_no = No_Type
@app.route('/api/payment/<paymentNo>' ,methods = ['GET'])
def getPayment(paymentNo):
    payment = paymentNo.split('_')
    data = dao.getPaymentDetail(payment[0],payment[1])
    return render_template("payment_detail.html",data=data,banks=BANKS,paymentTypes=PAYMENT_TYPES)

@app.route('/api/payment',methods = ['POST'])
def createupdate_payment():
    data = request.get_json()
    if(data["PAYMENT_NO"]==""):
        dao.newCompany(data)
    else:
        dao.updateCompany(data)
    return json.dumps({'status':'OK'})


@app.route('/api/noninvoice' ,methods=['GET'])
def create_noninvoicet():
    data = []
    return render_template("payment_detail.html", data=None, banks=BANKS, paymentTypes=PAYMENT_TYPES)


if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
    # app.run(host = '0.0.0.0',port=5000)
