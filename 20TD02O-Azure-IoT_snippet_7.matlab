% Initial parameters
initialTemperature = 25;
desiredTemperature = 22;

% Simulate the system
simTime = 3600; % Simuleringstid i sekunder
time = linspace(0, simTime, 100);
temperature = initialTemperature + 2 * sin(0.01 * time);

% Plot resultater
figure;
plot(time, temperature);
xlabel('Time (seconds)');
ylabel('Temperature (°C)');
title('Temperature Control Simulation');
grid on;