class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        dep = {}
        dep['amount'] =  amount
        dep['description']  = description
        self.ledger.append(dep)

    def check_funds(self, amount):
        #total amount deposited in budget category
        funds = 0
        for i in self.ledger:
            funds += float(i['amount']) #goes through budget category's ledger and converts the element in i['amounts'] to float and adds it to the funds variable
        if amount <= funds:
            return True #if amount less than budget/funds, proceed
        else:
            return False #if amount great than budget/funds, stop

    def get_balance(self):
        total_balance = 0
        for i in self.ledger:
            total_balance += float(i['amount'])
        return total_balance

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True: #must use self. to initialize the check_funds function
            w = {}
            w['amount'] = -(amount) #amount becomes negative
            w['description'] = description
            self.ledger.append(w)
            return True
        else:
            return False

    def transfer(self, amount, budget_category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + str(budget_category.name))
            budget_category.deposit(amount, 'Transfer from ' + str(self.name))
            return True
        else:
            return False

    def __str__(self):
        #controls how the class object is displayed when printed
        title = self.name.center(30, '*')
        items = ""
        total = 0
        for i in self.ledger:
            items += i['description'][:23] + str('{:.2f}'.format(i['amount'])).rjust( 30 - len(i['description'][:23]) ) + '\n'
            #displays the first 23 characters of description in ledger and formats the amount by 2 decimal places
            total += float(i['amount']) #totals amount of ledger
        total = '{:.2f}'.format(total)
        return title + '\n' + items  + 'Total: ' + str(total)


def create_spend_chart(categories):
    total_amount_withdrawn = 0
    a = []
    percents = []
    for i in categories:
        fdic = {}
        total_budget = 0
        for amt in i.ledger:
            if float(amt['amount']) < 0:
                dic = {}
                total_amount_withdrawn += float(amt['amount'])
                dic['amount'] = float(amt['amount'])
                dic['budget'] = i.name
                a.append(dic) #appending dictionary items to list as a list can take duplicate items
                total_budget += float(amt['amount'])
        fdic['total budget ' + str(i.name)] = total_budget
        a.append(fdic)

    for i in a:
        for k,v in i.items():
            if k[:5] == 'total':
                percent = round(abs(v) / abs(total_amount_withdrawn) * 100)
                percents.append(percent)

    #--------creating chart-----------
    num = 100
    chart = []
    dash = ('    ' + '---' * len(percents)) + '-'
    chart.append('Percentage spent by category' + '\n')
    for i in range(11):
        chart.append((str(num) + '|').rjust(4))
        sp = ' '
        chart.append(sp)
        for total in percents:
            if total >= num:
                chart.append("o " + sp)
            else:
                chart.append("  " + sp)
        chart.append('\n')
        num -= 10
    chart.append(dash + '\n')

    #-------creating bottom row of chart (category names)------
    maxcat = 0
    newname = []
    names = [i.name for i in categories] #adding names of the budgets to a list
    for i in names: #finds the longest name in list
        if len(i) > maxcat:
            maxcat = len(i)
    for i in names: #checking if name is less than the longest
        if len(i) < maxcat:
            newname.append( i + (' ' * ( maxcat - len(i)))) # if name is less than the longest name, add spaces
        else:
            newname.append(i)

    for i in range( len(newname[0])  ):
        for k in range(len(newname)):
            if k == 0:
                chart.append('    ') #adds 4 spaces in front of each letter of the first name
                chart.append(' ' + newname[k][i] + ' ')
            elif k == max(range(len(newname))):
                chart.append(' ' + newname[k][i] + '  ')
            else:
                chart.append(' ' + newname[k][i] + ' ')
        if i == max(range(len(newname[0]))): #removes the extra /n character at the end of the string
            break
        else:
            chart.append('\n')


    return ''.join(chart)


    






#--------------tests-------------

food = Category("Food")
entertainment = Category("entertainment")
business = Category('business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

create_spend_chart([business,food,entertainment])














#Percentage spent by category
#100|
# 90|
# 80|
# 70|
# 60| o
# 50| o
# 40| o
# 30| o
# 20| o  o
# 10| o  o  o
#  0| o  o  o
#    ----------
#     F  C  A
#     o  l  u
#     o  o  t
#     d  t  o
#        h
#        i
#        n
#        g

#try 2 loops, 1 to create % 100 to 0 and 1 to add dash/categories...maybe another to add the 'o'