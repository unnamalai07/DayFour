#print its primary use related to the device type
def primaryuse(devicetype):
    try:
        match devicetype:
            case "Mobile":
                return "Communication, calls, messaging, and light apps on the go."
            case "Laptop":
                return "Productivity, work, programming, and multitasking tasks."
            case "Tablet":
                return "Media consumption, reading, casual browsing, and light productivity."
            case _:
                return "Invalid device type"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    devicetype=input("Enter the device type ")
    print(primaryuse(devicetype))
    
