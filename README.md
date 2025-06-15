import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = 'your_api_key_here'
CITY = 'Delhi'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Extract temperature and time data
temperatures = []
times = []

for forecast in data['list'][:10]:  # Get next 10 data points
    temperatures.append(forecast['main']['temp'])
    times.append(forecast['dt_txt'])

# Plot using seaborn
plt.figure(figsize=(10, 5))
sns.lineplot(x=times, y=temperatures, marker='o', color='teal')
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
