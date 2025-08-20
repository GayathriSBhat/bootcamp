import typer
from rich.console import Console

console = Console()
app = typer.Typer()

@app.command()
def hello(name: str = "world"):
    console.print(f"[bold green]Hello {name}![/bold green]")

if __name__ == "__main__":
    app()
