# perform arithemtic opertaion
def performopertaion(operation):
    try:
        match operation:
            case "+":
                try:
                    num1=int(input("Enter the number1 "))
                    num2=int(input("Enter the number2 "))
                    result=num1+num2
                except Exception as e:
                    result=str(e)
            case "-":
                try:
                    num1=int(input("Enter the number1 "))
                    num2=int(input("Enter the number2 "))
                    result=num1-num2
                except Exception as e:
                    result=str(e)
            case "*":
                try:
                    num1=int(input("Enter the number1 "))
                    num2=int(input("Enter the number2 "))
                    result=num1*num2
                except Exception as e:
                    result=str(e)
            case "/":
                try:
                    num1=int(input("Enter the number1 "))
                    num2=int(input("Enter the number2 "))
                    result=num1/num2
                except Exception as e:
                    result=str(e)
            case _:
                result=str(e)
    except Exception as e:
        return result
    finally:
        return result
if __name__=="__main__":
   operation=input("Enter the opertaion ")
   print(performopertaion(operation))




            

                