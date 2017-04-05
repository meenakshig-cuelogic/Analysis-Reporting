import csv
from operator import itemgetter
def csv_file_reader(uploaded_file):
	main_list=[]
	final_list=[]
	with open(uploaded_file,'rb') as f:
		reader = csv.reader(f, delimiter=',')
		headers=reader.next()
		for column  in reader:
			main_list.append(list(column))
			final_list=sorted(main_list,key=itemgetter(0))
        return final_list

def csv_file_header(uploaded_file):
	with open(uploaded_file,'rb') as f:
		reader = csv.reader(f, delimiter=',')
		headers=reader.next()
	return headers	
  			
  			