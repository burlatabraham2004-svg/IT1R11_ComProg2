while True:
    ID = int(input("Enter your Student ID: "))
    Name = input("What is your name: ")
    course = input("Enter your Course: ")
    subject = input("Enter your Subject:")
    PreLim = int(input("Enter your prelim grades: "))
    MidTerm = int(input("Enter your Midterm grades: "))
    FinalTerm = int(input("Enter your Final grades: "))

    Average = (PreLim * 0.20) + (MidTerm * 0.30) + (FinalTerm * 0.50)

    print("---------------------------")
    print("Student ID:", ID)
    print("Student Name:", Name)
    print("Student Course: ", course)
    print("Student Subject: ", subject)
    print("Prelim Grade:", PreLim)
    print("Midterm Grade:", MidTerm)
    print("Final Term Grade:", FinalTerm)
    print(f"General Weighted Average: {Average:.2f}")

    if Average >= 75:
        print("Remarks: PASSED")
    else:
        print("Remarks: FAILED")

    print("---------------------------")

    choice = input("Do you want to enter another student? (y/n): ")

    if choice == 'n':
        print("Program terminated, Thanks for using!!")
        break

