#Print the sound of the pet
def sound(pet):
    try:
        match pet:
            case "dog":
                return "woof woof"
            case "cat":
                return "meow"
            case "fish":
                return "Doesn’t make audible sounds (generally silent to humans)"
            case _:
                return "Invalid pet animal"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    pet=input("Enter the pet animal ")
    print(sound(pet))