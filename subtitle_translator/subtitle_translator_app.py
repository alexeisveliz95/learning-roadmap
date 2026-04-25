# Subtile translator CLI
import typer
from rich.console import Console
from parse import parse_srt
from translator import translate_batches

app = typer.Typer()
console = Console()