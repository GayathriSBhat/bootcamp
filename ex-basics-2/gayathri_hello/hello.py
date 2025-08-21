import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

def say_hello():
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    message = Text(f"Hello {name}!", style="bold green")
    panel = Panel(message, title="[cyan]Greeting[/cyan]", border_style="magenta")
    console.print(panel)

