#print actvitity suggestion for weekend and weekday
def suggestion(days):
    try:
        match days:
            case "weekday":
                return "Focus on work or studies, exercise briefly, and keep a routine"
            case "weekend":
                return "Relax, spend time with family or friends, go out, pursue hobbies, or take short trips."
            case _:
                return "Invalid days"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    days=input("Enter the days ")
    print(suggestion(days))
    
