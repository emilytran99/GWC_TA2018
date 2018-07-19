def add(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

def finalAns(num):
    num = num + 3
    print(num)
    return num

num3 = 7

# --- Put your main program below! ---
def main():
    num1 = 5
    num2 = 3
    addResult = add(num1, num2)
    multResult = mult(addResult, num3)
    finalAns(multResult)
    
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
