def student_stat():
    marks_input = input("Enter marks separated by commas: ")
    marks = marks_input.split(",")
    marks = [int(m) for m in marks]
    
    total_students = len(marks)
    total_marks = sum(marks)
    average_marks = total_marks / total_students
    highest_mark = max(marks)
    lowest_mark = min(marks)



