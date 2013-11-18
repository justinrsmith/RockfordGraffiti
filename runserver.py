from flask import Flask, render_template, jsonify, request, flash
import csv, operator
from collections import Counter, OrderedDict
app = Flask(__name__)
import json

@app.route('/', methods = ['POST', 'GET'])
def home():
    
    reader = csv.DictReader(open('Graffiti (10).csv'))

    result = {}
    for row in reader:
        for column, value in row.iteritems():
            result.setdefault(column, []).append(value)
    
    coords=zip(result.get('Latitude'),result.get('Longitude'))
    
    #loop through key and values
    keys = []

    for k,v in result.iteritems():
            keys.append(k)

    keys.sort()

    return render_template('test.html',
        keys=keys,
        coords=coords
        )


@app.route('/type/<string:valin>', methods = ['POST', 'GET'])
def sort(valin):

    reader = csv.DictReader(open('Graffiti (10).csv'))

    result = {}
    for row in reader:
        for column, value in row.iteritems():
            result.setdefault(column, []).append(value)
    
    x = (Counter(result.get(valin)))
    q=sorted(x.iteritems(), key=operator.itemgetter(1), reverse=True)

    return render_template('sort.html',
        test=q,
        type=valin)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():

    newdata=[]
    for x in request.form:
        newdata.append(request.form[x])

    return render_template('newrow.html',
        newdata=newdata)
   

@app.route('/get_requests', methods=['GET','POST'])
def request():

    a = {'contact': 'john doe', 'address': '43 5th st', 'comment': 'On Building'}
    b = {'contact': 'john doe2', 'address': '1413 15th st', 'comment': 'On Statue'}
    c = {'contact': 'john doe3', 'address': '56 Pleanseant Rd', 'comment': 'Covered'}

    request_list = []
    request_list.append(a)
    request_list.append(b)
    request_list.append(c)

    return render_template('request.html',
        request_list=request_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

    #app.debug=True