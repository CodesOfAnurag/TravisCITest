import flask
from flask import request, jsonify
from CardValidity import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/validity', methods=['GET'])
def api_call():
    print(request.args)
    cardInfoValidity = dict()
    if 'name' in request.args:
        cardInfoValidity['name'] = validName(request.args['name'])
    if 'cardNo' in request.args:
        cardInfoValidity['cardNo'] = validCardNo(request.args['cardNo'])
    if 'cvv' in request.args:
        cardInfoValidity['cvv'] = validCVV(request.args['cvv'])
    if 'date' in request.args:
        cardInfoValidity['date'] = validDate(request.args['date'])
    if len(cardInfoValidity)==4:
        cardInfoValidity['card_validity'] = all(cardInfoValidity.values())
    return jsonify(cardInfoValidity)

app.run()
