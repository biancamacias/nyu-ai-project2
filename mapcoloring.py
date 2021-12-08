# CS-UY 4613 Artificial Intelligence Project 2: Map Coloring
# Isabel Huey, Bianca Macias
# ijh234, bm2815


# def minimum_remaining_values():
# def degree_heuristic():
# def order_domain_values():
# def inference():
# def select_unassigned_variable():

def main():
    # Ask for input to obtain filename and try to open the file
    file = None
    while file == None:
        filename = input("Enter the name of the input file: ")
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File not found, try again")

    the_input = []
    # Make a list of the initial input from the input file
    for line in file:
        line = line.strip()
        line = line.split(' ')
        the_input.append(line)

    # Seperate and label the number of variables (regions) and the number of domain values (colors)
    num_variables = the_input[0][0]
    num_domain_values = the_input[0][1]
    # Seperate the list of variable names and list of domain values from the rest of the the_input
    variable_names = the_input[1]
    domain_values = the_input[2]
    # Seperate the array of constraints from the rest of the the_input
    constraint_array = the_input[3:]


    print(num_variables)
    print(num_domain_values)
    print(variable_names)
    print(domain_values)
    print(constraint_array)




if __name__ == '__main__':
    main()
