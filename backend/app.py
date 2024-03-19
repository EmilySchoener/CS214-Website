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

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json

    # Accessing specific keys in the JSON data
    cases = data.get('cases', [])
    intCases = int(cases)

    char = data.get('char', '')

    base1 = data.get('base1', [])
    intBase1 = int(base1)

    relation = data.get('relation', '')

    newRelation = unit3.getEquation(char, relation)

    if intCases == 1:
        resultArray = []
        array = unit3.oneBaseCase(intBase1,char,2,newRelation, resultArray)

        return jsonify(array)

    elif intCases == 2:
        base2 = data.get('base2', [])
        intBase2 = int(base2)
        return jsonify(char)
    elif intCases == 3:
        base2 = data.get('base2', [])
        intBase2 = int(base2)

        base3 = data.get('base3', [])
        intBase3 = int(base3)
        return jsonify(base1)
    else:
        return jsonify(relation)
        #print("issue")

    #return jsonify(cases)
    #return jsonify(data)





#@app.route('/submit', methods=['POST'])
#def submit_form_dummy():
   #return jsonify({'message': 'This is a dummy response for form submission.'})

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'This is data from Flask backend!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
