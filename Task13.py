# Print the company name for a browser
def companyname(browser):
    try:
        match browser:
            case "chrome":
                return "Google"
            case "firefox":
                return "Firefox"
            case "edge":
                return "Microsoft"
            case _:
                return "Invalid  browser name "
    except Exception as e:
        return str(e)
if __name__=="__main__":
    browser=input("Enter the company name ")
    print(companyname(browser))