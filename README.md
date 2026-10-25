# PK fbr-wala — Stop Wasting Hours & Thousands on FBR Filing

![Python](https://img.shields.io/badge/Python-3.x-blue)
![CLI](https://img.shields.io/badge/Interface-CLI-green)
![Privacy](https://img.shields.io/badge/Privacy-100%25_Local-red)

**FBR IRIS portal par ghanton zaleel hona aur har saal CA ya wakeelon ko hazaron rupay fizool fees dena band karein.**

Agar aap software engineer, remote worker, freelancer ya salaried professional hain aur abhi tak tax filing manuals ya portal ke crash hone ke intezar mein baithe hain, to aap bohot peeche hain. **`fbr-wala`** aik ultra-fast, local CLI engine hai jo aapki tax computation aur sab se mushkil **Wealth Statement Reconciliation** ko terminal ke andar chand seconds mein zero-error ke sath hal karta hai.

## 🔥 Kyun Har Pakistani Tech Professional Ko Iski Zaroorat Hai?

* ⚡ **Zero Legal Fees:** Kisi tax consultant ko PKR 5,000–15,000 dene ki koi zaroorat nahi. Local verified code aapka pura hisab khud karega.
* ⚖️ **Automated Wealth Reconciliation:** Pakistani filing ka sab se bara dard — **Unreconciled Wealth** — ab guzray waqt ki baat hai. Tool $\Delta \text{Wealth} = \text{Inflow} - \text{Outflow}$ ko khud balance karta hai taake notice ka khatra na rahe.
* 🧾 **Recover Every Rupee of WHT:** Mobile bills, bijli ke bills, gari ke token aur salary par kata hua advance tax (Withholding Tax) khud track kar ke aapki tax liability mein se minus karein.
* 🎯 **Direct IRIS Box-Code Mapping:** IRIS portal ke complicated forms samajhne ki zaroorat nahi; yeh tool aapko exact **IRIS Code (e.g., Code 1000, 9200, 7001)** ke sath ready-to-paste sheet bana kar deta hai.
* 🔒 **100% Privacy & Local Control:** Aapka financial data kisi third-party cloud ya shady website par nahi jata; sab kuch aapke apne system par locally calculate hota hai.

## 🛠️ Installation & Setup

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
```

## 📂 Project Structure

```text
├── main.py              # Entry point
├── fbr_cli/
│   └── cli.py           # CLI commands
├── core/
│   ├── slabs.py         # Tax slabs
│   └── reconciler.py    # Wealth statement reconciliation
└── requirements.txt     # Dependencies
```

---

Built by **Syed Waqar Raza Zaidi** · 🌐 [Portfolio](https://portfolio-website-sigma-ashen-90.vercel.app)
