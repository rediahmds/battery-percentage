#!/usr/bin/env python

import psutil
from time import sleep
from collections import deque


def get_battery_percentage():
    try:
        battery = psutil.sensors_battery()
        return battery.percent
    except Exception as e:
        print(f"Error: {e}")
        return None


def draw_histogram(battery_percentage):
    bar_length = int(battery_percentage / 5)
    histogram = "[" + "=" * bar_length + " " * (20 - bar_length) + "]"
    return histogram


def main():
    update_interval = 10  # Adjust the update interval in seconds
    countdown = update_interval
    history_length = 30  # Number of data points to keep in the history
    battery_history = deque(maxlen=history_length)

    while True:
        battery_percentage = get_battery_percentage()

        if battery_percentage is not None:
            battery_history.append(battery_percentage)

            histogram = draw_histogram(battery_percentage)
            print(
                f"Battery Percentage: {battery_percentage}% | Histogram: {histogram} | Next Update in: {countdown}s",
                end="\r",
                flush=True,
            )

        sleep(1)
        countdown -= 1

        if countdown <= 0:
            countdown = update_interval


if __name__ == "__main__":
    main()
