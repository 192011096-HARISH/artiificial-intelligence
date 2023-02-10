def backtrack(choices, current_solution):
    if not choices:
        
        print(current_solution)
        return

    for choice in choices:
        updated_choices = choices.copy()
        updated_choices.remove(choice)
        updated_solution = current_solution + [choice]

        if is_valid(updated_solution):
            backtrack(updated_choices, updated_solution)
        else:
            continue

def is_valid(solution):
 
    return True

choices = [1, 2, 3, 4, 5]
backtrack(choices, [])
