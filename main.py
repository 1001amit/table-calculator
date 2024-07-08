#a script to calculate the table
table_of = int(input("Which number table do you want to calculate: "))
table_to = int(input("Till where do you want to calculate: "))

def table_calculator(table_of, table_to):
    for i in range(1, table_to + 1):
        x = table_of * i
        print(f"{table_of} x {i} = {x}")

table_calculator(table_of, table_to)
