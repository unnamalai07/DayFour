# Print the colour of the fruit
def colour(fruit):
    try:
        match fruit:
            case "Apple":
                return "Red"
            case "Orange":
                return "Orange"
            case "Banana":
                return "yellow"
            case _:
                return "Invalid fruit"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    fruit=input("Enter the fruit name ")
    print(colour(fruit))