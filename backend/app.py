from flask import Flask, jsonify, request
from flask_cors import CORS
import unit3
import Binary_Relations, Closure_Relations, Equivalence_Relations
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


string4_1_1 = None

@app.route('/4_1_1', methods=['GET', 'POST'])
def submit_4_1_1():
    global string4_1_1

    if request.method == 'POST':
        data = request.json
        string4_1_1 = SolveUnit4_1_1(data)
        return jsonify(string4_1_1)

    elif request.method == 'GET':
        if string4_1_1 is None:
            return 'No data available yet'
        else:
            return jsonify(string4_1_1)


def SolveUnit4_1_1(data):
    return "True"



@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'This is data from Flask backend!'}
    return jsonify(data)

#answer = []
answer = None
@app.route('/submitBinary', methods=['GET', 'POST'])
def submit__5_1form():

    global answer

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        lists = json.loads(S) #JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
        #strs = S.replace('[', '').split('],')
        #lists = [(int, S.replace(']', '').split(',')) for S in strs]
        #answer.append(BinarySolution(lists))
        answer = BinarySolution(lists)
        answer.insert(0, S)
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
   # reflexive = True
    #irreflexive = True
    #symmetric = True
   # antisymmetric = True
   # transitive = True
    reflexive = Binary_Relations.reflexive_rel(lists)
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

closure = None
@app.route('/submitClosure', methods=['GET', 'POST'])
def submit_closure_form():

    global closure

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        lists = json.loads(S) #JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
        closure = ClosureSolution(lists)
        #answer.insert(0, S)
        return jsonify(closure)

    elif request.method == 'GET':
        if closure is None:
            return 'No data available yet'
        else:
            return jsonify(closure)

def ClosureSolution(lists):
    reflexive_closure = Closure_Relations.reflexive_closure(lists)
    symmetric_closure = Closure_Relations.symmetric_closure(lists)
    transitive_closure = Closure_Relations.transitive_closure(lists)
    keyword = [''] * 3
    if reflexive_closure != lists:
        keyword[0] = "The list of S has a reflexive closure of " + str(reflexive_closure)
    elif reflexive_closure == lists:
        keyword[0] = "The list of S does not have a reflexive closure" #+ str(reflexive_closure)
    if symmetric_closure != lists:
        keyword[1] = "The list of S has a symmetric closure of " + str(symmetric_closure)
    elif symmetric_closure == lists:
        keyword[1] = "The list of S does not have a symmetric closure" #+ str(symmetric_closure)
    if transitive_closure != lists:
        keyword[2] = "The list of S has a transitive closure of " + str(transitive_closure)
    elif transitive_closure == lists:
        keyword[2] = "The list of S does not have a transitive closure" #+ str(transitive_closure)

    return keyword

equivalence = None
@app.route('/submitEquivalence', methods=['GET', 'POST'])
def submit_equivalence_form():

    global equivalence

    if request.method == 'POST':
        data = request.json
        part1 = data.get('part1', [])
        part2 = data.get('part2', [])
        partition_1 = json.loads(part1) #JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
        partition_2 = json.loads(part2)
        equivalence = Equivalence_Relations.equivalence_relations(partition_1, partition_2)
        return jsonify(equivalence)

    elif request.method == 'GET':
        if equivalence is None:
            return 'No data available yet'
        else:
            return jsonify(equivalence)

if __name__ == '__main__':
    app.run(debug=True)