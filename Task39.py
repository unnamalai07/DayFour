# print its category related to the social media app name
def category(socialmediaapp):
    try:
        match socialmediaapp:
            case "messaging":
                return "Whatspp","Message"
            case "Photo"|"Video":
                return "Instagram","TikTok"
            case _:
                return "Invalid social media app"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    socialmediaapp=input("Enter the social media app ")
    print(category(socialmediaapp))
    