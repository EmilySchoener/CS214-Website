from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import unit3
import Binary_Relations, Closure_Relations, Equivalence_Relations, Cyclical_Permutations, One_to_One, Onto, \
    Matrix_Multiplication, Boolean_Matrices, Composition_of_Cycles, Hasse_Diagram, MMGL
import unit4_1_1, unit4_1_2, unit4_1_3, unit4_1_4
import unit6_2_5
import unit7_1_2
import json
import Well_Formed_Formula

app = Flask(__name__, static_url_path='/backend')
CORS(app)


@app.route('/')
def index():
    return 'Hello, World!'


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
    # newRelation = unit3.getEquation(char, relation)

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
    condition = data.get("condition", [])
    intCondition = int(condition)
    set1 = data.get("set1", [])
    set1Array = unit4_1_1.convertArray(set1)
    set2 = data.get("set2", [])
    set2Array = unit4_1_1.convertArray(set2)
    set3 = data.get("set3", [])
    set3Array = unit4_1_1.convertArray(set3)
    leftSide = data.get("leftSide", [])
    rightSide = data.get("rightSide", [])

    if intCondition == 1:
        return unit4_1_1.elementOf(set1Array, set2Array, set3Array, leftSide, rightSide)
    elif intCondition == 2:
        return unit4_1_1.properSubset(set1Array, set2Array, set3Array, leftSide, rightSide)
    elif intCondition == 3:
        return unit4_1_1.subset(set1Array, set2Array, set3Array, leftSide, rightSide)
    else:
        return "error occurred"


string4_1_2 = None


@app.route('/4_1_2', methods=['GET', 'POST'])
def submit_4_1_2():
    global string4_1_2

    if request.method == 'POST':
        data = request.json
        string4_1_2 = SolveUnit4_1_2(data)
        return jsonify(string4_1_2)

    elif request.method == 'GET':
        if string4_1_2 is None:
            return 'No data available yet'
        else:
            return jsonify(string4_1_2)


def SolveUnit4_1_2(data):
    set = data.get("set", [])
    setArray = unit4_1_2.convertArray(set)
    return unit4_1_2.powerSet(setArray)


string4_1_3 = None


@app.route('/4_1_3', methods=['GET', 'POST'])
def submit_4_1_3():
    global string4_1_3

    if request.method == 'POST':
        data = request.json
        string4_1_3 = SolveUnit4_1_3(data)
        return jsonify(string4_1_3)

    elif request.method == 'GET':
        if string4_1_3 is None:
            return 'No data available yet'
        else:
            return jsonify(string4_1_3)


def SolveUnit4_1_3(data):
    set = data.get("set", [])
    set1Array = unit4_1_4.convertArray(set)
    oneOne = data.get("oneOne", [])
    oneTwo = data.get("oneTwo", [])
    oneThree = data.get("oneThree", [])
    twoOne = data.get("twoOne", [])
    twoTwo = data.get("twoTwo", [])
    twoThree = data.get("twoThree", [])
    threeOne = data.get("threeOne", [])
    threeTwo = data.get("threeTwo", [])
    threeThree = data.get("threeThree", [])
    return unit4_1_3.testMatrix(set1Array,oneOne,oneTwo,oneThree, twoOne, twoTwo, twoThree, threeOne, threeTwo, threeThree)


string4_1_4 = None


@app.route('/4_1_4', methods=['GET', 'POST'])
def submit_4_1_4():
    global string4_1_4

    if request.method == 'POST':
        data = request.json
        string4_1_4 = SolveUnit4_1_4(data)
        return jsonify(string4_1_4)

    elif request.method == 'GET':
        if string4_1_4 is None:
            return 'No data available yet'
        else:
            return jsonify(string4_1_4)


def SolveUnit4_1_4(data):
    condition = data.get("condition", [])
    intCondition = int(condition)
    set1 = data.get("set1", [])
    set1Array = unit4_1_4.convertArray(set1)
    set2 = data.get("set2", [])
    set2Array = unit4_1_4.convertArray(set2)
    set3 = data.get("set3", [])
    set3Array = unit4_1_4.convertArray(set3)
    subset = data.get("subset", [])
    subsetArray = unit4_1_4.convertArray(subset)
    leftSide = data.get("leftSide", [])
    rightSide = data.get("rightSide", [])

    if intCondition == 1:
        return unit4_1_4.Union(set1Array, set2Array, set3Array, leftSide, rightSide)
    elif intCondition == 2:
        return unit4_1_4.intersection(set1Array, set2Array, set3Array, leftSide, rightSide)
    elif intCondition == 3:
        return unit4_1_4.logicalNot(set1Array, set2Array, set3Array, subsetArray, leftSide)
    else:
        return "error occured"


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'This is data from Flask backend!'}
    return jsonify(data)


