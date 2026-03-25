# Print advice related to the password strength keyword
def advice(passwordstrength):
    try:
        match passwordstrength:
            case "weak":
                return "Your password is not secure — use a longer password with a mix of letters, numbers, and symbols."
            case "medium":
                return "Your password is okay but can be improved — add special characters and increase length for better security."
            case "strong":
                return "Your password is secure — keep it safe and avoid sharing it with anyone."
            case _:
                return "Invalid password strength keyword"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    passwordstrength=input("Enter the password strength keyword ")
    print(advice(passwordstrength))