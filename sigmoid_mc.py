'read vw raw predictions file, compute and normalize probabilities, write in submission format'

import sys, csv, math

def sigmoid(x):
	return 1 / (1 + math.exp(-x))
  
def normalize( predictions ):
	s = sum( predictions )
	normalized = []
	for p in predictions:
		normalized.append( p / s )
	return normalized  
  
###  
  
input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

reader = csv.reader( i, delimiter = " " )
writer = csv.writer( o )

for line in reader:
	
	post_id = reader.next()[1]
	
	probs = []
	for element in line:
		prediction = element.split( ":" )[1]
		prob = sigmoid( float( prediction ))
		probs.append( prob )
	
	new_line = normalize( probs )
	
	writer.writerow( [post_id] + new_line )