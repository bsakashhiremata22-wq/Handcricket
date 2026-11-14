
import random

print("I" * 190)
print("\t\t\t\t\t PLAYING HAND CRICKET WITH COMPUTER USING PYTHON AND RANDOM FUCTION ")
print("I" * 190)

print()
print(":" * 60)
print("\t\t\tTOSS TIME")
print(":" * 60)


user_choice = input("\nEnter the choice (Even or odd): ").lower()
while user_choice not in ["even", "odd"]:
    user_choice = input("\n you choice should not be character or number \nEnter the choice (Even or odd): ").lower()

if user_choice == "even":
    print("\nYour Choice is Even")
    print("Then the Computer Choice is Odd")
else:
    print("\nYour Choice is Odd")
    print("Then The Computer Choice is Even")

print()

try:
    user_number = int(input("Enter the number within the range(1-6): "))
except ValueError:
    user_number = int(input("Enter the number within the range(1-6): "))

while user_number not in [1, 2, 3, 4, 5, 6]:
    print()
    
    try:
        user_number = int(input("Enter the number within the range(1-6): "))
    except ValueError:
        user_number = int(input("Enter the number within the range(1-6): "))

computer_n = random.randint(1, 6)
print(f"Your Number is {user_number} ")
print(f"The Computer number is {computer_n}")

sum = user_number + computer_n
print()
print(f"The sum of both of numbers is {sum}\n")

computer_choice_bb = ["batting", "bowling"]

if (sum % 2 == 0 and user_choice == "even") or (sum % 2 != 0 and user_choice == "odd"):
    print("You have won the toss\n")
    bb = (input("Tell your decision (Batting or Bowling):")).lower()
    while bb not in ["batting", "bowling"]:
        bb = (input("Tell your decision (Batting or Bowling):")).lower()
    print(f"You have decide to {bb} first")
    if bb == "batting":
        your_score = 0
        try:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        except ValueError:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))

        while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
            print("Enter runs withing the range(1-6)")
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))

        computer_balling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {computer_balling_runs}\n")

        while your_batting_runs != computer_balling_runs:
            your_score += your_batting_runs
            try:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))
            except ValueError:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))

            while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
                print("\nEnter your runs within the range(1-6)")
                try:
                    your_batting_runs = int(
                        input("Enter your runs scored ball by ball: ")
                    )
                except ValueError:
                    your_batting_runs = int(
                        input("Enter your runs scored ball by ball: ")
                    )
            computer_balling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {computer_balling_runs}\n")

        print("\n !YOU GOT OUT\n")
        print("-" * 65)
        print(f"\t\t YOUR SCORE IS {your_score}")
        print("-" * 65)

        print()
        computer_score = 0
        computer_batting_runs = random.randint(1, 6)
        try:
            your_bowling_runs = int(input("\nEnter your bowling score: "))
        except ValueError:
            your_bowling_runs = int(input("\nEnter your bowling score: "))

        while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
            print("\nYour bowling score should be within the range(1-6)")
            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
        print(f"The Computer batting runs is {computer_batting_runs}")

        while computer_batting_runs != your_bowling_runs:
            computer_score += computer_batting_runs
            computer_batting_runs = random.randint(1, 6)
            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))

            while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
                print("\nYour bowling score should be within the range(1-6)")
                try:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
                except ValueError:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
            print(f"The Computer batting runs is {computer_batting_runs}")

        print("\n !COMPUTER GOT OUT\n")
        print("-" * 65)
        print(f"\t\t THE COMPUTER SCORE IS {computer_score}")
        print("-" * 65)

        lead_runs = abs(your_score - computer_score)

        print("=" * 150)
        if your_score > computer_score:
            print(
                f"\t\tCONGRATULATIONS YOU ARE THE WINNER \t YOU WON BY {lead_runs} RUNS"
            )
        else:
            print(f"\t\tBETTER LUCK NEXT TIME \t YOU LOST BY {lead_runs} RUNS")
        print("=" * 150)

    else:
        computer_score = 0
        computer_batting_runs = random.randint(1, 6)
        try:
            your_bowling_runs = int(input("\nEnter your bowling score: "))
        except ValueError:
            your_bowling_runs = int(input("\nEnter your bowling score: "))

        while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
            print("\nYour bowling score should be within the range(1-6)")
            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
        print(f"The Computer batting runs is {computer_batting_runs}")

        while computer_batting_runs != your_bowling_runs:
            computer_score += computer_batting_runs
            computer_batting_runs = random.randint(1, 6)
            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))

            while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
                print("\nYour bowling score should be within the range(1-6)")
                try:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
                except ValueError:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
            print(f"The Computer batting runs is {computer_batting_runs}")

        print("\n !COMPUTER GOT OUT\n")
        print("-" * 65)
        print(f"\t\tTHE COMPUTER SCORE IS {computer_score}")
        print("-" * 65)

        print()
        your_score = 0
        try:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        except ValueError:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))

        while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
            print("Enter runs withing the range(1-6)")
            try:
                your_batting_runs = int(
                    input("\nEnter your runs scored ball by ball: ")
                )
            except ValueError:
                your_batting_runs = int(
                    input("\nEnter your runs scored ball by ball: ")
                )

        computer_balling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {computer_balling_runs}")

        while your_batting_runs != computer_balling_runs:
            your_score += your_batting_runs
            try:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))
            except ValueError:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))

            while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
                print("\nEnter your runs within the range(1-6)")

                try:
                    your_batting_runs = int(input("Enter your runs scored ball by ball: "))
                except ValueError:
                    your_batting_runs = int(input("Enter your runs scored ball by ball: "))

            computer_balling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {computer_balling_runs}\n")

        print("\n !YOU GOT OUT\n")
        print("-" * 65)
        print(f"\t\tYOUR SCORE IS {your_score}")
        print("-" * 65)

        lead_runs = abs(your_score - computer_score)

        print("=" * 150)
        if your_score > computer_score:
            print(
                f"\t\tCONGRATULATIONS YOU ARE THE WINNER \t YOU WON BY {lead_runs} RUNS"
            )
        else:
            print(f"\t\tBETTER LUCK NEXT TIME \t YOU LOST BY {lead_runs} RUNS")
        print("=" * 150)
