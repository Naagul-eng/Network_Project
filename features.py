import pandas as pd

df = pd.read_csv('traffic.csv')

# Packets per second
df['second'] = df['time'].astype(int)
pps = df.groupby('second').size()

# Average packet size
avg_size = df.groupby('second')['length'].mean()

features = pd.DataFrame({
    'pps': pps,
    'avg_size': avg_size
}).fillna(0)

print(features.head())