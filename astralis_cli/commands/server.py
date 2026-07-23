import click
from astralis_cli.utils.display import print_success, print_warning, print_error

@click.group()
def server():
    """🖥️ Server management"""
    pass

@server.command()
def reboot():
    """Reboot the server"""
    if click.confirm("⚠️  Are you sure you want to reboot the server?"):
        click.echo("Rebooting...")
        import subprocess
        subprocess.run(["sudo", "reboot"])
    else:
        click.echo("Reboot cancelled")

@server.command()
def shutdown():
    """Shutdown the server"""
    if click.confirm("⚠️  Are you sure you want to shutdown the server?"):
        click.echo("Shutting down...")
        import subprocess
        subprocess.run(["sudo", "shutdown", "now"])
    else:
        click.echo("Shutdown cancelled")
