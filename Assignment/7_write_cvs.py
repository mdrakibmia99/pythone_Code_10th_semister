from prettytable import PrettyTable
from prettytable import from_csv

file_path = "student_record.csv"
csv_file = open(file_path)
data = from_csv(csv_file)
print(data)