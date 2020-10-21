import sqlite3

class financeoperations:
    def __init__(self, username):
        self.username=username

        conn=sqlite3.connect('finances.sqlite')
        self.sql=conn.cursor()
        initscript='''
            CREATE TABLE IF NOT EXISTS Balances(
                username VARCHAR2(50) NOT NULL UNIQUE PRIMARY KEY,
                savings NUMBER(50) NOT NULL,
                wallet NUMBER(50) NOT NULL
            )
        '''
        self.sql.executescript(initscript)

        self.savingsBalance=0
        self.walletBalance=0
        self.updateSelf()

    def updateSelf(self):   #Updates object balances from database
        self.sql.execute('SELECT * FROM Balances WHERE username=?',(self.username,))
        row=self.sql.fetchone()
        if row==None:
            self.sql.execute('''
                INSERT INTO Balances(username, savings, wallet)
                VALUES (?, 0, 0)
            ''',(self.username,))
        else:
            self.savingsBalance=row[1]
            self.walletBalance=row[2]

    def updateDB(self):     #Updates database from object balances
        self.sql.execute('''
            UPDATE Balances
            SET savings=?, wallet=?
            WHERE username=?
        ''',(self.savingsBalance, self.walletBalance, self.username,))
        self.sql.execute('COMMIT')

    def addMoney(self, account, amount):    #Adds money to specified account 's' or 'w'
        if account=='s':
            self.savingsBalance+=amount
        else:
            self.walletBalance+=amount
        self.updateDB()

    def spendMoney(self, account, amount):  #Spends money from specified account 's' or 'w'
        if account=='s':
            self.savingsBalance-=amount
        else:
            self.walletBalance-=amount
        self.updateDB()


    def moveMoney(self, account, amount):   #Moves money from specified account to the other
        if account=='s':
            self.savingsBalance-=amount
            self.walletBalance+=amount
        else:
            self.walletBalance-=amount
            self.savingsBalance+=amount
        self.updateDB()


#Testing Block for This Class
if __name__=='__main__':
    finances=financeoperations('elementalneil')
    finances.addMoney('w', 500)
    finances.addMoney('s', 5000)
    finances.spendMoney('w',300)
    finances.addMoney('s',3000)
    finances.moveMoney('s',1000)
    finances.spendMoney('s',2000)
    finances.moveMoney('w',700)
    print('Savings Balance:',finances.savingsBalance)
    print('Wallet Balance:',finances.walletBalance)