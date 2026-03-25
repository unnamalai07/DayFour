# prints the corresponding day related to the input
def days(inputId):
    try : 
        match inputId:
            case 1:
                #Monday
                return "Monday"
            case 2:
                #Tuesday
                return "Tuesday"
            case 3:
                #Wednesday
                return "Wednesday"
            case _:
                return "Logic is not implemented for this inputId"
    except Exception as e:
            return str(e)
if __name__ == "__main__":
    inputId = int(input("Enter the inputId "))   
    print(days(inputId))

        
        
