from flask import Flask, render_template,jsonify
from flask_cors import CORS
import  backend.dao as dao

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist/templates")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# @app.route('/api/random')
# def random_number():
#     rows = dao.getTour()
#     return jsonify(rows)

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
def getTour(tourID):
    data = dao.getTour(tourID)
    return render_template("tour_detail.html", data=data)

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run()
