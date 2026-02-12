def student_stat():
    marks_input = input("Enter marks separated by commas: ")
    marks = marks_input.split(",")
    marks = [int(m) for m in marks]
    
    total_students = len(marks)
    total_marks = sum(marks)
    average_marks = total_marks / total_students
    highest_mark = max(marks)
    lowest_mark = min(marks)
    if average_marks >= 75:
        performance = "Excellent"
    elif average_marks >= 50:
        performance = "Good"
    else:
        performance = "Needs Improvement"
    print("\n--- Student Performance Summary ---")
    print("Total Students:", total_students)
    print("Average Marks:", round(average_marks, 2))
    print("Highest Mark:", highest_mark)
    print("Lowest Mark:", lowest_mark)
    print("Overall Performance:", performance)

student_stat()
if total_students == 0:
    print("No marks provided")
    return



