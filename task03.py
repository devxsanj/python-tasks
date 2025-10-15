def getGrade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks < 50:
        return "Fail"
    
print(f"grade is {getGrade(95)}")
print(f"grade is {getGrade(68)}")
print(f"grade is {getGrade(44)}")