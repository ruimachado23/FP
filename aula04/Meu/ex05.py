import random

def main():
    secret = random.randrange(1, 11);
    print("Can you guess my secret?")
    n = int (input("Pick a number: "))
    t = 1
    while secret != n:
        if n > secret:
            print ("LOWER")
            n = int (input("Pick a new number: "))
        elif secret > n:
            print ("HIGHER!")
            n = int (input("Pick a new number: "))
        t+=1
        
    print ("GOOD JOB, you made it in", t, "times")
    

main()