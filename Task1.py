def matchcase(inputId):
    try : 
        result = None
        match inputId:
            case 1|2|3:
                # To Find the Positive or Negative
                try:
                    num=int(input("Enter the number "))
                    if num>=0 :
                        result="Positive number"
                    else:
                        result="Negative number"
                except Exception as e:
                    result=str(e)
                return result
            case 4|6:
                # To Find the Odd or even 
                try:
                    num=int(input("Enter the number "))
                    if num%2==0 :
                        result="even number"
                    else:
                        result="odd number"
                except Exception as e:
                    result=str(e)
                return result
            case 5:
                # To find the Greater number 
                try:
                    num1=int(input("Enter the number1 "))
                    num2=int(input("Enter the number2 "))
                    if num1!=num2:
                        if num1>num2:
                            result=f"{num1} is a greatest number"
                        else:
                            result=f"{num2} is a greatest number"
                    else:
                        result="Number is same"
                except Exception as e:
                        result=str(e)
                return result
            case _:
                return "Logic is not implemented for this inputId"
    except Exception as e:
        return result

if __name__ == "__main__":
    inputId = int(input("Enter the inputId "))
    print(matchcase(inputId))