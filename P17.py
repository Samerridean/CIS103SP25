import random

def generatenumbers(high,count):
    numbers = random.sample(range(1,high + 1),count)
    numbers.sort()
    return numbers
def display():
    print("1. Power Ball")
    print("2. Mega Million")
    print("3. Lucky Day Lotto")
    print("4. Lotto")
    print("9. Quit")
def main():
    LGames = {
        "1": ("Power Ball", 69, 5),
        "2": ("Mega Million", 70, 5),
        "3": ("Lucky Day Lotto", 45, 5),
        "4": ("Lotto", 52, 6)}
    while True:
        display()
        choice=input("Select an option: ").strip()      
        if choice == "9":
            break        
        elif choice in  LGames:
            name,high,count = LGames[choice]
            numbers=generatenumbers(high,count)
            numbers_str = ", ".join(str(num) for num in numbers)
            print(f"{name} {numbers_str}")
            retry = input("Hit Enter to Return to Menu").strip().lower()
        else:
            print("Invalid option.")
main()
