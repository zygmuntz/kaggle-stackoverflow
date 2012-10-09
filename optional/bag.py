'a script for averaging your [pretty good] solutions (in submission format) to get a better one'

# edit this:

input_files = [ "p_sub%s.csv" % ( x ) for x in range( 1, 6 ) ]
input_files.append( "p_sub_num.csv" )

output_file = "p_sub_bagged.csv"

print "%s ---> '%s'" % ( input_files, output_file )

###########################################################

import csv

num_files = len( input_files )

readers = {}
for i in range( num_files ):
	input = open( input_files[i] )
	readers[i] = csv.reader( input )

writer = csv.writer( open( output_file, 'wb' ))
reader_0 = readers[0]	
	
for line in reader_0:
	lines = [ line ] + [ readers[i].next() for i in range( 1, num_files ) ]
	#print lines
	
	post_id = line[0]
	new_line = [ post_id ]
	
	for column in range( 1, 6 ):		# columns in sub file
		votes = []
		for l in range( num_files ):	
			value = float( lines[l][column] )
			votes.append( value )
			
		prediction = sum( votes ) / num_files	
		new_line.append( prediction )
		
	writer.writerow( new_line )