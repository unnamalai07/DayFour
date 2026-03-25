# Print the side of the shape
def sides(shape):
    try:
        match shape:
            case "circle":
                return "No sides"
            case "square":
                return "4 sides"
            case "Traingle":
                return "3 sides"
            case _:
                return "Invalid shapes"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    shape=input("Enter the shape ")
    print(sides(shape))
