from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import unit3
import Binary_Relations, Closure_Relations, Equivalence_Relations, Cyclical_Permutations, One_to_One, Onto, \
    Matrix_Multiplication, Boolean_Matrices, Composition_of_Cycles, Hasse_Diagram, MMGL, Masters_Theorem, \
    Order_Of_Magnitude, Sequential_Tasks
import unit4_1_1, unit4_1_2, unit4_1_3, unit4_1_4
import unit6_2_5
import unit7_1_2, unit7_1_3, unit7_1_5
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
    keyword = [''] * 8
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

    if reflexive and antisymmetric and transitive:
        keyword[7] = "The list of S is a partial order or poset of the initial set"
    else:
        keyword[7] = "The list of S is not a partial order or poset of the initial set"

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


MMLG_answer = None


@app.route('/submitMMLG', methods=['GET', 'POST'])
def submit__MMGL_form():
    global MMLG_answer

    if request.method == 'POST':
        data = request.json
        print("Received data:", data)
        user_set = data.get('set', [])
        S = data.get('S', [])
        print("Received S:", S)
        print("Type of S:", type(S))
        MMLG_answer = MMGL.MMGL(user_set, S)
        return jsonify(MMLG_answer)

    elif request.method == 'GET':
        if MMLG_answer is None:
            return 'No data available yet'
        else:
            return jsonify(MMLG_answer)

closure = None
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
        part3 = data.get('part3', [])
        user_set = data.get('set', [])
       # initialSet = json.loads(user_set)
       # partition_1 = json.loads(part1)  # JSON.LOADS IS THE WAY TO DO IT, USE THIS FOR FUTURE THINGS, this will take the string input and put it into integers
       # partition_2 = json.loads(part2)
        if part3 == None:
            equivalence = Equivalence_Relations.equivalence_relations(part1, part2, user_set)
        else:
            equivalence = Equivalence_Relations.equivalence_relations_three(part1,part2,part3,user_set)

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

@app.route('/submitTasks', methods=['POST'])
def submit_ordered_tasks():
    try:
        tasks = request.json.get('tasks', [])
        tasks_with_prerequisites = {}
        for task_id, task_info in enumerate(tasks, start=1):
            task_info_parts = task_info.split(', Prerequisite')
            task_name = task_info_parts[0].strip()
            prerequisites = []
            if len(task_info_parts) > 1:
                prerequisites_str = task_info_parts[1].replace("Tasks are", "").replace("Task is", "").strip()
                prerequisites = [int(p.strip().split()[-1]) for p in prerequisites_str.split('and') if
                                 p.strip().split()[-1].isdigit()]
            tasks_with_prerequisites[task_id] = {"name": task_name, "prerequisites": prerequisites}

        tasks_in_order = Sequential_Tasks.find_task_order(tasks_with_prerequisites)
        return jsonify({"Ordered Tasks": tasks_in_order})

        print("Tasks with prerequisites:", tasks_with_prerequisites)
        tasks_in_order = Sequential_Tasks.find_task_order(tasks_with_prerequisites)
        return jsonify({"Ordered Tasks": tasks_in_order})

    except Exception as e:
        print("Error processing tasks:", e)
        return jsonify({"error": "Error processing tasks",}), 400

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



mast_theorem = None

@app.route('/submitMasterTheorem', methods=['GET', 'POST'])
def submit_master_theorem():
    global mast_theorem

    if request.method == 'POST':
        data = request.json
        a = data.get('a', [])
        intA = int(a)
        b = data.get('b', [])
        intB = int(b)
        c = data.get('c', [])
        intC = float(c)
        mast_theorem = str(Masters_Theorem.master_theorem(intA, intB, intC))
        return mast_theorem

    elif request.method == 'GET':
        if mast_theorem is None:
            return 'No data available yet'
        else:
            return mast_theorem

mult = None
dot = None


order_mag = None

