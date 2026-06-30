# Data Pipeline Training Sandbox

Welcome to the Data Pipeline Training repository! 

This repository contains mock Python scripts and data pipelines designed to help you practice code reading, debugging, and the Software Development Life Cycle (SDLC).

## What is a Virtual Environment (`venv`)?
Before we run the code, we are going to set up a **Virtual Environment**. 
Think of a virtual environment as a private sandbox for this specific project. It ensures that any tools or libraries we use here don't accidentally mess up other Python projects on your computer. 

---

## 🚀 Setup Instructions

### Step 1: Clone the Repository
First, bring the code from GitHub down to your local machine. Open your terminal (or Command Prompt) and run:
```bash
git clone https://github.com/swapnil-kondana/sdlc-training-repo
cd sdlc-training-repo
```

### Step 2: Create the Virtual Environment
Now, let's build your sandbox. Run the following command. (This will create a hidden folder named `venv` in your project directory).

**For Windows:**
```bash
python -m venv venv
```

**For macOS / Linux:**
```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment
You have built the sandbox, but now you need to step inside it. 

**For Windows:**
```bash
venv\Scripts\activate
```

**For macOS / Linux:**
```bash
source venv/bin/activate
```
*(You will know it worked if you see `(venv)` appear at the very beginning of your terminal prompt line!)*

### Step 4: Run the Pipeline Script
Now that you are safely inside your virtual environment, it's time to test the code. Run the mock revenue report pipeline:

**For Windows:**
```bash
python generate_revenue_report.py
```

**For macOS / Linux:**
```bash
python3 generate_revenue_report.py
```

Look at the output in your terminal. If the pipeline fails, read the error message carefully—your mission is to find the bug in the code, fix it, and run this command again until you see the green success message!

### Step 5: Deactivate (When you are done)
Once you are finished working for the day and want to leave the sandbox, simply type:
```bash
deactivate
```
This returns your terminal to its normal state.

---

## 🛠️ Troubleshooting
* **"Python is not recognized"**: Ensure Python is installed on your computer and added to your system's PATH. 
* **Errors when activating (Windows)**: If PowerShell gives you a security error when running the activate command, try running `Set-ExecutionPolicy Unrestricted -Scope CurrentUser` as an administrator, then try activating again.
