import customtkinter as ctk
import logging


class Gui:
    font_ote = ('helvetica', 16, 'bold')
    font_capital = ('helvetica', 20, 'bold')
    font_setup = ('helvetica', 18, 'bold')

    ote_label1 = 'Optimal Entry %1'
    ote_label2 = 'Optimal Entry %2'
    ote_label5 = 'Optimal Entry %5'
    stop_distance_text = 'Stop Distance: '
    r_ratio_text = 'R/R Ratio: '

    possible_loss_text = 'Possible loss'
    possible_profit_text = 'Possible profit'

    def __init__(self, root):
        self.root = root
        self.root.title('Margin Calculator')
        self.labels = []
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        logging.basicConfig(level=logging.INFO)

    def setup(self):
        # Frame
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        # Capital Label
        self.label = ctk.CTkLabel(master=self.frame, text='Enter Capital', font=Gui.font_setup)
        self.label.pack(pady=12, padx=10)

        self.entry = ctk.CTkEntry(master=self.frame, placeholder_text='$')
        self.entry.pack(pady=12, padx=10)

        # Capital button
        self.submit = ctk.CTkButton(master=self.frame, text='Go next', command=lambda: self.validate(self.entry.get()))
        self.submit.pack(pady=12, padx=10)

    def validate(self, capital):
        if capital.isdigit() and int(capital) >= 0:
            self.capital = int(capital)
            self.capital_int = int(capital)
            self.capital = self.format_capital()
            self.second_page()
        else:
            logging.info("Invalid input. Please enter a valid positive integer.")

    def validate_2(self):
        try:
            stop_distance = float(self.stop_distance.get())
            r_ratio = float(self.r_ratio.get())
            margin = int(100 / stop_distance)
            return stop_distance, r_ratio, margin
        except ValueError:
            logging.info("Invalid input. Please enter a valid float.")
            print("Invalid input. Enter float and use point for both")

    def ote_values(self):
        self.ote1_value = self.capital_int / 100
        self.ote2_value = (self.capital_int / 100) * 2
        self.ote5_value = (self.capital_int / 100) * 5
        return

    def format_capital(self):
        return '{:,}'.format(self.capital)

    def calculate_profits(self, r_ratio):
        ote1_profit = self.ote1_value * r_ratio
        ote2_profit = self.ote2_value * r_ratio
        ote5_profit = self.ote5_value * r_ratio
        return int(ote1_profit), int(ote2_profit), int(ote5_profit)

    def clear_labels(self):
        for label in self.labels:
            label.destroy()

        self.labels = []

    def create_label(self, row, profit, loss, margin):
        profit_text = f'{profit} $'
        loss_text = f'{int(loss)} $'
        margin_text = str(margin)

        label_profit = ctk.CTkLabel(master=self.frame, text=profit_text, font=Gui.font_capital, text_color='Green')
        label_profit.grid(sticky='W', column=1, row=row, padx=(30, 0), pady=(30, 0))
        self.labels.append(label_profit)

        label_loss = ctk.CTkLabel(master=self.frame, text=loss_text, font=Gui.font_capital, text_color='Red')
        label_loss.grid(sticky='W', column=2, row=row, padx=(30, 0), pady=(30, 0))
        self.labels.append(label_loss)
        label_margin = ctk.CTkLabel(master=self.frame, text=margin_text, font=Gui.font_capital, text_color='White')
        label_margin.grid(sticky='W', column=3, row=row, padx=(60, 0), pady=(30, 0))
        self.labels.append(label_margin)



    def calculate(self):
        stop_distance, r_ratio, margin = self.validate_2()
        profit1, profit2, profit5 = self.calculate_profits(r_ratio)


        self.clear_labels()
        self.create_label(6, profit1, self.ote1_value, margin)
        self.create_label(7, profit2, self.ote2_value, margin)
        self.create_label(8, profit5, self.ote5_value, margin)



    def second_page(self):
        self.clear_frame()
        text = f'Total Capital:   {self.capital}$'
        self.ote_values()

        # Frame
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(fill='both', expand=True)

        # Label for Total Capital
        self.label = ctk.CTkLabel(master=self.frame, text=text, font=Gui.font_capital)
        self.label.grid(sticky='W', column=0, row=0, padx=(10, 20))

        # Label and Entry for Stop Distance and R
        self.label1 = ctk.CTkLabel(master=self.frame, text=Gui.stop_distance_text, font=Gui.font_setup)
        self.label1.grid(sticky='W', column=0, row=1, padx=(10, 0), pady=(30, 0))

        self.stop_distance = ctk.CTkEntry(master=self.frame, placeholder_text='5.72')
        self.stop_distance.grid(sticky='W', column=1, row=1, padx=(0, 0), pady=(30, 0))

        self.label5 = ctk.CTkLabel(master=self.frame, font=Gui.font_setup, text=Gui.r_ratio_text)
        self.label5.grid(sticky='W', column=0, row=2, padx=(10, 0), pady=(30, 0))

        self.r_ratio = ctk.CTkEntry(master=self.frame, placeholder_text='3.23')
        self.r_ratio.grid(sticky='W', column=1, row=2, padx=(0, 0), pady=(30, 0))

        self.submit = ctk.CTkButton(master=self.frame, text='Calculate', command=lambda: self.calculate())
        self.submit.grid(sticky='W', column=1, row=3, padx=(0, 0), pady=(30, 0))

        # PROFIT
        self.label5 = ctk.CTkLabel(master=self.frame, text=Gui.possible_profit_text, font=Gui.font_ote)
        self.label5.grid(sticky='W', column=1, row=4, padx=(10, 30), pady=(30, 0))

        # Loss
        self.label6 = ctk.CTkLabel(master=self.frame, text=Gui.possible_loss_text, font=Gui.font_ote)
        self.label6.grid(sticky='W', column=2, row=4, padx=(10, 0), pady=(30, 0))

        # Calculate Button
        self.label7 = ctk.CTkLabel(master=self.frame, text='Margin', font=Gui.font_ote)
        self.label7.grid(sticky='W', column=3, row=4, padx=(50, 30), pady=(30, 0))

        self.label2 = ctk.CTkLabel(master=self.frame, text=Gui.ote_label1, font=Gui.font_ote)
        self.label2.grid(sticky='W', column=0, row=6, padx=(10, 0), pady=(30, 0))

        # Ote 2
        self.label3 = ctk.CTkLabel(master=self.frame, text=Gui.ote_label2, font=Gui.font_ote)
        self.label3.grid(sticky='W', column=0, row=7, padx=(10, 0), pady=(30, 0))

        # Ote 5
        self.label4 = ctk.CTkLabel(master=self.frame, text=Gui.ote_label5, font=Gui.font_ote)
        self.label4.grid(sticky='W', column=0, row=8, padx=(10, 0), pady=(30, 0))

        # Go back Button
        self.go_back = ctk.CTkButton(master=self.frame, text='Go back', command=lambda: self.first_page())
        self.go_back.grid(sticky='W', column=1, row=9, padx=(40, 0), pady=(30, 10))

    def first_page(self):
        self.clear_frame()
        self.setup()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.frame.pack_forget()

    def run(self):
        self.root.geometry('700x550')
        self.setup()
        self.root.mainloop()
