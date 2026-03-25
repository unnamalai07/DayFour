# Print the oppsoite direction related to the direction
def oppsoitedirection(direction):
    try:
        match direction:
            case "North":
                return "South"
            case "South":
                return "North"
            case "East":
                return "West"
            case "West":
                return "East"
            case _:
                return "Invalid direction"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    direction=input("Enter the direction ")
    print(oppsoitedirection(direction))