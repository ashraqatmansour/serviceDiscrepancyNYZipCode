import csv
from collections import defaultdict
from datetime import datetime
import pickle  # to save processed data

# Dictionary: {zipcode: {month: [response_times]}}
response_times = defaultdict(lambda: defaultdict(list))
all_response_times = defaultdict(list)

with open("../data/cleaned.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            created = datetime.strptime(row["Created Date"], "%m/%d/%Y %I:%M:%S %p")
            closed = datetime.strptime(row["Closed Date"], "%m/%d/%Y %I:%M:%S %p")
   
        except:
            continue  # skip rows with bad dates

        if closed < created:
            continue  # skip negative response times

        zipcode = row["Incident Zip"]
        if not zipcode:
            continue  # skip missing zipcodes

        # Response time in hours
        hours = (closed - created).total_seconds() / 3600
        month = closed.strftime("%Y-%m")  # e.g., "2024-01"

        response_times[zipcode][month].append(hours)
        all_response_times[month].append(hours)

# Compute averages
avg_times = defaultdict(dict)
for zipc, months in response_times.items():
    for month, times in months.items():
        avg_times[zipc][month] = sum(times) / len(times)

avg_times["ALL"] = {month: sum(times)/len(times) for month, times in all_response_times.items()}

# Save preprocessed data
with open("monthly_avg.pkl", "wb") as f:
    pickle.dump(avg_times, f)
