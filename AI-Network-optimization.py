
#AI for network optimization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Generate simulated network data
np.random.seed(42)

# Simulate network traffic data (e.g., packet size, throughput, RTT, etc.)
num_samples = 1000
packet_size = np.random.randint(100, 1500, num_samples)  # in bytes
throughput = np.random.randint(10, 100, num_samples)  # in Mbps
round_trip_time = np.random.uniform(10, 200, num_samples)  # in ms
error_rate = np.random.uniform(0, 0.1, num_samples)  # simulated error rate
network_load = np.random.randint(30, 90, num_samples)  # in percentage

# Target: 1 = High Congestion, 0 = Low Congestion
# High Congestion when throughput < 30 Mbps, round_trip_time > 100 ms, and error_rate > 0.05
target = ((throughput < 30) & (round_trip_time > 100) & (error_rate > 0.05)).astype(int)

# Create a DataFrame
data = pd.DataFrame({
    'Packet Size': packet_size,
    'Throughput': throughput,
    'RTT': round_trip_time,
    'Error Rate': error_rate,
    'Network Load': network_load,
    'Congestion': target
})

# Visualize the generated data
plt.figure(figsize=(10, 6))
plt.scatter(data['RTT'], data['Throughput'], c=data['Congestion'], cmap='coolwarm', alpha=0.6)
plt.title("Network Traffic vs. RTT and Throughput (Colored by Congestion)")
plt.xlabel('Round Trip Time (ms)')
plt.ylabel('Throughput (Mbps)')
plt.colorbar(label='Congestion Level')
plt.show()

# Split data into training and test sets
X = data[['Packet Size', 'Throughput', 'RTT', 'Error Rate', 'Network Load']]
y = data['Congestion']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Decision Tree Classifier for congestion prediction
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict congestion levels on the test data
y_pred = model.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Display results
print(f"Prediction Accuracy: {accuracy*100:.2f}%")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

# Visualizing Decision Tree
plt.figure(figsize=(12, 8))
from sklearn.tree import plot_tree
plot_tree(model, filled=True, feature_names=X.columns, class_names=['Low', 'High'], rounded=True)
plt.title("Decision Tree for Congestion Prediction")
plt.show()

# Simulate network optimization after AI predictions
# If high congestion is predicted, reduce bandwidth allocation and reroute traffic
optimized_throughput = np.where(y_pred == 1, throughput * 0.8, throughput)  # Reduce bandwidth by 20% if congestion
optimized_latency = np.where(y_pred == 1, round_trip_time * 1.2, round_trip_time)  # Increase latency if congestion

# Visualizing the optimization
plt.figure(figsize=(10, 6))
plt.scatter(optimized_latency, optimized_throughput, c=y_pred, cmap='coolwarm', alpha=0.6)
plt.title("Optimized Network Traffic vs. RTT and Throughput (Post-AI)")
plt.xlabel('Round Trip Time (ms)')
plt.ylabel('Throughput (Mbps)')
plt.colorbar(label='Congestion Level')
plt.show()

# Evaluate the optimized performance
optimized_accuracy = accuracy_score(y_test, y_pred)
print(f"Optimized Prediction Accuracy: {optimized_accuracy*100:.2f}%")

# Output performance summary
print(f"Optimized Network Throughput: {np.mean(optimized_throughput):.2f} Mbps")
print(f"Optimized Network Latency: {np.mean(optimized_latency):.2f} ms")
