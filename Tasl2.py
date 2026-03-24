

def matchcase(inputId):
    try : 
        result = None
        match inputId:
            case "a"|"o":
                print("Vowels")
            case _:
                return "Logic is not implemented for this inputId"
    except Exception as e:
        return result 

if __name__ == "__main__":
    inputId = int(input("Enter the inputId "))
    print(matchcase(inputId))