from scraper_files.hong_kong_poly_uni import hong_kong_poly_uni
import csv

def main():
    with open('faculty_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL", "Personal Webpage"])

        writer.writerows(hong_kong_poly_uni())


if __name__ == "__main__":
    main()