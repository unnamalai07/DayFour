#Print the roman numeral equivalent
def roman(number):
    try:
        match number:
            case 1:
                return "I"
            case 2:
                return "II"
            case 3:
                return "III"
            case 4 :
                return "IV"
            case _:
                return "Invalid number"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    number=input("Enter the number ")
    try:
        number=int(number)
    except Exception as e:
        print(str(e))
    print(roman(number))

            
