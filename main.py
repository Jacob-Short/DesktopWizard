from Session import StartSession


def main():

    session = StartSession()
    # entry_user_name = tk.Entry(fg="yellow", bg="blue", width=50)
    # Bind keypress event to handle_keypress()
    session.window.mainloop()

    # username = entry_user_name.get()


if __name__ == '__main__':
    exit(main())
