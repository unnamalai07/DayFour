# Print the month name related to the input
def monthname(inputID):
    try:
        match inputID:
            case 1:
                return "January"
            case 2:
                return "February"
            case 3:
                return "March"
            case 4:
                return "April"
            case 5:
                return "May"
            case 6:
                return "June"
            case 7:
                return "July"
            case 8:
                return "August"
            case 9:
                return "September"
            case 10:
                return "October"
            case 11:
                return "November"
            case 12:
                return "December"
            case _:
                return "Invalid input"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    inputID=int(input("Enter the value "))
    print(monthname(inputID))