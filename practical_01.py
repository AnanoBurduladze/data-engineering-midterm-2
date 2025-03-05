import pandas as pd

df = pd.read_csv("data.csv")

filtered_df = df[df["value"] > 50]

grouped_df = filtered_df.groupby("category", as_index=False)["value"].mean()


filtered_df.to_csv("filtered_data.csv", index=False)
grouped_df.to_csv("grouped_data.csv", index=False)




