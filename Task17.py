#print the language is compiled or interpreted language
def compiledinterpreted(language):
    try:
        match language:
            case "C"|"C++"|"Go":
                return "Compiled language"
            case "Python"|"JavaScript"|"Ruby":
                return "Interpreted lanuage"
            case _:
                return "Invalid language"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    language=input("Enter the language ")
    print(compiledinterpreted(language))


        