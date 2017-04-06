import csv
from operator import itemgetter
def csv_file_reader(uploaded_file):
	main_list=[]
	final_list=[]
	with open(uploaded_file,'rb') as f:
		reader = csv.reader(f, delimiter=',')
		headers=reader.next()
		for row in reader:
			row[0] = int(row[0])
			main_list.append(list(row))
			final_list=sorted(main_list,key=itemgetter(0))
        return final_list

def csv_file_header(uploaded_file):
	with open(uploaded_file,'rb') as f:
		reader = csv.reader(f, delimiter=',')
		headers=reader.next()
	return headers	

def csv_header_content(uploaded_file):
	main_list=[]
	save_list=[]
	with open(uploaded_file,'rb') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			
			main_list.append(list(row))
			save_list=sorted(main_list,key=itemgetter(0))
        return save_list
  			