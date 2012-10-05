'compute multiclass log loss from test file in CSV format (pre-processed) and predictions file'

import sys, csv
from math import log

statuses = ['not a real question', 'not constructive', 'off topic', 'open', 'too localized']

test_file = sys.argv[1]
predictions_file = sys.argv[2]

test_reader = csv.reader( open( test_file ))
p_reader = csv.reader( open( predictions_file ))

logs = []
n = 0

for p_line in p_reader:
	test_line = test_reader.next()
	p_line.pop( 0 )		# get rid of post id
	
	n += 1
	
	status = test_line[1]
	true_index = statuses.index( status )
	
	prediction_for_true = p_line[true_index]
	# print prediction_for_true
	
	log_p = log( float( prediction_for_true ))
	logs.append( log_p )
	
logs = sum( logs )
logloss = - logs / n * 1.0

print "%s %s" % ( test_file, predictions_file )
print logloss
print