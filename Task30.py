# Print system response related to the command
def systemresponse(command):
    try:
        match command:
            case "start":
                return "System is starting… initializing processes."
            case "stop":
                return "System is stopping… shutting down processes."
            case "pause":
                return "System is paused… temporarily halting operations."
            case _:
                return "Inavlid commad"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    command=input("Enter the command ")
    print(systemresponse(command))
