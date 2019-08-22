from tkinter import Frame, Tk, Label,font
import praw

class Ticker(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self._offsetx = 0
        self._offsety = 0
        self.parent = parent 
        self.parent.title("TICKER WINDOW")
        fonts = font.Font(family="Comic Sans Sarif", size=20)
        self.label = Label(self, text="", font=fonts, fg="#8B008B", bg="#d3d3d3")
        self.label.pack()
        self.configure(background="#646464")
        self.parent.overrideredirect(True)
        self.label.bind("<Button-1>", self.on_click)
        self.parent.bind("<Button-1>", self.on_click)
        self.parent.bind("<B1-Motion>", self.on_drag)
        self.label.bind("<B1-Motion>", self.on_drag)
        self.label.bind("<Button-3>", self.on_exit)
        self.parent.wm_attributes("-transparentcolor", "#646464") 
        self.pack(expand=True) 

    def on_click(self, e):
        self._offsetx = e.x
        self._offsety = e.y

    def on_drag(self, e):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.parent.geometry('+{x}+{y}'.format(x=x, y=y))

    def update_label(self, string):
        self.label.config(text=string)
        self.label.pack()
        self.pack(expand=True)

    def on_exit(self, e):
        self.parent.quit()

class TextObject: 
    index=0
    start_index=0
    str_builder=""
    def __init__(self, string, max_letters=100):
        self.string = string
        self.max_letters = max_letters
        self.index = max_letters
        self.str_builder = self.string[0:self.max_letters]

    def get_next_fragment(self): #
        if self.index < len(self.string):
            #adds chars one at a time to the str_builder string.
            # Every time it does this it also removes one from the front of the string
            self.str_builder =  self.str_builder[1:] + self.string[self.index]
            self.index += 1 #increase the string index to grab the next char
            return self.str_builder
        else:
            self.index=0
            return self.str_builder

def connect_to_reddit():
    r = praw.Reddit(client_id='xxxxxxxxx',client_secret='xxxxxxxxx',user_agent='xxxxxx')
    posts = r.subreddit('News').hot(limit=None)
    title_string = ""
    for post in posts:
        title_string += post.title.upper() + u"\u25BA"
    return TextObject(title_string)


#called once every n milliseconds by the graphics thread, wakes this thread to start changing the text
def update_event():
    ticker_window.update_label(news_tick.get_next_fragment())
    ticker_window.after(300, update_event)

#start window
news_tick = connect_to_reddit()
root_frame = Tk()
root_frame.resizable(0,0)
ticker_window = Ticker(root_frame) #create instance of ticker frame window and pass in Tk root window
root_frame.after(300, update_event)
root_frame.mainloop()
