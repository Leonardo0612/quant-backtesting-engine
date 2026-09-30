import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

ticker = "SPY"
start_date = "2016-01-01"
end_date = "2026-09-30"
data = yf.download(ticker, start=start_date, end=end_date)

df = pd.DataFrame(data["Close"]).ffill()
df.columns = ["Close"]

df["SMA50"] = df["Close"].rolling(window=50).mean()
df["SMA200"] = df["Close"].rolling(window=200).mean()
df = df.dropna()

df["Signal"] = np.where(df["SMA50"] > df["SMA200"], 1, 0)
df["Position"] = df["Signal"].shift(1)

def apply_stop_loss(df, stop_loss_pct=0.05):
    final_positions = df["Position"].copy()
    in_position = False
    entry_price = 0.0

    for i in range(len(df)):
        raw_pos = df["Position"].iloc[i]
        current_price = df["Close"].iloc[i]

        if raw_pos == 1 and not in_position:
            in_position = True
            entry_price = current_price
            final_positions.iloc[i] = 1

        elif in_position:
            stop_price = entry_price * (1 - stop_loss_pct)

            if current_price < stop_price:
                in_position = False
                final_positions.iloc[i] = 0

            elif raw_pos == 0:
                in_position = False
                final_positions.iloc[i] = 0

            else:
                final_positions.iloc[i] = 1

        else:
            final_positions.iloc[i] = 0

    return final_positions

df["Position"] = apply_stop_loss(df, stop_loss_pct=0.05)

annual_rf = 0.04
daily_rf = (1 + annual_rf) ** (1 / 252) - 1

df["Market_Return"] = df["Close"].pct_change()
df["Strategy_Return"] = np.where(
    df["Position"] == 1,
    df["Market_Return"],
    daily_rf
)

df["Market_Return"] = df["Market_Return"].fillna(0)
df["Strategy_Return"] = df["Strategy_Return"].fillna(0)

df["Cumulative_Market"] = (1 + df["Market_Return"]).cumprod()
df["Cumulative_Strategy"] = (1 + df["Strategy_Return"]).cumprod()

total_market_return = (df["Cumulative_Market"].iloc[-1] - 1) * 100
total_strategy_return = (df["Cumulative_Strategy"].iloc[-1] - 1) * 100

mean_return = df["Strategy_Return"].mean()
std_return = df["Strategy_Return"].std()

sharpe_ratio = (mean_return / std_return) * np.sqrt(252)

peak = df["Cumulative_Strategy"].cummax()
drawdown = (df["Cumulative_Strategy"] - peak) / peak
max_drawdown = drawdown.min()

print(sharpe_ratio)
print(max_drawdown)

plt.figure(figsize=(12, 6))

plt.plot(df.index, df["Cumulative_Market"], label=f"Market ({ticker})", color="Gray", linestyle="--", alpha=0.7)
plt.plot(df.index, df["Cumulative_Strategy"], label="SMA Crossover Strategy", color="blue", linewidth=2)

plt.title(f"{ticker} SMA Crossover Strategy vs Buy & Hold ({start_date[:4]}-{end_date[:4]})")
plt.xlabel("Date")
plt.ylabel("Growth of £1 Investement")
plt.legend(loc="upper left")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()