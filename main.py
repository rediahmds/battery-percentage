import psutil
from time import sleep

def get_battery_percentage():
    try:
        battery = psutil.sensors_battery()
        return battery.percent
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    UPDATE_INTERVAL = 60
    countdown = UPDATE_INTERVAL
    battery_percentage = get_battery_percentage()

    while True:

        if battery_percentage is not None:
            print(f"Battery Percentage: {battery_percentage}% | Next update in {countdown}s", end="\r", flush=True)

        sleep(1)
        countdown -= 1  # Adjust the sleep interval as needed

        if countdown <= 0:
            countdown = UPDATE_INTERVAL
            battery_percentage = get_battery_percentage()

if __name__ == "__main__":
    main()