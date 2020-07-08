from time import sleep

class QNA:
    def name(self): 
        n=input("What's your name?")
        try:
            n= str(n)
        except ValueError:
            print('Please insert a string.')
            name()
        sleep (1)
        
    def qa(self, name):    
        print('Hello ' + n)
        sleep (1)
        print("Do you wan't to continue, " + n + " ?")
        sleep(1)
        a1=input('y/n:')
        if a1 =='n':
            print('As you wish '+ n+ ", goodbye.")
            sleep (1)
            quit()
            
        sleep(1)
        x=input('''What's your age ''' + n + ':')
        x=int(x)
        sleep (2)

        if x < 100:
            y= 2020+(100-x)
            y=str(y)
            print("Do you want to know when you will stop living " + n + " ?")
            sleep(1)
            print('y/n:')
            a2=input()
        if a2 == 'y':
            print('Your expiry date is the year ' + y)
        if a2 =='n':
            print('As you wish '+ n + ", goodbye.")
            sleep (2)
            quit()

        sleep (2)    
        print('Thanks for your data!')
        sleep(1.5)
        print("Do you want to quit using Marcus?")
        print('y/n:')
        a3=input()
        if a3 =='y':
            sleep (1)
            quit()
        sleep(1.5)
        print("Do you wan't to enter another user?")
        sleep(1)

 
instanz= QNA()
instanz.name()

