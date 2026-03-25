#Print age group related to the school level
def agegroup(schoollevel):
    try:
        match schoollevel:
            case "primary":
                return "6–10 years"
            case "secondary":
                return "11–17 years"
            case "college":
                return "18–22+ years"
            case _:
                return "Invalid school level"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    schoollevel=input("Enter the school level ")
    print(agegroup(schoollevel))
    


