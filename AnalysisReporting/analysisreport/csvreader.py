import csv
def csv_file_reader(uploaded_file):
	with open(uploaded_file,'rb') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			my_list=list(row);
	return my_list	

                
