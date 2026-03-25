#print travel type related to the transport mode
def traveltype(transportmode):
    try:
        match transportmode:
            case "Train":
                return "Land"
            case "Flight":
                return "Air"
            case "Ship":
                return "Water"
            case _:
                return "Invalid Travel type"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    transportmode=input("Enter travel type ")
    print(traveltype(transportmode))
