import pandas as pd
import tensorflow as tf
import numpy as np
import shutil

graph_dir = "./graphs"
shutil.rmtree(graph_dir, ignore_errors=True)

adv = pd.read_csv('Advertising.csv')
tv_budget_x = adv.TV.tolist() / np.max(adv.TV.tolist())
sales_y = adv.Sales.tolist() / np.max(adv.Sales.tolist())

X = tf.placeholder("float32", name="X")
Y = tf.placeholder("float32", name = "Y")

with tf.name_scope("Model"):
    w = tf.Variable(0.0, name="b0", dtype="float32")
    b = tf.Variable(0.0, name="b1", dtype="float32")
    y_model = tf.add(tf.multiply(X, w), b)

with tf.name_scope("CostFunction"):
    cost = tf.pow(Y-y_model, 2, name="cost")/2

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

sess = tf.Session()
init = tf.global_variables_initializer()
cost_op = tf.summary.scalar("loss", cost)
w_op = tf.summary.histogram("weight", w)
cost_hist_op = tf.summary.histogram("loss_histo",cost)
merged = tf.summary.merge_all()
sess.run(init)
writer = tf.summary.FileWriter(graph_dir, sess.graph)
final_w = 0.0
final_b = 0.0
# for 200 iterations (epochs)
for i in range(200):
    # for 200 samples in data
    for (j, (x, y)) in enumerate(zip(tv_budget_x, sales_y)):
        feed_dict = {X:x, Y:y}
        summary, train = sess.run([merged, train_op], feed_dict=feed_dict)
        idx = (i * len(tv_budget_x)) + j
        # This writes to summary file 40,000 times. Tensorboard just reads summary file n converts to graphs n all.
        writer.add_summary(summary, idx)
    if (i+1) % 50 == 0:
        c = sess.run(cost, feed_dict={X:tv_budget_x, Y:sales_y})
        final_w = sess.run(w)
        final_b = sess.run(b)
        print("Epoch:", i, "W=", sess.run(w), "b=", sess.run(b))
