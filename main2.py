from scraper_files.korea_uni import korea_uni
import csv

def main():
    with open('faculty_data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL", "Personal Webpage"])

        writer.writerows(korea_uni())


if __name__ == "__main__":
    main()