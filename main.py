
# Analyzing sales data and optimizing restocking for a product like canned mackerels can be achieved through data analysis and forecasting techniques. 
# Here's a Python program that can help you analyze sales data and make restocking recommendations:

import pandas as pd
import numpy as np
from datetime import datetime
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

# Sample sales data (date and sales quantity)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Sales': np.random.randint(0, 10, size=365)
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Calculate the rolling mean and standard deviation for sales
rolling_mean = df['Sales'].rolling(window=7).mean()
rolling_std = df['Sales'].rolling(window=7).std()

# Plot the sales data and rolling statistics
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'], label='Daily Sales')
plt.plot(df['Date'], rolling_mean, label='7-Day Rolling Mean', color='orange')
plt.plot(df['Date'], rolling_std, label='7-Day Rolling Std Dev', color='red')
plt.title('Sales Analysis for Canned Mackerels')
plt.xlabel('Date')
plt.ylabel('Sales Quantity')
plt.legend()
plt.show()

# Use Holt-Winters Exponential Smoothing for forecasting
model = ExponentialSmoothing(df['Sales'], seasonal='add', seasonal_periods=7)
model_fit = model.fit()

# Forecast sales for the next 'n' days
n = 7
forecast = model_fit.forecast(steps=n)

# Determine when to restock based on the forecast
min_sales_threshold = 3  # Adjust as needed
restock_dates = []
for i in range(n):
    if forecast[i] < min_sales_threshold:
        restock_date = df['Date'].max() + pd.DateOffset(days=i+1)
        restock_dates.append(restock_date)

print("Recommended restocking dates:")
for date in restock_dates:
    print(date.strftime('%Y-%m-%d'))

# Calculate the recommended restocking quantity based on average sales
avg_sales = rolling_mean.dropna().mean()
min_restock_quantity = 10  # Adjust as needed
recommended_quantity = max(min_restock_quantity, round(avg_sales))

print(f"Recommended restocking quantity: {recommended_quantity} units")
