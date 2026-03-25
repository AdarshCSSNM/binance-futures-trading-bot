🚀 Binance Futures Trading Bot (USDT-M)A professional-grade, modular CLI application for interacting with the Binance Futures Testnet. This tool provides a secure environment for executing and auditing automated trading operations.📦 Project InformationCore Logic: Modular Python architecture for scalability.API Integration: Secure HMAC SHA256 signing via python-binance.Security: Decoupled credential management using .env files.Monitoring: Integrated logging system for real-time and persistent auditing.🛠️ Installation InstructionsFollow these steps to set up the environment on your local machine:Clone the RepositoryBashgit clone https://github.com/AdarshCSSNM/binance-futures-trading-bot.git
cd binance-futures-trading-bot
Install DependenciesEnsure you have Python 3.8+ installed.Bashpip install -r requirements.txt
Configure CredentialsDuplicate the example environment file and add your Testnet API keys:Bashcp .env.example .env
Open .env and insert your BINANCE_API_KEY and BINANCE_API_SECRET.💻 Use Case & ExecutionThe bot is designed for rapid execution of standard order types on the USDT-Margined futures market.Order TypeScenarioCommand ExampleMARKETImmediate entry at current pricepython cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.005LIMITTactical entry at a specific targetpython cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 85000📝 Technical Implementation Details<details><summary><b>Error Handling & Validation</b></summary>The bot includes internal logic to catch and log exchange-specific errors, such as <code>APIError(code=-4164)</code>. This ensures the user is notified if an order falls below the 100 USDT Minimum Notional requirement.</details><details><summary><b>Logging System</b></summary>Every execution generates a trace in <code>bot_activity.log</code>. This includes the request summary, order ID, and the raw JSON response from the Binance server for full transparency.</details><details><summary><b>Project Structure</b></summary>Plaintext├── bot/
│   ├── client.py           # Core API Logic
│   ├── logging_config.py   # System Logging
│   └── __init__.py
├── cli.py                  # CLI Entry Point
├── .env.example            # Credential Template
└── requirements.txt        # Dependency List
</details>
