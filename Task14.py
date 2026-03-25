#Print major 3 country name for each continent
def country(continent):
    try:
        match continent:
            case "Asia":
                return "India, China, Japan"
            case "Europe":
                return "Germany, France, United Kingdom"
            case "Africa":
                return "Nigeria, South Africa, Egypt"
            case _:
                return "Invalid continent"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    continent=input("Enter the continent name ")
    print(country(continent))
    
        
            