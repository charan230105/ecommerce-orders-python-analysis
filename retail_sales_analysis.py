import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("olist_orders_dataset.csv")

# Convert date column to datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# -----------------------------
# 1. Orders per Month Analysis
# -----------------------------
monthly_orders = df.groupby(
    df['order_purchase_timestamp'].dt.to_period('M')
).size()

plt.figure(figsize=(10,5))
monthly_orders.plot()

plt.title("Orders per Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("monthly_orders.png")
plt.show()


# -----------------------------
# 2. Order Status Distribution
# -----------------------------
plt.figure(figsize=(8,5))

df['order_status'].value_counts().plot(
    kind='bar'
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("order_status.png")
plt.show()


# -----------------------------
# 3. Top 10 Order Status (Extra insight)
# -----------------------------
top_status = df['order_status'].value_counts().head(10)

plt.figure(figsize=(8,5))
top_status.plot(kind='bar')

plt.title("Top Order Status")
plt.xlabel("Status")
plt.ylabel("Orders")

plt.tight_layout()
plt.savefig("top_status.png")
plt.show()

print("Analysis completed successfully!")
