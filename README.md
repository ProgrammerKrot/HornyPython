# HornyPython Interpreter 🔞

A **parodic custom Python dialect** that lets you write scripts using spicy alternative keywords. Built for fun, shock value, and educational exploration of language parsing.

You can create your own by changing values in CONFIG file

---

## 🚀 Installation (Linux/macOS)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/HornyPython.git
cd HornyPython
```

### 2. Install System-Wide
```bash
chmod +x execute_custom_python.py
sudo cp execute_custom_python.py /usr/local/bin/hornypy-exec
sudo cp my_python_config.py /usr/local/bin/
```

### 3. Register Custom MIME Type (Optional but Cool 😎)
```bash
mkdir -p ~/.local/share/mime/packages
cat > ~/.local/share/mime/packages/hornypy.xml <<EOF
<?xml version="1.0"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-hornypy">
    <comment>HornyPython Script</comment>
    <glob pattern="*.hornypy"/>
  </mime-type>
</mime-info>
EOF

update-mime-database ~/.local/share/mime
```

---

## 🧠 Usage

### Writing HornyPython Code
Create a script with the `.hornypy` extension and start it with this shebang:
```python
#!/usr/bin/env hornypy-exec

sex hello():
    moan("Oh yes!")
```

### Make Your Script Executable
```bash
chmod +x your_script.hornypy
```

### Run the Script
```bash
./your_script.hornypy
# Or directly:
hornypy-exec your_script.hornypy
```

---

## 🔤 Syntax Cheatsheet

| Standard Python | HornyPython |
|-----------------|-------------|
| `def`           | `sex`       |
| `print`         | `moan`      |
| `if`            | `you`       |
| `else`          | `me`        |
| `True`          | `Yes_daddy` |

More to come. Contributions welcome 😉

---

## 🛠️ Troubleshooting

### Permission Errors?
```bash
sudo chmod +x /usr/local/bin/hornypy-exec
```

### MIME Type Doesn’t Work?
Verify with:
```bash
xdg-mime query filetype your_script.hornypy
# Expected: application/x-hornypy
```

---

## ⚠️ Disclaimer

This is a **parody project** intended for **educational and entertainment purposes only**. Not affiliated with the Python Software Foundation. Don’t use this in production (unless your boss is really cool).

---

🧪 Built with questionable taste and lots of Python ❤️
