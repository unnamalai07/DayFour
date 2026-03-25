#Print the country related to the currency
def country(currency):
    try:
        match currency:
            case "USD":
                return "United States"
            case "INR":
                return "India"
            case "EUR":
                return "Germany, France, Italy, Spain"
            case _:
                return "Invalid currency"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    currency=input("Enter the country ")
    print(country(currency))
