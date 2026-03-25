#print a related keyword related to the subject
def keyword(subject):
    try:
        match subject:
            case "Math":
                return "Numbers"
            case "Science":
                return "Experiment"
            case "History":
                return "Timeline"
            case _:
                return "Invalid subject"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    subject=input("Enter the subject ")
    print(keyword(subject))