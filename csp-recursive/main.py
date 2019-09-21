import sys


class State:
    """States of assignment of domain numbers to variables.

    VALID - assignment has no constraint contradictions, but still has unassigned values.
    INVALID - assignment contradicts at least one constraint.
    COMPLETE - assignment has no constraint contradictions and all values are assigned.
    """

    INVALID = 0
    COMPLETE = 1
    VALID = 2


domain = [1, 2, 3, 4]
variables = []
values = [None]*8
solutions = []
failures = 0


def nextUnassigned(assignment):
    """Get next assignment variable that is still unassigned"""
    for var in assignment:
        if (var == None):
            return assignment.index(var)


def assignmentValid(assignment):
    """Check if given assignment contradicts any constraints"""
    global variables
    failedConstraint = ''

    a = assignment[variables.index('A')]
    b = assignment[variables.index('B')]
    c = assignment[variables.index('C')]
    d = assignment[variables.index('D')]
    e = assignment[variables.index('E')]
    f = assignment[variables.index('F')]
    g = assignment[variables.index('G')]
    h = assignment[variables.index('H')]

    if c != None:
        if d != None:
            if (d == c):
                failedConstraint = '(D=C)'

    if e != None:
        if c != None:
            if (e == c):
                failedConstraint = '(E=C)'

        if d != None:
            if (e >= (d-1)):
                failedConstraint = '(E>=D-1)'

    if f != None:
        if b != None:
            if (abs(f - b) != 1):
                failedConstraint = '(|F-B|!=1)'

        if c != None:
            if (c == f):
                failedConstraint = '(C=F)'

        if d != None:
            if (d == f):
                failedConstraint = '(D=F)'

        if e != None:
            if ((e-f) % 2 == 0):
                failedConstraint = '(E-F is Even)'

        if g != None:
            if (g == f):
                failedConstraint = '(G=F)'

    if g != None:
        if a != None:
            if (a < g):
                failedConstraint = '(A<G)'

        if c != None:
            if (abs(g-c) != 1):
                failedConstraint = '(|G-C|!=1)'

        if d != None:
            if (d < g):
                failedConstraint = '(D<G)'

    if h != None:
        if a != None:
            if (a >= h):
                failedConstraint = '(A>H)'

        if c != None:
            if ((h-c) % 2 == 1):
                failedConstraint = '(H-C is odd)'

        if d != None:
            if (h == d):
                failedConstraint = '(H=D)'

        if e != None:
            if (e == (h-2)):
                failedConstraint = '(E=H-2)'

        if f != None:
            if (h == f):
                failedConstraint = '(H=F)'

        if g != None:
            if (g >= h):
                failedConstraint = '(G>=H)'

    return (failedConstraint == '', failedConstraint)


def assignmentState(assignment):
    """Check given assignment state"""
    isAssignmentValid, failedConstraint = assignmentValid(assignment)

    if (nextUnassigned(assignment) == None):
        if isAssignmentValid:
            state = State.COMPLETE
        else:
            state = State.INVALID

    else:
        if not isAssignmentValid:
            state = State.INVALID
        else:
            state = State.VALID

    return state, failedConstraint


def numberAssigned(assignment):
    """Return number of assigned variables"""
    return len(list(filter(lambda x: x != None, assignment)))


def printNode(assignment, depth, keepGoingCount, complete, failedConstraint):
    """Print out current assignment state"""
    indentLevel = depth - keepGoingCount

    for _ in range(indentLevel):
        print('   '),

    for i in range(indentLevel, numberAssigned(assignment)):
        print(variables[i] + '=' + str(assignment[i]) + ''),

    if complete:
        print('solution')
    else:
        print('failure        ' + failedConstraint)


def solve(assignment, depth, keepGoingCount, verbose):
    """Print out current assignment state.

    assignment - current node of assigned variables.
    depth - current depth of the tree. Only required to indent print out correctly.
    keepGoingCount - number of last consecutive nodes that are neither failures
                     nor solutions. Only required to postpone print out
                     until a branch fails/finds a solution (i.e. print out only leaves).
    verbose - whether to print out the tree.
    """

    global solutions, failures
    state, failedConstraint = assignmentState(assignment)

    if (state == State.VALID):
        keepGoingCount += 1
    else:
        if state == State.COMPLETE:
            solutions.append(assignment[:])
        else:
            failures += 1
        if verbose:
            printNode(assignment, depth, keepGoingCount,
                    state == State.COMPLETE, failedConstraint)

            if state == State.COMPLETE:
                return True
    if state == State.VALID:
        nextIndex = nextUnassigned(assignment)
        if (nextIndex != None):
            for value in domain:
                assignment[nextIndex] = value
                solve(assignment, depth + 1, keepGoingCount, verbose)
                assignment[nextIndex] = None
                keepGoingCount = 0

    return False


def printSolution():
    global solutions, failures
    print('\n\nNumber of solutions found:\n' + str(len(solutions)))
    print('Solutions:')
    for solution in solutions:
        for value, var in zip(solution, variables):
            print(var + '=' + str(value)),
        print('')
    print('Number of failed branches:\n' + str(failures))


def main(argv):
    global variables, solutions, failures
    optimal = len(argv) > 0 and argv[0] == 'optimal'

    # check multiple variable arrangments if argument 'optimal' is used
    # otherwise use default arrangment
    if optimal:
        arrangments = [['F', 'H', 'C', 'D', 'G', 'E', 'A', 'B'],
                ['F', 'H', 'D', 'C', 'G', 'E', 'A', 'B'],
                ['H', 'F', 'C', 'D', 'G', 'E', 'A', 'B'],
                ['H', 'F', 'D', 'G', 'C', 'E', 'A', 'B'],
                ['H', 'F', 'G', 'E', 'D', 'C', 'A', 'B'],
                ['D', 'C', 'F', 'H', 'B', 'A', 'E', 'G'],
                ['G', 'C', 'F', 'E', 'H', 'B', 'D', 'A']]
    else:
        arrangments = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']]

    for arrangment in arrangments:
        solutions = []
        failures = 0
        variables = arrangment
        solve(values, -1, 0, not optimal)
        printSolution()


if __name__ == "__main__":
    main(sys.argv[1:])

