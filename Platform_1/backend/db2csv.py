import csv
import sqlite3  # or other database library

# Database connection details
db_path = '.\\backend\\instance\\mydatabase.db'
table_name = 'contact'
csv_file_path = 'output.csv'

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Execute the query
cursor.execute(f'SELECT * FROM {table_name}')
rows = cursor.fetchall()

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header row (optional)
    column_names = [description[0] for description in cursor.description]
    writer.writerow(column_names)

    # Write data rows
    writer.writerows(rows)

# Close the connection
conn.close()

# rows = cursor.fetchall()
# fp = open(csv_file_path, 'w')
# myFile = csv.writer(fp)
# myFile.writerows(rows)
# fp.close()