# answer = []
answer = None


@app.route('/submitBinary', methods=['GET', 'POST'])
def submit__5_1form():
    global answer

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        user_set = data.get('set', [])
        initialSet = json.loads(user_set)
        lists = json.loads(
            S)  # JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
        # strs = S.replace('[', '').split('],')
        # lists = [(int, S.replace(']', '').split(',')) for S in strs]
        # answer.append(BinarySolution(lists))
        answer = BinarySolution(lists, initialSet)
        answer.insert(0, S)
        return jsonify(answer)

    elif request.method == 'GET':
        if answer is None:
            return 'No data available yet'
        else:
            return jsonify(answer)

    # Accessing specific keys in the JSON data
    # S = data.get('S', [])
    # strs = S.replace('[', '').split('],')
    # lists = [map(int, S.replace(']', '').split(',')) for S in strs]


def BinarySolution(lists, set):
    # reflexive = True
    # irreflexive = True
    # symmetric = True
    # antisymmetric = True
    # transitive = True
    reflexive = Binary_Relations.reflexive_rel(lists, set)
    irreflexive = Binary_Relations.irreflexive_rel(lists)
    symmetric = Binary_Relations.symmetric_rel(lists)
    antisymmetric = Binary_Relations.antisymmetric_rel(lists)
    transitive = Binary_Relations.transitive_rel(lists)
    keyword = [''] * 7
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
    if antisymmetric and irreflexive:
        keyword[5] = "The list of S is asymmetric"
    elif not antisymmetric or not irreflexive:
        keyword[5] = "The list of S is not asymmetric"

    if reflexive and symmetric and transitive:
        keyword[6] = "The list of S is an equivalence relation"
    else:
        keyword[6] = "The list of S is not an equivalence relation"

    return keyword

diagram = None

@app.route('/submitHasse', methods=['GET','POST'])
def submit__Hasse_form():
    global diagram

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        diagram = Hasse_Diagram.Hasse_Diagram(S)
        return diagram

    elif request.method == 'GET':
        if diagram is None:
            return 'No data available yet'
        else:
            return diagram

closure = None


MMLG_answer = None


@app.route('/submitMMLG', methods=['GET', 'POST'])
def submit__MMGL_form():
    global MMLG_answer

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        user_set = data.get('set', [])
        MMLG_answer = MMGL.MMGL(S,user_set)
        return jsonify(MMLG_answer)

    elif request.method == 'GET':
        if MMLG_answer is None:
            return 'No data available yet'
        else:
            return jsonify(MMLG_answer)


@app.route('/submitClosure', methods=['GET', 'POST'])
def submit_closure_form():
    global closure

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        lists = json.loads(
            S)  # JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
        user_set = data.get('set', [])
        initialSet = json.loads(user_set)
        closure = ClosureSolution(lists, initialSet)
        # answer.insert(0, S)
        return jsonify(closure)

    elif request.method == 'GET':
        if closure is None:
            return 'No data available yet'
        else:
            return jsonify(closure)


def ClosureSolution(lists, initialSet):
    reflexive_closure = Closure_Relations.reflexive_closure(initialSet, lists)
    symmetric_closure = Closure_Relations.symmetric_closure(initialSet)
    transitive_closure = Closure_Relations.transitive_closure(initialSet, lists)
    keyword = [''] * 3
    if reflexive_closure != lists:
        keyword[0] = "The list of S has a reflexive closure of " + str(reflexive_closure)
    elif reflexive_closure == lists:
        keyword[0] = "The list of S does not have a reflexive closure"  # + str(reflexive_closure)
    if symmetric_closure != lists:
        keyword[1] = "The list of S has a symmetric closure of " + str(symmetric_closure)
    elif symmetric_closure == lists:
        keyword[1] = "The list of S does not have a symmetric closure"  # + str(symmetric_closure)
    if transitive_closure != lists:
        keyword[2] = "The list of S has a transitive closure of " + str(transitive_closure)
    elif transitive_closure == lists:
        keyword[2] = "The list of S does not have a transitive closure"  # + str(transitive_closure)

    return keyword


equivalence = None


