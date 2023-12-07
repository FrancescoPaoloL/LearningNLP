import nltk
from nltk.sem import Expression

persons = ['she', 'he', 'they']

for person in persons:
    # Define basic predicates and statements
    #	- Predicates provide a reusable and abstract representation of logical conditions, 
    # 	- Statements allow the code to specify and test concrete instances of these conditions 
    # 	  for different individuals. 
    predicates = {
        'is_hungry': lambda x: x == person,
        'will_eat_sandwich': lambda x: x == person,
    }

    statements = [
        'is_hungry',
        'will_eat_sandwich',
    ]


    # process a statement
    print(f"Testing with {person}:")
    for statement in statements:
        parsed_expression = nltk.sem.Expression.fromstring(statement)
        predicate_name = statement.split('(')[0]
        truth_value = predicates[predicate_name](person)
        
        print(f"\tInput: {statement}")
        print(f"\t\t{person} {statement}: {truth_value}")
        print(f"\t\t{person} not {statement}: {not truth_value}")
    print("\n" + "-"*30 + "\n")

