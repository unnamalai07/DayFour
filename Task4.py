# Print the day related to the input
def weekdays(inputID):
    try:
        match inputID:
            case 1:
                return "Sunday"
            case 2:
                return "Monday"
            case 3:
                return "Tuesday"
            case 4:
                return "wednesday"
            case 5:
                return "Thursday"
            case 6:
                return "Friday"
            case 7:
                return "Saturday"
            case _:
                return "Invalid input"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    inputID=int(input("Enter the value "))
    print(weekdays(inputID))