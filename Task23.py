#Print temperature related to the climate
def temperature(climate):
    try:
        match climate:
            case "Summer":
                return "Hot — around 30°C to 45°C"
            case "Winter":
                return "Cool to cold — around 10°C to 25°C"
            case "Rainy":
                return "Moderate — around 20°C to 30°C"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    climate=input("Enter the climate ")
    print(temperature(climate))

        
            