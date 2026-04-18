from flask import Flask, abort, render_template


app = Flask(__name__)


USER_PROFILE = {
    "username": "kimdayoung",
    "cash_balance": 620000,
    "portfolio_value": 845600,
    "coins": {
        "BTC": 0.42,
        "ETH": 5.8,
        "XRP": 1240,
    },
}

MARKETS = {
    "BTC": {
        "symbol": "BTC",
        "name": "Bitcoin",
        "pair": "BTC/KRW",
        "price": 132,
        "change_pct": 7.4,
        "high": 138,
        "low": 96,
        "open": 100,
        "volume": 8942,
        "market_supply": 64.8,
        "user_supply": 35.2,
        "spread": 4,
        "sentiment": "Bullish",
        "description": "가장 거래량이 큰 기준 마켓으로, PDF의 초기 마켓 개념을 대표하는 코인입니다.",
        "price_points": [190, 178, 140, 144, 200, 176, 88, 98, 156, 74],
        "order_book": {
            "asks": [
                {"amount": 12.0, "price": 136},
                {"amount": 8.5, "price": 135},
                {"amount": 6.1, "price": 134},
            ],
            "bids": [
                {"amount": 9.3, "price": 130},
                {"amount": 14.2, "price": 128},
                {"amount": 16.4, "price": 127},
            ],
        },
        "sell_posts": [
            {"seller": "user_aria", "amount": 2.8, "price": 134},
            {"seller": "trader_min", "amount": 5.2, "price": 136},
            {"seller": "holder_lee", "amount": 1.6, "price": 139},
        ],
        "history": [
            {"time": "09:12", "type": "Market Buy", "amount": "3.0 coin", "price": "₩132", "status": "체결", "tone": "success"},
            {"time": "09:08", "type": "Sell Post", "amount": "4.5 coin", "price": "₩137", "status": "등록", "tone": "neutral"},
            {"time": "08:54", "type": "Deposit", "amount": "-", "price": "₩300,000", "status": "완료", "tone": "success"},
            {"time": "08:40", "type": "Market Sell", "amount": "1.8 coin", "price": "₩129", "status": "변동", "tone": "warning"},
        ],
    },
    "ETH": {
        "symbol": "ETH",
        "name": "Ethereum",
        "pair": "ETH/KRW",
        "price": 96,
        "change_pct": 4.1,
        "high": 104,
        "low": 87,
        "open": 92,
        "volume": 6210,
        "market_supply": 42.3,
        "user_supply": 57.7,
        "spread": 3,
        "sentiment": "Stable",
        "description": "스마트 컨트랙트 기반 거래 시나리오를 보여주는 보조 마켓입니다.",
        "price_points": [180, 172, 168, 152, 146, 132, 118, 104, 112, 92],
        "order_book": {
            "asks": [
                {"amount": 7.8, "price": 98},
                {"amount": 6.2, "price": 99},
                {"amount": 3.4, "price": 100},
            ],
            "bids": [
                {"amount": 10.1, "price": 95},
                {"amount": 13.7, "price": 94},
                {"amount": 15.3, "price": 93},
            ],
        },
        "sell_posts": [
            {"seller": "chain_park", "amount": 1.4, "price": 98},
            {"seller": "eth_seller", "amount": 2.1, "price": 99},
            {"seller": "defi_kim", "amount": 0.8, "price": 101},
        ],
        "history": [
            {"time": "10:02", "type": "Market Buy", "amount": "1.2 coin", "price": "₩96", "status": "체결", "tone": "success"},
            {"time": "09:30", "type": "Sell Post", "amount": "0.7 coin", "price": "₩99", "status": "등록", "tone": "neutral"},
            {"time": "09:14", "type": "Withdraw", "amount": "-", "price": "₩120,000", "status": "완료", "tone": "success"},
            {"time": "08:50", "type": "Market Sell", "amount": "0.9 coin", "price": "₩94", "status": "변동", "tone": "warning"},
        ],
    },
    "XRP": {
        "symbol": "XRP",
        "name": "Ripple",
        "pair": "XRP/KRW",
        "price": 58,
        "change_pct": -1.8,
        "high": 63,
        "low": 55,
        "open": 60,
        "volume": 13280,
        "market_supply": 78.4,
        "user_supply": 21.6,
        "spread": 2,
        "sentiment": "Cooling",
        "description": "고빈도 주문과 좁은 스프레드를 표현하기 위한 서브 마켓입니다.",
        "price_points": [130, 120, 112, 108, 114, 118, 126, 134, 138, 146],
        "order_book": {
            "asks": [
                {"amount": 130, "price": 59},
                {"amount": 240, "price": 60},
                {"amount": 510, "price": 61},
            ],
            "bids": [
                {"amount": 340, "price": 57},
                {"amount": 410, "price": 56},
                {"amount": 620, "price": 55},
            ],
        },
        "sell_posts": [
            {"seller": "xrp_hub", "amount": 220, "price": 59},
            {"seller": "swing_yoon", "amount": 140, "price": 60},
            {"seller": "ripple_j", "amount": 310, "price": 61},
        ],
        "history": [
            {"time": "11:10", "type": "Market Buy", "amount": "80 coin", "price": "₩58", "status": "체결", "tone": "success"},
            {"time": "10:44", "type": "Sell Post", "amount": "200 coin", "price": "₩60", "status": "등록", "tone": "neutral"},
            {"time": "10:03", "type": "Deposit", "amount": "-", "price": "₩50,000", "status": "완료", "tone": "success"},
            {"time": "09:40", "type": "Market Sell", "amount": "120 coin", "price": "₩57", "status": "변동", "tone": "warning"},
        ],
    },
}


def build_chart_path(points):
    if not points:
        return ""

    x_step = 600 / (len(points) - 1)
    segments = [f"M20 {points[0]}"]
    for index, point in enumerate(points[1:], start=1):
        segments.append(f"L{20 + index * x_step:.1f} {point}")
    return " ".join(segments)


def build_chart_area(points):
    line = build_chart_path(points)
    if not line:
        return ""
    return f"{line} L620 240 L20 240 Z"


def market_cards():
    cards = []
    for market in MARKETS.values():
        cards.append(
            {
                "symbol": market["symbol"],
                "name": market["name"],
                "pair": market["pair"],
                "price": market["price"],
                "change_pct": market["change_pct"],
                "market_supply": market["market_supply"],
                "sentiment": market["sentiment"],
            }
        )
    return cards


@app.context_processor
def inject_globals():
    return {
        "all_markets": market_cards(),
        "user_profile": USER_PROFILE,
    }


@app.route("/")
def home():
    featured = MARKETS["BTC"]
    return render_template(
        "home.html",
        featured=featured,
        chart_path=build_chart_path(featured["price_points"]),
        chart_area=build_chart_area(featured["price_points"]),
    )


@app.route("/markets/<symbol>")
def market_detail(symbol):
    market = MARKETS.get(symbol.upper())
    if not market:
        abort(404)
    return render_template(
        "market.html",
        market=market,
        chart_path=build_chart_path(market["price_points"]),
        chart_area=build_chart_area(market["price_points"]),
    )


@app.route("/signin")
def signin():
    return render_template("auth.html", mode="signin")


@app.route("/signup")
def signup():
    return render_template("auth.html", mode="signup")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4173)
