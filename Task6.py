# Print in letter related to the inputed number
def number(inputID):
    try:
        match inputID:
            case 1:
                return "One"
            case 2:
                return "Two"
            case 3:
                return "Three"
            case 4:
                return "Four"
            case 5:
                return "Five"
            case 6:
                return "Six"
            case 7:
                return "Seven"
            case 8:
                return "Eight"
            case 9:
                return "Nine"
            case _:
                return "Invalid number"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    input=int(input("Enter the number "))
    print(number(input))