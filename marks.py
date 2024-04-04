# if, else if ladder
# >80 -> distinction
# 60-80 -> first division
# 40-60 -> second division
# <40 -> fail

marks = 70

if (marks >= 80): # 70 >= 80 false
    print("Distinction")
elif (marks >= 60): # 70 >= 60 true
    print("First Division")
elif (marks >= 40): # 70 >= 40 true but will not be checked
    print("Second Division")
else:
    print("Fail")
