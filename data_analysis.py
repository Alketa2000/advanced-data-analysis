
import pandas as pd
import matplotlib.pyplot as plt
print("FILE I RI PO EKZEKUTOHET")
df = pd.read_csv("data.csv")

#Konverto date ne datetime
df["date"]=pd.to_datetime(df["date"])

#Krijo kolone per muaj
df["month"]=df["date"].dt.month


print("DATASET:")
print(df)

# KPI
total = df["amount"].sum()
avg = df["amount"].mean()
transactions=len(df)


print("\n---KPI ---")
print("Total:",total)
print("Mesatarja:", avg)
print("Nr. Transaksioneve:", transactions)


#Analize sipas kategorive
category_sum = df.groupby("category")["amount"].sum().sort_values(ascending=False)

print("\n---SIPAS KATEGORIVE---")
print(category_sum.to_string())

#Analize mujore
monthly=df.groupby("month")["amount"].sum()
print("\n--- SIPAS MUAJIT ---")
print(monthly.to_string())
#Krahasim muajsh(ndryshimi)
monthly_change=monthly.diff()
print("\n--- NDRYSHIMI MUJOR ---")
print(monthly_change.to_string())


# Grafik kategori
category_sum.plot(kind="bar", title="Shpenzime sipas kategorive")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()


#Grafik trend mujor
monthly.plot(kind="line", marker="o",title="Trend mujor")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

