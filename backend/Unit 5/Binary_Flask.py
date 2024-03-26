from flask import Flask, jsonify, request
from flask_cors import CORS
import Binary_Relations
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

@app.route('/submitBinary', methods=['POST'])
def submit_form():

    global answer

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        strs = S.replace('[', '').split('],')
        lists = [map(int, S.replace(']', '').split(',')) for S in strs]
        answer = BinarySolution(lists)
        return jsonify(answer)

    elif request.method == 'GET':
        if answer is None:
            return 'No data available yet'
        else:
            return jsonify(answer)

    # Accessing specific keys in the JSON data
    #S = data.get('S', [])
    #strs = S.replace('[', '').split('],')
    #lists = [map(int, S.replace(']', '').split(',')) for S in strs]

def BinarySolution(lists):
    reflexive = Binary_Relations.antisymmetric_rel(lists)
    irreflexive = Binary_Relations.irreflexive_rel(lists)
    symmetric = Binary_Relations.symmetric_rel(lists)
    antisymmetric = Binary_Relations.antisymmetric_rel(lists)
    transitive = Binary_Relations.transitive_rel(lists)
    keyword = [''] * 5
    if reflexive:
        keyword[0] = "The list of S is reflexive"
    elif not reflexive:
        keyword[0] = "The list of S is not reflexive"

    if irreflexive:
        keyword[1] = "The list of S is irreflexive"
    elif not irreflexive:
        keyword[1] = "The list of S is not irreflexive"

    if symmetric:
        keyword[2] = "The list of S is symmetric"
    elif not symmetric:
        keyword[2] = "The list of S is not symmetric"

    if antisymmetric:
        keyword[3] = "The list of S is antisymmetric"
    elif not antisymmetric:
        keyword[3] = "The list of S is not antisymmetric"

    if transitive:
        keyword[4] = "The list of S is transitive"
    elif not transitive:
        keyword[4] = "The list of S is not transitive"

    return keyword




@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'This is data from Flask backend!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
