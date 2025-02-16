import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
SIMULATION_TIME = 120  # (minutes)
ARRIVAL_RATE = 3  # (avg customers per minute)
SERVICE_RATE = 2  # (avg baristas serving per minute)

def simulate_queue(num_baristas, num_simulations=1000):
    wait_times = []
    
    for _ in range(num_simulations):
        arrival_times = np.cumsum(np.random.exponential(1 / ARRIVAL_RATE, size=SIMULATION_TIME))
        service_times = np.random.exponential(1 / SERVICE_RATE, size=len(arrival_times))
        
        barista_available_times = np.zeros(num_baristas)
        queue = []
        
        for i in range(len(arrival_times)):
            next_available = np.argmin(barista_available_times)
            
            if barista_available_times[next_available] <= arrival_times[i]:
                start_time = arrival_times[i]
            else:
                start_time = barista_available_times[next_available]
                queue.append(start_time - arrival_times[i])
            
            barista_available_times[next_available] = start_time + service_times[i]
        
        if queue:
            wait_times.append(np.mean(queue))
        else:
            wait_times.append(0)

    return np.mean(wait_times)

# Run simulations
wait_time_2_baristas = simulate_queue(2)
wait_time_3_baristas = simulate_queue(3)

# Display results
print(f"Average wait time with 2 baristas: {wait_time_2_baristas:.2f} minutes")
print(f"Average wait time with 3 baristas: {wait_time_3_baristas:.2f} minutes")

# Bar Chart
plt.bar(["2 Baristas", "3 Baristas"], [wait_time_2_baristas, wait_time_3_baristas], color=['red', 'green'])
plt.ylabel("Average Wait Time (minutes)")
plt.title("Monte Carlo Simulation of Coffee Shop Queue")
plt.show()
