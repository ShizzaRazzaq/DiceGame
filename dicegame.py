import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def main():
    print("🎲 Welcome to the Dice Rolling Simulator!")
    total_rolls = 0

    try:
        num_dice = int(input("How many dice would you like to roll? "))
        if num_dice <= 0:
            print("Number of dice must be at least 1.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    while True:
        input("Press Enter to roll the dice... ")
        results = roll_dice(num_dice)
        total_rolls += 1

        print(f"Roll #{total_rolls}: ", end="")
        print(" | ".join(f"Die {i+1}: {value}" for i, value in enumerate(results)))

        again = input("Would you like to roll again? (y/n): ").strip().lower()
        if again != 'y':
            break

    print(f"🎯 You rolled the dice {total_rolls} times. Thanks for playing!")

if __name__ == "__main__":
    main()
