import customtkinter
from typing import List
from util import text_index_advance

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("800x400")
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        # self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        # self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        # self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

        self.font = customtkinter.CTkFont(family="Cascadia Code", size=16)
        self.textbox = customtkinter.CTkTextbox(self, width=400, font=self.font, wrap="word")
        self.textbox.tag_config("red_color", foreground="red")
        self.textbox.tag_config("kw_color", foreground="#74ade9")
        self.textbox.insert(index="1.0", text="\n"*5, tags="red_color")
        self.textbox.insert(index="1.0", text="red color", tags="red_color")
        self.textbox.insert(index="2.0", text="test", tags="red_color")
        self.textbox.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")

        self.textbox.bind("<KeyRelease>", self.update)

    def text_search(self, keyword: str) -> List[str]:
        keyword_index = []
        res = self.textbox.search(keyword, "0.0", "end")
        while(len(res) != 0):
            keyword_index.append(res)
            res = self.textbox.search(keyword, text_index_advance(res, f"0.{len(keyword)}"), "end")
        return keyword_index

    def update(self, event):
        kw_index = self.text_search("int")
        for index in kw_index:
            self.textbox.tag_add("kw_color", index, text_index_advance(index, "0.3"))

    def button_callback(self):
        self.textbox.insert(index="2.0", text="int", tags="2")
        # self.textbox.event_add()
        print("button pressed")

def main() -> None:
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()