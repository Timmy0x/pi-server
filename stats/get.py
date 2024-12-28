import os
import psutil
from datetime import datetime
from io import BytesIO
from flask import Flask, Blueprint, jsonify

cpu_temp_history = []
gpu_temp_history = []
cpu_usage_history = []
memory_usage_history = []
disk_usage_history = []

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read().strip()) / 1000.0
        if temp == None:
            temp = 0
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

def get_stats(save=False):
    stats = {}
    stats["cpu_temp"] = get_cpu_temp()
    stats["gpu_temp"] = get_gpu_temp()
    stats["cpu_usage"] = get_cpu_usage()
    stats["memory_usage"] = get_memory_usage()
    stats["disk_usage"] = get_disk_usage()
    if save == True:
        cpu_temp_history.append(stats["cpu_temp"])
        gpu_temp_history.append(stats["gpu_temp"])
        cpu_usage_history.append(stats["cpu_usage"])
        memory_usage_history.append(stats["memory_usage"])
        disk_usage_history.append(stats["disk_usage"])
    return stats

def get_history():
    history = {}
    history["cpu_temp"] = get_cpu_temp_history()
    history["gpu_temp"] = get_gpu_temp_history()
    history["cpu_usage"] = get_cpu_usage_history()
    history["memory_usage"] = get_memory_usage_history()
    history["disk_usage"] = get_disk_usage_history()
    return history

def get_cpu_temp_history():
    return cpu_temp_history

def get_gpu_temp_history():
    return gpu_temp_history

def get_cpu_usage_history():
    return cpu_usage_history

def get_memory_usage_history():
    return memory_usage_history

def get_disk_usage_history():
    return disk_usage_history

def clear_history():
    global cpu_temp_history, gpu_temp_history, cpu_usage_history, memory_usage_history, disk_usage_history
    cpu_temp_history = []
    gpu_temp_history = []
    cpu_usage_history = []
    memory_usage_history = []
    disk_usage_history = []
