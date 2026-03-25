#Print the number of players
def players(game):
    try:
        match game:
            case "tennis":
                return "2 players"
            case "cricket":
                return "11 players"
            case "football":
                return "11 players"
            case _:
                return "Invalid game"
    except Exception as e:
        return str(e)
if __name__=="__main__":
    game=input("Enter the game ")
    print(players(game))