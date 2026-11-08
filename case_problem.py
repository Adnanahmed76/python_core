# we are gonna write code to solve student marks analysis

def analyze_student_marks(marks):

    total_marks=sum(marks)
    avg=total_marks/len(marks)
    hightest=max(marks)
    print(f"Total Marks is : {total_marks}, Average Marks is : {avg}, Highest Marks is : {hightest}")

print(analyze_student_marks([78,85,90,67]))