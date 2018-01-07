from flask import Flask, render_template,jsonify,request,json
from flask_cors import CORS
import backend.dao as dao
import backend.config_data as config_data


app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist/templates")
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

#  Tour member ------------------------
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
        return render_template("tour_detail.html", data=data,countrys=COUNTRYS, nations=NATIONS, provinces=PROVINCES)

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
    if(data["tour_id"]==""):
        print("new")
    else:
        print("update")
    # print(issueDate)
    return json.dumps({'status':'OK','user':data})

@app.route('/api/update_company',methods = ['POST'])
def createupdate_company():
    data =  request.get_json()
    # issueDate = request.form['password']
    print(data)
    if(data["COMPANY_ID"]==""):
        dao.newCompany(data)
    else:
        print("update")
    # print(issueDate)
    return json.dumps({'status':'OK','user':data})

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

#  payment_no = No_Type
@app.route('/api/search_payment/<paymentNo>')
def getPayment(paymentNo):
    payment = paymentNo.split('_')
    data = dao.getPaymentDetail(payment[0],payment[1])
    return render_template("payment_detail.html",data=data,banks=BANKS,paymentTypes=PAYMENT_TYPES)


@app.route('/api/signUp')
def signUp():
    return render_template('test.html')

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
