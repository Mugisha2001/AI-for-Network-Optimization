Key Components
X-axis: Round Trip Time (RTT) (in ms)

Represents the time taken for a signal to travel from the source to the destination and back.
Higher RTT values often indicate potential network delays.
Y-axis: Throughput (in Mbps)

Represents the rate of successful data transfer over the network.
Higher throughput indicates better network performance.
Color Scale: Congestion Level

Blue (0.0): No congestion or low congestion.
Red (1.0): High congestion.
Observations
Congestion Patterns:

Congestion (red points) is mostly concentrated at higher RTT values (> 100 ms) and lower throughput levels (< 30 Mbps). This makes sense, as higher RTT and lower throughput often correspond to congested network conditions.
Lower RTT and higher throughput areas (blue points) indicate stable, congestion-free network performance.
Throughput Distribution:

A majority of the points fall in the mid-to-high throughput range (40–100 Mbps), indicating that the network operates efficiently under normal conditions.
RTT and Congestion Relationship:

As RTT increases, the likelihood of congestion also increases. This suggests that network delays contribute to congestion.
Interpretation of Results
Congestion Detection:

The graph effectively separates congested and non-congested states, which is useful for understanding how RTT and throughput correlate with congestion levels.
Network Optimization:

To optimize network performance, the focus should be on reducing RTT and increasing throughput in the regions where congestion occurs.
Predictive Modeling:

These patterns can be used to train machine learning models to predict congestion based on RTT and throughput.
Actionable Insights
Network Design:
Implement measures to reduce RTT, such as optimizing routing or improving infrastructure, to mitigate congestion.
Monitoring and Prediction:
Deploy real-time monitoring of RTT and throughput to anticipate congestion before it happens.

![Screenshot 2024-12-03 104317](https://github.com/user-attachments/assets/e93d7d19-42fd-46f2-92c7-8fe8c9ceb2a7)
