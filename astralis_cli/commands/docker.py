import click
import subprocess

@click.group()
def docker():
    """Docker container management"""
    pass

@docker.command()
def list():
    """List all containers"""
    result = subprocess.run(["docker", "ps", "-a", "--format", "table {{.Names}}\t{{.Status}}"], capture_output=True, text=True)
    click.echo(result.stdout)

@docker.command()
@click.argument("name")
def start(name):
    """Start a container"""
    subprocess.run(["docker", "start", name])
    click.echo(f"✅ Started {name}")

@docker.command()
@click.argument("name")
def stop(name):
    """Stop a container"""
    subprocess.run(["docker", "stop", name])
    click.echo(f"⏹️ Stopped {name}")