@app.route('/submitOrderOfMag', methods=['GET', 'POST'])
def submit_order_mag():
    global order_mag

    if request.method == 'POST':
        data = request.json
        f = data.get('f', [])
        strF = str(f)
        g = data.get('g', [])
        strG = str(g)
        x = data.get('x', [])
        intX = float(x)
        if intX <= 0:
            return order_mag
        order_mag = Order_Of_Magnitude.find_constants(strF, strG, intX)
        return order_mag

    elif request.method == 'GET':
        if order_mag is None:
            return 'No data available yet'
        else:
            return order_mag

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



string_bool_data = None


@app.route('/submitBoolMatrix', methods=['GET', 'POST'])
def submit_Bool_form():
    global string_bool_data

    if request.method == 'POST':
        data = request.json
        string_bool_data = Solve_Bool_Matrix(data)
        return jsonify(string_bool_data)

    elif request.method == 'GET':
        if string_bool_data is None:
            return 'No data available yet'
        else:
            return jsonify(string_bool_data)


def Solve_Bool_Matrix(data):
    mat1oneOne = data.get("oneOne", [])
    mat1oneTwo = data.get("oneTwo", [])
    mat1oneThree = data.get("oneThree", [])
    mat1oneFour = data.get("oneFour", [])
    mat1twoOne = data.get("twoOne", [])
    mat1twoTwo = data.get("twoTwo", [])
    mat1twoThree = data.get("twoThree", [])
    mat1twoFour = data.get("twoFour", [])
    mat1threeOne = data.get("threeOne", [])
    mat1threeTwo = data.get("threeTwo", [])
    mat1threeThree = data.get("threeThree", [])
    mat1threeFour = data.get("threeFour", [])
    mat1fourOne = data.get("fourOne", [])
    mat1fourTwo = data.get("fourTwo", [])
    mat1fourThree = data.get("fourThree", [])
    mat1fourFour = data.get("fourFour", [])

    mat_2oneOne = data.get("mat_2oneOne", [])
    mat_2oneTwo = data.get("mat_2oneTwo", [])
    mat_2oneThree = data.get("mat_2oneThree", [])
    mat_2oneFour = data.get("mat_2oneFour", [])
    mat_2twoOne = data.get("mat_2twoOne", [])
    mat_2twoTwo = data.get("mat_2twoTwo", [])
    mat_2twoThree = data.get("mat_2twoThree", [])
    mat_2twoFour = data.get("mat_2twoFour", [])
    mat_2threeOne = data.get("mat_2threeOne", [])
    mat_2threeTwo = data.get("mat_2threeTwo", [])
    mat_2threeThree = data.get("mat_2threeThree", [])
    mat_2threeFour = data.get("mat_2threeFour", [])
    mat_2fourOne = data.get("mat_2fourOne", [])
    mat_2fourTwo = data.get("mat_2fourTwo", [])
    mat_2fourThree = data.get("mat_2fourThree", [])
    mat_2fourFour = data.get("mat_2fourFour", [])

    if mat1oneThree == "-" and mat1twoThree == "-" and mat1threeThree == "-" and mat1fourThree == "-" and mat1oneFour == "-" and mat1twoFour == "-" and mat1threeFour == "-" and mat1fourFour == "-" and mat_2oneThree == "-" and mat_2twoThree == "-" and mat_2threeThree == "-" and mat_2threeFour == "-" and mat_2fourOne == "-" and mat_2fourTwo == "-" and mat_2fourThree == "-" and mat_2fourFour ==  "-"  :
        mat1oneOne = int(mat1oneOne)
        mat1oneTwo = int(mat1oneTwo)
        mat1twoOne = int(mat1twoOne)
        mat1twoTwo = int(mat1twoTwo)

        mat_2oneOne = int(mat_2oneOne)
        mat_2oneTwo = int(mat_2oneTwo)
        mat_2twoOne = int(mat_2twoOne)
        mat_2twoTwo = int(mat_2twoTwo)
        A = [[0, 0],[0, 0]]
        A[0][0] = mat1oneOne
        A[0][1] = mat1oneTwo
        A[1][0] = mat1twoOne
        A[1][1] = mat1twoTwo

        B = [[0, 0], [0, 0]]
        B[0][0] = mat_2oneOne
        B[0][1] = mat_2oneTwo
        B[1][0] = mat_2twoOne
        B[1][1] = mat_2twoTwo

        and_2x2 = Boolean_Matrices.matrix_and_2x2(A,B)
        or_2x2 = Boolean_Matrices.matrix_or_2x2(A,B)
        AxB_2x2 = Boolean_Matrices.matrix_mult_2x2(A,B)
        AxB_2x2_reverse = Boolean_Matrices.matrix_mult_reverse_2x2(B,A)
        mat_key = [''] * 4
        mat_key[0] = and_2x2
        mat_key[1] = or_2x2
        mat_key[2] = AxB_2x2
        mat_key[3] = AxB_2x2_reverse
        return mat_key

    if mat1oneThree != "-" and mat1twoThree != "-" and mat1threeThree != "-" and mat1fourThree == "-" and mat1oneFour == "-" and mat1twoFour == "-" and mat1threeFour == "-" and mat1fourFour == "-" and mat_2oneThree != "-" and mat_2twoThree != "-" and mat_2threeThree != "-" and mat_2threeFour == "-" and mat_2fourOne == "-" and mat_2fourTwo == "-" and mat_2fourThree == "-" and mat_2fourFour == "-":
        mat1oneOne = int(mat1oneOne)
        mat1oneTwo = int(mat1oneTwo)
        mat1oneThree = int(mat1oneThree)
        mat1twoOne = int(mat1twoOne)
        mat1twoTwo = int(mat1twoTwo)
        mat1twoThree = int(mat1twoThree)
        mat1threeOne = int(mat1threeOne)
        mat1threeTwo = int(mat1threeTwo)
        mat1threeThree = int(mat1threeThree)

        mat_2oneOne = int(mat_2oneOne)
        mat_2oneTwo = int(mat_2oneTwo)
        mat_2oneThree = int(mat_2oneThree)
        mat_2twoOne = int(mat_2twoOne)
        mat_2twoTwo = int(mat_2twoTwo)
        mat_2twoThree = int(mat_2twoThree)
        mat_2threeOne = int(mat_2threeOne)
        mat_2threeTwo = int(mat_2threeTwo)
        mat_2threeThree = int(mat_2threeThree)
        A = [[0, 0, 0],[0, 0, 0], [0,0,0]]
        A[0][0] = mat1oneOne
        A[0][1] = mat1oneTwo
        A[0][2] = mat1oneThree
        A[1][0] = mat1twoOne
        A[1][1] = mat1twoTwo
        A[1][2] = mat1twoThree
        A[2][0] = mat1threeOne
        A[2][1] = mat1threeTwo
        A[2][2] = mat1threeThree

        B = [[0, 0, 0],[0, 0, 0], [0,0,0]]
        B[0][0] = mat_2oneOne
        B[0][1] = mat_2oneTwo
        B[0][2] = mat_2oneThree
        B[1][0] = mat_2twoOne
        B[1][1] = mat_2twoTwo
        B[1][2] = mat_2twoThree
        B[2][0] = mat_2threeOne
        B[2][1] = mat_2threeTwo
        B[2][2] = mat_2threeThree

        and_3x3 = Boolean_Matrices.matrix_and_3x3(A,B)
        or_3x3 = Boolean_Matrices.matrix_or_3x3(A,B)
        AxB_3x3 = Boolean_Matrices.matrix_mult_3x3(A,B)
        AxB_3x3_reverse = Boolean_Matrices.matrix_mult_reverse_3x3(B,A)
        mat_key = [''] * 4
        mat_key[0] = and_3x3
        mat_key[1] = or_3x3
        mat_key[2] = AxB_3x3
        mat_key[3] = AxB_3x3_reverse
        return mat_key

    if mat1oneThree != "-" and mat1twoThree != "-" and mat1threeThree != "-" and mat1fourThree != "-" and mat1oneFour != "-" and mat1twoFour != "-" and mat1threeFour != "-" and mat1fourFour != "" and mat_2oneThree != "-" and mat_2twoThree != "-" and mat_2threeThree != "-" and mat_2threeFour != "-" and mat_2fourOne != "-" and mat_2fourTwo != "-" and mat_2fourThree != "-" and mat_2fourFour !=  "-"  :
        mat1oneOne = int(mat1oneOne)
        mat1oneTwo = int(mat1oneTwo)
        mat1oneThree = int(mat1oneThree)
        mat1oneFour = int(mat1oneFour)
        mat1twoOne = int(mat1twoOne)
        mat1twoTwo = int(mat1twoTwo)
        mat1twoThree = int(mat1twoThree)
        mat1twoFour = int(mat1twoFour)
        mat1threeOne = int(mat1threeOne)
        mat1threeTwo = int(mat1threeTwo)
        mat1threeThree = int(mat1threeThree)
        mat1threeFour = int(mat1threeFour)
        mat1fourOne = int(mat1fourOne)
        mat1fourTwo = int(mat1fourTwo)
        mat1fourThree = int(mat1fourThree)
        mat1fourFour = int(mat1fourFour)

        mat_2oneOne = int(mat_2oneOne)
        mat_2oneTwo = int(mat_2oneTwo)
        mat_2oneThree = int(mat_2oneThree)
        mat_2oneFour = int(mat_2oneFour)
        mat_2twoOne = int(mat_2twoOne)
        mat_2twoTwo = int(mat_2twoTwo)
        mat_2twoThree = int(mat_2twoThree)
        mat_2twoFour = int(mat_2twoFour)
        mat_2threeOne = int(mat_2threeOne)
        mat_2threeTwo = int(mat_2threeTwo)
        mat_2threeThree = int(mat_2threeThree)
        mat_2threeFour = int(mat_2threeFour)
        mat_2fourOne = int(mat_2fourOne)
        mat_2fourTwo = int(mat_2fourTwo)
        mat_2fourThree = int(mat_2fourThree)
        mat_2fourFour = int(mat_2fourFour)
        A = [[0, 0, 0, 0],[0, 0, 0,0], [0,0,0,0], [0,0,0,0]]
        A[0][0] = mat1oneOne
        A[0][1] = mat1oneTwo
        A[0][2] = mat1oneThree
        A[0][3] = mat1oneFour
        A[1][0] = mat1twoOne
        A[1][1] = mat1twoTwo
        A[1][2] = mat1twoThree
        A[1][3] = mat1twoFour
        A[2][0] = mat1threeOne
        A[2][1] = mat1threeTwo
        A[2][2] = mat1threeThree
        A[2][3] = mat1threeFour
        A[3][0] = mat1fourOne
        A[3][1] = mat1fourTwo
        A[3][2] = mat1fourThree
        A[3][3] = mat1fourFour

        B = [[0, 0, 0, 0],[0, 0, 0, 0], [0,0,0, 0], [0,0,0,0]]
        B[0][0] = mat_2oneOne
        B[0][1] = mat_2oneTwo
        B[0][2] = mat_2oneThree
        B[0][3] = mat_2oneFour
        B[1][0] = mat_2twoOne
        B[1][1] = mat_2twoTwo
        B[1][2] = mat_2twoThree
        B[1][3] = mat_2twoFour
        B[2][0] = mat_2threeOne
        B[2][1] = mat_2threeTwo
        B[2][2] = mat_2threeThree
        B[2][3] = mat_2threeFour
        B[3][0] = mat_2fourOne
        B[3][1] = mat_2fourTwo
        B[3][2] = mat_2fourThree
        B[3][3] = mat_2fourFour

        and_4x4 = Boolean_Matrices.matrix_and_4x4(A,B)
        or_4x4 = Boolean_Matrices.matrix_or_4x4(A,B)
        AxB_4x4 = Boolean_Matrices.matrix_mult_4x4(A,B)
        AxB_4x4_reverse = Boolean_Matrices.matrix_mult_reverse_4x4(B,A)
        mat_key = [''] * 4
        mat_key[0] = and_4x4
        mat_key[1] = or_4x4
        mat_key[2] = AxB_4x4
        mat_key[3] = AxB_4x4_reverse
        return mat_key




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

            # Return the processed result
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error="Error")


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


