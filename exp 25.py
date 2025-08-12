# ffnn_no_numpy.py  — pure Python (no numpy)
import random
import math

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(sig):
    return sig * (1.0 - sig)

# XOR dataset
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

random.seed(42)

# Network shape
input_neurons = 2
hidden_neurons = 4
output_neurons = 1

# Initialize weights and biases
W1 = [[random.uniform(-1, 1) for _ in range(input_neurons)] for _ in range(hidden_neurons)]
b1 = [random.uniform(-1, 1) for _ in range(hidden_neurons)]
W2 = [[random.uniform(-1, 1) for _ in range(hidden_neurons)] for _ in range(output_neurons)]
b2 = [random.uniform(-1, 1) for _ in range(output_neurons)]

learning_rate = 0.5
epochs = 10000

for epoch in range(epochs):
    total_loss = 0.0
    for xi, yi in zip(X, y):
        # Forward pass
        hidden_input = [sum(W1[j][i] * xi[i] for i in range(input_neurons)) + b1[j] for j in range(hidden_neurons)]
        hidden_output = [sigmoid(h) for h in hidden_input]
        final_input = [sum(W2[k][j] * hidden_output[j] for j in range(hidden_neurons)) + b2[k] for k in range(output_neurons)]
        final_output = [sigmoid(f) for f in final_input]

        # Loss (MSE for this sample)
        total_loss += (yi - final_output[0]) ** 2

        # Backpropagation
        d_output = [(yi - final_output[k]) * sigmoid_derivative(final_output[k]) for k in range(output_neurons)]

        # Hidden layer gradients
        d_hidden = [0.0 for _ in range(hidden_neurons)]
        for j in range(hidden_neurons):
            for k in range(output_neurons):
                d_hidden[j] += d_output[k] * W2[k][j]
            d_hidden[j] *= sigmoid_derivative(hidden_output[j])

        # Update W2, b2
        for k in range(output_neurons):
            for j in range(hidden_neurons):
                W2[k][j] += learning_rate * d_output[k] * hidden_output[j]
            b2[k] += learning_rate * d_output[k]

        # Update W1, b1
        for j in range(hidden_neurons):
            for i in range(input_neurons):
                W1[j][i] += learning_rate * d_hidden[j] * xi[i]
            b1[j] += learning_rate * d_hidden[j]

    if epoch % 2000 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss / len(X):.6f}")

# Show final outputs
print("\nFinal outputs:")
for xi in X:
    hidden = [sum(W1[j][i] * xi[i] for i in range(input_neurons)) + b1[j] for j in range(hidden_neurons)]
    hidden_out = [sigmoid(h) for h in hidden]
    out = sigmoid(sum(W2[0][j] * hidden_out[j] for j in range(hidden_neurons)) + b2[0])
    print(f"{xi} -> {out:.4f}")
