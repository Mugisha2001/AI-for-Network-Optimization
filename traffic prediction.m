###create network data traffic using code below

% Create synthetic data
packet_size = randi([64, 1500], 1000, 1); % Random packet sizes in bytes
arrival_rate = rand(1000, 1) * 100; % Random arrival rates in packets per second
congestion_level = randi([0, 1], 1000, 1); % 0 = no congestion, 1 = congestion

% Combine into a dataset
X = [packet_size, arrival_rate];
Y = congestion_level;

% Save to a .mat file
save('network_traffic_data.mat', 'X', 'Y');

###then after load your network traffic data using the following code
% Load network traffic data (assuming you have a dataset with packet size and arrival rate)
% Example: X - input features (packet size, arrival rate), Y - target (congestion level)

load('network_traffic_data.mat'); % This file should contain variables X and Y

% Split data into training and testing sets
train_ratio = 0.8;
[trainInd,~,testInd] = dividerand(length(X), train_ratio, 0, 1 - train_ratio);

X_train = X(trainInd, :);
Y_train = Y(trainInd, :);
X_test = X(testInd, :);
Y_test = Y(testInd, :);

% Train a Decision Tree model
mdl = fitctree(X_train, Y_train);

% Predict congestion level for test data
Y_pred = predict(mdl, X_test);

% Calculate accuracy
accuracy = sum(Y_pred == Y_test) / length(Y_test);
disp(['Prediction Accuracy: ', num2str(accuracy * 100), '%']);

% Visualize results
figure;
subplot(2,1,1);
plot(Y_test, 'b');
title('Actual Congestion Levels');
subplot(2,1,2);
plot(Y_pred, 'r');
title('Predicted Congestion Levels');


