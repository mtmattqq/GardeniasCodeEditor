import customtkinter
from typing import List
from util.position import Position

class EditorFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, width, height):
        super().__init__(master, width, height)
        self.width = width
        self.height = height
        self.grid_columnconfigure((10, 2), weight=0, pad=0)

        self.font = customtkinter.CTkFont(family='Cascadia Code', size=16)
        self.textbox = customtkinter.CTkTextbox(
            self, width=self.width-50, height=self.height, font=self.font, wrap='word', spacing1=0, spacing2=0, spacing3=10,
            activate_scrollbars=False)
        self.textbox.tag_config('white_color', foreground='#ffffff')
        self.textbox.tag_config('red_color', foreground='red')
        self.textbox.tag_config('kw_color', foreground='#74ade9')
        self.textbox.grid(row=0, column=1, padx=20, pady=0, sticky='w', rowspan=10)
        self.textbox.bind('<KeyRelease>', self.update)
        self.line_numbers = [
            customtkinter.CTkLabel(
                self, width=50, height=15, font=self.font, text=str(i), anchor='ne') 
                for i in range(1, 10 + 1)]
        for index, line_number in enumerate(self.line_numbers):
            line_number.grid(row=index, column=0, padx=10, pady=0, sticky='w')

    def text_search(self, keyword: str) -> List[str]:
        keyword_index = []
        res = self.textbox.search(keyword, '0.0', 'end')
        while(len(res) != 0):
            keyword_index.append(res)
            res = self.textbox.search(keyword, str(Position(res) + Position((0, len(keyword)))), 'end')
        return keyword_index

    def update(self, event):
        self.textbox.tag_remove(tagName='red_color', index1='0.0', index2='end')
        self.textbox.tag_remove(tagName='kw_color', index1='0.0', index2='end')

        kw_index = self.text_search('int')
        for index in kw_index:
            self.textbox.tag_add('kw_color', index, Position(index) + Position((0, 3)))