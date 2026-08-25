students={
    "Vidya" : 85,
    "Rahul" : 72,
    "Priya" : 91,
    "Amit" : 68,
    "Gauri" :35
}
for name,marks in students.items():
    if marks>=75:
        print("Name:-",name," Marks",marks," Result:-Distinction")
    elif marks>=60:
        print("Name:-",name," Marks",marks ," Result:-First Class")
    elif marks>=40:
        print("Name:-",name," Marks",marks," Result:-Pass")
    else:
        print("Name:-",name," Marks",marks," Result:-Fail")