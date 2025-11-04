💳 Financial Transactions Data Analysis (Python)
📘 Project Overview

This project performs exploratory data analysis (EDA) on a financial transactions dataset.
The goal is to uncover insights about spending patterns, transaction volumes, merchant performance, and regional trends using Python, Pandas, Matplotlib, and Seaborn.

The dataset contains transaction records including client IDs, card usage, transaction amounts, merchant details, and timestamps.
Through this analysis, we visualize how financial activity varies across states, months, and times of the day.

🧰 Technologies & Tools

Python 3.x

Pandas – data cleaning and manipulation

Matplotlib – static visualizations

Seaborn – statistical data visualization

Jupyter Notebook / VS Code – for running and documenting the analysis

📂 Dataset

File name: transactions.csv

Columns include:

id — Transaction ID

date — Date and time of transaction

client_id — Unique identifier for the client

card_id — Card number used

amount — Transaction amount ($)

merchant_city, merchant_state — Merchant’s location

mcc — Merchant Category Code

use_chip — Type of transaction (e.g., Swipe, Chip, Online)

errors — Any reported transaction errors

🧮 Key Steps in the Analysis

Data Cleaning

Removed $ symbols and converted amount to numeric

Handled missing values and date formatting

Extracted Year, Month, and Hour for time-based insights

Exploratory Data Analysis

Transaction trends by state, month, and hour

Average transaction values by merchant region

Identification of the most active and high-spending states

Visualizations

Top 10 merchant states by transaction count

Average transaction amount per state

Monthly total transaction values

Hourly transaction trends

Insights

Which regions and months are most financially active

How average spending varies by time of day

General patterns of card usage

📊 Sample Visuals

🗺️ Top 10 Merchant States by Transactions

💵 Average Transaction Amount by State

📆 Monthly Transaction Value Trend

⏰ Hourly Average Transaction Value

📈 Results Summary

Identified the most active merchant state based on transaction volume.

Found the state with highest total spending using aggregate transaction values.

Calculated key metrics: total transactions, total value, and average transaction amount.
