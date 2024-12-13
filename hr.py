import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://api.ouraring.com/v2/usercollection/sleep' 
params={ 
    'start_date': '2023-10-01', 
    'end_date': '2024-12-03' 
}
headers = { 
  'Authorization': 'Bearer 5CPZI5TMFUQMH5G7ZW5Y624ESQ4YEOZX' 
}
response = requests.request('GET', url, headers=headers, params=params) 
# print(response.text)


data = json.loads(response.text)
# print(data)
# print(data['data'][0])
data = data['data']
# print(data)

# print(data[0])
days = []
hrv = []
body_temps = []

for day_data in data:
    day = day_data['day']
    hrv_balance = day_data['heart_rate']
    # body_temp = day_data['contributors']['body_temperature']
    days.append(day)
    hrv.append(hrv_balance)
    # body_temps.append(body_temp)

print(hrv[0]['items'])
plt.plot(hrv[0]['items'])
plt.plot(hrv[10]['items'])
plt.show()
# df = pd.DataFrame({'day': days, 'hrv_balance': hrv})
# print(df)

# # plt.plot(df['day'], df['hrv_balance'])
# plt.plot(df['day'], df['body_temp'])

# # dont show all the dates
# plt.xticks(np.arange(0, len(df['day']), step=30))
# plt.xticks(rotation=45)

# plt.show()
# # df = pd.DataFrame(data['daily_readiness'])