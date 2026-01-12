## Overview

A remote orchestration simulator written in Python. It mimics high-level command-and-control patterns for learning, detection testing, and incident response practice — only using non-destructive, auditable actions.

Run "server help" for a list of simulator commands and options.

`karth@HP:~$ server --help
karth@HP:~$ server help
Client Commands:
client download FILENAME - transfer a file from the server to the client
client upload FILENAME - transfer a file from the client to the server
client zip FILENAME - zip and encrypt a file on the client
client unzip FILENAME - unzip and decrypt a file on the client
client kill - permanently shutdown the active client
client delay SECONDS - change the delay setting for a client's reconnection attempts (coming soon)
client delay SECONDS - change the delay setting for a client's reconnection attempts
client get clipboard - grab a copy of the client's clipboard
client keylog on - start up a keylogger on the client
client keylog off - turn off the keylogger on the client and write the results to disk
client type TEXT - type the text of your choice on a client's keyboard
client screenshot - grab a copy of the client's screens
client display IMAGE - display an image on the client's screen
client flip screen - flip a client's screen upside down (Windows only)
client rotate screen - rotate a client's screen (Windows only)
client max sound - turn a client's volume all the way up
client play FILENAME.wav - play a .wav sound file on the client (Windows only)
* - run an OS command on the client that doesn't require input
* & - run an OS command on the client in the background

Server Commands:
server show clients - print an active listing of our pwned clients
server control PWNED_ID - change the active client that you have a prompt for
server zip FILENAME - zip and encrypt a file in the outgoing folder on the server
server unzip FILENAME - unzip and decrypt a file in the incoming folder on the server
server exit - gracefully shuts down the server
server list DIRECTORY - obtain a file listing of a directory on the server
server shell - obtain a shell on the server`

# Technologies
- Python 3.9+

# Usage (safe, lab-only)
- Place c2_client.py on the target device.
- Place c2_server.py on your device only run after running the c2_client.py on your wsl.

# Installation
1. Clone the repository
git clone https://github.com/KarthikMudgal/py_c2
cd py_c2

2. Create and activate a virtual environment
On Windows:
python -m venv .venv
.venv\Scripts\activate

On macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate


💡 You’ll know the virtual environment is active when you see (.venv) at the start of your terminal prompt.

3. Install dependencies from requirements.txt

- Once the virtual environment is active, run:
  - pip install -r requirements.txt
- This will automatically install all the required Python packages (and correct versions) listed in the requirements.txt file.

4. Verify installation
- You can confirm everything installed correctly by running:
- pip list


You should see the same packages as listed in requirements.txt.
