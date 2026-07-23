import click
from astralis_cli.commands import docker, system, server

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Astralis CLI - DevOps tool for Docker and server management"""
    pass

cli.add_command(docker.docker)
cli.add_command(system.system)
cli.add_command(server.server)

if __name__ == "__main__":
    cli()
