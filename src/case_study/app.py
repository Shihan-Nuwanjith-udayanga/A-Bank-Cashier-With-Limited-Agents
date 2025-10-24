import simpy
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------
# Parameters
# ---------------------------------------
RANDOM_SEED = 42           # for reproducibility
CUSTOMERS = 50             # total customers arriving
INTERVAL = 5               # average time between arrivals
SERVICE_TIME = (3, 7)      # min and max service duration
CASHIERS = 2               # number of available bank agents

# ---------------------------------------
# Customer Process
# ---------------------------------------
def customer(env, name, bank, wait_times, service_times, busy_time):
    """Simulates a customer arriving, waiting, and being served."""
    arrive = env.now
    # print(f"{name} arrives at {arrive:.2f}")

    with bank.request() as req:
        yield req
        wait = env.now - arrive
        wait_times.append(wait)

        service_duration = random.uniform(*SERVICE_TIME)
        service_times.append(service_duration)
        busy_time[0] += service_duration  # total service time handled by all cashiers

        yield env.timeout(service_duration)
        # print(f"{name} leaves at {env.now:.2f}")

# ---------------------------------------
# Customer Arrival Generator
# ---------------------------------------
def setup(env, cashiers, interval, wait_times, service_times, busy_time):
    """Generates customers and schedules their arrivals."""
    bank = simpy.Resource(env, cashiers)
    for i in range(CUSTOMERS):
        env.process(customer(env, f"Customer {i+1}", bank, wait_times, service_times, busy_time))
        yield env.timeout(random.expovariate(1.0 / interval))  # random arrivals

# ---------------------------------------
# Run Simulation
# ---------------------------------------
def run_simulation():
    print("\n--- Bank Cashier Simulation ---\n")
    random.seed(RANDOM_SEED)
    env = simpy.Environment()

    wait_times = []
    service_times = []
    busy_time = [0]  # store total busy time of all cashiers

    env.process(setup(env, CASHIERS, INTERVAL, wait_times, service_times, busy_time))
    env.run()

    # -----------------------------------
    # Results
    # -----------------------------------
    avg_wait = statistics.mean(wait_times)
    avg_service = statistics.mean(service_times)
    total_time = env.now
    utilization = (busy_time[0] / (total_time * CASHIERS)) * 100

    print(f"Total customers served: {CUSTOMERS}")
    print(f"Average wait time: {avg_wait:.2f} time units")
    print(f"Average service time: {avg_service:.2f} time units")
    print(f"Total simulation time: {total_time:.2f}")
    print(f"Cashier utilization: {utilization:.2f}%")

    # -----------------------------------
    # Visualization 1: Wait Time per Customer
    # -----------------------------------
    plt.figure(figsize=(8, 4))
    plt.plot(wait_times, marker='o', color='b')
    plt.title("Customer Wait Time per Customer")
    plt.xlabel("Customer")
    plt.ylabel("Wait Time (time units)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # -----------------------------------
    # Visualization 2: Histogram of Wait Times
    # -----------------------------------
    plt.figure(figsize=(8, 4))
    plt.hist(wait_times, bins=10, color='orange', edgecolor='black')
    plt.title("Distribution of Customer Wait Times")
    plt.xlabel("Wait Time (time units)")
    plt.ylabel("Number of Customers")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # -----------------------------------
    # Visualization 3: Cashier Utilization
    # -----------------------------------
    labels = ['Busy Time', 'Idle Time']
    busy = utilization
    idle = 100 - utilization
    plt.figure(figsize=(5, 5))
    plt.pie([busy, idle], labels=labels, autopct='%1.1f%%', colors=['green', 'lightgrey'], startangle=90)
    plt.title("Cashier Utilization")
    plt.tight_layout()
    plt.show()

# ---------------------------------------
# Main Entry
# ---------------------------------------
if __name__ == "__main__":
    run_simulation()