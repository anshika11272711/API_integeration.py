import requests
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Fetch data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 5, "page": 1}
response = requests.get(url, params=params)
data = response.json()

# Step 2: Setup rich console and table
console = Console()
table = Table(title="💰 Top 5 Cryptocurrencies (Live)", show_lines=True)
table.add_column("Coin", style="cyan")
table.add_column("Price ($)", justify="right", style="green")
table.add_column("24h Change (%)", justify="right", style="magenta")

# Step 3: Process and print data
coin_names = []
coin_prices = []

for coin in data:
    name = coin["name"]
    price = round(coin["current_price"], 2)
    change = round(coin["price_change_percentage_24h"], 2)

    coin_names.append(name)
    coin_prices.append(price)

    change_color = "red" if change < 0 else "green"
    table.add_row(name, f"{price}", f"[{change_color}]{change}%[/{change_color}]")

console.print(table)

# Step 4: Plotting prices
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x=coin_names, y=coin_prices, palette="coolwarm")
plt.title("Top 5 Cryptos by Price (USD)")
plt.xlabel("Cryptocurrency")
plt.ylabel("Price in USD")
plt.tight_layout()
plt.show()