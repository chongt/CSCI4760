#
# The ChangeMaker class computes change from
# a purchase as a list [quarters, dimes, nickels, pennies]
#

class ChangeMaker:

    remainder = 0;

    def __init__(self):
        '''Constructor does nothing'''
        pass

    def coinlist(self,amount):
        ''' returns a list of coins [quarters, dimes, nickels,pennies]
        whose total value is 'amount' and has the fewest number of coins
        possible
        amount: a positive integer number of cents
        `'''        
        
        # Implemented by Tiffany Chong
        
        self.amount = amount # get given amount of change to be processed
    
        q = 0 # number of quarters
        d = 0 # number of dimes
        n = 0 # number of nickels
        p = 0 # number of pennies
        
        # loop to obtain number of quarters by substracting 25 from given amount
        while amount >= 25:
            amount = amount - 25
            q = q + 1
        # after loop, amount should be less than 25
        
        # loop to obtain number of dimes by substracting 10 from current amount
        while amount >= 10:
            amount = amount - 10
            d = d + 1
        # after loop, amount should be less than 10 
        
        # loop to obtain number of nickels by substracting 5 from current amount
        while amount >= 5:
            amount = amount - 5
            n = n + 1
        # after loop, amount should be less than 5
        
        # loop to obtain number of pennies by substracting 1 from current amount
        while amount > 0:
            amount = amount - 1
            p = p + 1
        # after loop, amount should be 0 
        
        #return numbers of coins in an array
        return [q,d,n,p]

    def changelist(self, purchase_amount, cash_tendered):
        '''Returns the change from a purchase as a list of coins
        purchase_amount: a positive integer number of cents representing purchase amount
        cash_tendered: a positive integer number of cents representing  the cash given to the clerk,
        with cash_tendered >= purchase_amount
        `'''
        
        # Implemented by Tiffany Chong
    
        amount = cash_tendered - purchase_amount # obtain amount of change to be processed

        # call the coinlist method to process amount to return array of coins
        return ChangeMaker.coinlist(self,amount)
