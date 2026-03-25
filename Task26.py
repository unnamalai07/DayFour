# Print even or odd related to the number
def findevenodd(number):
    try:
        match number:
            case 2|4|6|8|0:
                return "even number"
            case _:
                return "odd number"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    number=int(input("Enter the number "))
    print(findevenodd(number))

