import click
import subprocess

@click.group()
def system():
    """System monitoring"""
    pass

@system.command()
def info():
    """Show system information"""
    click.echo("🖥️ System Information")
    click.echo("=" * 40)
    
    # CPU
    cpu = subprocess.run(["top", "-bn1", "|", "grep", "Cpu(s)"], capture_output=True, text=True, shell=True).stdout.strip()
    click.echo(f"CPU: {cpu}")
    
    # RAM
    ram = subprocess.run(["free", "-h", "|", "grep", "Mem:"], capture_output=True, text=True, shell=True).stdout.strip()
    click.echo(f"RAM: {ram}")
    
    # Disk
    disk = subprocess.run(["df", "-h", "/"], capture_output=True, text=True).stdout.strip()
    click.echo(f"Disk:\n{disk}")
