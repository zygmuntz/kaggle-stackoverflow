'train, predict and output predictions in submission format'

train_file = 'train.vw'
test_file = 'test.vw'

model_file = 'model'
r_file = 'raw_predictions.txt'
p_file = 'p.txt'

import os

cmd = 'vw --loss_function logistic --oaa 5 -d %s -f %s' % ( train_file, model_file )
print cmd
os.system( cmd ) 

cmd = 'vw --loss_function logistic --oaa 5 -i %s -t -d %s -r %s' % ( model_file, test_file, r_file )
print cmd
os.system( cmd ) 	

cmd = 'python sigmoid_mc.py %s %s' % ( r_file, p_file )
print cmd
os.system( cmd ) 	

