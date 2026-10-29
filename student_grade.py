
# Get student name
name = input("Enter student name: ")

# Get marks for three subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Validate marks
if not (0 <= mark1 <= 100 and 0 <= mark2 <= 100 and 0 <= mark3 <= 100):
    print("Invalid marks! Enter marks between 0 and 100.")

else:
    # Calculate total and average
    total = mark1 + mark2 + mark3
    average = total / 3

    # Calculate grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    # Display student results
    print("\n--- Student Results ---")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)
