# py_c2: Command And Control

## Overview
A remote orchestration simulator written in Python. It mimics high-level command-and-control patterns for learning, detection testing, and incident response practice — only using non-destructive, auditable actions.

## Technologies
- Python 3.9+

## Installation
1. Clone the repository
```bash
git clone https://github.com/KarthikMudgal/py_c2
cd py_c2
```
2. Create and activate a virtual environment
- On Windows:
```python 
python -m venv .venv
.venv\Scripts\activate
```
On macOS / Linux:
```python
python3 -m venv .venv
source .venv/bin/activate
```

💡 You’ll know the virtual environment is active when you see (.venv) at the start of your terminal prompt.

3. Install dependencies from requirements.txt

- Once the virtual environment is active, run:
```python
pip install -r requirements.txt
```
- This will automatically install all the required Python packages (and correct versions) listed in the requirements.txt file.

4. Verify installation
- You can confirm everything installed correctly by running:
- pip list


You should see the same packages as listed in requirements.txt.

## Usage 
1. On the target device run the ```c2_client.py``` file
```bash
sudo python3 c2_client.py
```
2. On the controller device run the ```c2_server.py``` file
```bash
sudo python3 c2_server.py
```
3. Run "server help" for a list of simulator commands and options.
```bash
server help
```
<img width="1028" height="599" alt="image" src="https://github.com/user-attachments/assets/a5434bc5-f0d2-4c5d-b94c-b77492a90beb" />
