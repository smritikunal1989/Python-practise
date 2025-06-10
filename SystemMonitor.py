import psutil
import time

def get_system_info():
    #cpu usage
    cpu_percent =psutil.cpu_percent(interval=1)

    #Memoryusahe
    memory =psutil.virtual_memory()
    memory_percent =memory.percent

    #Diskusage

    disk =psutil.disk_usage('/')
    disk_percent =disk.percent

    #Netwrokstats

    network =psutil.net_io_counters()

    return{
        "cpu":cpu_percent,
        "memory":memory_percent,
        "disk": round(disk_percent,1),
        "network_receivd":round(network.bytes_recv/(1024**2),2)
    }


def monitor_system(duration=60):
    print("===System Monitor Started=====")
    print("-"*40)

    for i in range(duration):
        stats =get_system_info()
        print(f"CPU: {stats['cpu']} %| "
              f"Memory: {stats['memory']} %| "
              f"Disk: {stats['disk']} %| "
               )
        time.sleep(3)
monitor_system(30)
print("==system monitor ready======")