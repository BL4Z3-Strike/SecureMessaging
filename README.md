# SecureMessaging

SecureMessaging is a web application that provides secure messaging with end-to-end encryption features. Developed using Flask, this application ensures that your messages are transmitted in a confidential and secure manner.

## Features

- **End-to-End Encryption:** Messages are encrypted in a way that only the sender and receiver can read them.
- **Access with Secret Key:** Access to the application is granted using a specific secret key (`SECRETKEY`).
- **Simple User Interface:** Provides an easy-to-use and straightforward interface for messaging.

## Getting Started

### Requirements

- Python 3.8 or higher
- Flask
- Flask-SocketIO (and other required packages)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/BL4Z3-Strike/SecureMessaging.git
2. **Navigate to the Project Directory:**

   ```bash
   cd SecureMessaging
3. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
4. **Activate the Virtual Environment:**
    - On Windows
      ```bash
      venv\Scripts\activate
    - On MacOS/Linux
      ```bash
      source venv/bin/activate
5. **Install the Required Packages:**
   ```bash
   pip install -r requirements.txt
6. **Set Up the Secret Key:**
   Create a .env file in the project root and add your secret key:
   ```bash
   SECRETKEY=your_secret_key_here
7. **Run the Application:**
   ```bash
   python app.py
8. **Open Your Browser:**
    - Go to http://127.0.0.1:5000 to access the application
## Usage
Once the application is running, you can:
 - Log in using the secret key.
 - Start sending encrypted messages to other users.
