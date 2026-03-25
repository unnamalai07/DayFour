# Print advice related to the tempertaure
def advice(temperature):
    try:
        match temperature:
            case "cold":
                return "It’s quite chilly—wear warm clothes, stay covered, and avoid prolonged exposure."
            case "warm":
                return "The temperature is comfortable—dress lightly and stay hydrated."
            case "hot":
                return "It’s very hot—drink plenty of water, avoid direct sun, and wear light, breathable clothing."
            case _:
                return "Invalid Temperature"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    tempertaure=input("Enter the termperature ")
    print(advice(tempertaure))