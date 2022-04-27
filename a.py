
import pandas as pd
data = pd.read_csv("data.csv")

x=data.iloc[2:,:-1]
print(x)