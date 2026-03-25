#Print file type related to the extension
def filtype(extension):
    try:
        match extension:
            case ".txt":
                return "Notepad"
            case ".jpg":
                return "Image"
            case ".py":
                return "Python"
            case _:
                return "Invalid extension"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    extension=input("enter the extension ")
    print(filtype(extension))
