def print_menu():
    print("------")
    print(" Menu ")
    print("------")
    
    print("0) Exit")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")

def get_option():
    while True:
        input_num = input("[Enter your option]\n")
        try:
            int(input_num)
        except ValueError:
            print("<What you entered must be a digit>")
            continue
        break
    return int(input_num)

def get_float(i):
    while True:
        if i == 1:
            input_num = input("[Enter your first float number]\n")
        else:
            input_num = input("[Enter your second float number]\n")
        try:
            float(input_num)
        except ValueError:
            print("<What you entered must be a float>")
            continue
        break
    return float(input_num)



print_menu()
option = get_option()
while (option != 0):
    x = get_float(1)
    y = get_float(2)
    if option == 1:
       print("%.2f + %.2f = %.2f" % (x, y, x + y))
    elif option == 2:
        print("%.2f - %.2f = %.2f" % (x, y, x - y))
    elif option == 3:
        print("%.2f * %.2f = %.2f" % (x, y, x * y))
    elif option == 4 and y != 0 :
        print("%.2f / %.2f = %.2f" % (x, y, x / y))
    else:
        print("<error>")

    print_menu()
    option = get_option()

print("<Bye!>")
