import socket
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.username = self.get_username()

        self.root = tk.Tk()
        self.create_gui()

        self.connect_to_server()

    def get_username(self):
        return simpledialog.askstring("Username", "Enter your name:")

    def create_gui(self):
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.chat_area.pack(expand=True, fill=tk.BOTH)

        self.message_entry = tk.Entry(self.root)
        self.message_entry.pack(expand=True, fill=tk.BOTH)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        self.client_socket.send(self.username.encode())

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        self.root.mainloop()

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode())
            self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                self.chat_area.insert(tk.END, message + "\n")
                self.chat_area.yview(tk.END)
            except OSError:
                break

if __name__ == "__main__":
    client = ChatClient("localhost", 12345)
