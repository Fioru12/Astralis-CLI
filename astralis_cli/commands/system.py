import click
import psutil
from astralis_cli.utils.display import print_success, print_error, create_table, console

@click.group()
def system():
    """🖥️ System monitoring"""
    pass

@system.command()
def info():
    """Show system information"""
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # Memory
    mem = psutil.virtual_memory()
    
    # Disk
    disk = psutil.disk_usage('/')
    
    # Uptime
    boot_time = psutil.boot_time()
    import time
    uptime_seconds = time.time() - boot_time
    uptime_days = int(uptime_seconds // 86400)
    uptime_hours = int((uptime_seconds % 86400) // 3600)
    
    table = create_table(
        "System Information",
        ["Metric", "Value"],
        [
            ["CPU Usage", f"{cpu_percent}% ({cpu_count} cores)"],
            ["Memory", f"{mem.percent}% used"],
            ["Memory Total", f"{mem.total / (1024**3):.2f} GB"],
            ["Memory Used", f"{mem.used / (1024**3):.2f} GB"],
            ["Disk Total", f"{disk.total / (1024**3):.2f} GB"],
            ["Disk Used", f"{disk.used / (1024**3):.2f} GB ({disk.percent}%)"],
            ["Uptime", f"{uptime_days}d {uptime_hours}h"]
        ]
    )
    console.print(table)

@system.command()
def monitor():
    """Monitor system resources in real-time"""
    import time
    try:
        while True:
            console.clear()
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory()
            
            console.print(f"CPU: {cpu}%")
            console.print(f"RAM: {mem.percent}%")
            console.print("\nPress Ctrl+C to stop")
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Monitoring stopped[/yellow]")

@system.command()
def processes():
    """List top processes"""
    table = create_table(
        "Top Processes",
        ["PID", "Name", "CPU%", "Memory%"],
        []
    )
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            table.add_row(
                str(proc.info['pid']),
                proc.info['name'],
                f"{proc.info['cpu_percent']:.1f}",
                f"{proc.info['memory_percent']:.1f}"
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    console.print(table)
