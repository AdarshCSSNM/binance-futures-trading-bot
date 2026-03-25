Binance Futures Trading Bot (USDT-M)
A modular Python-based Command Line Interface (CLI) application developed to interact with the Binance Futures Testnet. This tool provides a secure and automated way to execute trading operations while maintaining detailed logs.

📁 Project Overview
This project was built to demonstrate proficiency in integrating financial APIs, handling real-time trade data, and implementing robust error handling within a Python environment. It serves as a lightweight foundation for automated strategy execution.

🛠 Installation
Clone the repository:

Bash
git clone https://github.com/AdarshCSSNM/binance-futures-trading-bot.git
cd binance-futures-trading-bot
Install required dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Rename .env.example to .env and insert your Binance Testnet API credentials:

Bash
cp .env.example .env
🚀 Use Case & Execution
The bot is designed for rapid execution of standard order types on the USDT-Margined futures market.

Market Orders
Used for immediate execution at current market prices.

Bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.005
Limit Orders
Used for tactical entry/exit at a specific price point.

Bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 85000
📝 Implementation Notes
Minimum Notional: Handles APIError(code=-4164) by ensuring order sizes meet the 100 USDT requirement.

Auditing: All API responses and execution traces are recorded in bot_activity.log.
