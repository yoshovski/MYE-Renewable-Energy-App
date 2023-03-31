import random
from datetime import datetime, timedelta

import os
import time

# Define the start and end dates for the dataset
start_date = datetime(2021, 1, 1, 0, 0, 0)
end_date = datetime(2021, 12, 31, 23, 59, 59)

# Define the range of possible temperatures and humidities
min_temp = 10
max_temp = 40
min_humidity = 20
max_humidity = 90

# Define the range of possible produced and consumed energy values
min_energy = 0
max_energy = 200

# Define the probability of adverse weather conditions occurring
adverse_weather_prob = 0.2

# Define the probability of construction work occurring
construction_work_prob = 0.1

# Define the probability of special events occurring
special_events_prob = 0.1

# Loop through each hour in the dataset and generate data
current_date = start_date

print('elaborating...wait a moment')

while current_date <= end_date:
    # Determine the time of day and day of week
    time_of_day = current_date.strftime('%H:%M:%S')
    day_of_week = current_date.weekday()

    # Determine if adverse weather conditions are present
    adverse_weather = random.random() < adverse_weather_prob

    # Determine if construction work is occurring
    construction_work = random.random() < construction_work_prob

    # Determine if special events are occurring
    special_events = random.random() < special_events_prob

    # Determine the produced energy value based on the time of day
    if current_date.hour >= 7 and current_date.hour <= 10:
        produced_energy = random.randint(min_energy, max_energy)
    elif current_date.hour >= 11 and current_date.hour <= 14:
        produced_energy = random.randint(max_energy, max_energy*2)
    elif current_date.hour >= 15 and current_date.hour <= 18:
        produced_energy = random.randint(min_energy, max_energy)
    else:
        produced_energy = 0

    if current_date.hour >= 19 or current_date.hour <= 6:
        produced_energy = 0

    if adverse_weather:
        produced_energy *= 0.5

    # Determine the consumed energy value based on the time of day and day of week
    if day_of_week >= 0 and day_of_week <= 4:
        if current_date.hour >= 6 and current_date.hour <= 8:
            consumed_energy = random.randint(max_energy, max_energy*2)
        elif current_date.hour >= 17 and current_date.hour <= 22:
            consumed_energy = random.randint(max_energy, max_energy*2)
        else:
            consumed_energy = random.randint(min_energy, max_energy)
    else:
        consumed_energy = random.randint(max_energy, max_energy*2)

    if day_of_week >= 5 and day_of_week <= 6:
        consumed_energy *= 1.5

    # Determine the temperature and humidity values
    temperature = random.randint(min_temp, max_temp)
    humidity = random.randint(min_humidity, max_humidity)

    # Print the data point as a comma-separated string
    outputData = '{:.1f},{:.1f},{:.1f},{:.1f},{},{},{},{},{},{}'
    fileName = 'DataGenerator/data.txt'


    filename = "data.txt"
    filelocation = f"DataGenerator/{filename}"

    if os.path.isfile(filename):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        newfilename = f"data_{timestamp}.txt"
        filelocation = f"DataGenerator/{newfilename}"
    

    # Save generated data from print in txt file, each generated data point is saved in a new line
    with open(filelocation, 'a') as f:
        f.write(outputData.format(
            produced_energy,
            consumed_energy,
            temperature,
            humidity,
            current_date.strftime('%Y-%m-%d'),
            time_of_day,
            day_of_week,
            adverse_weather,
            special_events,
            construction_work
        ))
        f.write('\n')

        

    # Move to the next hour
    current_date += timedelta(hours=1)

    # print done when program finished
    

if __name__ == "__main__":
    print("done")