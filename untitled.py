import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load your dataset
data = pd.read_csv('city_day.csv')  
data.head()
data.info()
data.describe()
data.isnull().sum()
# Drop rows with missing AQI
data = data.dropna(subset=['AQI'])

# Convert date to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Fill missing pollutant values with mean
pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
for col in pollutants:
    data[col] = data[col].fillna(data[col].mean())
  plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='AQI', data=data[data['City']=='Delhi'])
plt.title('Delhi Air Quality Index Over Time')
plt.show()
plt.figure(figsize=(10,6))
top_cities = data.groupby('City')['AQI'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_cities.index, y=top_cities.values)
plt.xticks(rotation=45)
plt.title('Top 10 Most Polluted Cities')
plt.show()
data.to_csv('cleaned_air_quality.csv', index=False)
print("Cleaned dataset saved!")
