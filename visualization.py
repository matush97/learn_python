import matplotlib.pyplot as plt
import json

with open("api_json.json", "r") as file:
    data = json.load(file)


xpoints = []
for time in data["hourly"]["time"]:
    actual_time = time.split("T")[1]
    xpoints.append(actual_time)

ypoints = data["hourly"]["temperature_2m"]

plt.plot(xpoints, ypoints)


plt.xlim(0, 25)
plt.ylim(0, 50)

plt.show()