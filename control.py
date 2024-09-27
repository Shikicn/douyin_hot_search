import webbrowser
from tkinter import *

from search import *

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        self.hot_searches = []
    # 刷新热搜
    def on_button_click(self,evt):
        self.hot_searches = get_hot_searches()
        content = self.hot_searches
        lb = self.ui.tk_list_box_m1kmajms
        lb.delete(1, END)
        lb.insert(END, f'置顶：{content[0]["word"]}')
        
        for index in range(1, len(content)):
            if index < 10:
                lb.insert(END, f' {index}：{content[index]["word"]}')
            else:
                lb.insert(END, f'{index}：{content[index]["word"]}')
    
    def on_double_button_1(self,evt):
        lb: Listbox = self.ui.tk_list_box_m1kmajms
        
        if lb.size() <= 1:
            return
        
        index = lb.curselection()[0] - 1
        if index < 0:
            return
        
        video_url = f'https://www.douyin.com/hot/{self.hot_searches[index]["sentence_id"]}'
        webbrowser.open(video_url)