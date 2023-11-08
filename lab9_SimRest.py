import random
import time

class CafeSimulation:
    def __init__(self):
        self.tables = 10
        self.waiters = 2
        self.cooks = 2
        self.totalProfit = 0
        self.totalClientsServed = 0

    def simulate(self, simulationHours):
        countClients = 0

        for hour in range(1, simulationHours + 1):
            clientsArrival = random.randint(0, 5)
            clientsToServe = min(clientsArrival, self.tables)
            countClients += clientsToServe

            print(f"Hour {hour}: {clientsToServe}/{self.tables} clients")

            for client in range(clientsToServe):
                if self.tables > 0 and self.waiters > 0 and self.cooks > 0:
                    self.tables -= 1
                    self.waiters -= 1
                    self.cooks -= 1

                    print(f"Hour {hour}: Client {client + 1} seated.")
                    time.sleep(0.5)

                    print(f"\tWaiter took order.")
                    time.sleep(0.5)

                    print(f"\t\tCook prepared the order.")
                    time.sleep(0.5)

                    print(f"\tWaiter served the client.")
                    time.sleep(0.5)

                    print(f"Hour {hour}: Client {client + 1} left.")
                    countClients -= 1
                    time.sleep(0.5)

                    self.tables += 1
                    self.waiters += 1
                    self.cooks += 1

            time.sleep(1)

        return countClients

cafe = CafeSimulation()
clientsServed = cafe.simulate(simulationHours=12)
print(f"Total clients served: {clientsServed}")
