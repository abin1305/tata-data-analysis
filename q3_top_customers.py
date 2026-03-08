import matplotlib.pyplot as plt
from cleaning import load_and_clean_data, OUTPUT_DIR

df = load_and_clean_data()
top_customers = (
    df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_customers.plot(kind="bar")
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue (£)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "Q3_top10_customers.png", dpi=300)
plt.close()

print("✅ Q3 visual saved: Q3_top10_customers.png")
