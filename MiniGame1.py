import random

choice=random.choice(["stone","paper","scissor"])

user=str(input("Enter Your Choice Stone,Paper or Scissor: ")).strip().lower()

if(choice=="stone" and user=="paper"):
    print(f'''Computer's Choice: {choice}
Your Choice: {user}
        YOU WIN THE GAME !
          ''')
    
elif(choice=="stone" and user=="scissor"):
    print(f'''Computer's Choice: {choice}
Your Choice: {user}
        YOU LOSE THE GAME !
          ''')
    
elif(choice=="scissor" and user=="paper"):
    print(f'''Computer's Choice: {choice}
Your Choice: {user}
        YOU LOSE THE GAME !
          ''')
    
elif(choice=="scissor" and user=="stone"):
    print(f'''Computer's Choice: {choice}
Your Choice: {user}
        YOU WIN THE GAME !
          ''')
    
elif(choice=="paper" and user=="scissor"):
    print(f'''Computer's Choice: {choice}
Your Choice: {user}
        YOU WIN THE GAME !
          ''')
    
elif(choice=="paper" and user=="stone"):
    print(f'''Computer's Choice: {choice}
Your Choice: {user}
        YOU LOSE THE GAME !
          ''')
    
elif(choice==user):
    print(f'''Computer's Choice: {choice}
Your Choice: {user}
        THE GAME IS A DRAW !
          ''')
    




