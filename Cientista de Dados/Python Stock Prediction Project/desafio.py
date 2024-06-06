""" In the Python file, you will be creating a neural network to predict the price of a stock. Part of the program is already implemented, your goal is to set up the model, train the model on the training data set, then finally predict the values from the testing data set.

These are the following details you need to implement:

You should create a Sequential model with 5 layers.

Your model should use 2 LSTM layers, and after each use a Dropout layer with a rate of 0.2. The first LSTM layer should have input_shape as a parameter along with units set to 4. The final layer should be a Dense layer with units set to 1.

Once the model is set up, you should compile it with a mean_squared_error loss and the optimizer set to adam.

When you fit the training dataset, make sure to set the following values: epochs=5, batch_size=16, verbose=0

Finally, print the model summary and then run the predict function on the x_test dataset and print the last column of the array. """

import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense

# Simulating some data for demonstration
# Assume each sample has 10 time steps and each time step has 2 features
num_samples = 100
time_steps = 10
features = 2

x_train = np.random.random((num_samples, time_steps, features))
y_train = np.random.random((num_samples, 1))  # corresponding targets
x_test = np.random.random((20, time_steps, features))  # smaller test set

# Create the model
model = Sequential()

#Adding the LSTM layers and Dropout layers
model.add(LSTM(units=4, return_sequences=True, input_shape=(time_steps, features))) # Corrected input_shape
model.add(Dropout(0.2)) # First Dropout layer

model.add(LSTM(units=4, return_sequences=False))  # Second LSTM layer
model.add(Dropout(0.2))  # Second Dropout layer

# Adding the Dense layer at the end 
model.add(Dense(units= 1)) # Final Dense layer

# Compiling the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Fitting the model on the training dataset
model.fit(x_train, y_train, epochs=5, batch_size=16, verbose=0)

# Print model summary
model.summary()

# Predicting the values for the testing dataset
predictions = model.predict(x_test)

# Print the predictions
print(predictions.flatten())  # Assuming predictions need to be flattened for display