#Print the star pattern for the number
def starcount(number):
    try:
        match number:
            case 1:
                return "*"
            case 2:
                return "**"
            case 3:
                return "***"
            case 4:
                return "****"
            case 5:
                return "*****"
            case _:
                return "Invalid number"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    number=input("enter the number ")
    try:
        number=int(number)
    except Exception as e:
        print(str(e))
    print(starcount(number))
    
        