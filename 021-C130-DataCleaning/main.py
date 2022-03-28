import pandas

df = pandas.read_csv("merged.csv")
df = df.dropna()
df = df.drop_duplicates()

del df["luminosity"]
del df["distance"]
del df["mass"]
del df["radius"]

df.rename(columns={"distance_ly": "distance", })

df.to_csv("merged_cleaned.csv", index=False)
