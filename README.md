# DroidRun AI Agent – Natural Language Mobile Automation 🤖📱

This project demonstrates how to use **DroidRun** to build an AI-powered Android automation agent that can understand natural language instructions and perform real actions on a physical Android device. Instead of using brittle scripts or app-specific APIs, the agent visually interprets the mobile UI and interacts with apps dynamically.

The main demo showcases **automated train ticket booking in the ixigo app**, where the AI scans available options, compares prices, avoids ads and offers, and safely pauses before completing a UPI payment.

---

## 🚀 Features

* 🧠 **Natural Language Control** – Give simple text prompts like a human assistant
* 📱 **Real Device Automation** – Runs on a physical Android phone via ADB
* 👀 **UI-Aware Navigation** – Reads screen state instead of relying on hardcoded steps
* 💸 **Cheapest Option Finder** – Compares prices across dates and coach types
* 🛑 **Safe Payment Flow** – Skips offers/insurance and pauses before final payment
* 🔌 **LLM Flexible** – Supports Gemini, DeepSeek, Ollama, or other local/cloud models

---

## 🧩 Example Prompt

```
Open ixigo train app
Find train from Rishikesh (YNRK) to New Delhi (NDLS)
Date after 23 Jan 2026 and before 26 Jan
Select 3A, 3E or Sleeper Coach (Find cheapest option)
Select Himanshu Haldar as Passenger
NO insurance or offers
Tick Consider Auto Upgradation
Proceed to pay
Use UPI ID: himanshuhaldar@fifedral
Submit
```

---

## 🏗️ Tech Stack

* **DroidRun** – Mobile automation and AI agent framework
* **Python 3.10+** – Core runtime
* **ADB (Android Debug Bridge)** – Device communication
* **LLM Providers**

  * Google Gemini (Cloud)
  * Ollama / DeepSeek (Local)

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Himansh-u2000/droidrun.git
cd droidrun
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📱 Android Device Setup

### Install ADB

Download Android Platform Tools and add `adb` to your system PATH.

Verify:

```bash
adb devices
```

### Setup DroidRun Portal

```bash
droidrun setup
```

This will:

* Install the DroidRun Portal APK
* Enable Accessibility Services

---

## 🔐 LLM Configuration

### Option 1: Gemini (Cloud)

Set API key:

```powershell
setx GOOGLE_API_KEY "YOUR_API_KEY"
```

### Option 2: Local LLM (Recommended)

Install Ollama:

```bash
ollama run deepseek
```

Then configure DroidRun to use the local model in your `.droidrun/config.yml`

---

## ▶️ Run the Agent

```bash
python agent.py
```

Or use CLI mode:

```bash
droidrun run "Open Settings and show battery level"
```

---

## 🛡️ Safety Design

* Automatically skips ads, offers, and insurance screens
* Stops before final payment for human confirmation
* Works only on user-authorized devices

---

## 🎯 Use Cases

* Train & flight booking
* Form filling
* App onboarding automation
* Accessibility assistance
* QA & mobile testing
* Digital literacy support

---

## 🏆 Hackathon Context

This project was built for a **DroidRun-sponsored hackathon**, where the challenge was to create a real-world solution using DroidRun’s mobile automation platform.

The goal: **Make complex mobile workflows simple, accessible, and safe using AI.**

---

## 📹 Demo

🎥 YouTube Demo: *(Add your link here)*

---

## 🔗 Repository

GitHub: [https://github.com/Himansh-u2000/droidrun](https://github.com/Himansh-u2000/droidrun)

---

## 👨‍💻 Author

**Himanshu Haldar**
Computer Science Student | Mobile & AI Automation Developer

---

## ⭐ Acknowledgments

* DroidRun Team – Platform & Hackathon Support
* Google Gemini / Ollama / DeepSeek – LLM Providers

---

If you like this project, consider giving it a ⭐ on GitHub — it really helps!
