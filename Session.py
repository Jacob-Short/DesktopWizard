import tkinter as tk


class StartSession:
    window = tk.Tk()
    frame_a = tk.Frame(master=window)
    frame_b = tk.Frame(master=window)
    frame_c = tk.Frame(master=window)
    next_button_1 = tk.Button(text='NEXT')
    next_button_2 = tk.Button(text='NEXT')
    next_button_3 = tk.Button(text='NEXT')
    entry_user_name = tk.Entry()
    label_1 = None
    label_2 = None
    label_3 = None

    def __init__(self):
        self.window.rowconfigure([0, 1, 2], weight=1, minsize=50)
        self.window.columnconfigure(1, weight=1, minsize=75)
        self.frame_a.grid(row=0, column=1, sticky="n")
        self.frame_b.grid(row=1, column=1, sticky="n")
        self.frame_c.grid(row=2, column=1, sticky="n")
        self.labels(
            lgs_text='Lets Get Started',
            stage_label_text='1/3',
            name_label_text='Enter your name below'
        )
        self.next_button_1.bind("<ButtonRelease>",
                                self.handle_next_button_1_release)
        self.entry_user_name.grid(row=3, column=1)
        self.entry_user_name.insert(0, 'Name')
        # entry_user_name.pack(row=3, column=1)
        self.next_button_1.grid(row=4, column=1)

    def handle_next_button_1_release(self, event):
        print(self.entry_user_name.get())
        self.entry_user_name.destroy()
        self.next_button_1.destroy()
        self.next_button_2.bind("<ButtonRelease>",
                                self.handle_next_button_2_release)
        self.next_button_2.grid(row=4, column=1)
        self.labels(
            lgs_text='Profiles',
            stage_label_text='2/3',
            name_label_text='What will you be doing?'
        )

    def handle_next_button_2_release(self, event):
        self.next_button_2.destroy()
        self.next_button_3.bind("<ButtonRelease>",
                                self.handle_next_button_3_release)
        self.next_button_3.grid(row=4, column=1)
        self.labels(
            lgs_text='Monitors',
            stage_label_text='3/3',
            name_label_text='Confirm your monitor layout below'
        )

    def handle_next_button_3_release(self, event):
        self.next_button_3.destroy()
        self.labels(
            lgs_text='Dashboard',
            stage_label_text='- Dashboard Layout Below -',
            name_label_text='...'
        )

    def labels(self, lgs_text, stage_label_text, name_label_text):
        if self.label_1 is not None:
            self.label_1.destroy()
            self.label_2.destroy()
            self.label_3.destroy()

        self.label_1 = tk.Label(
            master=self.frame_a,
            text=lgs_text
            # relief=tk.RAISED
        )
        self.label_1.pack(padx=100, pady=50)

        self.label_2 = tk.Label(
            master=self.frame_b,
            text=stage_label_text
        )
        self.label_2.pack(padx=100, pady=50)

        self.label_3 = tk.Label(
            master=self.frame_c,
            text=name_label_text
        )
        self.label_3.pack(padx=100, pady=100)

    def page_two(self):
        ...