string7_1_3 = None


@app.route('/7_1_3', methods=['GET', 'POST'])
def submit_7_1_3():
    global string7_1_3

    if request.method == 'POST':
        data = request.json
        string7_1_3 = SolveUnit7_1_3(data)
        return jsonify(string7_1_3)

    elif request.method == 'GET':
        if string7_1_3 is None:
            return 'No data available yet'
        else:
            return jsonify(string7_1_3)


def SolveUnit7_1_3(data):
    algo = data.get("algo", [])
    intAlgo = int(algo)
    oneOne = data.get("oneOne", [])
    oneTwo = data.get("oneTwo", [])
    oneThree = data.get("oneThree", [])
    oneFour = data.get("oneFour", [])
    oneFive = data.get("oneFive", [])
    twoOne = data.get("twoOne", [])
    twoTwo = data.get("twoTwo", [])
    twoThree = data.get("twoThree", [])
    twoFour = data.get("twoFour", [])
    twoFive = data.get("twoFive", [])
    threeOne = data.get("threeOne", [])
    threeTwo = data.get("threeTwo", [])
    threeThree = data.get("threeThree", [])
    threeFour = data.get("threeFour", [])
    threeFive = data.get("threeFive", [])
    fourOne = data.get("fourOne", [])
    fourTwo = data.get("fourTwo", [])
    fourThree = data.get("fourThree", [])
    fourFour = data.get("fourFour", [])
    fourFive = data.get("fourFive", [])
    fiveOne = data.get("fiveOne", [])
    fiveTwo = data.get("fiveTwo", [])
    fiveThree = data.get("fiveThree", [])
    fiveFour = data.get("fiveFour", [])
    fiveFive = data.get("fiveFive", [])
    if intAlgo == 1:
        return unit7_1_3.custom(oneOne, oneTwo, oneThree, oneFour, oneFive, twoOne, twoTwo, twoThree, twoFour, twoFive, threeOne, threeTwo, threeThree, threeFour, threeFive,
           fourOne, fourTwo, fourThree, fourFour, fourFive, fiveOne, fiveTwo, fiveThree, fiveFour, fiveFive)
    elif intAlgo == 2:
        return unit7_1_3.warshall(oneOne, oneTwo, oneThree, oneFour, oneFive, twoOne, twoTwo, twoThree, twoFour, twoFive, threeOne, threeTwo, threeThree, threeFour, threeFive,
           fourOne, fourTwo, fourThree, fourFour, fourFive, fiveOne, fiveTwo, fiveThree, fiveFour, fiveFive)


string7_1_4 = None


@app.route('/7_1_4', methods=['GET', 'POST'])
def submit_7_1_4():
    global string7_1_4

    if request.method == 'POST':
        data = request.json
        string7_1_4 = SolveUnit7_1_4(data)
        return jsonify(string7_1_4)

    elif request.method == 'GET':
        if string7_1_4 is None:
            return 'No data available yet'
        else:
            return jsonify(string7_1_4)


def SolveUnit7_1_4(data):
    return "true"


string7_1_5 = None


@app.route('/7_1_5', methods=['GET', 'POST'])
def submit_7_1_5():
    global string7_1_5

    if request.method == 'POST':
        data = request.json
        string7_1_5 = SolveUnit7_1_5(data)
        return jsonify(string7_1_5)

    elif request.method == 'GET':
        if string7_1_5 is None:
            return 'No data available yet'
        else:
            return jsonify(string7_1_5)


def SolveUnit7_1_5(data):
    set = data.get("set", [])
    p = data.get("p", [])
    return unit7_1_5.WarshallClosure(set, p)


if __name__ == '__main__':
    app.run(debug=True)
