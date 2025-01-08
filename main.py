import os
import curses



class Program:
    def __init__(self):
        self.path = os.getcwd()
        self.pathlist = self.path.split("/")
        self.dirlist = os.listdir()
        self.position = 0

    def mainloop(self):
        screen.clear()
        screen.addstr(0, 0, self.path)

        for i, name in enumerate(self.dirlist):
            word = name
            if i == self.position:
                word += " *"
            screen.addstr(i + 1, 0, word)



        self.move()
        self.dirlist = os.listdir(self.path)


        screen.refresh()


    def move(self):
        key = screen.getkey()
        if key == "w":
            if self.position >= 0:
                self.position -= 1
        elif key == "s":
            if self.position <= len(self.dirlist):
                self.position += 1
        elif key == "d":
            self.further()
            self.position = 0
        elif key == "a":
            self.back()
            self.position = 0
        elif key == "e":

            os.chdir(self.path)



            screen.refresh()
            screen.clear()


            os.system("reset")
            os.system("/bin/bash")




    def back(self):
        self.pathlist.pop()
        self.path = "/".join(self.pathlist)

    def further(self):
        self.path += "/" + self.dirlist[self.position]
        self.pathlist.append(self.dirlist[self.position])




if __name__ == "__main__":

    program = Program()

    screen = curses.initscr()
    curses.noecho()

    curses.curs_set(0)

    while True:
        program.mainloop()
