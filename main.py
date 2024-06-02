from redo.mit import mit
from redo.stanford import stanford
from redo.harvard import harvard

from redo.oxford import oxford
import csv

def main():
    with open('faculty_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University", "Country", "Name", "Email", "URL", "Personal Webpage"])

        writer.writerows(mit())

        writer.writerows(stanford())

        writer.writerows(harvard())

        writer.writerows(oxford())

if __name__ == "__main__":
    main()