else:
    cc_rand = random.randint(0, 1)
    cc = computer_choice_bb[cc_rand]
    print(f"Computer won the toss and Computer had  decide to {cc} first")

    if cc_rand == 0:
        computer_score = 0
        computer_batting_runs = random.randint(1, 6)
        try:
            your_bowling_runs = int(input("\nEnter your bowling score: "))
        except ValueError:
            your_bowling_runs = int(input("\nEnter your bowling score: "))

        while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
            print("\nYour bowling score should be within the range(1-6)")
            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            print(f"The Computer batting runs is {computer_batting_runs}\n")

        while computer_batting_runs != your_bowling_runs:
            computer_score += computer_batting_runs
            computer_batting_runs = random.randint(1, 6)
            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))

            while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
                print("\nYour bowling score should be within the range(1-6)")
                try:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
                except ValueError:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
                print(f"The Computer batting runs is {computer_batting_runs}\n")

        print("\n !COMPUTER GOT OUT\n")
        print("-" * 65)
        print(f"\t\tTHE COMPUTER SCORE IS {computer_score}")
        print("-" * 65)

        print()
        your_score = 0
        try:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        except ValueError:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
            print("Enter runs withing the range(1-6)")
            try:
                your_batting_runs = int(
                    input("\nEnter your runs scored ball by ball: ")
                )
            except ValueError:
                your_batting_runs = int(
                    input("\nEnter your runs scored ball by ball: ")
                )

        computer_balling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {computer_balling_runs}\n")

        while your_batting_runs != computer_balling_runs:
            your_score += your_batting_runs
            try:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))
            except ValueError:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))

            while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
                print("\nEnter your runs within the range(1-6)")
                try:
                    your_batting_runs = int(
                        input("Enter your runs scored ball by ball: ")
                    )
                except ValueError:
                    your_batting_runs = int(
                        input("Enter your runs scored ball by ball: ")
                    )
            computer_balling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {computer_balling_runs}")

        print("\n !YOU GOT OUT\n")
        print("-" * 65)
        print(f"\t\tYOUR SCORE IS {your_score}")
        print("-" * 65)

        lead_runs = abs(your_score - computer_score)

        print("=" * 150)
        if your_score > computer_score:
            print(
                f"\t\tCONGRATULATIONS YOU ARE THE WINNER \t YOU WON BY {lead_runs} RUNS"
            )
        else:
            print(f"\t\tBETTER LUCK NEXT TIME \t YOU LOST BY {lead_runs} RUNS")
        print("=" * 150)

    else:
        your_score = 0
        try:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))
        except ValueError:
            your_batting_runs = int(input("\nEnter your runs scored ball by ball: "))

        while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
            print("Enter runs withing the range(1-6)")
            try:
                your_batting_runs = int(
                    input("\nEnter your runs scored ball by ball: ")
                )
            except ValueError:
                your_batting_runs = int(
                    input("\nEnter your runs scored ball by ball: ")
                )

        computer_balling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {computer_balling_runs}\n")

        while your_batting_runs != computer_balling_runs:
            your_score += your_batting_runs
            try:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))
            except ValueError:
                your_batting_runs = int(input("Enter your runs scored ball by ball: "))

            while your_batting_runs not in [1, 2, 3, 4, 5, 6]:
                print("\nEnter your runs within the range(1-6)")
                try:
                    your_batting_runs = int(
                        input("Enter your runs scored ball by ball: ")
                    )
                except ValueError:
                    your_batting_runs = int(
                        input("Enter your runs scored ball by ball: ")
                    )
            computer_balling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {computer_balling_runs}\n")

        print("\n !YOU GOT OUT\n")
        print("-" * 65)
        print(f"\t\tYOUR SCORE IS {your_score}")
        print("-" * 65)

        print()
        computer_score = 0
        computer_batting_runs = random.randint(1, 6)
        try:
            your_bowling_runs = int(input("\nEnter your bowling score: "))
        except ValueError:
            your_bowling_runs = int(input("\nEnter your bowling score: "))

        while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
            print("\nYour bowling score should be within the range(1-6)")
            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
        print(f"The Computer batting runs is {computer_batting_runs}")

        while computer_batting_runs != your_bowling_runs:
            computer_score += computer_batting_runs
            computer_batting_runs = random.randint(1, 6)

            try:
                your_bowling_runs = int(input("\nEnter your bowling score: "))
            except ValueError:
                your_bowling_runs = int(input("\nEnter your bowling score: "))

            while your_bowling_runs not in [1, 2, 3, 4, 5, 6]:
                print(
                    "\nYour bowling scoryour_bowling_runse should be within the range(1-6)"
                )
                try:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
                except ValueError:
                    your_bowling_runs = int(input("\nEnter your bowling score: "))
        print(f"The Computer batting runs is {computer_batting_runs}")

        print("\n !COMPUTER GOT OUT\n")
        print("-" * 65)
        print(f"\t\tTHE COMPUTER SCORE IS {computer_score}")
        print("-" * 65)

        lead_runs = abs(your_score - computer_score)

        print("=" * 150)
        if your_score > computer_score:
            print(f"\t\tCONGRATULATIONS YOU ARE THE WINNER \t YOU WON BY {lead_runs} RUNS")
        else:
            print(f"\t\tBETTER LUCK NEXT TIME \t YOU LOST BY {lead_runs} RUNS")
        print("=" * 150)
