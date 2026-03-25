#print its opposite value related to the boolean value
def oppositevalue(booleanvalue):
    try:
        match booleanvalue:
            case "True":
                return "False"
            case "False":
                return "True"
            case _:
                return "Invalid boolean value"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    booleanvalue=input("Enter the boolean value ")
    print(oppositevalue(booleanvalue))