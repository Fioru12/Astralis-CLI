import click
import subprocess

@click.group()
def server():
    """Server management"""
    pass

@server.command()
def reboot():
    """Reboot the server"""
    click.confirm("⚠️  Are you sure you want to reboot?", abort=True)
    subprocess.run(["sudo", "reboot"])
