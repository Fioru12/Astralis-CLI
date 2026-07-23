import click
from astralis_cli.utils.display import print_success, print_error, create_table, console
from astralis_cli.utils.helpers import get_docker_containers

@click.group()
def docker():
    """🐳 Docker container management"""
    pass

@docker.command()
def list():
    """List all containers"""
    containers = get_docker_containers()
    
    if not containers:
        console.print("[yellow]No containers found[/yellow]")
        return
    
    table = create_table(
        "Docker Containers",
        ["Name", "Status", "Ports"],
        [[c["name"], c["status"], c["ports"]] for c in containers]
    )
    console.print(table)

@docker.command()
@click.argument("name")
def start(name):
    """Start a container"""
    from astralis_cli.utils.helpers import run_command
    stdout, stderr = run_command(["docker", "start", name])
    if stdout:
        print_success(f"Container {name} started")
    else:
        print_error(f"Failed to start {name}: {stderr}")

@docker.command()
@click.argument("name")
def stop(name):
    """Stop a container"""
    from astralis_cli.utils.helpers import run_command
    stdout, stderr = run_command(["docker", "stop", name])
    if stdout:
        print_success(f"Container {name} stopped")
    else:
        print_error(f"Failed to stop {name}: {stderr}")

@docker.command()
@click.argument("name")
def restart(name):
    """Restart a container"""
    from astralis_cli.utils.helpers import run_command
    stdout, stderr = run_command(["docker", "restart", name])
    if stdout:
        print_success(f"Container {name} restarted")
    else:
        print_error(f"Failed to restart {name}: {stderr}")

@docker.command()
@click.argument("name")
@click.option("--tail", "-n", default=50, help="Number of lines to show")
def logs(name, tail):
    """Show container logs"""
    from astralis_cli.utils.helpers import run_command
    stdout, _ = run_command(["docker", "logs", "--tail", str(tail), name])
    console.print(stdout)
