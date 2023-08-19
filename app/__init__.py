from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def index():
    online_devices = find_online_devices()
    return render_template('index.html', online_devices=online_devices)

def find_online_devices():
    online_devices = []
    # Replace with your actual code to find online devices
    for i in range(1, 255):
        ip = f'192.168.1.{i}'
        try:
            socket.create_connection((ip, 80), timeout=1)
            online_devices.append(ip)
        except OSError:
            pass
    return online_devices
