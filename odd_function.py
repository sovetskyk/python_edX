"""
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")

else:
    print("Odd")
"""

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print ("Even")
    else:
        print ("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
