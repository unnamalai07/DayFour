# Print the action related to tyhe colour
def signal(inputID):
    try:
        match inputID:
            case "red":
               return "Need to stop"
            case "yellow":
               return "Ready"
            case "green":
               return "Go"
            case _:
                return "Invalid signal"      
    except Exception as e:
        return str(e)
    
if __name__=="__main__":
   inputID= input("Enter the value ")
   print(signal(inputID))
               
              