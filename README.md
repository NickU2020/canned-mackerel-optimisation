# mackerel-optimise
Mackerel Sales and Restocking Optimisation

Analysing sales data and optimising restocking for a product like canned mackerels can be achieved through data analysis and forecasting techniques. Here's a Python program that can help you analyse sales data and make restocking recommendations.

[see main.py]

In this program:

    We create sample sales data for canned mackerels using random values.
    We calculate and plot rolling statistics (7-day rolling mean and standard deviation) to visualise sales trends.
    We use the Holt-Winters Exponential Smoothing method to forecast sales for the next 'n' days.
    We determine recommended restocking dates based on the forecast and a minimum sales threshold.
    We calculate the recommended restocking quantity based on the average sales and a minimum restocking quantity.

You can replace the sample data with your actual sales data to get more accurate recommendations. Adjust the parameters like the rolling window size, minimum sales threshold, and minimum restocking quantity to suit your specific needs.

