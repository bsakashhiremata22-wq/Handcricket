import random

print("I" * 190)
print("\n\t\t\t\t\t PLAYING HAND CRICKET WITH COMPUTER USING PYTHON AND RANDOM FUCTION\n ")
print("I" * 190)

print()
print(":" * 60)
print("\t\t\tTOSS TIME")
print(":" * 60)

def start_game():
        print("-"*80)
        print("\t\t\t\tGAMEPLAY BEGINS")
        print("-"*80)

def result(Your_score,Computer_score,lead_runs):
    lead_runs = abs(Your_score - Computer_score)
    print("=" * 150)
    if Your_score > Computer_score:
        print(f"\t\tCONGRATULATIONS YOU ARE THE WINNER \t YOU WON BY {lead_runs} RUNS")
    elif Your_score < Computer_score:
        print(f"\t\tBETTER LUCK NEXT TIME \t YOU LOST BY {lead_runs} RUNS")
    elif Your_score == Computer_score:
        print(f"\t\t\tDRAW MATCH YOUR SCORE AND THE COMPUTER SCORE BOTH ARE SAME")
    print("=" * 150)

def Computer_out(Computer_score):
    print("\n\t\t [ COMPUTER GOT OUT ]")
    print("-" * 65)
    print(f"\t\t THE COMPUTER SCORE IS {Computer_score}")
    print("-" * 65)

def You_out(Your_score):
    print("\n\t\t [ YOU GOT OUT ]")
    print("-" * 65)
    print(f"\t\tYOUR SCORE IS {Your_score}")
    print("-" * 65)

def your_batting(Your_batting_runs):
    while True:
        try:
            if Your_batting_runs in [1,2,3,4,5,6]:
                break
            elif Your_batting_runs not in [1,2,3,4,5,6]:
                Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        except ValueError:
            print("Enter only numbers with in range of 1 to 6")

def your_bowling(Your_bowling_runs):
    while True:
        try:
            if Your_bowling_runs in [1,2,3,4,5,6]:
                break
            elif Your_bowling_runs not in [1,2,3,4,5,6]:
                Your_bowling_runs = int(input("\nEnter your bowling runs within (1,2,3,4,5,6): "))
        except ValueError:
            print("Enter only numbers with in range of 1 to 6")


User_Choice = input("\nEnter the choice (Even or odd): ").lower()
while User_Choice not in ["even", "odd"]:
    User_Choice = input("\n enter the choice as per given in the bracket \nEnter the choice (Even or odd): ").lower()

if User_Choice == "even":
    print("\nYour Choice is Even \nThen the Computer Choice is Odd\n")
else:
    print("\nYour Choice is Odd \nThen The Computer Choice is Even\n")

while True:
    try:
        user_number = int(input("Enter the number within the range(1-6): "))
        if  user_number  in [1, 2, 3, 4, 5, 6]:
            break
        elif user_number not in [1, 2, 3, 4, 5, 6]:
            user_number = int(input("Enter the number within the range(1-6): "))
    except ValueError:
        print("Enter the number don't enter anything it doesn't work")

Computer_number = random.randint(1, 6)
print(f"\nYour Number is {user_number}\nThe Computer number is {Computer_number}\n")

Total = user_number + Computer_number
if Total%2==0:
    Total_as_per_choice='Even'
else:
    Total_as_per_choice='Odd'
print(f"The sum of both of numbers is {Total} and It is {Total_as_per_choice} \n")

Computer_decision = ["batting", "bowling"]

if (Total % 2 == 0 and User_Choice == "even") or (Total % 2 != 0 and User_Choice == "odd"):
    print("You have won the toss\n")

    Your_decision = (input("Tell your decision (Batting or Bowling):")).lower()
    
    while Your_decision not in ["batting", "bowling"]:
        Your_decision = (input("Tell your decision (Batting or Bowling):")).lower()

    start_game()

    if Your_decision == "batting":
        Your_score = 0

        Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        your_batting(Your_batting_runs)
    

        Computer_bowling_runs = random.randint(1, 6)
        print(f"Computer bowling runs is {Computer_bowling_runs}")

        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs

            Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
            your_batting(Your_batting_runs)

            Computer_bowling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {Computer_bowling_runs}")

        You_out(Your_score)

        print()
        Computer_score = 0
        Computer_batting_runs = random.randint(1, 6)
    
        Your_bowling_runs = int(input("\nEnter your bowling score: "))
        your_bowling(Your_bowling_runs)



        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs
            Computer_batting_runs = random.randint(1, 6)

            while Computer_score < Your_score:
                break

            Your_bowling_runs = int(input("\nEnter your bowling score: "))
            your_bowling(Your_bowling_runs)

            print(f"The Computer batting runs is {Computer_batting_runs}")

        Computer_out(Computer_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score,lead_runs)

    else:
        Computer_score = 0
        Computer_batting_runs = random.randint(1, 6)

        Your_bowling_runs = int(input("\nEnter your bowling score: "))
        your_bowling(Your_bowling_runs)

        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs
            Computer_batting_runs = random.randint(1, 6)

            Your_bowling_runs = int(input("\nEnter your bowling score: "))
            your_bowling(Your_bowling_runs)

            print(f"The Computer batting runs is {Computer_batting_runs}")

        Computer_out(Computer_score)

        print()
        Your_score = 0
        Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        your_batting(Your_batting_runs)

        Computer_bowling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {Computer_bowling_runs}")


        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs

            while Computer_score > Your_score:
                break

            Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
            your_batting(Your_batting_runs)

            Computer_bowling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {Computer_bowling_runs}")

        You_out(Your_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score,lead_runs)
else:
    Computer_choosen = random.randint(0, 1)
    Computer_choice= Computer_decision[Computer_choosen]
    print(f"Computer won the toss and Computer had  decide to {Computer_choice} first")

    start_game()

    if Computer_choosen == 0:
        Computer_score = 0
        Computer_batting_runs = random.randint(1, 6)

        Your_bowling_runs = int(input("\nEnter your bowling score: "))
        your_bowling(Your_bowling_runs)
        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs
            Computer_batting_runs = random.randint(1, 6)
            Your_bowling_runs = int(input("\nEnter your bowling score: "))
            your_bowling(Your_bowling_runs)
            print(f"The Computer batting runs is {Computer_batting_runs}")

        Computer_out(Computer_score)

        print()
        Your_score = 0
        Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        your_batting(Your_batting_runs)

        Computer_bowling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {Computer_bowling_runs}")

        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs

            while Computer_score > Your_score:
                break

            Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
            your_batting(Your_batting_runs)
            Computer_bowling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {Computer_bowling_runs}")

        You_out(Your_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score,lead_runs)

    else:
        Your_score = 0
        Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        your_batting(Your_batting_runs)

        Computer_bowling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {Computer_bowling_runs}")

        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs
            Your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
            your_batting(Your_batting_runs)
            Computer_bowling_runs = random.randint(1, 6)
            print(f"Computer bowling runs is {Computer_bowling_runs}")

        You_out(Your_score)

        print()
        Computer_score = 0
        Computer_batting_runs = random.randint(1, 6)

        Your_bowling_runs = int(input("\nEnter your bowling score: "))
        your_bowling(Your_bowling_runs)

        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs

            while Computer_score < Your_score:
                break

            Computer_batting_runs = random.randint(1, 6)

            Your_bowling_runs = int(input("\nEnter your bowling score: "))
            your_bowling(Your_bowling_runs)

            print(f"The Computer batting runs is {Computer_batting_runs}")

        Computer_out(Computer_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score,lead_runs)
            
