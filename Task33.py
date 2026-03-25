#print a typical dish related to the meal time
def dish(mealtime):
    try:
        match mealtime:
            case "Breakfast"|"Dinner":
                return "Idly","Dosai","Poori","Upma"
            case "Lunch":
                return "Meal","Briyani"
            case _:
                return "Invalid meal time"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    mealtime=input("Enter the mealtime ")
    print(dish(mealtime))
