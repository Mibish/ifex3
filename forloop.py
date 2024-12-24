#1
'''
pri=float(input("Price of an item"))
if pri>=1000:
   d=0.1
elif pri>=500 and pri<1000:
   d=0.05
else:
   d=0
pri=pri-(pri*d)
print("The price after discount is ",pri)
'''

#2
'''
ctmr=str(input("Are you vegetarian or non-vegetarain:"))
if ctmr=='vegetarian':
    fd=str(input("Do you want salad or pasta:"))
elif ctmr=='non-vegetarian':
    st=str(input("Do you want fish or chicken:"))
'''

#3
'''
sal=float(input("Please,Enter your monthly salary:"))
if sal>50000:
    print("High Earner")
elif sal<=50000 and sal>20000:
    print("Mid Earner")
else:
    print("Low Earner")
'''

#4
'''
num=int(input("Enter a number"))
if num%5==0 and num%2==0:
        print("It is divisible by both 2 and 5")
elif num%2==0:
      print("it is only divisible by 2")
else:
    print("It is not divisble by both")'''

#5
'''
mk=float(input("Enter your marks:"))
if mk>=90 and mk<=100: print("Excellent")
elif mk>=51 and mk<90: print("Good")
elif mk<51: print("Fail")'''

#6
'''
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
if num1>num2:
    if num1>num3:
        print(f"{num1} is the largest")
    else:
        print(f"{num3} is the largest")
elif num2>num1:
    if num2>num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest")'''

#7
'''
print("Welcome to the Forest Adventure")
lr=str(input("Choose left or right path:"))
if lr=='right': print("You fell into a trap. Game Over.")
elif lr=='left': 
    er=str(input("Do you want to explore or rest?"))
    if er=='explore': print("You found treasure!")
    elif er=='rest': print("You were attacked by wild animals. Game Over.")'''

#8
'''print("Welcome to the Jungle Survival Challenge")
lr=str(input("Do you want to search for food or build a shelter?"))
if lr=='bulid a shelter': print("Your shelter collapsed in the rain. Game Over.")
elif lr=='search for food': 
    er=str(input("Do you hunt or gather?"))
    if er=='gather': print("You found enough food. You Win!")
    elif er=='hunt': print("You were attacked by wild animals. Game Over.")'''

#9
'''print("Welcome to the Space Adventure")
lr=str(input("Choose to land on mars or fly to jupiter:"))
if lr=='fly to jupiter': print("Your spaceship crashed.Game Over")
elif lr=='land on mars': 
    er=str(input("Do you want to explore or build a base?"))
    if er=='explore': print("You found alien artifacts. You Win!")
    elif er=='build a base': print("You ran out of resources. Game Over.")'''

#10
'''print("Welcome to the Haunted Castle")
lr=str(input("Do you want to enter the castle or run away?"))
if lr=='run away': print("you eacaped safely")
elif lr=='enter the castle': 
    er=str(input("Choose a door red,green or black"))
    if er=='red': print("You entered a room full of flames. Game Over.")
    elif er=='green': print("You found the treasure. You Win!")
    elif er=='black': print("You were captured by ghosts. Game Over.")'''

#11
'''print("Welcome to the Underwater World")
lr=str(input("Choose to dive deeper or surface:"))
if lr=='surface': print("You returned safely")
elif lr=='dive deeper':
    er=str(input("Do you want to search for pearls or chase the fish?"))
    if er=='search for pearls': print("You found a rare pearl. You Win")
    elif er=='chase the fish': print("You got lost underwater. Game Over.")'''

#12
'''print("Welcome to the Pirate Ship Adventure")
td = str(input("Choose between searches for treasure or battle enemy ships: "))
if td == 'searches for treasure':
    lr = str(input("Do you want to dig on the island or explore the cave? "))
    if lr == 'dig on the island': print("You found a hidden treasure chest. You Win!")
    elif lr == 'explore the cave': print("You were trapped inside. Game Over.")
elif td == 'battle enemy ships':
    fight=str(input("You want to attack or defend?"))
    if fight=='attack':  print("You won the battle. You Win!")
    elif fight=='defend': print("You were outnumbered. Game Over.")'''

#13
'''print("Welcome to the Wizarding World")
subject = str(input("Choose a subject: 'spells' or 'potions': "))
if subject == 'spells':
    lr = str(input("Do you want to 'practice magic' or 'compete in duels'? "))
    if lr == 'practice magic':print("You mastered a powerful spell. You Win!")
    elif lr == 'compete in duels':print("You lost to a rival wizard. Game Over.")
elif subject == 'potions':
    lr = str(input("Do you want to 'brew an elixir' or 'create poison'? "))
    if lr == 'brew an elixir':print("You healed a village. You Win!")
    elif lr == 'create poison': print("Your potion backfired. Game Over.")'''

