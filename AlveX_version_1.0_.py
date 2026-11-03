import random
import csv
import time
from datetime import datetime

# ==================================
# ALVEX TECHNOLOGIES
# MACHINE INTELLIGENCE V1.0
# ==================================

MACHINE_NAME = "ALVEX-MOTOR-001"

MAX_TEMPERATURE = 80
MAX_VIBRATION = 8.0

# 1. Read machine temperature
def read_machine_temperature():
    temperature = random.randint(35, 100)
    return temperature


# 2. Read machine vibration
def vibration_level():
    vibration = round(random.uniform(1, 12), 2)
    return vibration


# 3. Detect abnormal readings
def abnormal_readings(temperature, vibration):

    problems = []

    if temperature > MAX_TEMPERATURE:
        problems.append("High temperature")

    if vibration > MAX_VIBRATION:
        problems.append("Excessive vibration")

    return problems


# 4. Generate warnings
def generate_warnings(problems):

    if problems:
        print("\nWARNING: MACHINE ABNORMALITY!")

        for problem in problems:
            print("ALERT:", problem)

    else:
        print("\nMachine operating normally.")


# 5. Save machine readings
def save_readings(temperature, vibration, problems):

    with open("alvex_data.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            MACHINE_NAME,
            temperature,
            vibration,
            "; ".join(problems) if problems else "Normal"
        ])


# 6. Main machine controller
def start_machine_monitor():

    print("==============================")
    print(" ALVEX MACHINE INTELLIGENCE")
    print("==============================")

    for cycle in range(1, 6):

        temperature = read_machine_temperature()
        vibration = vibration_level()

        print("\nMachine:", MACHINE_NAME)
        print("Monitoring cycle:", cycle)
        print("Temperature:", temperature, "°C")
        print("Vibration:", vibration, "mm/s")

        problems = abnormal_readings(
            temperature, vibration
        )

        generate_warnings(problems)

        save_readings(
            temperature, vibration, problems
        )

        print("------------------------------")

        time.sleep(2)

    print("\nMonitoring completed.")
    print("Machine data saved.")


# START SYSTEM
start_machine_monitor()