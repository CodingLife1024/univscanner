from scraper_files.carnegie_mellon import carnegie_mellon
import csv

def main():
    with open('faculty_data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL", "Personal Webpage"])

        writer.writerows(carnegie_mellon())


if __name__ == "__main__":
    main()