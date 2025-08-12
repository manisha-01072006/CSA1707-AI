import math
from collections import Counter

# Example dataset: Outlook, Temperature, Humidity, Windy, PlayTennis
dataset = [
    ['Sunny', 'Hot', 'High', False, 'No'],
    ['Sunny', 'Hot', 'High', True, 'No'],
    ['Overcast', 'Hot', 'High', False, 'Yes'],
    ['Rain', 'Mild', 'High', False, 'Yes'],
    ['Rain', 'Cool', 'Normal', False, 'Yes'],
    ['Rain', 'Cool', 'Normal', True, 'No'],
    ['Overcast', 'Cool', 'Normal', True, 'Yes'],
    ['Sunny', 'Mild', 'High', False, 'No'],
    ['Sunny', 'Cool', 'Normal', False, 'Yes'],
    ['Rain', 'Mild', 'Normal', False, 'Yes'],
    ['Sunny', 'Mild', 'Normal', True, 'Yes'],
    ['Overcast', 'Mild', 'High', True, 'Yes'],
    ['Overcast', 'Hot', 'Normal', False, 'Yes'],
    ['Rain', 'Mild', 'High', True, 'No']
]

# Attribute names
attributes = ['Outlook', 'Temperature', 'Humidity', 'Windy']

# Calculate entropy
def entropy(data):
    labels = [row[-1] for row in data]
    label_counts = Counter(labels)
    total = len(data)
    ent = 0.0
    for count in label_counts.values():
        prob = count / total
        ent -= prob * math.log2(prob)
    return ent

# Calculate information gain
def info_gain(data, attr_index):
    total_entropy = entropy(data)
    values = set(row[attr_index] for row in data)
    weighted_entropy = 0.0
    for val in values:
        subset = [row for row in data if row[attr_index] == val]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    return total_entropy - weighted_entropy

# Build the decision tree recursively
def build_tree(data, attributes):
    labels = [row[-1] for row in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    # Choose best attribute
    gains = [info_gain(data, i) for i in range(len(attributes))]
    best_attr_index = gains.index(max(gains))
    best_attr = attributes[best_attr_index]

    tree = {best_attr: {}}
    values = set(row[best_attr_index] for row in data)
    for val in values:
        subset = [row[:best_attr_index] + row[best_attr_index+1:] for row in data if row[best_attr_index] == val]
        sub_attributes = attributes[:best_attr_index] + attributes[best_attr_index+1:]
        tree[best_attr][val] = build_tree(subset, sub_attributes)

    return tree

# Train the decision tree
decision_tree = build_tree(dataset, attributes)
print("Decision Tree:")
print(decision_tree)
