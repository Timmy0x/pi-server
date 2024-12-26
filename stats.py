import os
import psutil
import time
from threading import Thread, Lock

# Global dictionary to store statistics
stats = {}
lock = Lock()

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read().strip()) / 1000.0
        return temp
    except FileNotFoundError:
        return None

def get_gpu_temp():
    try:
        temp = os.popen("vcgencmd measure_temp").readline()
        return float(temp.replace("temp=", "").replace("'C\n", ""))
    except Exception:
        return None

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage("/").percent

def update_stats():
    global stats
    while True:
        with lock:
            stats["cpu_temp"] = get_cpu_temp()
            stats["gpu_temp"] = get_gpu_temp()
            stats["cpu_usage"] = get_cpu_usage()
            stats["memory_usage"] = get_memory_usage()
            stats["disk_usage"] = get_disk_usage()
        time.sleep(5)

def update_and_get_stats():
    global stats
    with lock:
        stats["cpu_temp"] = get_cpu_temp()
        stats["gpu_temp"] = get_gpu_temp()
        stats["cpu_usage"] = get_cpu_usage()
        stats["memory_usage"] = get_memory_usage()
        stats["disk_usage"] = get_disk_usage()
    return stats

if __name__ == "__main__":
    # Start the stats updater thread
    updater_thread = Thread(target=update_stats, daemon=True)
    updater_thread.start()

    # Keep the main thread alive
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break