from scraper_files.national_taiwan_university import national_taiwan_university
import csv

def main():
    with open('faculty_data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL", "Personal Webpage"])
        
        writer.writerows(national_taiwan_university())


if __name__ == "__main__":
    main()