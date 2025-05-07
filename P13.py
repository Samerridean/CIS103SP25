romandict={1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
    11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV",
    16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX",
    21: "XXI", 22: "XXII", 23: "XXIII", 24: "XXIV"}

def isroman(roman):
    return roman.isalpha()
ans='y'
while ans=='y':
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Dictionary:")
            print(romandict)
            break
        if num in romandict:
            print(f"{num}->{romandict[num]}")
        else:
            addnew = input(f"{num} is not in dictionary. Would you like to add it? y/n: ").strip().lower()
            if addnew == "y":
                romannum = input(f"Enter the Roman numeral for {num}: ").strip().upper()
                if isroman(romannum):
                    romandict[num] = romannum
                    print(f"Added {num} -> {romannum}")
                else:
                    print("Invalid Roman numeral. Must be alphabetic.")
            print("Dictionary:")
            print(romandict)
    except ValueError:
        print("Invalid input. Please Enter an A Number.")
    ans=input('Again? y/n:')


