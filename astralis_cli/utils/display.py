from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def print_banner():
    banner = """
    ╔═══════════════════════════════════════╗
    ║   🛠️  Astralis CLI v1.0.0            ║
    ║   DevOps Tool for Docker & Servers   ║
    ╚═══════════════════════════════════════╝
    """
    console.print(Panel(banner, style="bold blue"))

def print_error(message: str):
    console.print(f"❌ [bold red]{message}[/bold red]")

def print_success(message: str):
    console.print(f"✅ [bold green]{message}[/bold green]")

def print_warning(message: str):
    console.print(f"⚠️  [bold yellow]{message}[/bold yellow]")

def create_table(title: str, columns: list, rows: list) -> Table:
    table = Table(title=title, show_header=True, header_style="bold magenta")
    for col in columns:
        table.add_column(col)
    for row in rows:
        table.add_row(*row)
    return table
