'pre-process a CSV file'

import sys, csv, re

input_file = sys.argv[1]
output_file = sys.argv[2]

def get_words( text ):
	text = text.replace( "'", "" )
	text = re.sub( r'\W+', ' ', text )
	text = text.lower()
	
	text = text.split()
	words = []
	for w in text:
		if w in words:
			continue
		words.append( w )
		
	words = " ".join( words )
	return words

def prepare_tag( tag ):
	tag = re.sub( r'\W+', '', tag )
	tag = tag.lower()
	return tag
	
def get_unique_tags( tags ):
	unique_tags = []
	for tag in tags:
		if tag in unique_tags:
			unique_tags.append( '' )
		else:
			unique_tags.append( tag )
	return unique_tags

reader = csv.reader( open( input_file ))
writer = csv.writer( open( output_file, 'wb' ))

headers = reader.next()

counter = 0
for line in reader:

	post_id = line[0]
	try:
		post_status = line[14]
	except IndexError:
		post_status = 0
	
	reputation = line[4]
	good_posts = line[5]
	
	post_title = get_words( line[6] )
	post_body = get_words( line[7] )
	tags = line[8:13]
	tags = map( prepare_tag, tags )
	
	unique_tags = get_unique_tags( tags )

	
	writer.writerow( [ post_id, post_status, reputation, good_posts, post_title] + unique_tags + [ post_body ] )
	
	counter += 1
	if counter % 10000 == 0:
		print counter
