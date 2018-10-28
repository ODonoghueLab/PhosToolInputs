#!/usr/bin/python
import sys

# change the following three lines if different 
uniprot_resSite = 1  
peptideId = 3
tp_start = 4


# conver the data. 
def convertToReqFormat(fn_phosphoInput):

	print ("Id\tRatio")
	with open(fn_phosphoInput, 'r') as fh_:
		for line in fh_:

			line = line.strip()

			arr = line.split("\t") # split line. 

			line_out = arr[uniprot_resSite] + "-" + arr[peptideId] 

			counter_tp = 1
			for i in range (tp_start, len(arr)): # the time series part.
				print (line_out  + "-" + str(counter_tp) + "\t" + arr[i])
				counter_tp = counter_tp + 1



def main():

	usage = "python3 script.py <datasetWithTpVals.phos>"

	if len(sys.argv) != 2:
		sys.stderr.write("Error: incorrect number of inputs.\n" + usage +'\n\n')
		sys.exit()


	convertToReqFormat(sys.argv[1])


if __name__ == '__main__':
	main()
