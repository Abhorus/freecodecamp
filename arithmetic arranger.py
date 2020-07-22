def arithmetic_arranger(problems,value=False):

    if len(problems) > 5:
            return 'Error: Too many problems.'

    arranged = []
    arranged_numbers = []
    for i in problems:
        b = i.split()

        num = b[0]
        op = b[1]
        num2 = b[2]
        m = max(len(str(num)), len(str(num2)))
        dash = '-' * (len(op) + m + 1)

        if num.isdigit() == False or num2.isdigit() == False:
             return 'Error: Numbers must only contain digits.'
        elif op != '-' and op != '+':
            return "Error: Operator must be '+' or '-'."
        elif len(num) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'


        if op == '+':
            total = int(num) + int(num2)
        elif op =='-':
            total = int(num) - int(num2)
        #adds numbers, operator, and dash to a variable
        if value == True:
            arr = num.rjust(len(dash)), op.ljust(len(dash) - len(num2)) + num2, dash.rjust(len(dash)), str(total).rjust(len(dash))

        else:
            arr = num.rjust(len(dash)), (op.ljust(len(dash) - len(num2)) + num2), dash.rjust(len(dash))
        #adds the variable to a list as an individual list
        arranged.append(arr)


    #goes through the array and adds first element of each individual list to another list and adds 4 spaces and newlines
    for j in range(len(arranged[0])):
        for k in range(len(arranged)):
            if k == max(range(len(arranged))): #removes spaces after last element in array
                arranged_numbers.append(arranged[k][j])
            else:
                arranged_numbers.append(arranged[k][j] + '    ')
        if k == max(range(len(arranged))) and j == max(range(len(arranged[0]))): #removes extra \n at end of list
            break
        else:
            arranged_numbers.append( '\n' )
    #returns new list as a single string
    return ''.join(arranged_numbers)





#print(arithmetic_arranger(['3255 + 21', '31 - 22', '2 + 1', '4 + 1'], False))

#print(arithmetic_arranger(['3255 - 21'] , False))

#print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
#print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])) #test

#print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))

#expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
#need to print single string
#print(len("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"))
#print(len("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"))

#fuction has one extra character than expected result