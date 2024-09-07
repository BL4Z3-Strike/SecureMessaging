from flask import Flask, request, render_template_string, abort
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = 'your_secret_key'
socketio = SocketIO(app)

# Just Change SECRET_KEY
SECRET_KEY = 'hackedbyz!'

@app.route('/')
def index():
    key = request.args.get('key')
    if key == SECRET_KEY:
        return render_template_string('''
            <!doctype html>
            <html>
            <head>
                <title>Secure Chat</title>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.min.js"></script>
                <script>
                    document.addEventListener("DOMContentLoaded", function() {
                        var socket = io();
                        var form = document.getElementById("form");
                        var input = document.getElementById("message");
                        var messages = document.getElementById("messages");

                        form.addEventListener("submit", function(e) {
                            e.preventDefault();
                            var message = input.value;
                            socket.send(message);
                            input.value = '';
                        });

                        socket.on("message", function(msg) {
                            var item = document.createElement("li");
                            item.textContent = msg;
                            messages.appendChild(item);
                        });
                    });
                </script>
            </head>
            <body>
                <h1>Secure Chat</h1>
                <ul id="messages"></ul>
                <form id="form">
                    <input id="message" autocomplete="off" />
                    <button>Send</button>
                </form>
            </body>
            </html>
        ''')
    else:
        abort(403)

@socketio.on('message')
def handle_message(msg):
    send(msg)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
