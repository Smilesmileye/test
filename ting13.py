from flask import Blueprint
app = Blueprint('apk',__name__)

@app.route('/tengliting',methods=['POST'])
def tengliting():
    return '“    201806404113✌     滕丽婷✌      耶耶耶✌          ” '