#Print the city name related to the country
def country(cityname):
    try:
        match cityname:
            case "Chennai":
                return "India"
            case "New York City":
                return "United States"
            case "Paris":
                return "France"
            case "Tokyo":
                return "Japan"
            case "Sydney":
                return "Australia"
            case _:
                return "Invalid country"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    ciityname=input("Enter the cityname ")
    print(country(ciityname))