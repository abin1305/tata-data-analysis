import matplotlib.pyplot as plt
from cleaning import load_and_clean_data, OUTPUT_DIR

df = load_and_clean_data()
non_uk_df = df[df["Country"] != "United Kingdom"]

top_countries = (
    non_uk_df.groupby("Country")
    .agg(Revenue=("Revenue", "sum"), Quantity=("Quantity", "sum"))
    .sort_values("Revenue", ascending=False)
    .head(10)
)

ax = top_countries.plot(kind="bar", y="Revenue", figsize=(12, 6), legend=False)
ax.set_title("Top 10 Countries by Revenue (Excl. UK)")
ax.set_ylabel("Revenue (£)")
ax.set_xlabel("Country")

# Add Quantity as data labels
for bar, qty in zip(ax.patches, top_countries["Quantity"]):
    ax.annotate(f"{int(qty)}", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "Q2_top10_countries.png", dpi=300)
plt.close()

print("✅ Q2 visual saved: Q2_top10_countries.png")
