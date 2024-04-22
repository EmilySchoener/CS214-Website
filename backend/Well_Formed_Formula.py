# Error Function used as a test throughout the program. Not used in final program.
def error(msg):
    pass
    # # Get the caller's frame information
    # caller_frame = inspect.stack()[1]
    # line_number = caller_frame.lineno
    #
    # # Print the line number and message
    # print(f"Line {line_number} in {"PokeDex"} with: {msg}")


class WFF:
    def __init__(self):
        self.statement = None
        self.result = ""
        self.A = True
        self.B = True
        self.C = True
        self.T = True
        self.F = False
        self.properties = []

    def set_statement(self, statement):
        self.statement = statement

    def set_letters(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def set_A(self):
        self.A = not self.A

    def set_B(self):
        self.B = not self.B

    def set_C(self):
        self.C = not self.C

    def get_A(self):
        return self.A

    def get_B(self):
        return self.B

    def get_C(self):
        return self.C

    def wff_solver(self, statement, a, b, c):
        try:
            self.statement = str(statement)
            self.A = bool(a)
            self.B = bool(b)
            self.C = bool(c)
        except:
            print("Invalid input for wff_solver")

        # try:
        #     self.parser_loop()
        # except:
        #     print("Regular Loop Failed Trying advanced parse ")

        try:
            return str(self.parser_adv(statement))
        except:
            return "Failed"

    def parser_loop(self):
        proposition = ""
        for token in self.statement:
            if token == "[":
                self.brackets_func()
            elif token == "(":
                self.parentheses_func()
            elif token == "(":
                self.parentheses_func()
            elif token == "(":
                self.parentheses_func()
            elif token == "(":
                self.parentheses_func()
            elif token == "(":
                self.parentheses_func()
            elif token == "(":
                self.parentheses_func()

    def brackets_func(self):
        pass

    def parentheses_func(self):
        pass

    def negation_func(self):
        pass

    def conjunction_func(self):
        pass

    def disjunction_func(self):
        pass

    def implication_func(self):
        pass

    def equivalence_func(self):
        pass

    def eval_func(self):
        pass

    def eval_adv(self, middle):
        A = self.A
        B = self.B
        C = self.C
        T = self.T
        F = self.F
        try:
            if eval(middle):
                return "T"
            else:
                return "F"
        except SyntaxError:
            print("Invalid syntax in logical expression:", middle)
            return "I"

    def parser_adv(self, logic):
        proposition = str(logic)
        error("Post Input: " + proposition)
        # Solve  Brackets
        proposition = self.brackets_func_adv(proposition)
        # error("Post Brackets: " + proposition)
        # Solve  parentheses
        proposition = self.parentheses_func_adv(proposition)
        error("Post Parentheses: " + proposition)
        # Solve  negation
        proposition = self.negation_func_adv(proposition)
        # error("Post negation: " + proposition)
        # Solve  conjunction
        proposition = self.conjunction_func_adv(proposition)
        # error("Post Conjunction: " + proposition)
        # Solve  disjunction
        proposition = self.disjunction_func_adv(proposition)
        # error("Post Disjunction: " + proposition)
        # Solve  implication
        proposition = self.implication_func_adv(proposition)
        # error("Post implication: " + proposition)
        # Solve  equivalence
        proposition = self.equivalence_func_adv(proposition)
        # error("Post equivalence: " + proposition)
        return proposition

    def brackets_func_adv(self, logic):
        start, stop = None, None
        starts = 0
        error("bracket: " + logic)
        for i, token in enumerate(logic):
            if token == "[":
                starts += 1
                if start is None:
                    start = i + 1  # Adjusting index to get the content after '['
            elif token == "]":
                starts -= 1
                if starts == 0 and stop is None:
                    stop = i
                    break  # No need to continue once the closing bracket is found
        if start is not None and stop is not None:
            try:
                starting_logic = str(logic[0:start - 1])
            except IndexError:
                starting_logic = " "
            content_within_brackets = logic[start:stop]
            remaining_logic = logic[stop + 1:]  # Getting content after ']'
            # print("This is what is inside the bracket, ", content_within_brackets, "\nstarting", starting_logic,
            # "\nRemaining", remaining_logic)
            result = self.parser_adv(content_within_brackets)
            test_str = starting_logic + " " + result + " " + remaining_logic
            return test_str
        else:
            error("No complete set of bracket found.")
            return logic

        pass

    def parentheses_func_adv(self, logic):
        result = logic
        error("parentheses" + logic)
        while True:
            start, stop = None, None
            is_found = False
            starts = 0

            for i, token in enumerate(result):
                if token == "(":
                    is_found = True
                    starts += 1
                    if start is None:
                        start = i + 1
                elif token == ")":
                    starts -= 1
                    if starts == 0 and stop is None:
                        stop = i
                        break

            if start is not None and stop is not None:
                try:
                    starting_logic = str(result[0:start - 1])
                except IndexError:
                    starting_logic = " "
                content_within_brackets = result[start:stop]
                remaining_logic = result[stop + 1:]
                result_within_brackets = self.parser_adv(content_within_brackets)
                result = starting_logic + " " + result_within_brackets + " " + remaining_logic
            else:
                error(result)
                error("No complete set of parentheses found.")

            if not is_found:
                break

        return result

    def negation_func_adv(self, logic):
        error("neg" + logic)
        parts = logic.split()
        result = logic
        while True:
            implication_found = False
            for i, part in enumerate(parts):
                if part == "'":
                    implication_found = True
                    subject = parts[i - 1]
                    # Construct the implication as "not left or right"
                    middle = " not " + subject
                    evaluated_middle = self.eval_adv(middle)
                    error(evaluated_middle)
                    # Replace the original implication with its evaluated result
                    parts = parts[:i - 1] + [evaluated_middle] + parts[i + 1:]
                    result = " ".join(parts)
                    error(result)
                    break

            if not implication_found:
                return result

    def conjunction_func_adv(self, logic):
        error("conjunction" + logic)
        parts = logic.split()
        result = logic
        while True:
            is_found = False
            test = ""
            for i, part in enumerate(parts):
                if part == "&":
                    is_found = True
                    left = " ".join(parts[:i - 1])
                    right = " ".join(parts[i + 2:])
                    middle = parts[i - 1] + " and " + parts[i + 1]
                    evaluated_middle = self.eval_adv(middle)
                    test = left + " " + evaluated_middle + " " + right
                    result = test
                    break

            if not is_found:
                return result
            parts = test.split()

    def disjunction_func_adv(self, logic):
        error("disjunction" + logic)
        parts = logic.split()
        results = ""
        result = logic
        while True:
            is_found = False
            test = ""
            for i, part in enumerate(parts):
                if part == "*":
                    is_found = True
                    left = " ".join(parts[:i - 1])
                    right = " ".join(parts[i + 2:])
                    middle = parts[i - 1] + " or " + parts[i + 1]
                    evaluated_middle = self.eval_adv(middle)
                    test = left + " " + evaluated_middle + " " + right
                    result = test
                    break

            if not is_found:
                return result
            parts = test.split()

    def implication_func_adv(self, logic):
        error("implication" + logic)
        parts = logic.split()
        result = logic
        while True:
            implication_found = False
            for i, part in enumerate(parts):
                if part == "-":
                    implication_found = True
                    left = " ".join(parts[:i])
                    right = " ".join(parts[i + 1:])
                    # Construct the implication as "not left or right"
                    middle = "not " + left + " or " + right
                    evaluated_middle = self.eval_adv(middle)
                    error(evaluated_middle)
                    # Replace the original implication with its evaluated result
                    parts = parts[:i - 1] + [evaluated_middle] + parts[i + 2:]
                    result = " ".join(parts)
                    break

            if not implication_found:
                return result

    def equivalence_func_adv(self, logic):
        error("Equivalence" + logic)
        parts = logic.split()
        while True:
            implication_found = False
            for i, part in enumerate(parts):
                if part == "=":
                    implication_found = True
                    left = " ".join(parts[:i])
                    right = " ".join(parts[i + 1:])
                    # Construct the implication as "not left or right"
                    middle = left + " == " + right
                    evaluated_middle = self.eval_adv(middle)
                    error(evaluated_middle)
                    # Replace the original implication with its evaluated result
                    parts = parts[:i - 1] + [evaluated_middle] + parts[i + 2:]
                    break

            if not implication_found:
                break

        # Join the parts back into a single string
        result = " ".join(parts)
        return result

    def solve(self):
        try:
            return self.parser_adv(self.statement)
        except:
            return "Failed"


class Truth_Table:
    def __init__(self):
        self.results = ""
        self.table = ""
        self.source = ""
        self.index = 0
        self.wff = WFF()

    def table_creation(self, source):
        self.wff.set_statement(source)
        self.wff.set_letters(True, True, True)
        self.source = source
        self.results = ""
        self.table = ""
        self.index = 0
        if "C" in source:
            self.C_table()
            self.C_table_print()
        elif "B" in source:
            self.B_table()
            self.B_table_print()
        else:
            self.A_table()
            self.A_table_print()
        self.results_test()
        return self.table

    def C_table(self):
        for _ in range(2):
            self.B_table()
            self.wff.set_C()

    def B_table(self):
        for _ in range(2):
            self.A_table()
            self.wff.set_B()

    def A_table(self):
        for _ in range(2):
            self.results += self.wff.solve()
            self.wff.set_A()

    def C_table_print(self):
        self.table = "C|\tB|\tA|\t" + self.source + "\n"
        for _ in range(2):
            for _ in range(2):
                for _ in range(2):
                    self.table += str(self.wff.get_C()) + "|\t" + str(self.wff.get_B()) + "|\t" + str(
                        self.wff.get_A()) + "|\t"
                    self.results_table_print()
                    self.wff.set_A()
                self.wff.set_B()
            self.wff.set_C()

    def B_table_print(self):
        self.table = "B|\tA|\t" + self.source + "\n"
        for _ in range(2):
            for _ in range(2):
                self.table += (str(self.wff.get_B()) + "|\t" + str(self.wff.get_A()) + "|\t")
                self.results_table_print()
                self.wff.set_A()
            self.wff.set_B()

    def A_table_print(self):
        self.table = "A|\t" + self.source + "\n"
        for _ in range(2):
            self.table += (str(self.wff.get_A()) + "|\t")
            self.results_table_print()
            self.wff.set_A()

    def results_table_print(self):
        try:
            self.table += self.results[self.index] + "\n"
        except IndexError:
            self.table += "\n"
        self.index += 1

    def results_test(self):
        if "F" not in self.results:
            self.table += "Tautology\n"
        if "T" not in self.results:
            self.table += "Contradiction\n"


class Proof:
    def __init__(self):
        self.rhs = None
        self.properties = None
        self.lhs = None
        self.wff = None
        self.statement = ""

    def tautology_proof(self, source):
        self.statement = source
        self.split_func()
        statement = self.lhs
        self.recursive_proof(statement)

    def split_func(self):
        parts = self.statement.split()
        for i, part in enumerate(parts):
            if part == "=":
                implication_found = True
                self.lhs = (" ".join(parts[:i]))
                self.properties = "Given, "
                self.rhs = " ".join(parts[i + 1:])
                self.lhs = "".join(self.lhs.split())
                self.rhs = "".join(self.rhs.split())
                break
        # print(self.lhs, " ", self.rhs)

    def compare_func(self):
        if self.rhs in self.lhs:
            return True
        else:
            return False

    def commutative_func(self):
        pass

    def associative_func(self):
        pass

    def distributive_func(self):
        pass

    def identity_func(self):
        pass

    def complement_func(self):
        pass

    def recursive_proof(self, statement):
        self.commutative_func()
        self.associative_func()
        self.distributive_func()
        self.identity_func()
        self.complement_func()


web_wff = WFF()
web_table = Truth_Table()


def truth_table_func(S):
    result = web_table.table_creation(S)
    result = str(result)
    return result


def process_wff(A, B, C, S):
    web_wff.set_letters(A, B, C)
    result = web_wff.wff_solver(S, A, B, C)
    result = str(result)
    return result
