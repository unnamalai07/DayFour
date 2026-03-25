#print its multiplication table result for related to the number
def multiplication(number):
    try:
        match number:
            case 1:
                return 1*5
            case 2:
                return 10/2
            case 3:
                return 15/3
            case _:
                return "Invalid number"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    number=int(input("Enter the number "))
    print(int(multiplication(number)))
                
               
                 
                
                   