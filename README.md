# Binance Futures Trading Bot (USDT-M)

A robust Command Line Interface (CLI) tool for executing Market and Limit orders on the Binance Futures Testnet. This project was developed as a technical assessment, focusing on API security, modular architecture, and structured logging.

---

## 📂 Project Structure

```text
trading_bot/
├── bot/
│   ├── client.py           # Core Binance API interaction logic
│   ├── logging_config.py   # Centralized logging (File + Stream)
│   └── __init__.py
├── .env.example            # Configuration template
├── .gitignore              # Security: Excludes credentials and logs
├── cli.py                  # CLI Entry point (argparse)
├── LICENSE                 # MIT License
├── README.md               # Documentation
└── requirements.txt        # Project dependencies

🛠️ Installation & Setup
Clone the repository
git clone [https://github.com/AdarshCSSNM/binance-futures-trading-bot.git](https://github.com/AdarshCSSNM/binance-futures-trading-bot.git)
cd binance-futures-trading-bot
