import os
from flask import Flask, render_template, jsonify, request, json , redirect, url_for
from flask_cors import CORS
import backend.dao as dao
import backend.config_data as config_data
from werkzeug import utils
import backend.Tools as Tools

UPLOAD_FOLDER = './dist/static/image/tour_picture'
app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist/templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/test', methods=['POST','GET'])
def test():
   if request.method == 'POST':
      result = request.form
      d = result["json"]
      # d = json.loads(result["json"])
      print(d)
      return redirect(url_for('hello'))
   else:
       user = request.args.get('nm')
       print("post")
       print(user)
       return redirect(url_for('hello'))

#  Tour member ------------------------
@app.route('/api/upload')
def upload():
   return render_template('upload.html')


@app.route('/api/hello')
def hello():
   return ("hello world")

@app.route('/api/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and Tools.allowed_file(file.filename):
            filename = utils.secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return 'file uploaded successfully'

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
    # app.run(host = '0.0.0.0',port=5000)
