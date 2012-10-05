'convert from CSV to VW format'

import sys, csv, re

def get_label( status ):
	statuses = ['not a real question', 'not constructive', 'off topic', 'open', 'too localized']
	label = statuses.index( status ) + 1
	return label

input_file = sys.argv[1]
output_file = sys.argv[2]

reader = csv.reader( open( input_file ))
o = open( output_file, 'wb' )

counter = 0	
for line in reader:

	counter += 1

	post_id = line[0]
	status = line[1]
	reputation = line[2]
	good_posts = line[3]
	words = line[4]
	tags = line[5:10]
	tags = " ".join( tags ).strip()
	
	body = line[10]
	
	if status != '0':
		label = get_label( status )	
	else:
		label = status		# test set
		
	output_line = "%s %s %s" % ( label, 1, post_id ) 	# weight is 1
	output_line += "|n %s %s" % ( reputation, good_posts )
	output_line += "|w %s |t %s |b %s" % ( words, tags, body )
	output_line += "\n"

	o.write( output_line )

	if counter % 100000 == 0:
		print counter