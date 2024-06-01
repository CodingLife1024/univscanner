from redo.mit import mit
from redo.stanford import stanford
import csv

def main():
    with open('faculty_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL"])

        # Try calling mit() and writing its output to the CSV file
        try:
            mit_data = mit()
            writer.writerows(mit_data)
        except Exception as e:
            print("Error occurred while fetching and writing MIT data:", e)

        # Try calling stanford() and writing its output to the CSV file
        try:
            stanford_data = stanford()
            writer.writerows(stanford_data)
        except Exception as e:
            print("Error occurred while fetching and writing Stanford data:", e)

if __name__ == "__main__":
    main()
