import tkinter as tk
from tkinter import messagebox
import keyring


def CreateUser(user, password, password_again):
    if password != password_again:
        # checks the passwords against each other
        return False
        # asks to enter again if passwords do not match
    keyring.set_password("system", user, password)
    # stores password securely in windows itself
    return True


def checkDetails(username, password):
    if username and password:
        if keyring.get_password("system", username) == password:
            # checks if stored password matches the username and password provided
            print("Successfully Logged in!")
            return True
        else:
            print("Something went wrong!")


def logout():
    logoutWindow = tk.Tk()
    # creates a new window
    logoutWindow.geometry("300x200")
    # sets size of window
    logoutWindow.title("Logout")
    # sets title of window

    tk.Label(logoutWindow, text="Press Logout to logout and quit", bg="grey", font=("helvetica", 13), height=2,
             width=300).pack(side="top")
    # creates label saying press logout to logout

    tk.Button(logoutWindow, text="Logout", bg="light slate grey", height=2, width=30,
              command=logoutWindow.quit).pack(padx=10, pady=10)
    # creates a logout button which destroys window but will not exit main game loop

    logoutWindow.mainloop()
    # runs window loop


class Start:

    def __init__(self):
        # creates master window object
        self.window = tk.Tk()
        # sets all of these as strings for register method
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password_again = tk.StringVar()
        # sets all these strings for login method
        self.user = tk.StringVar()
        self.passw = tk.StringVar()
        # usernames
        self.users = []
        # to see if people are logged in
        self.loggedIn = False

    def Login(self):
        # for login verification
        user = self.user.get()
        pas = self.passw.get()
        # gets username and password from the input fields
        if user and pas:
            # if they have truthy values i.e not empty strings
            if checkDetails(user, pas):
                # if successfully logged in
                tk.messagebox.showinfo(title="Successfully Logged In",
                                       message="Successfully Logged in, game will play in console")
                # creates a popup saying successfully logged in
                self.loggedIn = True
                # to show that logged is true
                self.users.append(user)
                # adds usernames to a list
                self.loginScreen.destroy()
                # destroys login screen
                self.window.destroy()
                # destroys main screen

    def Register(self):

        u = self.username.get()
        p = self.password.get()
        pa = self.password_again.get()
        # gets input from textvariable and stores it in these new variables to be used

        if u or p or pa:
            # if they aren't empty strings
            if CreateUser(u, p, pa):
                # if account created
                tk.messagebox.showinfo(title="Successfully Registered", message="Successfully Registered")
                # creates a popup saying successfully registered
                self.registerScreen.destroy()
                # destroys register screen
                return

    def startWindow(self):
        self.window.geometry("300x200")
        # sets size
        self.window.title("Start")
        # sets title
        self.window.configure(bg="white")

        tk.Label(text="Choose Login Or Register", bg="light grey", width="300", height="2",
                 font=("Helvetica", 13)).pack()
        # sets label which has text at top

        tk.Button(text="Register", height=2, width=30, bg="light slate grey", command=self.registerWindow).pack(pady=10,
                                                                                                                padx=10)
        # creates register button
        tk.Button(text="Login", height=2, width=30, bg="light slate grey", command=self.loginWindow).pack(pady=10,
                                                                                                          padx=10)
        # creates login button

        self.window.tk.mainloop()
        # starts window loop

    def registerWindow(self):
        self.registerScreen = tk.Toplevel(self.window)
        # creates window
        self.registerScreen.geometry("335x275")
        # sets dimensions
        self.registerScreen.title("Register")
        # sets title

        tk.Label(self.registerScreen, text="Register With your Username and password", bg="light grey",
                 height=2, width=300, font=("Helvetica", 13)).pack(side="top")
        # sets label to say register with username and password

        tk.Label(self.registerScreen, text="Username").pack()
        # creates label for the entry widget

        tk.Entry(self.registerScreen, textvariable=self.username).pack(padx=10, pady=10)
        # creates input field for username

        tk.Label(self.registerScreen, text="password").pack()
        # creates label saying password

        tk.Entry(self.registerScreen, show="*", textvariable=self.password).pack(padx=10, pady=10)
        # creates input field for password which only shows *

        tk.Label(self.registerScreen, text="re-enter password").pack()
        # creates label saying to re-enter password

        tk.Entry(self.registerScreen, show="*", textvariable=self.password_again).pack(padx=10, pady=10)
        # creates entry input field

        registerButton = tk.Button(self.registerScreen, height=2, width=30, text="Register", bg="light slate grey",
                                   command=lambda: self.Register())
        registerButton.pack(padx=10, pady=10)
        # creates a register button

        self.registerScreen.mainloop()
        # starts window loop

    def loginWindow(self):
        self.loginScreen = tk.Toplevel(self.window)
        # creates window
        self.loginScreen.geometry("335x225")
        # sets size
        self.loginScreen.title("Login")
        # sets title

        tk.Label(self.loginScreen, text="Login With your Username and password", bg="light grey",
                 height=2, width=300, font=("Helvetica", 13)).pack(side="top")

        tk.Label(self.loginScreen, text="Username", ).pack()
        # creates label saying username

        tk.Entry(self.loginScreen, textvariable=self.user).pack(padx=10, pady=10)
        # gets user input for username

        tk.Label(self.loginScreen, text="password").pack()
        # creates new label

        tk.Entry(self.loginScreen, textvariable=self.passw, show="*").pack(padx=10, pady=10)
        # gets input for password

        loginButton = tk.Button(self.loginScreen, height=2, width=30, bg="light slate grey", text="Login",
                                command=lambda: self.Login())
        loginButton.pack(padx=10, pady=10)
        # creates a login button

        self.loginScreen.mainloop()
        # starts window loop
