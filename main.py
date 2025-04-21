import math
def start_game():
    print(" Welcome to the GCD Game ofr Kids!")
    print("Let's find the biggest number that divides both!")
    print("Let's find the biggest number that divides both")


    while True:
        num1 = input(" Enter the first number(or type 'exit' to quit):")
        if num1.lower()== 'exit':
            print("Thanks for playing! You're a math star!")

        num2 = input(" Enter the second number:")
        if num2.lower() == 'exit':
            print("Thanks for playing! Keep rocking numbers! ")    
            break

        if not num1.isdigit() or not num2.isdigit():
            print(" Please enter numbers only! No letters or symbols!\n")
            continue

        a = int(num1)
        b=  int(num2)
        gcd = math.gcd(a,b)

        print(f" The GCD OF {a} and {b} is: {gcd} \n")

# star the game        

    