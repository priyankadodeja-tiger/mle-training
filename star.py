# Python 3.x code to demonstrate star pattern


# Function to demonstrate printing pattern
def pypart(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")

        print("\r")


# Driver Code
n = 5
pypart(n)
