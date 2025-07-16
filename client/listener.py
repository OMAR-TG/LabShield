import socket
from cleaner import clear_user_files

HOST = "0.0.0.0"
PORT = 9090

def start_listener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"✅ مستعد على {PORT}...")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"📡 اتصال من {addr}")
                data = conn.recv(1024).decode().strip()
                if data == "CLEAR_FILES":
                    clear_user_files()
                    conn.sendall(b"FILES_CLEARED")
                else:
                    conn.sendall(b"UNKNOWN_COMMAND")
