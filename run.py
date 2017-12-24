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

@app.route('/api/search_tour')
def searchTour():
    rows = dao.searchTour()
    return render_template("tour_search.html", rows=rows)

@app.route('/api/search_invoice')
def searchInvoice():
    rows = dao.searchInvoice()
    return render_template("invoice_search.html", rows=rows)

@app.route('/api/search_payment')
def searchPayment():
    rows = dao.searchPayment()
    return render_template("payment_search.html", rows=rows)

@app.route('/api/search_tour/<tourID>')
def getMember(tourID):
    # data = []
    if("C" in tourID):
        data = dao.getCompanyDetail(tourID)
        return render_template("company_detail.html", data=data, provinces=PROVINCES,types=COMPANY_TYPES)
    else:
        data = dao.getTourDetail(tourID)
        return render_template("tour_detail.html", data=data,countrys=COUNTRYS, nations=NATIONS, provinces=PROVINCES)

@app.route('/api/temp/<tourID>')
def temp(tourID):
    data = []
    # data = dao.getTour(tourID)
    return render_template("company_detail.html", data=data)

@app.route('/api/update_tour',methods = ['POST'])
def createupdate_tour():
    passport =  request.get_json()
    # issueDate = request.form['password']
    print(passport["name_th"])
    # print(issueDate)
    return json.dumps({'status':'OK','user':passport})

@app.route('/api/search_invoice/<invoiceNo>')
def getInvoice(invoiceNo):
    data = []
    return render_template("invoice_detail.html",data=data)

@app.route('/api/search_payment/<paymentNo>')
def getPayment(paymentNo):
    data = []
    return render_template("payment_detail.html",data=data,banks=BANKS,paymentTypes=PAYMENT_TYPES)


@app.route('/api/signUp')
def signUp():
    return render_template('test.html')

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
