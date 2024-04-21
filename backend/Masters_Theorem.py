def master_theorem(a, b, c):

    if a < 1:
        return "Invalid input for a, must be integer greater than or equal to 1"
    if b <= 1:
        return "Invalid input for b, must be integer greater than 1"
    if c < 0:
        return "Invalid input for c, must be non-negative real number"
    #Case 1
    if a < b**c:
        return f"S(n) = O(n^{c})"

    #Case 2
    if a == b**c:
        return f"S(n) = O(n^{c} log n)"

    #Case 3
    if a > b**c:
        return f"S(n) = O(n^{c} log_{b}({a})"


#print(master_theorem(4,2,2))