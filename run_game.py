import sys
import tkinter

#local imports
from src import game_main as game



# required python version for this project
MIN_VER = (3, 8)


class Launcher():
    def __init__(self):
        root.geometry("400x200")
        root.title("pyweek31 - placeholder")
        self.banner = tkinter.Label(root, text = "pygame 31!").pack()
        self.start_game_button = tkinter.Button(root,text="Start game",command=self.launch_game).pack()
        self.exit_game_button = tkinter.Button(root,text="Exit game",command=root.destroy).pack()
        root.mainloop()

    def launch_game(self):
        if sys.version_info[:2] < MIN_VER:
            #raise insufficient python version error
            self.raise_error_to_user("To run this game you need Python {}.{} installed. Please upgrade to that version to play.".format(*MIN_VER))
            return
        root.destroy()
        game.launch_game()

    def raise_error_to_user(self,error):
        error_win = tkinter.Toplevel()
        error_win.title("Error!")
        error_message_label = tkinter.Label(error_win,text=error).pack()
        close_button = tkinter.Button(error_win,text="Close",command=error_win.destroy).pack()


if __name__=="__main__":
    root = tkinter.Tk()
    Launcher()
