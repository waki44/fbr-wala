# 🇵🇰 fbr-wala (Pakistani Tax & Wealth CLI Assistant)

A lightweight CLI tool to compute Pakistan Income Tax liability and automatically reconcile Wealth Statements for FBR IRIS e-filing.

### 🚀 Features
- 📊 **Updated Tax Slabs:** Salaried & Business tax bracket computations.
- ⚖️ **Wealth Reconciliation Engine:** Matches Inflows, Outflows, and Closing Assets.
- 🧾 **WHT Adjustments:** Tracks advance tax on salary, mobile, and vehicles.
- 📋 **IRIS Mapping:** Shows accurate IRIS box codes for easy copy-pasting.

### 🛠️ Installation & Setup
```bash
# Clone the repository
git clone https://github.com/waki44/fbr-wala.git
cd fbr-wala

# Create & activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the tool
python main.py start