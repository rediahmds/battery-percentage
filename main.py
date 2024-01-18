#!/usr/bin/env python

import psutil
import matplotlib.pyplot as plt
from time import sleep
from collections import deque

def get_battery_percentage():
    try:
        battery = psutil.sensors_battery()
        return battery.percent
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    update_interval = 10  # Adjust the update interval in seconds
    countdown = update_interval
    history_length = 30  # Number of data points to keep in the history
    battery_history = deque(maxlen=history_length)

    plt.ion()  # Turn on interactive mode for real-time plotting
    fig, ax = plt.subplots()

    while True:
        battery_percentage = get_battery_percentage()

        if battery_percentage is not None:
            battery_history.append(battery_percentage)

            ax.clear()
            ax.plot(range(len(battery_history)), battery_history)
            ax.set_title("Battery Percentage Over Time")
            ax.set_xlabel("Time (Update Intervals)")
            ax.set_ylabel("Battery Percentage")
            plt.pause(0.1)

            print(f"Battery Percentage: {battery_percentage}% | Next Update in: {countdown}s", end="\r", flush=True)

        sleep(1)
        countdown -= 1

        if countdown <= 0:
            countdown = update_interval

if __name__ == "__main__":
    main()
