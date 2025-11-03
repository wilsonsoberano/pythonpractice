x = 0
while x < 10:
 x = x + 2
 print(x)

print("There is a rectangle, of which one side is 3 and the other side is 4.") 
side_1 = 3
side_2 = 4
print(f"I think the area of the rectangle is: {side_1 * side_2}.") # This line prints a f-string, 

print("Hello, COMP101 students!")
print("Do you want to play a guessing game with me?")

while True:
    start = input('Enter "1" to play or replay, "0" to stop: ')
    
    if start == "0":
        print("Okay, goodbye!")
        break
    elif start == "1":
        print("\nGreat! Think of a number between 1 and 1000 and write it down.")
        print("I will try to guess it. Type:")
        print('   "b" if your number is bigger than my guess,')
        print('   "s" if your number is smaller than my guess,')
        print('   "y" if I guessed it right.\n')

        low = 1
        high = 1000
        rounds = 0

        while low <= high:
            guess = (low + high) // 2
            rounds += 1
            print(f"My guess #{rounds}: {guess}")
            response = input('Is your number (b)igger, (s)maller, or (y)es? ').lower()

            if response == "y":
                print(f"\nYay! I found your number {guess} in {rounds} rounds!\n")
                break
            elif response == "b":
                low = guess + 1
            elif response == "s":
                high = guess - 1
            else:
                print("Invalid input. Please type 'b', 's', or 'y'.")
    else:
        print('Please enter only "1" or "0".')