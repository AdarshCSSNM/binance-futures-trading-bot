<b>Binance Futures Trading Bot (USDT-M)
A robust Command Line Interface (CLI) tool for executing Market and Limit orders on the Binance Futures Testnet. This project focuses on API security, modular architecture, and structured logging.</b>

📂 Project Structure:
```bash
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
```
🛠️ Installation & Setup
1. Clone the repository
```bash
git clone [https://github.com/AdarshCSSNM/binance-futures-trading-bot.git](https://github.com/AdarshCSSNM/binance-futures-trading-bot.git)
```
2. Enter the project directory
```bash
cd binance-futures-trading-bot
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Configure Environment Variables
Rename .env.example to .env and add your Binance Testnet credentials:
Windows:
```bash
copy .env.example .env
```
Linux / macOS:
```bash
cp .env.example .env
```
<b>🚀 Use Cases & Execution</b><br>
1. Market Execution
For immediate entry at the current market price.
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.005
```
2. Limit Execution
For tactical entry at a specific price target.
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 85000
```
<b>📝 Key Implementation Features<br></b>
Error Handling: Implemented logic to intercept APIError(code=-4164) (Minimum Notional) to ensure orders meet the >100 USDT requirement.

Audit Logging: Every transaction is recorded in bot_activity.log with a timestamp, order ID, and the full JSON response.

Credential Security: Built with python-dotenv to ensure API Secret Keys are never hardcoded or committed to version control.
