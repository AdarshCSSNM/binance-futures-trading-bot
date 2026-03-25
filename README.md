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
```bash
git clone [https://github.com/AdarshCSSNM/binance-futures-trading-bot.git](https://github.com/AdarshCSSNM/binance-futures-trading-bot.git)
```bash
```bash
cd binance-futures-trading-bot
```bash

Install dependencies
```bash
pip install -r requirements.txt
```bash

Configure Environment Variables
Rename .env.example to .env and add your Binance Testnet credentials:
# Windows
```bash
copy .env.example .env
# Linux/macOS
```bash
cp .env.example .env

🚀 Use Cases & Execution
1. Market Execution
For immediate entry at the current market price. Useful for strategies requiring instant liquidity.
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.005

2. Limit Execution
For tactical entry at a specific price target. Orders remain open until the target price is reached.
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 85000

📝 Key Implementation Features
Error Handling: Implemented logic to intercept APIError(code=-4164) (Minimum Notional). This ensures orders meet the Binance requirement (typically >100 USDT) before rejection.

Audit Logging: Every transaction is recorded in bot_activity.log with a timestamp, order ID, and the full JSON response from the exchange for transparency.

Credential Security: Built with python-dotenv to ensure API Secret Keys are never hardcoded or committed to version control.
