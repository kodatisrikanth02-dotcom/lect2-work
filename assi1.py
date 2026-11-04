length =float(input("Enter the length of the zander in centimeters: "))
if length < 42:
    short = 42 - length
    print(f"The zander is too small. Please release it back into the lake.")
    print(f"The zander is {short} centimeters short of the legal size limit.")
else:
    print("The zander is legal size. You can keep it.")