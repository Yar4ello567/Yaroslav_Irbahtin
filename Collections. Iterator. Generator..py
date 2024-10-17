import json
import csv

def filter_users(json_file, csv_file):
    with open(json_file, 'r') as f:
        users = json.load(f)

    users_from_usa_with_safari = (
        user for user in users
        if (user.get('phoneNumber', '').startswith('+1') or user.get('phoneNumber', '').startswith('1'))
           and '4.0 Safari' in user.get('userAgent', '')
    )

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)

        for user in users_from_usa_with_safari:
            writer.writerow([user.get('name'), user.get('address'), user.get('email')])

filter_users('in.json', 'output.csv')