# coding: utf-8
import math
import numpy as np
import h5py
import sklearn.metrics
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.framework import ops
from tf_utils import load_dataset, random_mini_batches, convert_to_one_hot, predict

#np.random.seed(1)

# Loading the dataset
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()


# Change the index below and run the cell to visualize some examples in the dataset.

# Example of a picture
#index = np.random.randint(0, X_train_orig.shape[1])
#plt.imshow(X_train_orig[index])
#plt.show()
#print ("y = " + str(np.squeeze(Y_train_orig[:, index])))


# As usual you flatten the image dataset, then normalize it by dividing by 255. On top of that, you will convert each label to a one-hot vector as shown in Figure 1. Run the cell below to do so.

# Flatten the training and test images
X_train_flatten = X_train_orig.reshape(X_train_orig.shape[0], -1).T
X_test_flatten = X_test_orig.reshape(X_test_orig.shape[0], -1).T
# Normalize image vectors
X_train = X_train_flatten/255.
X_test = X_test_flatten/255.
# Convert training and test labels to one hot matrices
Y_train = convert_to_one_hot(Y_train_orig, 6)
Y_test = convert_to_one_hot(Y_test_orig, 6)

print ("number of training examples = " + str(X_train.shape[1]))
print ("number of test examples = " + str(X_test.shape[1]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))


def create_placeholders(n_x, n_y):
    print(n_x,n_y)
    X = tf.placeholder(tf.float32, [n_x, None])
    Y = tf.placeholder(tf.float32, [n_y, None])

    return X, Y

def initialize_parameters(layers_dims):

    parameters = {}
    L = len(layers_dims) # number of layers in the network

    for l in range(1, L):
        parameters["W" + str(l)] = tf.get_variable("W" + str(l), [layers_dims[l],layers_dims[l-1]], initializer = tf.contrib.layers.xavier_initializer(seed = 1))
        parameters["b" + str(l)] = tf.get_variable("b" + str(l), [layers_dims[l], 1], initializer = tf.zeros_initializer())

    return parameters

def forward_propagation(X, parameters):

    A = X
    L = len(parameters) // 2                  # number of layers in the neural network
    for l in range(1, L):
        A_prev = A
        A = tf.nn.relu(tf.add(tf.matmul(parameters['W' + str(l)], A_prev), parameters['b' + str(l)]))

    ZL = tf.add(tf.matmul(parameters['W' + str(L)], A), parameters['b' + str(L)])

    return ZL

def compute_cost(ZL, Y):

    # to fit the tensorflow requirement for tf.nn.softmax_cross_entropy_with_logits(...,...)
    logits = tf.transpose(ZL)
    labels = tf.transpose(Y)

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = labels))

    return cost


def model(X_train, Y_train, X_test, Y_test, learning_rate = 0.0001,
          num_epochs = 1500, minibatch_size = 64, print_cost = True):

    ops.reset_default_graph()                         # to be able to rerun the model without overwriting tf variables
    tf.set_random_seed(1)                             # to keep consistent results
    seed = 1
#    seed = np.random.randint(0,10000)                                          # to keep consistent results
    (n_x, m) = X_train.shape                          # (n_x: input size, m : number of examples in the train set)
    n_y = Y_train.shape[0]                            # n_y : output size
    costs = []                                        # To keep track of the cost
    layers_dims = [n_x, 15, 10, 10, n_y]

    # Create Placeholders of shape (n_x, n_y)
    X, Y =  create_placeholders(n_x, n_y)

    # Initialize parameters
    parameters = initialize_parameters(layers_dims)

    # Forward propagation: Build the forward propagation in the tensorflow graph
    ZL = forward_propagation(X, parameters)

    # Cost function: Add cost function to tensorflow graph
    cost = compute_cost(ZL, Y)

    # Backpropagation: Define the tensorflow optimizer. Use an AdamOptimizer.
    optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

    # Initialize all the variables
    init = tf.global_variables_initializer()

    # Start the session to compute the tensorflow graph
    with tf.Session() as sess:

        # Run the initialization
        sess.run(init)

        # Do the training loop
        for epoch in range(num_epochs):

            epoch_cost = 0.                       # Defines a cost related to an epoch
            num_minibatches = int(m / minibatch_size) # number of minibatches of size minibatch_size in the train set
            seed = seed + 1
            minibatches = random_mini_batches(X_train, Y_train, minibatch_size, seed)

            for minibatch in minibatches:

                # Select a minibatch
                (minibatch_X, minibatch_Y) = minibatch
                # IMPORTANT: The line that runs the graph on a minibatch.
                # Run the session to execute the "optimizer" and the "cost", the feedict should contain a minibatch for (X,Y).
                _ , minibatch_cost = sess.run([optimizer, cost], feed_dict = {X: minibatch_X, Y: minibatch_Y})

                epoch_cost += minibatch_cost / num_minibatches

            # Print the cost every epoch
            if print_cost == True and epoch % 1000 == 0:
                print ("Cost after epoch %i: %f" % (epoch, epoch_cost))
            if print_cost == True and epoch % 10 == 0:
                costs.append(epoch_cost)

        # plot the cost
        #plt.plot(np.squeeze(costs))
        #plt.ylabel('cost')
        #plt.xlabel('iterations (per tens)')
        #plt.title("Learning rate =" + str(learning_rate))
        #plt.show()

        # lets save the parameters in a variable
        parameters = sess.run(parameters)
        print ("Parameters have been trained!")

        # Calculate the correct predictions
        correct_prediction = tf.equal(tf.argmax(ZL), tf.argmax(Y))

        # Calculate accuracy on the test set
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print (accuracy)
        print ("Train Accuracy:", accuracy.eval({X: X_train, Y: Y_train}))
        print ("Test Accuracy:", accuracy.eval({X: X_test, Y: Y_test}))

        y_p = tf.argmax(ZL, axis = 0)

        precision, update = tf.metrics.precision(tf.argmax(Y), tf.argmax(ZL))
        sess.run(tf.local_variables_initializer())

        val_precision = update.eval(feed_dict = {X: X_test, Y: Y_test})
#        sess.run(precision, feed_dict = {X: X_train, Y: Y_train})

#        recall, _ = tf.metrics.recall(labels = tf.argmax(Y), predictions = tf.argmax(ZL))
#        auc, _ = tf.metrics.auc(labels = tf.argmax(Y), predictions = tf.argmax(ZL))
#        cf = tf.confusion_matrix(labels = tf.argmax(Y), predictions = tf.argmax(ZL))
#        val_precision, val_recall, val_auc, val_cf = sess.run([precision, reca], feed_dict= {X:np.random.randn(12288,1080), Y:np.random.randn(6,1080)})
#        print ("Precision", sess.run(precision))
#        print ("Precision", val_precision)
#        print ("recall",val_recall)
#        print ("auc", val_auc)
#        print ("confusion_matrix")
        print (val_precision)


        y_true = np.argmax(Y_train, axis = 0)
        print ("validation accuracy:")
        val_accuracy, y_pred = sess.run([accuracy, y_p], feed_dict={X:X_test, Y: Y_test})
        print (y_true, y_pred)

        print ("Precision",sklearn.metrics.precision_score(y_true, y_pred, average = 'micro'))
        print ("Recall", sklearn.metrics.recall_score(y_true, y_pred, average = 'micro'))
        print ("f1_score", sklearn.metrics.f1_score(y_true, y_pred, average = 'micro'))
        print ("confusion_matrix")
        print (sklearn.metrics.confusion_matrix(y_true, y_pred))
#        fpr, tpr, tresholds = sklearn.metrics.roc_curve(y_true, y_pred)

#        predicted = y_pred
#        actual = y_true
#        TP = tf.count_nonzero(predicted * actual)
#        TN = tf.count_nonzero((predicted - 1) * (actual - 1))
#        FP = tf.count_nonzero(predicted * (actual - 1))
#        FN = tf.count_nonzero((predicted - 1) * actual)
#        precision = TP / (TP + FP)
#        recall = TP / (TP + FN)
#        f1 = 2 * precision * recall / (precision + recall)

        return parameters, costs

parameters, costs = model(X_train, Y_train, X_test, Y_test, learning_rate = 1e-5, num_epochs = 10, minibatch_size = 16, print_cost = True)

# random grid search
#costs_grid = []
#grid_size = 6
#learning_rate_grid = [np.power(10, i * (-3) - 3) for i in np.random.rand(grid_size)]
#minibatch_size_grid = [np.power(2, i) for i in np.random.randint(8,size = grid_size)]

#for ig in range(grid_size):
#    parameters, costs = model(X_train, Y_train, X_test, Y_test, learning_rate = learning_rate_grid[ig],
#          num_epochs = 10000, minibatch_size = minibatch_size_grid[ig], print_cost = True)
#    costs_grid.append(costs)

#print (learning_rate_grid, minibatch_size_grid, costs_grid)


# predict
#import scipy
#from PIL import Image
#from scipy import ndimage

#my_image = "images.jpg"

# We preprocess your image to fit your algorithm.
#fname = "images/" + my_image
#image = np.array(ndimage.imread(fname, flatten=False))
#my_image = scipy.misc.imresize(image, size=(64,64)).reshape((1, 64*64*3)).T
#my_image_prediction = predict(my_image, parameters)

#plt.imshow(image)
#print("Your algorithm predicts: y = " + str(np.squeeze(my_image_prediction)))



