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
def getTour():
    rows = dao.searchTour()
    return render_template("tour_search.html", rows=rows)

@app.route('/api/search_invoice')
def getInvoice():
    rows = dao.searchInvoice()
    return render_template("invoice_search.html", rows=rows)

@app.route('/api/search_payment')
def getPayment():
    rows = dao.searchPayment()
    return render_template("payment_search.html", rows=rows)

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run()
