#Print corresponding GPA value related to the grade
def gpavalue(grade):
    try:
        match grade:
            case "O":
                return "10"
            case "A+":
                return "9"
            case "A":
                return "8"
            case "B+":
                return "7"
            case "B":
                return "6"
            case _:
                return "Invalid garde"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    grade=input("Enter the grade ")
    print(gpavalue(grade))
