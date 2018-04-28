from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

FLAGS = None

def main(_):
	# Import data
	mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
	# Create the model
	# This is for data. Data would be any samples x 784. Correct.
	x = tf.placeholder(tf.float32, [None, 784])
	# y = tf.placeholder(tf.float32, [None, 10])
	y_actual = tf.placeholder(tf.float32, [None, 10])

	#todo - add a new hidden layer.
	# LEARNING - if you use tf.zeros - then it gives 10-20% accuracy only. :|  
	W1 = tf.Variable(tf.random_normal([784, 300], stddev=0.03), name="W1")
	b1 = tf.Variable(tf.random_normal([300]), name='b1')

	W2 = tf.Variable(tf.random_normal([300, 10], stddev=0.03), name="W2")
	b2 = tf.Variable(tf.random_normal([10]), name='b2')

	h1 = tf.add(tf.matmul(x,W1), b1)
	h1 = tf.nn.relu(h1)
	# h1 = tf.sigmoid(h1)

	y = tf.add(tf.matmul(h1,W2),b2)

	# Since only 0 hidden layer, you have input and output basically.
	# Which means only one weight value. One weight scalar. 

	# Define loss and optimizer


	#todo - change entropy function

	cross_entropy = tf.reduce_mean(
	  tf.nn.softmax_cross_entropy_with_logits(labels=y_actual, logits=y))
	train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

	sess = tf.InteractiveSession()
	tf.global_variables_initializer().run()
	# Train
	epoch_set = []
	cost_set = []
	for i in range(100):
		batch_xs, batch_ys = mnist.train.next_batch(100)
		_, cost = sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y_actual: batch_ys})
		epoch_set.append(i+1)
		cost_set.append(cost)
	print(epoch_set)
	print(cost_set)



	# Test trained model
	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_actual, 1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	print(sess.run(accuracy, feed_dict={x: mnist.test.images,
	                                  y_actual: mnist.test.labels}))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
	                  help='Directory for storing input data')
	FLAGS, unparsed = parser.parse_known_args()
	tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)