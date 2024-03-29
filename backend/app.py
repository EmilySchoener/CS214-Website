from flask import Flask, jsonify, request
from flask_cors import CORS
import unit3
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

#@app.route('/submit', methods=['POST'])
#def submit_form():
    #data = request.json
    #print('Received data:', data)
    # Process the data and return a response
    #return jsonify({'message': 'Form submitted successfully!'})
    #return jsonify(data)

array = None

@app.route('/3_1', methods=['GET', 'POST'])
def submit_form():
    global array

    if request.method == 'POST':
        data = request.json
        array = SolveUnit3(data)
        return jsonify(array)

    elif request.method == 'GET':
        if array is None:
            return 'No data available yet'
        else:
            return jsonify(array)

def SolveUnit3(data):
    # Accessing specific keys in the JSON data
    cases = data.get('cases', [])
    intCases = int(cases)
    char = data.get('char', '')
    base1 = data.get('base1', [])
    intBase1 = int(base1)
    relation = data.get('relation', "")
    #newRelation = unit3.getEquation(char, relation)

    if intCases == 1:
        resultArray = []
        return unit3.oneBaseCase(intBase1, char, 2, relation, resultArray)

    elif intCases == 2:
        resultArray = []
        base2 = data.get('base2', [])
        intBase2 = int(base2)
        return unit3.twoBaseCase(intBase1, intBase2, char, 3, relation, resultArray)

    elif intCases == 3:
        resultArray = []
        base2 = data.get('base2', [])
        intBase2 = int(base2)

        base3 = data.get('base3', [])
        intBase3 = int(base3)
        return unit3.threeBaseCase(intBase1, intBase2, intBase3, char, 4, relation, resultArray)
    else:
        return "error occured"



#@app.route('/submit', methods=['POST'])
#def submit_form_dummy():
   #return jsonify({'message': 'This is a dummy response for form submission.'})

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'This is data from Flask backend!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
