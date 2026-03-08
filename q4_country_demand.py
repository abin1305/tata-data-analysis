import matplotlib.pyplot as plt
from cleaning import load_and_clean_data, OUTPUT_DIR

df = load_and_clean_data()
non_uk = df[df["Country"] != "United Kingdom"]

country_demand = (
    non_uk.groupby("Country")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(16, 7))
country_demand.plot(kind="bar")
plt.title("Demand by Country (Quantity, Excl. UK)")
plt.xlabel("Country")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "Q4_demand_by_country.png", dpi=300)
plt.close()

print("✅ Q4 visual saved: Q4_demand_by_country.png")
