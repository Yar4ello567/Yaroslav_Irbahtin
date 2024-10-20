import json
import csv

def read(json_file):
    with open(json_file, 'r') as f:
        users = json.load(f)
    return users

def filters(users):
    return [
        user for user in users
        if (user.get('phoneNumber', '').startswith('+1')
        or user.get('phoneNumber', '').startswith('1'))
        and '4.0 Safari' in user.get('userAgent', '')
    ]

def write(filtered_users, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Address', 'Email'])
        for user in filtered_users:
            writer.writerow([user.get('name'), user.get('address'), user.get('email')])

def main(json_file, csv_file):
    users = read(json_file)
    filtered_users = filters(users)
    write(filtered_users, csv_file)

main('in.json', 'output.csv')
