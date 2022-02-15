print("Program Started!")
code = int(input("Please enter an ASCII code: \n"))

if code >= 32 and code <= 126:
    print(f"The character represented by the ASCII code {code} is {chr(code)} ")
else:
    print("Enter a value within 32 and 126")
print("Program Ended!")