@app.route('/submitEquivalence', methods=['GET', 'POST'])
def submit_equivalence_form():
    global equivalence

    if request.method == 'POST':
        data = request.json
        part1 = data.get('part1', [])
        part2 = data.get('part2', [])
        user_set = data.get('set', [])
        initialSet = json.loads(user_set)
        partition_1 = json.loads(
            part1)  # JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
        partition_2 = json.loads(part2)
        equivalence = Equivalence_Relations.equivalence_relations(partition_1, partition_2, initialSet)
        if not equivalence:
            equivalence = "There is no equivalence between the Set and the partitions"
            return jsonify(equivalence)
        else:
         equivalence = "The Equivalence Relation is: " + str(equivalence)
         return jsonify(equivalence)

    elif request.method == 'GET':
        if equivalence is None:
            return 'No data available yet'
        else:
            return jsonify(equivalence)


cycle = None


@app.route('/submitCyclical', methods=['GET', 'POST'])
def submit_cyclical_form():
    global cycle

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        lists = json.loads(S)
        user_set = data.get('set', [])
        initialSet = json.loads(user_set)
        cycle = Cyclical_Permutations.cycle_permutation(initialSet, lists)
        return cycle

    elif request.method == 'GET':
        if cycle is None:
            return 'No data available yet'
        else:
            return cycle


oneto = None


@app.route('/submitOneToOne', methods=['GET', 'POST'])
def submit_OneToOne_form():
    global oneto

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        domain = data.get('domain', [])
        codomain = data.get('codomain', [])
        func = data.get('func', [])
        d = json.loads(domain)
        cd = json.loads(codomain)
        f = json.loads(func)
        oneto = OneToOneSolution(d, cd, f)
        return jsonify(oneto)

    elif request.method == 'GET':
        if oneto is None:
            return 'No data available yet'
        else:
            return jsonify(oneto)


def OneToOneSolution(d, cd, f):
    OneToOne = One_to_One.one_to_one(d, cd, f)
    keyword = [''] * 1
    if OneToOne:
        keyword[0] = "The function is One to One"
    elif not OneToOne:
        keyword[0] = "The function is not One to One"

    return keyword


onto = None


@app.route('/submitOnto', methods=['GET', 'POST'])
def submit_Onto_form():
    global onto

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        domain = data.get('domain', [])
        codomain = data.get('codomain', [])
        func = data.get('func', [])
        d = json.loads(domain)
        cd = json.loads(codomain)
        f = json.loads(func)
        onto = OntoSolution(d, cd, f)
        return jsonify(onto)

    elif request.method == 'GET':
        if onto is None:
            return 'No data available yet'
        else:
            return jsonify(onto)


def OntoSolution(d, cd, f):
    onto = Onto.onto(d, cd, f)
    keyword = [''] * 1
    if onto:
        keyword[0] = "The function is Onto"
    elif not onto:
        keyword[0] = "The function is not Onto"

    return keyword


comp = None


@app.route('/submitComposition', methods=['GET', 'POST'])
def submit_comp_form():
    global comp

    if request.method == 'POST':
        data = request.json
        S = data.get('S', [])
        user_set = data.get('set', [])
        initialSet = json.loads(user_set)
        # lists = json.loads(S) #JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
        comp = Composition_of_Cycles.compose_cycles(S, initialSet)
        return comp

    elif request.method == 'GET':
        if comp is None:
            return 'No data available yet'
        else:
            return comp


mult = None
dot = None


@app.route('/submitMatrixMult', methods=['GET', 'POST'])
def submit_Mult_form():
    global mult
    global dot

    if request.method == 'POST':
        data = request.json
        matrix1 = data.get('matrix1', [])
        matrix2 = data.get('matrix2', [])
        m1 = json.loads(matrix1)
        m2 = json.loads(matrix2)
        mult = Matrix_Multiplication.matrix_mult(m1, m2)
        mult = "The Matrix Multiplication gives: " + str(mult)
        dot = Matrix_Multiplication.matrix_dot(m1, m2)
        dot = "The Dot Product gives: " + str(dot)
        return jsonify(mult, dot)

    elif request.method == 'GET':
        if mult is None and dot is None:
            return 'No data available yet'
        else:
            return jsonify(mult, dot)


bool_mat = None
bool_and = None
bool_or = None
bool_dot = None


