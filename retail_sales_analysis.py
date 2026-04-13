import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("olist_orders_dataset.csv")

# convert date
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# monthly orders
monthly_orders = df.groupby(df['order_purchase_timestamp'].dt.to_period('M')).size()

# plot
plt.figure(figsize=(10,5))
monthly_orders.plot()
plt.title("Orders per Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_orders.png")
plt.show()

# order status
plt.figure(figsize=(8,5))
df['order_status'].value_counts().plot(kind='bar')
plt.title("Order Status Distribution")
plt.tight_layout()
plt.savefig("order_status.png")
plt.show()

print("Analysis completed!")