from abc import ABC, abstractmethod
import random

# Abstract base class for Sensor
class Sensor(ABC):
    @abstractmethod
    def read_sensor(self):
        pass

# Abstract base class for Actuator
class Actuator(ABC):
    @abstractmethod
    def control_actuator(self, value):
        pass

# Simulated Sensor Implementation
class SimulatedSensor(Sensor):
    def read_sensor(self):
        # Simulate sensor reading with a random value
        return random.uniform(0, 100)

# Simulated Actuator Implementation
class SimulatedActuator(Actuator):
    def control_actuator(self, value):
        # Simulate controlling the actuator by printing the value
        print(f"Actuator controlled with value: {value}")

def main():
    # Create instances of the simulated sensor and actuator
    sensor = SimulatedSensor()
    actuator = SimulatedActuator()

    # Read sensor data **ONCE** and store it
    sensor_value = sensor.read_sensor()
    
    print(f"Sensor reading: {sensor_value}")  # Print sensor reading
    actuator.control_actuator(sensor_value)   # Use the same value for actuator

if __name__ == "__main__":
    main()
