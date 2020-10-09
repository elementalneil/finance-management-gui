import sqlite3
import bcrypt

class portal:
    def __init__(self):
        conn=sqlite3.connect('accounts.sqlite')
        self.sql=conn.cursor()
        initscript='''
            CREATE TABLE IF NOT EXISTS Accounts(
                username VARCHAR2(50) NOT NULL UNIQUE PRIMARY KEY,
                password VARCHAR2(50) NOT NULL
            )
        '''
        self.sql.execute(initscript)

    def login(self, username, password):
        self.sql.execute('SELECT username, password FROM Accounts WHERE username=?',(username,))
        row=self.sql.fetchone()
        password=bytes(password,'utf-8')
        if row==None:
            return 1
        else:
            if bcrypt.checkpw(password, row[1]):
                return 3
            else:
                return 2

    def signup(self, username, password):
        password=bytes(password,'utf-8')
        password=bcrypt.hashpw(password, bcrypt.gensalt(12))
        try:
            self.sql.execute('''
                INSERT INTO Accounts(username, password) 
                VALUES (?,?)
                ''',(username, password,))
            self.sql.execute('COMMIT')
            print('Account Created.')
            return True
        except:
            return False

    def mainProg(self):
        print('Inside Main Program')
        quit()

#Console Runner Code:

if __name__=='__main__':
    newportal=portal()
    print('Options:    1. Login')
    print('            2. Signup')
    print('            3. Exit')
    while(True):
        option=input('Please enter your choice (1/2/3): ')
        if option=='1':
            print()
            while True:
                username=input('Username: ')
                password=input('Password: ')
                loginstatus=newportal.login(username, password)
                if loginstatus==1:
                    print('The username does not exist. Sign up to create a new account.')
                    break
                else:
                    print('Wrong Password. Try again.')
                    continue

        elif option=='2':
            print()
            while True:
                username=input('Username: ')
                password1=input('Password: ')
                password2=input('Confirm Password: ')
                if password1==password2:
                    if newportal.signup(username, password1):
                        break
                    else:
                        print('Username already exists. Try again.')
                        continue
                else:
                    print('Passwords do not match. Try again.')
        elif option=='3':
            quit()
        else:
            print('Wrong Input. Try Again!')
            continue