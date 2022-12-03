from prettytable import PrettyTable
from prettytable import from_csv
import csv
csv_rowlist = [["Name", "ID", "Admission Year"], 
               ["Md Rakib Mia", 1935202029, 2019],
               ["Joya Sarker", 1935202083, 2019],
               ["Rayhan Khan Durjoy", 1935202002, 2019],
               ["Hasna Hena", 1935202053, 2019],
               ["Laish Islam", 1935202043,2019],
               ["Sabbir", 1935202073,2019],
               ["Sadia Khanom", 19352020401,2019],
               ["Miraj", 1935202019,2019],
               ["Maruf", 1935202028,2019],
               ["Sayem",1935202018,2019]
               ]
with open('student_Info.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)

# file_path = "student_Info.csv"
# csv_file = open(file_path)
# data = from_csv(csv_file)
# print(data)