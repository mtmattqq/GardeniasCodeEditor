import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x200")
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

        self.font = customtkinter.CTkFont(family="Cascadia Code", size=16)
        self.textbox = customtkinter.CTkTextbox(self, width=200, font=self.font, wrap="word")
        self.textbox.tag_config("1", foreground="red")
        self.textbox.insert(index=0.0, text="red color", tags="1")        
        self.textbox.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")
        
    def button_callback(self):
        print("button pressed")

def main() -> None:
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()