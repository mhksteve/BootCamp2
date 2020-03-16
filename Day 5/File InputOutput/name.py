import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('save_names.csv', 'w') as new_file:
		fieldnames = ['first_name', ' ', 'last_name']

		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)

# Create_name.csv (original file name)
# save_names.csv (new save file)
# ID in front
# excel with header
# separate beween first name and last name
# within the new excel file, ID first_name and last name must be included
