# 
# Write a GUI application where:
# There is a button select version_input (includes v4, v3 and defaults to v4)
# There is a button select encoding_method(binary, commander, product, sequential and default is binary)
# There is a button select type_encoding (ALO, noALO and default ALO)
# There is an input type to enter the timeout (default value is 900 ms)
# Then generate the command:
# ls input_[version_input]/[encoding_method]/cnf_[type_encoding]_[version_input]/*.cnf | xargs -n 1 ./build/kissat --time=[timeout] | ./process.py > output_[version_input]/[encoding_method]/[type_encoding]_[Datetime].txt
# Then display this command in a text box 
# There is a button to execute the command on Linux
#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import subprocess
import datetime
import time
import os
import sys
import re
import random
import string

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Kissat GUI')
        self.master.geometry('900x600')
        self.master.resizable(False, False)

        self.version_input = tk.StringVar()
        self.version_input.set("v4")
        self.encoding_method = tk.StringVar()
        self.encoding_method.set("binary")
        self.type_encoding = tk.StringVar()
        self.type_encoding.set("ALO")
        self.timeout = tk.StringVar()
        self.timeout.set("900")

        self.version_input_label = ttk.Label(self.master, text="Version Input").grid(row=0, column=0)
        self.version_input_menu = ttk.OptionMenu(self.master, self.version_input, "v4", "v4", "v3", "v2")
        self.version_input_menu.grid(row=0, column=1)

        self.encoding_method_label = ttk.Label(self.master, text="Encoding Method").grid(row=1, column=0)
        self.encoding_method_menu = ttk.OptionMenu(self.master, self.encoding_method, "binary", "binary", "commander", "product", "sequential", "binomial")
        self.encoding_method_menu.grid(row=1, column=1)

        self.type_encoding_label = ttk.Label(self.master, text="Type Encoding").grid(row=2, column=0)
        self.type_encoding_menu = ttk.OptionMenu(self.master, self.type_encoding, "ALO", "ALO", "noALO")
        self.type_encoding_menu.grid(row=2, column=1)

        self.timeout_label = ttk.Label(self.master, text="Timeout (ms)").grid(row=3, column=0)
        self.timeout_entry = ttk.Entry(self.master, textvariable=self.timeout)
        self.timeout_entry.grid(row=3, column=1)

        self.generate_button = ttk.Button(self.master, text="Generate", command=self.generate)
        self.generate_button.grid(row=4, column=0)

        self.execute_button = ttk.Button(self.master, text="Execute", command=self.execute)
        self.execute_button.grid(row=4, column=1)

        # add Kill button to kill kissat process
        self.kill_button = ttk.Button(self.master, text="Kill", command=self.kill)
        self.kill_button.grid(row=4, column=2)

        self.command_text = tk.Text(self.master, height=20, width=100)
        self.command_text.grid(row=5, columnspan=2)

        self.command_text.insert(tk.END, "ls input_" + self.version_input.get() + "/" + self.encoding_method.get() + "/cnf_" + self.type_encoding.get() + "_" + self.version_input.get() + "/*.cnf | xargs -n 1 ./build/kissat --time=" + self.timeout.get() + " | ./process.py > output_" + self.version_input.get() + "/" + self.encoding_method.get() + "/" + self.type_encoding.get() + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt")

    def generate(self):
        self.command_text.delete('1.0', tk.END)
        self.command_text.insert(tk.END, "ls input_" + self.version_input.get() + "/" + self.encoding_method.get() + "/cnf_" + self.type_encoding.get() + "_" + self.version_input.get() + "/*.cnf | xargs -n 1 ./build/kissat --time=" + self.timeout.get() + " | ./process.py > output_" + self.version_input.get() + "/" + self.encoding_method.get() + "/" + self.type_encoding.get() + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt")

    def execute(self):
        self.generate()
        command = self.command_text.get("1.0", tk.END)
        print(command)
        os.system(command)

    def kill(self):
        os.system("killall kissat")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()