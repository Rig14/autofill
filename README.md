# Autofill software

## How to use

1. Write something.
2. Press shortcut.
3. See how it generates text for you.

## How to run

### Linux

1. Become super user.
```bash
su -
```
2. Navigate to this project folder.
3. Create venv.
```bash
python3 -m venv .venv
```
4. Activate venv.
```bash
source .venv/bin/activate
```
5. Install requirements.
```bash..
pip install -r requirements.txt
```
6. Start program with python.
```bash
python3 main.py
```

## API keys

In the project root directory there is a `.env.example` file. Copy it and rename it to `.env`. Insert your OpenAI API key into the file.