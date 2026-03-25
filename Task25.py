#print access level related to the role
def accesslevel(role):
    try:
        match role:
            case "admin":
                return "Full access — can create, read, update, delete data, and manage users/settings."
            case "guest":
                return "Minimal access — can only view basic or public information, no editing or management rights."
            case "user":
                return "Limited access — can read and modify their own data, but cannot manage system settings or other users."
            case _:
                return "Invalid role"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    role=input("Enter the role ")
    print(accesslevel(role))
    

