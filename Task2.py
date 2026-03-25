# find vowels or consonant
def vowels(inputId):
    try :
        match inputId:
            case "a"|"o"|"e"|"i"|"u":
                return "Vowels"
            case _:
                return "Consonant"
    except Exception as e:
        return str(e) 

if __name__ == "__main__":
    inputId =input("Enter the inputId ")
    print(vowels(inputId))