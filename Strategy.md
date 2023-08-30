# Explaining the Strategy:
## Moving Averages
### Concept:
* Moving Averages smooth out price data to create a single flowing line, which makes it easier to identify the direction of the trent
* Two times: Short-Term (fast) MA and Long-Term(Slow) MA.

### Usage in the strategy:
* Short-Term MA: Average of the last two closing prices.
* Long-Term MA: Average of the last 4 closing prices.
* Crossover Strategy:
* ### Buy Signal - 
When the short term MA crosses above the Long-term it indicates that recent prices are rising faster than older prices, making an uptrend.
* ### Sell Signal - 
When the Short-term MA crosses below the Long-Term MA it indicates that recent prices are falling faster than older prices creaing a downtrend.

## Relative Strength Index (RSI)
### Concept:

* RSI is a momentum oscillator that measures the speed and change of price movements.
* Ranges between 0 to 100 and is typically used to identify overbought or oversold conditions in a traded security.

### Usage in the strategy:

* Overbought Condition: RSI value over 70. This means the stock might be overvalued, and there's a higher chance of it going down.
* Oversold Condition: RSI value under 30. This suggests the stock might be undervalued, indicating a potential rise in the future.
* Buy Signal: When RSI crosses above 30, indicating a potential reversal from an oversold condition.
* Sell Signal: When RSI crosses below 70, hinting at a possible reversal from an overbought condition.

### Strategy Flow:
1. For each stock symbol, retrieve the last 5 closing prices.
2. If there are fewer than 3 closing prices available (or less than 14 for RSI), recommend holding the stock as there's not enough data to make a decision.
3. Calculate Short-term and Long-term MAs.
4. Based on the crossover of these MAs, decide if the signal is to buy, sell, or hold.
5. Calculate RSI using the closing prices.
6. Combine RSI signal with the MA crossover signal to make a final decision:
* If both RSI and MA suggest buying, strongly consider buying.
* If both RSI and MA recommend selling, strongly consider selling.
* In mixed conditions (e.g., RSI suggests buying but MA recommends selling), you might decide to hold or weigh one indicator over the other based on your personal trading philosophy.

## Main Points:
* Adaptive: The strategy uses both trend-following (MA) and momentum (RSI) indicators, adapting to different market conditions.
* Safety Nets: It considers holding in cases of insufficient data or mixed signals, reducing the chances of false positives.
* Versatility: While optimized for the current data granularity, it can be adjusted (e.g., changing MA or RSI periods) to adapt to different trading horizons or stock behaviors.
* Limitations: Like all strategies, it's not foolproof. It's essential to consider external factors (news, market conditions, etc.) and not rely solely on technical indicators.