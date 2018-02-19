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


@app.route('/api/search_tour')
def searchTour():
    rows = dao.searchTour()
    return render_template("tour_search.html", rows=rows)

@app.route('/api/search_tour/<tourID>')
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

@app.route('/api/new_tour')
def newTour():
    data = []
    return render_template("tour_detail.html", data=data, countrys=COUNTRYS, nations=NATIONS, provinces=PROVINCES)

@app.route('/api/new_company')
def newCompany():
    data = []
    return render_template("company_detail.html", data=data, provinces=PROVINCES, types=COMPANY_TYPES)

@app.route('/api/update_tour',methods = ['POST'])
def createupdate_tour():
    data =  request.get_json()
    # issueDate = request.form['password']
    print(data)
    if(""==data["TOUR_ID"]):
        dao.newTour(data)
    else:
        dao.updateTour(data)
    return json.dumps({'status':'OK'})

@app.route('/api/update_company',methods = ['POST'])
def createupdate_company():
    data = request.get_json()
    if(data["COMPANY_ID"]==""):
        dao.newCompany(data)
    else:
        dao.updateCompany(data)
    return json.dumps({'status':'OK'})

#  Tour member ------------------------

@app.route('/api/search_invoice')
def searchInvoice():
    rows = dao.searchInvoice()
    return render_template("invoice_search.html", rows=rows)

@app.route('/api/search_payment')
def searchPayment():
    rows = dao.searchPayment()
    return render_template("payment_search.html", rows=rows)

@app.route('/api/search_invoice/<invoiceNo>')
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

@app.route('/api/new_invoice/<invoiceType>')
def newInvoice(invoiceType):
    invoiceTypes = []
    if("rts" in invoiceType):
        invoiceTypes = RTS_TYPE
    else:
        invoiceTypes = RT_TYPE
    return render_template("invoice_detail.html",data=[],rows=[],invoiceTypes=invoiceTypes)

#  payment_no = No_Type
@app.route('/api/search_payment/<paymentNo>')
def getPayment(paymentNo):
    payment = paymentNo.split('_')
    data = dao.getPaymentDetail(payment[0],payment[1])
    return render_template("payment_detail.html",data=data,banks=BANKS,paymentTypes=PAYMENT_TYPES)

@app.route('/api/create_noninvoice')
def create_noninvoicet():
    data = []
    return render_template("payment_detail.html", data=data, banks=BANKS, paymentTypes=PAYMENT_TYPES)

@app.route('/api/update_payment',methods = ['POST'])
def createupdate_payment():
    data = request.get_json()
    if(data["PAYMENT_NO"]==""):
        dao.newCompany(data)
    else:
        dao.updateCompany(data)
    return json.dumps({'status':'OK'})

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
    # app.run(host = '0.0.0.0',port=5000)
