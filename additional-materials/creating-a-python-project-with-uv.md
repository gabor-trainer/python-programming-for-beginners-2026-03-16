# Creating a Python project with uv

**Purpose:** Create a new Python project using uv, set up the virtual environment, and configure VS Code  
**Time:** 10-15 minutes  
**Prerequisites:** 
- Python 3.12+ installed (see [Python environment setup](python-environment-setup.md))
- uv installed (see [Python environment setup](python-environment-setup.md))
- VS Code installed with Python extension (see [VS Code setup](python-vscode-setup.md))

---

## Overview

In this guide, you will:
1. Create a new Python project using `uv init`
2. Open the project in VS Code
3. Set up the virtual environment
4. Configure VS Code to use the correct Python interpreter

---

## Step 1: Open Command Prompt and navigate to your work directory

1. Press `Win+R`, type `cmd`, press **Enter**
2. Navigate to your work directory:

```cmd
cd C:\Users\YourUsername\work
```

**Note:** Replace `YourUsername` with your actual Windows username, or use any directory where you want to store your projects.

**Tip:** If the folder doesn't exist, create it first:
```cmd
mkdir C:\Users\YourUsername\work
cd C:\Users\YourUsername\work
```

---

## Step 2: Create a new project with `uv init`

Run the following command to create a new Python project:

```cmd
uv init myproject
```

**Replace `myproject`** with your desired project name (e.g., `weather-app`, `data-analyzer`, etc.).

**Expected output:**
```
Initialized project `myproject` at `C:\Users\YourUsername\work\myproject`
```

**What this creates:**
| File | Purpose |
|------|---------|
| `pyproject.toml` | Project configuration and dependencies |
| `main.py` | Entry point for your Python code |
| `README.md` | Project documentation |
| `.python-version` | Specifies the Python version to use |

---

## Step 3: Open the project in VS Code

There are two ways to open the project:

### Option A: From Command Prompt (recommended)

```cmd
cd myproject
code .
```

### Option B: From VS Code

1. Open VS Code
2. Go to **File** → **Open Folder...**
3. Navigate to `C:\Users\YourUsername\work\myproject`
4. Click **Select Folder**

---

## Step 4: Trust the folder (if prompted)

When VS Code opens a new folder, it may ask if you trust the authors:

1. A dialog appears: **"Do you trust the authors of the files in this folder?"**
2. Click **"Yes, I trust the authors"**

**Why?** VS Code restricts certain features in untrusted folders for security. Since this is your own project, it's safe to trust it.

---

## Step 5: Verify the project structure

In the VS Code **Explorer** panel (left side), confirm these files exist:

```
myproject/
├── .python-version
├── main.py
├── pyproject.toml
└── README.md
```

**Troubleshooting:**

| Issue | Solution |
|-------|----------|
| Files not showing | Click the refresh icon in Explorer or press `Ctrl+Shift+E` |
| Wrong folder opened | Go to **File** → **Open Folder** and select the correct project folder |

---

## Step 6: Open the VS Code terminal

1. Go to **Terminal** → **New Terminal** (or press `` Ctrl+` ``)
2. A terminal panel opens at the bottom of VS Code

---

## Step 7: Verify you are in the project folder

In the terminal, check your current directory:

```cmd
cd
```

**Expected output:**
```
C:\Users\YourUsername\work\myproject
```

**Alternative:** Use `pwd` in PowerShell:
```powershell
Get-Location
```

**If you're in the wrong folder:**
```cmd
cd C:\Users\YourUsername\work\myproject
```

---

## Step 8: Create the virtual environment

There are two ways to create the `.venv` folder:

### Option A: Add a package (recommended)

Install a package your project needs. This automatically creates the virtual environment:

```cmd
uv add requests
```

**Expected output:**
```
Using CPython 3.12.x
Creating virtual environment at: .venv
Resolved 5 packages in 156ms
Installed 5 packages in 12ms
 + certifi==2024.x.x
 + charset-normalizer==3.x.x
 + idna==3.x
 + requests==2.31.x
 + urllib3==2.x.x
```

### Option B: Sync dependencies (if no new packages needed)

If your `pyproject.toml` already has dependencies defined:

```cmd
uv sync
```

This creates the virtual environment and installs all dependencies from `pyproject.toml`.

### Option C: Create venv directly (without adding packages)

If you just want to create the virtual environment without installing any packages:

```cmd
uv venv
```

**Expected output:**
```
Using CPython 3.12.x
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
```

This creates an empty `.venv` folder with the Python interpreter ready to use.

---

## Step 9: Verify the .venv folder was created

In the VS Code **Explorer** panel, you should now see a `.venv` folder:

```
myproject/
├── .venv/           ← New folder!
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock          ← New file (dependency lock file)
```

**Note:** The `.venv` folder contains:
- Python interpreter (copy or link)
- Installed packages
- Scripts for activating the environment

---

## Step 10: Select the Python interpreter in VS Code

Tell VS Code to use the Python interpreter from your virtual environment:

1. Press `Ctrl+Shift+P` to open the Command Palette
2. Type **"Python: Select Interpreter"** and press **Enter**
3. Look for an option that shows `.venv` in the path:
   ```
   Python 3.12.x ('.venv': venv) .\venv\Scripts\python.exe
   ```
4. Click to select it

**Alternative:** Click on the Python version in the bottom-left status bar:

![Python interpreter status bar](images/python-interpreter-statusbar.png)

**Troubleshooting:**

| Issue | Solution |
|-------|----------|
| `.venv` interpreter not listed | Click "Enter interpreter path..." and browse to `.venv\Scripts\python.exe` |
| Multiple interpreters shown | Choose the one with `.venv` in the path to use the project's virtual environment |

---

## Step 11: Close and reopen the terminal

To ensure the virtual environment is properly activated:

1. Click the **trash can icon** (🗑️) on the terminal panel to close it
   - Or type `exit` and press **Enter**
2. Open a new terminal: **Terminal** → **New Terminal** (or press `` Ctrl+` ``)

---

## Step 12: Verify the virtual environment is activated

When you open a new terminal, VS Code should automatically activate the virtual environment.

### How to check if venv is activated:

**Look at the terminal prompt.** You should see `(.venv)` at the beginning:

```
(.venv) C:\Users\YourUsername\work\myproject>
```

**Or run this command:**

```cmd
where python
```

**Expected output (venv is active):**
```
C:\Users\YourUsername\work\myproject\.venv\Scripts\python.exe
C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\python.exe
```

The `.venv` path should appear **first**, indicating the virtual environment's Python is being used.

**In PowerShell:**
```powershell
Get-Command python | Select-Object Source
```

**Expected output:**
```
Source
------
C:\Users\YourUsername\work\myproject\.venv\Scripts\python.exe
```

---

## Quick reference

| Step | Command |
|------|---------|
| Navigate to work directory | `cd C:\Users\YourUsername\work` |
| Create new project | `uv init myproject` |
| Open project in VS Code | `code .` |
| Add a package (creates venv) | `uv add requests` |
| Sync dependencies | `uv sync` |
| Create venv only | `uv venv` |
| Check Python location | `where python` (cmd) or `Get-Command python` (PowerShell) |

---

## Summary

You have successfully:
- ✅ Created a new Python project with `uv init`
- ✅ Opened the project in VS Code
- ✅ Created a virtual environment with `uv add` or `uv sync`
- ✅ Configured VS Code to use the virtual environment's Python interpreter
- ✅ Verified the virtual environment is activated in the terminal

Your project is now ready for development!
