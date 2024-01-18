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
    while True:
        battery_percentage = get_battery_percentage()

        if battery_percentage is not None:
            print(f"Battery Percentage: {battery_percentage}%")

        sleep(60)  # Adjust the sleep interval as needed

if __name__ == "__main__":
    main()