#Print wheels count related to vechile type
def wheelcount(vehicle):
    try:
        match vehicle:
            case "car":
                return "4 wheels"
            case "bike":
                return "2 wheels"
            case "bus":
                return "8 wheels"
            case _:
                return "Invalid vechile"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    vehicle=input("Enter the vehicle name ")
    print(wheelcount(vehicle))
    