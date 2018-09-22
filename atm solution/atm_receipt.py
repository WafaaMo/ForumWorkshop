  # allowed papers: 100, 50, 10, 5, and cents
class ATM:
    """ This class provides a way to withdraw money from ATM """
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def withdraw(self, request):

        print ('Welcome to '+ self.bank_name)
        print ('current balance = '+ str(self.balance))
        if   request >= self.balance:
            print("Can't give you all this money !!")
        elif request < 0:
            print("More than zero plz!")

        else:
            self.balance -= request
            self.withdrawals_list.append(request)

            while request > 0:
                if request >= 100:
                    request -= 100
                    print("give 100")

                elif request >= 50:
                    request -= 50
                    print("give 50")

                elif request >= 10:
                    request -= 10
                    print("give 10")

                elif request >= 5:
                    request -= 5
                    print("give 5")

                elif request < 5:
                    print("give " + str(request))
                    request = 0

        #self.withdrawals_list.append(request) ''' You should delete this line
        return self.balance

    def show_withdrawals(self):
        print("==========Withdrawals==========")
        for withdrawal in self.withdrawals_list:
            print(withdrawal)
            print("--------------------")

balance1 = 500

atm1 = ATM(balance1, "Smart Bank")

""" Smart Bank """
atm1.withdraw(277)
atm1.withdraw(800)
atm1.withdraw(25)
atm1.withdraw(10)

atm1.show_withdrawals()
