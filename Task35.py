#print advice related to the weather condition
def advice(weather):
    try:
        match weather:
            case "Sunny":
                return "Wear light clothes, use sunscreen, and stay hydrated."
            case "Cloudy":
                return "Good for outdoor activities, but carry a light jacket just in case."
            case "Rainy":
                return "Carry an umbrella or raincoat, and avoid slippery roads."
            case "Stormy":
                return "Stay indoors, avoid traveling, and secure loose objects."
            case _:
                return "Invalid weather"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    weather=input("Enter the weather ")
    print(advice(weather))