#14
'''print("Welcome to the Cybersecurity Mission")
task = str(input("Choose to 'trace the hacker' or 'secure the system': "))
if task == 'trace the hacker':
    td = str(input("Do you want to 'track their IP' or 'decode their message'? "))
    if td == 'track their IP':print("You caught the hacker. You Win!")
    elif td == 'decode their message':print("The message was a trap. Game Over.")
elif task == 'secure the system':
    td = str(input("Do you want to 'shut down the server' or 'upgrade the firewall'? "))
    if td == 'shut down the server':print("The attack was stopped. You Win!")
    elif td == 'upgrade the firewall': print("The hacker bypassed it. Game Over.")'''

#15
'''num=int(input("Enter a number:"))
if num%2==0 and num%7==0: print("Double Seven")
elif num%2==0 and num%7!=0: print("Even")
elif num%7==0 and num%2!=0: print("Lucky Seven")
else: print(num)'''

#16
'''num=int(input("Enter a number:"))
if num>=100: print("Big Number")
elif num>=50 and num<100: print("Medium Number")
else: print("Small Number")'''

#17
'''clr=str(input("Enter a traffic light color"))
if clr=='red':print("Stop")
elif clr=='yellow':print("Slow Down")
elif clr=='green':print("GO")
else: print("Invalid Signal")'''

#18
'''tem=float(input("Enter the temerature in celsius:"))
if tem>=40: print("Hot")
elif tem>=20 and tem<40: print("Warm")
else: print("Cold")'''

#19
'''bmi=float(input("What is your BMI?"))
if bmi<18.5: print( "Underweight")
elif 18.5<=bmi<24.9: print("Normal weight")
elif 25<=bmi<29.9: print("Overweight")
else: print("Obesity")'''

#20
'''a=int(input("Enter 1st number:")) 
b=int(input("Enter 2nd number:"))
if a%2==0 and b%2==0: print("The sum is ",a+b)
elif (a%2==0 and b%2!=0) or (a%2!=0 and b%2==0): print("The difference is ",a-b)
else: print("The product is ",a*b)'''

#21
'''pri=float(input("Enter the price of an item:"))
if pri>1000: d=0.2
elif 500<=pri<1000: d=0.1
else: d=0
print("The new price will be ",pri-(pri*d))'''

#22
'''ag=int(input("Enter your age:"))
if ag<18:
    print("You are underage")
    exit()
gen=str(input("Are you male or female(M or F)?"))
inc=float(input("Enter your income:"))
if 18<=ag<60:
    if gen=='M':
        if inc>1000000:inc=inc*0.3
        elif 500000<inc<=1000000: inc=inc*0.2
        elif inc<=500000: inc=inc*0.1
    elif gen=='F':
        if inc>1000000: inc=inc*0.25
        elif 500000<inc<=1000000: inc=inc*0.15
        elif inc<=500000: inc=inc*0.05
elif ag>=60:
    if gen=='M' or gen=='F':
        if inc>1000000: inc=inc*0.2
        elif inc<=1000000:inc=inc*0.1
print(f"You have to pay {inc} as tax")'''
        
#23
'''age=int(input("Enter your age:"))
gen=str(input("Are you M or F"))
acs=float(input("What is your academic score?"))
if 18<=age<=25:
    if gen=='M':
        if acs>=85: print("Full Scholarship")
        elif acs>=70: print("Partial Scholarship")
        else: print("No scholarship")
    elif gen=='F':
        if acs>=80: print("Full Scholarship")
        elif acs>=65:print("Partial Scholarship")
        else: print("No Scholarship")'''

#24
'''age=int(input("Enter your age:"))
gen=str(input("Are you M or F?"))
exp=float(input("What is your experience(years)?"))
if 21<=age<=35:
    if gen=='M':
        if exp>=5: print("Senior Developer")
        else: print("Junior Developer")
    elif gen=='F':
        if exp>=5: print("Senior Analyst")
        else: print("Junior Analyst")
elif age>35: print("Manager Role")'''

#25
'''age=int(input("Enter your age:"))
gen=str(input("Are you M or F?"))
st=str(input("What is your show type(matinee or evening)?"))
if age<12:
    if st=='matinee': print("Rs500")
    elif st=='evening': print("Rs700")
elif 12<=age<60:
    if gen=='M':
        if st=='matinee': print("Rs800")
        elif st=='evening': print("Rs1000")
    elif gen=='F':
        if st=='matinee': print("Rs700")
        elif st=='evening': print("Rs900")
else:print("Rs600")'''

#26
'''age=int(input("Enter your age:"))
if age<18:
    print("You can't take membership")
    exit()
gen=str(input("Are you M or F?"))
mt=str(input("What is your membership type(monthly or yearly)?"))
if 18<=age<30:
    if gen=='M':
        if mt=='monthly': print("Rs50")
        elif mt=='yearly': print("Rs500")
    elif gen=='F':
        if mt=='monthly': print("Rs45")
        elif mt=='yearly': print("Rs450")
elif 30<=age<=50:
    if mt=='monthly': print("Rs60")
    elif mt=='yearly': print("Rs600")
else:
    if mt=='monthly': print("Rs40")
    elif mt=='yearly': print("Rs400")'''