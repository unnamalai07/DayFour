#Print square value related to the number
def squarevalue(number):
    try:
        match number:
            case 1:
                return 1*1
            case 2:
                return 2*2
            case 3:
                return 3*3
            case 4:
                return 4*4
            case 5:
                return 5*5
            case _:
                return "Invalid number"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    number=int(input("Enter the number "))
    print(squarevalue(number))
    
               