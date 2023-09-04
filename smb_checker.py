import subprocess
import tkinter as tk
import socket
import threading

# Function to check if SMB port is open on a given IP address
def check_smb(ip):
    try:
        with socket.create_connection((ip, 445), timeout=2) as sock:
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

# Function to change the color and text of a label based on SMB availability
def change_color(item, ip, available):
    if available:
        item.config(bg="green")
        item["text"] = f"{ip} - On"
    else:
        item.config(bg="red")
        item["text"] = f"{ip} - Off"

# Function to open a network share link in Windows Explorer
def open_link(ip):
    link = fr"\{ip}\c$"
    print(link)
    subprocess.Popen(f'explorer "{link}"')

# Function to check the SMB availability of all IP addresses in a loop
def check_ips():
    global count
    global items
    count = 0
    for ip in ips:
        if count < len(items):
            item = items[count]
            thread = threading.Thread(target=check_ip_thread, args=(item, ip))
            thread.start()
            count += 1
    window.after(5000, check_ips)

# Function to check SMB availability in a separate thread
def check_ip_thread(item, ip):
    available = check_smb(ip)
    window.after(0, change_color, item, ip, available)

# Create the main window
window = tk.Tk()
window.title("Checking SMB")

# Load IP addresses from a file
ips = set()
with open("pclist.txt") as f:
    ips.update(line.strip() for line in f)

items = []
# Create labels for each IP address
for i, ip in enumerate(ips):
    item = tk.Label(window, text=f"IP {i+1}")
    item.grid(row=i // 5, column=i % 5, padx=10, pady=10)
    item.bind("<Button-1>", lambda event, ip=ip: open_link(ip))
    items.append(item)

# Start checking SMB availability
check_ips()

# Start the main event loop
window.mainloop()
