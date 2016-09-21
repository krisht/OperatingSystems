import sys; 
import os;
import time; 
import csv; 

out = [j for j in range(0,19)];

with open('result.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL);
	for jj in out:
		for kk in range(0, 5): 
			start = time.time(); 
			os.system("./copycat -b %d -o output.txt input1.txt input2.txt input3.txt input4.txt" % 2**jj)
			end = time.time(); 
			spamwriter.writerow([2**jj, jj ,  (end-start)]);  
