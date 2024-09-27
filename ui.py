from tkinter import *
from tkinter.ttk import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_m1km5b62 = self.__tk_button_m1km5b62(self)
        self.tk_frame_m1km6rqb = self.__tk_frame_m1km6rqb(self)
        self.tk_list_box_m1kmajms = self.__tk_list_box_m1kmajms(self.tk_frame_m1km6rqb) 

    def __win(self):
        self.title("抖音热搜助手")
        # 设置窗口大小、居中
        width = 480
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.minsize(width=width, height=height)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_button_m1km5b62(self,parent):
        btn = Button(parent, text="刷新", takefocus=False,)
        btn.place(relx=0.7500, rely=0.0000, relwidth=0.2500, relheight=0.1167)
        return btn

    def __tk_frame_m1km6rqb(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.1167, relwidth=1.0000, relheight=0.8833)
        return frame

    def __tk_list_box_m1kmajms(self, parent):
        lb = Listbox(parent)
        
        lb.insert(END, "抖音热搜：")        
        
        lb.place(relx=0.0000, rely=0.0000, relwidth=1.0000, relheight=1.0000)
        return lb
    
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    
    def __event_bind(self):
        self.tk_button_m1km5b62.bind('<Button>',self.ctl.on_button_click)
        self.tk_list_box_m1kmajms.bind('<Double-Button-1>',self.ctl.on_double_button_1)
        pass
    
    def __style_config(self):
        pass
