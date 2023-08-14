import torch
import torch.nn as nn
import torch.utils.data as utils
import torch.utils.data as td
torch.manual_seed(1234)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split   #sklearn package helps in splitting the data for train, validation and test set

#Todo: Go line by line to understand what each line is doing.

#Load the iris dataset
df = pd.read_csv('iris.data.csv', header=None)

#Assign labels
label_dict = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}

x = df[[0,1,2,3]].values   #inputs
y = np.vectorize(label_dict.get)(df[4])    #classes


input_size = 4  #How many features does each data point have?
h1 = 6  #the first hidden layer has 6 nodes, it's your choice to give any number
h2 = 4  #the second hidden layer has 4 nodes, again it's your choice to give any number
output = 3  #How many output classes are there?
#What happens when you increase the number of nodes in the hidden layers?

#Define the structure of your neural network.
#We have 2 hidden layers of size 6 and 4 respectively.
#we have used ReLU activation function (since it is widely used for such applications),
# you can use other activations functions too
# https://pytorch.org/docs/stable/nn.html#non-linear-activations-weighted-sum-nonlinearity
class IrisNet1(nn.Module):

    def __init__(self,input_size,h1,h2,output):
        super(IrisNet1, self).__init__()

        self.fc1 = nn.Linear(input_size, h1)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(h1, h2)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(h2, output)

    def forward(self, x):  #define the forward propagation operations
        out = self.fc1(x)
        out = self.relu1(out)
        out = self.fc2(out)
        out = self.relu2(out)
        out = self.fc3(out) #Note: No activations on the last layer.

        return out


#Define hyperparameters
learning_rate = 0.01  #the standard learning rate value = 0.1 is adapted. For gradient descent
learning_momentum = 0.9  #we saw this in the last session.
epochs = 20   #What is an epoch?
batch_sz = 10  #what is batch size?

#Initialise the Model
model = IrisNet1(input_size, h1, h2, output)

#You can check that the weights have been initialised at random.
for param_tensor in model.state_dict():
    print(param_tensor, "\n", model.state_dict()[param_tensor].numpy())


#Choose Optimizer and Loss function
#https://pytorch.org/docs/stable/nn.html#loss-functions
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=learning_momentum)
# we are using stochastic gradient descent
#https://datascience.stackexchange.com/questions/36450/what-is-the-difference-between-gradient-descent-and-stochastic-gradient-descent


#we want to split the dataset for training, validation and testing.
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1) # splitting for train and validation set
x_test,x_val,y_test,y_val=train_test_split(x_test,y_test,test_size=0.5,random_state=1) #further validation set is splitted for test set

#print if you need to see what has happened.
#print(x)
#print(x_train)
#print(len(x_train))
#print(len(x_test))



# Create DataLoaders. Change from numpy arrays to torch tensor format.
# Create a dataset and loader for the training data and labels
train_x = torch.Tensor(x_train).float()
train_y = torch.Tensor(y_train).long()
train_ds = utils.TensorDataset(train_x,train_y)
train_loader = td.DataLoader(train_ds, batch_size=batch_sz, shuffle=True, num_workers=0)

#similarly for validation and test data
test_x = torch.Tensor(x_test).float()
test_y = torch.Tensor(y_test).long()
test_ds = utils.TensorDataset(test_x,test_y)
test_loader = td.DataLoader(test_ds, batch_size=batch_sz, shuffle=True, num_workers=0)

val_x = torch.Tensor(x_val).float()
val_y = torch.Tensor(y_val).long()
val_ds = utils.TensorDataset(val_x,val_y)
val_loader = td.DataLoader(val_ds, batch_size=batch_sz, shuffle=True, num_workers=0)


# Function to Train the model
def train(model, train_loader, valid_loader, criterion, optimizer):
    model.train()    #sets the model to training mode
    train_loss = 0  #to measure our training and validation loss
    valid_loss = 0

    for batch, tensor in enumerate(train_loader):
        data, target = tensor
        optimizer.zero_grad()  #reset gradients
        out = model(data)       #forward propagate
        loss = criterion(out, target)   #compute loss
        train_loss += loss.item()
        loss.backward()     #backpropagate
        optimizer.step()    #update gradient with Stochastic Gradient Descent
        train_loss += loss.item()
    ## evaluation part
    model.eval()    #set model to evaluation mode (so we don't backpropagate)
    for batch1, tensor1 in enumerate(valid_loader):
        data1, target1 = tensor1
        output = model(data1)
        loss1 = criterion(output, target1)
        valid_loss += loss1.item()

    #Return loss
    avg_loss = train_loss / len(train_loader.dataset)
    avg_loss1 = valid_loss/len(valid_loader.dataset)

    return avg_loss, avg_loss1

#Function to test the trained model
def test(model, test_loader,criterion):
    # Switch the model to evaluation mode (so we don't backpropagate)
    model.eval()
    test_loss = 0
    correct = 0

    with torch.no_grad():
        for batch, tensor in enumerate(test_loader):
            data, target = tensor
            out = model(data) # Forward propagate to Get the predictions
            test_loss += criterion(out, target).item()  # calculate the loss
            _, predicted = torch.max(out.data, 1)  # Calculate the accuracy #What is going on here?
            correct += torch.sum(target==predicted).item() #What is going on here?

    # return validation loss and prediction accuracy for the epoch
    avg_accuracy = correct / len(test_loader.dataset)
    avg_loss = test_loss / len(test_loader.dataset)

    return avg_loss, avg_accuracy


#Train the model - track metrics for each epoch in these arrays
epoch_nums = []
training_loss = []
validation_loss = []


# Train over set epochs
for epoch in range(1, epochs + 1):

    # Feed the training data into the model to optimize the weights
    train_loss,valid_loss = train(model, train_loader,val_loader, criterion, optimizer)

    # Log the metrcs for this epoch
    epoch_nums.append(epoch)
    training_loss.append(train_loss)
    validation_loss.append(valid_loss)

    # Print stats for every 10th epoch so we can see training progress
    if (epoch) % 1 == 0:
        print('Epoch {:d}: Training loss= {:.4f}, Validation loss= {:.4f}'.format(epoch, train_loss, valid_loss))



#let's visualise the training of our model.

from matplotlib import pyplot as plt

plt.plot(epoch_nums, training_loss)
plt.plot(epoch_nums, validation_loss)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['training loss', 'validation loss'], loc='upper right')
plt.show()
# both training and validation loss decreases,
# i.e. the value of the loss function decreases,
# using stochastic gradient descent we update the weights (parameters) and minimize the loss function,


#let's test our model!
test_loss, accuracy = test(model, test_loader,criterion)
print('Test loss= {:.4f}, Accuracy={:.4%}'.format(test_loss, accuracy))


#let's predict on a new datapoint
x_new = [[7,3.2,4.7,1.4]] #given the input data for which you want to predict the class of the Iris plant
print ('New sample: {}'.format(x_new[0]))

model.eval()

# Get a prediction for the new data sample
x = torch.Tensor(x_new).float()
_, predicted = torch.max(model(x).data, 1)

invert_label_dict = {v: k for k, v in label_dict.items()}
print('Prediction:',invert_label_dict[predicted.item()])
