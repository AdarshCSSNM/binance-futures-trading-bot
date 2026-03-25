Binance Futures Trading Bot (USDT-M)
A modular Python-based Command Line Interface (CLI) application designed to interact with the Binance Futures Testnet. This project demonstrates secure API integration, structured logging, and robust error handling for automated trading operations.

Project Structure
Plaintext
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance API wrapper and order logic
│   ├── logging_config.py   # Centralized logging configuration
│   └── validators.py       # Input validation logic
├── cli.py                  # CLI entry point (argparse)
├── .env.example            # Environment variable template
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
Features
Order Types: Full support for MARKET and LIMIT orders.

Security: HMAC SHA256 request signing via python-binance and credential management using .env files.

Logging: Detailed execution logs saved to bot_activity.log, including full API responses and error traces.

Error Handling: Graceful handling of network failures, invalid inputs, and exchange-specific constraints (e.g., Minimum Notional Value).

Getting Started
Prerequisites
Python 3.8 or higher

Binance Futures Testnet API Key and Secret

Installation
Clone the repository:

Bash
git clone https://github.com/AdarshCSSNM/binance-futures-trading-bot.git
cd trading-bot-binance
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Rename .env.example to .env and add your credentials:

Bash
cp .env.example .env
# Edit .env with your API Key and Secret
Usage
The bot is executed via cli.py. Use the --help flag to see all available options.

Place a Market Order
Bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.005
Place a Limit Order
Bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 85000
Implementation Details
Minimum Notional Value: The bot includes logic to handle APIError(code=-4164), ensuring orders meet the Binance Testnet requirement (typically >100 USDT).

Logging Architecture: Implemented using Python's logging module with both FileHandler and StreamHandler for real-time monitoring and persistent auditing.
