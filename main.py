import csv
import os
from analyzer import analyze_water
from validator import valid_ph, valid_date, valid_location
from report import generate_report
from statistics import calculate_statistics

FILE_NAME = "water_quality_samples.csv"

def read_records():
    records = []
    if not os.path.exists(FILE_NAME):
        return records
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records

def generate_id():
    records = read_records()
    if not records:
        return 1
    ids = []
    for record in records:
        try:
            ids.append(int(record["id"]))
        except (ValueError, KeyError):
            pass
    if not ids:
        return 1
    return max(ids) + 1
 

def water_test_report():
    print("\n")
    print("-" * 55)
    print("          WATER TEST REPORT GENERATOR")
    print("\n")
    print("-" * 55)

    while True:
        location = input("Enter Location: ")
        if valid_location(location):
            break
        print("Invalid location. Please enter a location.")

    while True:
        date = input("Enter Date (YYYY-MM-DD): ")
        if valid_date(date):
            break

        print("Invalid date format. Use YYYY-MM-DD.")

    while True:
        ph = input("Enter pH: ")
        if valid_ph(ph):
            break
        print("Invalid pH. Enter a value between 0 and 14.")

    parameters = [
        ("tds", "Enter TDS (mg/L): "),
        ("turbidity", "Enter Turbidity (NTU): "),
        ("hardness", "Enter Hardness (mg/L): "),
        ("nitrate", "Enter Nitrate (mg/L): "),
        ("sulphate", "Enter Sulphate (mg/L): "),
        ("chlorine", "Enter Chlorine (mg/L): "),
        ("temperature", "Enter Temperature (°C): ")
    ]

    values = {}

    for name, message in parameters:
        while True:
            value = input(message)

            try:
                number = float(value)

                if number >= 0:
                    values[name] = value
                    break
                else:
                    print("Value cannot be negative.")

            except ValueError:
                print("Please enter a valid number.")

    record = {
        "id": "TEST",
        "location": location,
        "date": date,
        "pH": ph,
        "tds": values["tds"],
        "turbidity": values["turbidity"],
        "hardness": values["hardness"],
        "nitrate": values["nitrate"],
        "sulphate": values["sulphate"],
        "chlorine": values["chlorine"],
        "temperature": values["temperature"]
    }

    score, status, problems = analyze_water(record)
    generate_report(record, score, status, problems)

def add_record():
    print("\n--- ADD WATER RECORD ---")
    while True:
        location = input("Enter Location: ")
        if valid_location(location):
            break
        print("Invalid location.")
    while True:
        date = input("Enter Date (YYYY-MM-DD): ")
        if valid_date(date):
            break
        print("Invalid date format.")
    while True:
        ph = input("Enter pH: ")
        if valid_ph(ph):
            break
        print("Invalid pH.")

    fields = [
        ("tds", "Enter TDS: "),
        ("turbidity", "Enter Turbidity: "),
        ("hardness", "Enter Hardness: "),
        ("nitrate", "Enter Nitrate: "),
        ("sulphate", "Enter Sulphate: "),
        ("chlorine", "Enter Chlorine: "),
        ("temperature", "Enter Temperature: ")
    ]

    values = {}

    for name, message in fields:
        while True:
            value = input(message)
            try:
                if float(value) >= 0:
                    values[name] = value
                    break
                else:
                    print("Value cannot be negative.")

            except ValueError:
                print("Please enter a valid number.")

    record = {
        "id": generate_id(),
        "location": location,
        "date": date,
        "pH": ph,
        "tds": values["tds"],
        "turbidity": values["turbidity"],
        "hardness": values["hardness"],
        "nitrate": values["nitrate"],
        "sulphate": values["sulphate"],
        "chlorine": values["chlorine"],
        "temperature": values["temperature"]
    }

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        fieldnames = ["id","location","date","pH","tds","turbidity","hardness","nitrate","sulphate","chlorine","temperature"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(record)

    print("\nRecord added successfully.")
    print("Record ID:", record["id"])

def view_records():
    records = read_records()

    if not records:
        print("\nNo records found.")
        return

    print("\n")
    print("=" * 100)
    print("                         WATER RECORDS")
    print("=" * 100)

    for record in records:
        print(
            "ID:", record["id"],
            "| Location:", record["location"],
            "| Date:", record["date"],
            "| pH:", record["pH"],
            "| TDS:", record["tds"],
            "| Turbidity:", record["turbidity"]
        )

    print("*" * 100)


def find_by_id(record_id):

    records = read_records()

    for record in records:

        if str(record["id"]) == str(record_id):
            return record

    return None



def search_by_location():

    location = input("\nEnter location to search: ").strip().lower()
    records = read_records()
    found = []

    for record in records:
        if location in record["location"].lower():
            found.append(record)
    if not found:
        print("No records found.")
        return
    print("\nMatching Records")
    print("-" * 70)

    for record in found:
        print(
            "ID:", record["id"],
            "| Location:", record["location"],
            "| Date:", record["date"],
            "| pH:", record["pH"]
        )


def analyze_record():
    record_id = input("\nEnter Record ID: ")
    record = find_by_id(record_id)
    if record is None:
        print("Record not found.")
        return
    score, status, problems = analyze_water(record)
    generate_report(record, score, status, problems)


def delete_record():
    record_id = input("\nEnter Record ID to delete: ")
    records = read_records()
    found = False
    for record in records:
        if str(record["id"]) == str(record_id):
            found = True
    if not found:
        print("Record not found.")
        return

    new_records = []

    for record in records:
        if str(record["id"]) != str(record_id):
            new_records.append(record)

    fieldnames = ["id","location","date","pH","tds","turbidity","hardness","nitrate","sulphate","chlorine","temperature"]

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(new_records)

    print("Record deleted successfully.")

while True:

    print("\n")
    print("=" * 40)
    print("       WATER QUALITY ANALYZER")
    print("=" * 40)

    print("1. Water Test Report Generator")
    print("2. Add Record")
    print("3. View Records")
    print("4. Search by Location")
    print("5. Analyze Record")
    print("6. Delete Record")
    print("7. Statistical Analysis")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        water_test_report()
    elif choice == "2":
        add_record()
    elif choice == "3":
        view_records()
    elif choice == "4":
        search_by_location()
    elif choice == "5":
        analyze_record()
    elif choice == "6":
        delete_record()
    elif choice == "7":
        records = read_records()
        calculate_statistics(records)
    elif choice == "8":
        print("\nThank you for using Water Quality Analyzer.")
    break