# Keras: A Comprehensive Overview

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, Theano, or CNTK. It allows for easy and fast prototyping, supports both convolutional and recurrent networks, and runs seamlessly on both CPU and GPU.

## Key Features

- **User-Friendly API**: Designed for human beings, not machines. Keras follows best practices for reducing cognitive load.
- **Modular and Composable**: A model is understood as a sequence or a graph of standalone, fully-configurable modules that can be plugged together with as few restrictions as possible.
- **Easy to Extend**: New modules are simple to add (as new classes and functions), and existing modules provide ample examples.

## Installation

To install Keras, use pip:

```bash
pip install keras
```

## Basic Concepts and Terms

### 1. **Model**

A model is the core data structure of Keras. There are two main types of models available in Keras: the `Sequential` model and the `Model` class used with the functional API.

### 2. **Layer**

A layer is a basic building block of neural networks in Keras. Layers are combined to create a model.

### 3. **Sequential Model**

The `Sequential` model is a linear stack of layers.

**Example:**

```python
from keras.models import Sequential
from keras.layers import Dense

# Creating a Sequential model
model = Sequential()
model.add(Dense(32, input_shape=(784,), activation='relu'))
model.add(Dense(10, activation='softmax'))
```

### 4. **Functional API**

The functional API is a way to create models that are more flexible than the `Sequential` model. It allows for the creation of complex models, such as multi-output models, directed acyclic graphs, or models with shared layers.

**Example:**

```python
from keras.layers import Input, Dense
from keras.models import Model

# Creating a model using the functional API
inputs = Input(shape=(784,))
x = Dense(32, activation='relu')(inputs)
outputs = Dense(10, activation='softmax')(x)
model = Model(inputs=inputs, outputs=outputs)
```

### 5. **Compiling the Model**

Before training a model, you need to configure the learning process, which is done via the `compile` method. It specifies the optimizer, loss function, and metrics.

**Example:**

```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

### 6. **Training the Model**

Training the model involves feeding the training data into the model in batches, and the model learns to map inputs to outputs.

**Example:**

```python
model.fit(x_train, y_train, epochs=10, batch_size=32)
```

### 7. **Evaluating the Model**

After training, you can evaluate the model's performance on test data.

**Example:**

```python
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')
```

### 8. **Making Predictions**

Once the model is trained, you can use it to make predictions on new data.

**Example:**

```python
predictions = model.predict(x_new)
print(predictions)
```

## Example: Building a Simple Neural Network

Here's a complete example of building, compiling, training, and evaluating a simple neural network using Keras:

```python
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from keras.utils import to_categorical

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train = x_train.reshape((60000, 784)).astype('float32') / 255
x_test = x_test.reshape((10000, 784)).astype('float32') / 255
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Build the model
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=128)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')
```

## Conclusion

Keras is a powerful and user-friendly library for building and training neural networks. Its high-level API makes it easy to prototype and build complex models, while its integration with TensorFlow ensures that it can scale to handle large datasets and complex computations.

---

Feel free to experiment with these examples and explore more features of Keras! If you have any questions or need further assistance, just let me know.

Zdroj: konverzace s Copilotem, 15. 11. 2024
(1) How to Visualize a Deep Learning Neural Network Model in Keras. <https://machinelearningmastery.com/visualize-deep-learning-neural-network-model-keras/>.
(2) how-to-generate-a-summary-of-your-keras-model.md - GitHub. <https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-generate-a-summary-of-your-keras-model.md>.
(3) Keras: Understanding the Basics with a Detailed Example. <https://dev.to/dazevedo/keras-understanding-the-basics-with-a-detailed-example-4b0h>.
(4) Code examples - Keras. <https://keras.io/examples/>.
