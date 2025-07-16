import socket
import json

with open("config.json") as f:
    config = json.load(f)

devices = config["devices"]
PORT = config["port"]

def send_command_to_device(ip, command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((ip, PORT))
            s.sendall(command.encode())
            response = s.recv(1024).decode()
            return response
    except Exception as e:
        return f"❌ خطأ: {e}"
