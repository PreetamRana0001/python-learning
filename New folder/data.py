# 📊 Sales Data Analysis Project
# Author: Preetam Rana

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
data = {
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05',
             '2025-01-06', '2025-01-07', '2025-01-08', '2025-01-09', '2025-01-10'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Units_Sold': [10, 5, 12, 8, 9, 11, 4, 13, 6, 15],
    'Price_per_Unit': [100, 150, 100, 200, 150, 100, 200, 150, 100, 200]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# Step 2: Add new column (Total Sales)
# -----------------------------
df['Total_Sales'] = df['Units_Sold'] * df['Price_per_Unit']

print("✅ Dataset Preview:")
print(df.head())

# -----------------------------
# Step 3: Summary Statistics
# -----------------------------
print("\n📈 Summary Statistics:")
print(df.describe())

# -----------------------------
# Step 4: Total & Average Sales
# -----------------------------
total_sales = df['Total_Sales'].sum()
avg_sales = df['Total_Sales'].mean()
print(f"\n💰 Total Sales: ₹{total_sales}")
print(f"📊 Average Sales per Day: ₹{round(avg_sales, 2)}")

# -----------------------------
# Step 5: Best-selling Product
# -----------------------------
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
print(f"🏆 Best-Selling Product: {best_product}")

# -----------------------------
# Step 6: Visualization
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Total_Sales'], marker='o', color='teal')
plt.title("Daily Sales Trend", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Total Sales (₹)")
plt.grid(True)
plt.show()

# -----------------------------
# Step 7: Product-wise Sales Chart
# -----------------------------
sales_by_product = df.groupby('Product')['Total_Sales'].sum()
sales_by_product.plot(kind='bar', color=['orange', 'green', 'blue'])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (₹)")
plt.show()
