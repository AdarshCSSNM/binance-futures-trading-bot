<b>Binance Futures Trading Bot (USDT-M)
A robust Command Line Interface (CLI) tool for executing Market and Limit orders on the Binance Futures Testnet. This project focuses on API security, modular architecture, and structured logging.</b>

📂 Project Structure:
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
