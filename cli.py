import argparse
from bot.client import BinanceBot
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()
    try:
        bot = BinanceBot()
        logger.info(f"Placing {args.type} {args.side} for {args.symbol}")
        res = bot.place_order(args.symbol, args.side, args.type, args.qty, args.price)
        logger.info(f"Order Success: {res['orderId']}")
        print(f"Success! Order ID: {res['orderId']}")
    except Exception as e:
        logger.error(f"Error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
