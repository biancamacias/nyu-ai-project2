# CS-UY 4613 Artificial Intelligence Project 2: Map Coloring
# Isabel Huey, Bianca Macias
# ijh234, bm2815

# Takes in the number of variables,
# the variable_names, the domain_values, the constraint_array, and the current assignments.
# Will return a list of the variable_names with the smallest amount of remaining values
# gonna have remaining_values be a list of lists so it is easy to index and remove values
def minimum_remaining_values(num_variables, variable_names, domain_values, constraint_array, assignment):
    # if the assignment is empty then return all of the variable names
    if assignment == {}:
        return variable_names

    # Make a list of lists of the domain_values
    # Have to remake this each time we calculate minimum_remaining_values in case an assignment has been removed
    remaining_values = []
    for num in range(num_variables):
        remaining_values.append(domain_values)

    # edit the lsit of remaining values according to the assignments and the constraints
    for key in assignment:
        row = variable_name.index(key)
        constraint_row = constraint_array[row]
        index_count = 0
        for value in constraint_row:
            if value = 1:
                theVar = variable_names[index_count]





    # if

# def degree_heuristic():
# def order_domain_values(num_variables, num_domain_values, variable_names, domain_values, constraint_array, var, assignment):
# def inference(num_variables, num_domain_values, variable_names, domain_values, constraint_array, var, assignment):
def select_unassigned_variable(num_variables, num_domain_values, variable_names, domain_values, constraint_array, assignment):
    return None

#returns a solution or failure
def backtrack(num_variables, num_domain_values, variable_names, domain_values, constraint_array, remaining_values, assignment):
    assigned variables = []
    unassigned_variables = []
    for name in variable_names:
        if assigment[name]:
            assigned_variables.append(name)
        else:
            unassigned_variables.append(name)
    if unassigned_variables == []:
        return assignment

    var = select_unassigned_variable(unassigned_variables, assignment)
    """
    order_domain = order_domain_values(csp,var,assignment)
    for each value in order_domain:
        if value is consistent with assignment:
            add {var = value} to assignment
            inferences = inference(csp, var, assignment)
            if inferences != failure:
                add inferences to csp
                result = backtrack(csp, assignment)
                if result != failure:
                    return result
                remove inferences from csp
            remove {var = value} from assignment
        return failure


    """


#returns a solution or failure
def backtracking_search(num_variables, num_domain_values, variable_names, domain_values, constraint_array):
    return backtrack(num_variables, num_domain_values, variable_names, domain_values, constraint_array, {})

def main():
    # Ask for input to obtain filename and try to open the file
    file = None
    while file == None:
        filename = input("Enter the name of the input file: ")
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File not found, try again")

    initial_state = []
    # Make a list of the initial input from the input file
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_state.append(line)


    # Seperate and label the number of variables (regions) and the number of domain values (colors)
    num_variables = initial_state[0][0]
    num_domain_values = initial_state[0][1]
    # Seperate the list of variable names and list of domain values from the rest of the the_input
    variable_names = initial_state[1]
    domain_values = initial_state[2]
    # Seperate the array of constraints from the rest of the the_input
    constraint_array = initial_state[3:]


    goal_state = backtracking_search(num_variables, num_domain_values, variable_names, domain_values, constraint_array)





if __name__ == '__main__':
    main()
