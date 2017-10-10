import tensorflow as tf
import pandas as pd
import numpy as np
import math

def encode(a, l):
    b = np.zeros((len(a), l))
    b[np.arange(len(a)), a] = 1
    return b

def decode(b):
    a = np.argmax(b, axis=1)
    return a




def next_batch(num, data, labels):
    idx = np.arange(0 , len(data))
    np.random.shuffle(idx)
    idx = idx[:num]
    data_shuffle = [data[ i] for i in idx]
    labels_shuffle = [labels[ i] for i in idx]
    return np.asarray(data_shuffle), np.asarray(labels_shuffle)

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={train_inputs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={train_inputs: v_xs, train_labels: v_ys})
    return result


train_data = pd.read_csv("Z:\\P.AI\\Model\\features.csv")
dic = pd.read_csv("Z:\\P.AI\\Model\\dictionary.csv")
dic_d = pd.read_csv("Z:\\P.AI\\Model\\dictionary_disease.csv")


train_feature = np.array(train_data.input.astype(int)).reshape([-1,1])
train_label =  np.array(train_data.output.astype(int)).reshape([-1,1])




batch_size = 128
vocabulary_size = len(dic)
embedding_size = 200
output_size = len(dic_d)
num_sampled = 64

sess = tf.InteractiveSession()


train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
nce_weights = tf.Variable(tf.truncated_normal([output_size, embedding_size], stddev=1.0 / math.sqrt(embedding_size)))
nce_biases = tf.Variable(tf.zeros([output_size]))

embed = tf.nn.embedding_lookup(embeddings, train_inputs)


loss = tf.reduce_mean(
  tf.nn.nce_loss(weights=nce_weights,
                 biases=nce_biases,
                 labels=train_labels,
                 inputs=embed,
                 num_sampled=num_sampled,
                 num_classes=output_size))

prediction = tf.nn.softmax(tf.matmul(embed, tf.transpose(nce_weights)) + nce_biases)


optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)


sess.run(tf.global_variables_initializer())


for i in range(50000):
    batch_inputs, batch_labels = next_batch(batch_size, train_feature, train_label)
    feed_dict = {train_inputs: batch_inputs[:,0], train_labels: batch_labels}
    _, loss_val = sess.run([optimizer, loss], feed_dict=feed_dict)
    if i % 100 == 0: print("Step %d, In sample accuracy is %f" % (i, loss_val))



txt = [3281,2004,2623,897,910,3784,3825,5122,8076]
pre = tf.nn.softmax(tf.matmul(tf.reshape(tf.reduce_mean(tf.nn.embedding_lookup(embeddings,txt), 0), [1,200]), tf.transpose(nce_weights)) + nce_biases).eval()
result = sorted(zip(pre[0], range(len(pre[0]))),reverse = True)


pro = [x[0] for x in result[:5]]
pro = [x/sum(pro) * 100 for x in pro]
dis = [number2disease[x[1]] for x in result[:5]]
for i in range(5):
    if i ==0: print("##User Input: My cat has been fighting and got a cut ear that has been bleeding his over grommed it and now has hair loss and bleeding slightly\n")
    print("%i: Disease: %s , Probability: %f percentage\n" % ((i+1, dis[i], pro[i])))

