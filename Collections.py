import json
import csv
import os
from typing import List, Dict, Any


def read(json_file: str) -> List[Dict[str, Any]]:
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"The file does not exist.")
    with open(json_file, 'r') as f:
        users = json.load(f)
    return users


def filters(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        user for user in users
        if (user.get('phoneNumber', '').startswith('+1') or
            user.get('phoneNumber', '').startswith('1')) and
        '4.0 Safari' in user.get('userAgent', '')
    ]


def write(filtered_users: List[Dict[str, Any]], csv_file: str) -> None:
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Address', 'Email'])
        for user in filtered_users:
            writer.writerow([
                user.get('name'),
                user.get('address'),
                user.get('email')
            ])


def main(json_file: str, csv_file: str) -> None:
    try:
        users = read(json_file)
        filtered_users = filters(users)
        write(filtered_users, csv_file)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main('in.json', 'output.csv')
