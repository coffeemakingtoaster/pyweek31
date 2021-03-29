from src import game_main as game
import sys



# required python version for this project
MIN_VER = (3, 9)


def main():
    #exit program if wrong version of python is used
    if sys.version_info[:2] < MIN_VER:
        sys.exit(
            "This game requires Python {}.{}.".format(*MIN_VER)
        )
    game.launch_game()
    
    
    
if __name__=="__main__":
    main()
