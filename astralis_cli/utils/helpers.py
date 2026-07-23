import subprocess
from typing import Optional

def run_command(command: list, shell: bool = False) -> tuple[str, str]:
    """Run command and return (stdout, stderr)"""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=shell,
            timeout=30
        )
        return result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return "", "Command timed out"
    except Exception as e:
        return "", str(e)

def check_docker_installed() -> bool:
    stdout, _ = run_command(["docker", "--version"])
    return bool(stdout)

def get_docker_containers() -> list[dict]:
    """Get list of Docker containers"""
    stdout, _ = run_command([
        "docker", "ps", "-a",
        "--format", "{{.Names}}\t{{.Status}}\t{{.Ports}}"
    ])
    
    containers = []
    if stdout:
        for line in stdout.split("\n"):
            if line:
                parts = line.split("\t")
                if len(parts) >= 2:
                    containers.append({
                        "name": parts[0],
                        "status": parts[1],
                        "ports": parts[2] if len(parts) > 2 else ""
                    })
    return containers
