import matplotlib.pyplot as plt
from cleaning import load_and_clean_data, OUTPUT_DIR

df = load_and_clean_data()
df_2011 = df[df["InvoiceDate"].dt.year == 2011]
monthly_revenue = df_2011.set_index("InvoiceDate").resample("M")["Revenue"].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
plt.title("Monthly Revenue in 2011")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "Q1_revenue_2011.png", dpi=300)
plt.close()

print("✅ Q1 visual saved: Q1_revenue_2011.png")