@app.route('/submitBoolMatrix', methods=['GET', 'POST'])
def submit_Bool_form():
    global bool_mat
    global bool_and
    global bool_or
    global bool_dot

    if request.method == 'POST':
        data = request.json
        bool_matrix1 = data.get('bool_matrix1', [])
        bool_matrix2 = data.get('bool_matrix2', [])
        bool_m1 = json.loads(bool_matrix1)
        bool_m2 = json.loads(bool_matrix2)
        bool_mat = Boolean_Matrices.matrix_mult(bool_m1, bool_m2)
        bool_mat = "The Matrix Multiplication gives: " + str(bool_mat)
        bool_and = Boolean_Matrices.matrix_and(bool_m1, bool_m2)
        bool_and = "The Boolean And gives: " + str(bool_and)
        bool_or = Boolean_Matrices.matrix_or(bool_m1, bool_m2)
        bool_or = "The Boolean Or gives: " + str(bool_or)
        bool_dot = Boolean_Matrices.matrix_dot(bool_m1, bool_m2)
        bool_dot = "The Dot Product gives: " + str(bool_dot)
        return jsonify(bool_mat, bool_and, bool_or, bool_dot)

    elif request.method == 'GET':
        if bool_mat is None and bool_and is None and bool_or is None and bool_dot is None:
            return 'No data available yet'
        else:
            return jsonify(bool_mat, bool_and, bool_or, bool_dot)


@app.route('/submitwff', methods=['GET', 'POST'])
def submit_wff_form():
    try:
        data = request.json

        S = data.get('S', '')
        A = data.get('A', False)
        B = data.get('B', False)
        C = data.get('C', False)
        truthTable = data.get('truthTable', True)  # Default value is True if not provided

        if truthTable:
            result = Well_Formed_Formula.truth_table_func(S)

        else:
            # Perform your processing logic here using the Well_Formed_Formula module
            result = Well_Formed_Formula.process_wff(A, B, C, S)
            result = str(result)

            # Return the processed result
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e))


string6_2_5 = None


@app.route('/6_2_5', methods=['GET', 'POST'])
def submit_6_2_5():
    global string6_2_5

    if request.method == 'POST':
        data = request.json
        string6_2_5 = SolveUnit6_2_5(data)
        return jsonify(string6_2_5)

    elif request.method == 'GET':
        if string6_2_5 is None:
            return 'No data available yet'
        else:
            return jsonify(string6_2_5)


def SolveUnit6_2_5(data):
    notation = data.get("notation", [])
    intNotation = int(notation)
    userInput = data.get("input", [])

    if intNotation == 1:
        return unit6_2_5.prefix(userInput)

    elif intNotation == 2:
        return unit6_2_5.infix(userInput)

    elif intNotation == 3:
        return unit6_2_5.postfix(userInput)

    else:
        return "error occurred"


string7_1_2 = None


@app.route('/7_1_2', methods=['GET', 'POST'])
def submit_7_1_2():
    global string7_1_2

    if request.method == 'POST':
        data = request.json
        string7_1_2 = SolveUnit7_1_2(data)
        return jsonify(string7_1_2)

    elif request.method == 'GET':
        if string7_1_2 is None:
            return 'No data available yet'
        else:
            return jsonify(string7_1_2)


def SolveUnit7_1_2(data):
    oneOne = data.get("oneOne", [])
    oneTwo = data.get("oneTwo", [])
    oneThree = data.get("oneThree", [])
    oneFour = data.get("oneFour", [])
    twoOne = data.get("twoOne", [])
    twoTwo = data.get("twoTwo", [])
    twoThree = data.get("twoThree", [])
    twoFour = data.get("twoFour", [])
    threeOne = data.get("threeOne", [])
    threeTwo = data.get("threeTwo", [])
    threeThree = data.get("threeThree", [])
    threeFour = data.get("threeFour", [])
    fourOne = data.get("fourOne", [])
    fourTwo = data.get("fourTwo", [])
    fourThree = data.get("fourThree", [])
    fourFour = data.get("fourFour", [])
    if (oneFour == "-"):
        return unit7_1_2.ThreeByThree(oneOne, oneTwo, oneThree, twoOne, twoTwo, twoThree, threeOne, threeTwo, threeThree)
    else:
        return unit7_1_2.FourByFour(oneOne, oneTwo, oneThree,oneFour, twoOne, twoTwo, twoThree,twoFour, threeOne, threeTwo, threeThree, threeFour, fourOne, fourTwo, fourThree, fourFour)


if __name__ == '__main__':
    app.run(debug=True)
