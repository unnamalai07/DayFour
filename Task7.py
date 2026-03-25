# Print the performamnce message related to the grade
def performancemessage(grade):
    try:
        match grade:
            case "A":
                return "Excellent"
            case "B":
                return "Good"
            case "C":
                return "Average"
            case "D":
                return "Below Average"
            case "F":
                return "Fasil"
            case _:
                return "Invalid Grade"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    grade=input("Enter the grade ")
    print(performancemessage(grade))

