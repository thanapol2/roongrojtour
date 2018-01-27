ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

def genToDateSQL(date):
    if date is not None :
        sql = "TO_date('"+date+"','YYYY-MM-DD')"
        return sql
    else:
        return None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS