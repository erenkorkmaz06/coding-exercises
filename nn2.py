import numpy as np
import matplotlib.pyplot as plot


class NN():
    def __init__(self, i_nodes=2, o_nodes=2, h_nodes=3, batch_size=8, i_data=None, o_data=None, epochs=100):
        self.i_nodes = i_nodes
        self.o_nodes = o_nodes
        self.h_nodes = h_nodes
        self.batch_size = batch_size
        self.epochs = epochs

        self.i_data = i_data
        self.o_data = o_data

        self.w1 = np.random.randn(i_nodes, h_nodes)
        self.w2 = np.random.randn(h_nodes, o_nodes)

        self.loss_arr = np.array([[]])
        self.ind = np.array([[]])

    def forward(self):
        h_val = self.i_data.dot(self.w1)

        h_relu = np.maximum(h_val, 0)
        o_data_prediction = h_relu.dot(self.w2)
        return [h_val,h_relu,o_data_prediction]

    def loss(self):
        loss = np.square(self.forward()[2] - self.o_data).sum()
        self.loss_arr = np.append(self.loss_arr, loss)
        return loss

    def backward(self):
        grad_pred = 2 * (self.forward()[2] - self.o_data)
        grad_w2 = self.forward()[1].T.dot(grad_pred)
        grad_h_relu = grad_pred.dot(self.w2.T)
        grad_h_val = grad_h_relu.copy()
        grad_h_val[self.forward()[0] < 0] = 0
        grad_w1 = self.i_data.T.dot(grad_h_val)
        self.w1 -= grad_w1 * 1e-4
        self.w2 -= grad_w2 * 1e-4

    def train(self):
        for i in range(self.epochs):

            h_val,h_relu,o_data_prediction = self.forward()


            loss = self.loss()
            self.ind = np.append(self.ind,i)
            if i%10 == 0:
                print(f"epoch: {i}")
                print("loss: {}".format(loss))

            self.backward()

    def predict(self,x):
        h_val = x.dot(self.w1)
        h_relu = np.maximum(h_val, 0)
        o_data_prediction = h_relu.dot(self.w2)
        return o_data_prediction

    def err_table(self):
        plot.plot(self.ind,self.loss_arr)
        plot.legend(["Loss over iterations"])
        plot.show()

np.random.seed(34)
model = NN(8,2,4,8,np.random.randn(8,8),np.random.randn(8,2),1000)

model.train()
model.err_table()

