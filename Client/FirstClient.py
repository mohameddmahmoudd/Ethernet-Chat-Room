import socket
import threading
import tkinter as tk

# Choose Nickname
username = input("Enter username: ")
password = input("Enter password: ")

while (username != "Masoud" or password != "12345678") and (username != "Helmy" or password != "87654321") and (username != "Hazem" or password != "1234567890"):
    print("Incorrect credentials, please try again")
    username = input("Enter username: ")
    password = input("Enter password: ")

#ip = '169.254.61.182'
ip = socket.gethostname()
port = 1234

# Connecting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

# Create a Tkinter window
window = tk.Tk()
window.title("Chat Client")

# Create a Text widget for displaying messages
chat_display = tk.Text(window, height=10, width=40)
chat_display.pack()

# Create an Entry widget for typing messages
message_entry = tk.Entry(window, width=40)
message_entry.pack()

# Function to send a message to the server
def send_message(event=None):
    message = message_entry.get()
    if message:
        message = '{}: {}'.format(username, message)
        client.send(message.encode('ascii'))
        message_entry.delete(0, tk.END)

# Function to handle received messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'HELMY':
                client.send(username.encode('ascii'))
            else:
                chat_display.insert(tk.END, message + '\n')
        except:
            print("An error occurred!")
            client.close()
            break

# Create a Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Bind the Enter key to send a message
window.bind('<Return>', send_message)

# Start the receive thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start the Tkinter main loop
window.mainloop()
