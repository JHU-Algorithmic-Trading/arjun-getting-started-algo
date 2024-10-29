# arjun-getting-started-algo

## test-algo-1
### Algorithm Overview: Mean Reversion with Profit-Taking
This algorithm is designed to trade between two assets—SPY (S&P 500 ETF) and BND (U.S. bond ETF)—based on a mean reversion strategy. Mean reversion assumes that prices will tend to move back toward their average over time. The algorithm buys or sells each asset when the price deviates from its average, expecting it will eventually "revert" to that average. To protect gains, the algorithm includes a profit-taking mechanism, which sells a position if it reaches a target profit or falls below a certain level.

### Step-by-Step Explanation
1. Identify Trends Using Moving Averages
For each asset (SPY and BND), the algorithm tracks two averages:
- A fast (short-term) moving average (10 days).
- A slow (long-term) moving average (50 days).
When the fast average is higher than the slow one, it signals a potential upward trend, suggesting it's a good time to buy. When it’s lower, it suggests a downward trend, signaling a potential sell.

2. Trading Once a Week
To minimize frequent trading, the algorithm only makes trades once a week (every Wednesday). This helps reduce trading fees and keeps the strategy simple.

3. Profit-Taking Mechanism
When the algorithm buys SPY or BND, it sets two conditions to secure profits:
- Target Profit: If the price rises by 2% above the entry price, the algorithm sells the position to lock in gains.
- Trailing Stop: If the price falls 1.5% below the highest reached price since buying, the algorithm exits the position to prevent large losses.

4. Switching Assets
The algorithm only holds one asset at a time. If it identifies a buy signal for SPY, it will sell BND (if owned) before buying SPY, and vice versa.

### Summary
This strategy combines a mean reversion approach with a simple profit-taking mechanism. It aims to capture gains when prices move favorably but minimizes the risk of loss by selling when a profit target or stop level is met. This makes the strategy adaptive, letting it benefit from upward trends while being cautious about potential reversals.

### Cloud Backtest Results

| Statistic                  | Value            | Statistic                   | Value       | 
|----------------------------|------------------|------------------------------|-------------|
| Equity                     | $3,438.43        | Fees                        | -$155.00    |  
| Holdings                   | $3,387.70        | Net Profit                  | $472.23     |  
| Probabilistic Sharpe Ratio | 10.469%          | Return                      | 14.61 %     |  
| Unrealized                 | $-34.79          | Volume                      | $476,208.91 |  
| Total Orders               | 171              | Average Win                 | 1.25%       |  
| Average Loss               | -1.19%           | Compounding Annual Return   | 4.653%      |  
| Drawdown                   | 14.700%          | Expectancy                  | 0.172       |  
| Start Equity               | 3000             | End Equity                  | 3438.43     |  
| Net Profit                 | 14.614%          | Sharpe Ratio                | 0.197       |  
| Sortino Ratio              | 0.179            | Probabilistic Sharpe Ratio  | 10.469%     |  
| Loss Rate                  | 43%              | Win Rate                    | 57%         |  
| Profit-Loss Ratio          | 1.05             | Alpha                       | 0.021       |  
| Beta                       | 0.103            | Annual Standard Deviation   | 0.089       |  
| Annual Variance            | 0.008            | Information Ratio           | 0.237       |  
| Tracking Error             | 0.237            | Treynor Ratio               | 0.171       |  
| Total Fees                 | $155.00          | Estimated Strategy Capacity | $3000000.00 |  
| Lowest Capacity Asset      | BND TRO5ZARLX6JP | Portfolio Turnover          | 13.98%      |  
