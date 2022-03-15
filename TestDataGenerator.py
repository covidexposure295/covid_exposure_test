import random
from datetime import datetime, timedelta
from faker import Faker
import csv

fake = Faker()

location_num = 100
population = 2000
record_num = population
status_num = 50

email = []
for i in range(population):
    email.append(fake.email(True, 'outlook.com'))

def generate_location():
    print("Generate Location: county, latitude, longitude, name, state, type, zipcode")

    fields = ["county", "latitude", "longitude", "name", "state", "type", "zipcode"]

    low_latitude = 33.545
    high_latitude = 33.756
    left_longitude = -118.107
    right_longitude = -117.775

    with open('location.csv', 'w', newline='') as statusFile:
        writer = csv.writer(statusFile, delimiter=',')
        writer.writerow(fields)
        for i in range(location_num):
            latitude = random.random() * (high_latitude - low_latitude) + low_latitude
            longitude = random.random() * (right_longitude - left_longitude) + right_longitude

            location = ["", latitude, longitude, "", "CA", "", ""]

            writer.writerow(location)

    print("Generate Location Done!")

def generate_record():
    print("Generate Record: email, locationId, timestamp")

    fields = ["email", "location", "timestamp"]

    with open('record.csv', 'w', newline='') as statusFile:
        writer = csv.writer(statusFile, delimiter=',')
        writer.writerow(fields)

        end_time = datetime.now()
        start_time = end_time - timedelta(days=50)

        for i in range(int(population / 2)):
            times = random.randrange(1, 3)
            for _ in range(times):
                record = [email[i], random.randrange(1, location_num + 1), fake.unix_time(end_time, start_time) * 1000]
                writer.writerow(record)

    print("Generate Record Done!")


def generate_status_exist():
    print("Generate Status Visitor Exist: email, status, timestamp")

    fields = ['email', 'status', 'timestamp']

    end_time = datetime.now()
    start_time = end_time - timedelta(days=3)

    with open('status_visitor_exist.csv', 'w', newline='') as statusFile:
        writer = csv.writer(statusFile, delimiter=',')
        writer.writerow(fields)
        for i in range(status_num):
            status = [email[i], 'ACTIVE', fake.unix_time(end_time, start_time) * 1000]
            writer.writerow(status)

    print("Generate Status Exist Visitor Done!")

def generate_status_not_exist():
    print("Generate Status Visitor Not Exist: email, status, timestamp")

    fields = ['email', 'status', 'timestamp']

    end_time = datetime.now()
    start_time = end_time - timedelta(days=3)

    with open('status_visitor_not_exist.csv', 'w', newline='') as statusFile:
        writer = csv.writer(statusFile, delimiter=',')
        writer.writerow(fields)
        for i in range(int(population / 2) + 1, int(population / 2) + status_num):
            status = [email[i], 'ACTIVE', fake.unix_time(end_time, start_time) * 1000]
            writer.writerow(status)

    print("Generate Status Not Exist Visitor Done!")

if __name__ == '__main__':
    generate_location()
    generate_record()
    generate_status_exist()
    generate_status_not_exist()
