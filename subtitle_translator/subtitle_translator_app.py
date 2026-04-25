# Subtile translator CLI
import typer
from rich.console import Console
from parse import parse_srt
from translator import translate_batches

app = typer.Typer()
console = Console()

def load_subtitles(path):
    return parse_srt(path)

def run_translation(blocks, lang):
    translate_batches(blocks, lang)
    pass

def save_file(blocks, path):
    with open(path, "w", encoding="utf-8") as file:
        for block in blocks:
            file.write(f"{block.index}\n")
            file.write(f"{block.timestamp}\n")

            if block.translated_content:
                text_to_write = block.translated_content
            else:
                block.content

            for line in text_to_write:
                file.write(f"{line}\n")

            file.write("\n")
        pass

@app.command()
def translate(
    input_file: str = typer.Argument(..., help= "Original .srt path file"),
    output_file: str = typer.Argument(..., help= "Path to will be saved the translated .srt file "),
    lang: str = typer.Option("es", "--lang", "-l", help="Destined language to translate(es, en, fr)")
):
    """
    Subtitle Traslator CLI v1.0
    """
    console.print(f"[bold blue]Loading File:[/bold blue] {input_file}")
    blocks = load_subtitles(input_file)
    console.print(f"[bold yellow]Translating to {lang}...[/bold yellow]")
    run_translation(blocks, lang)
    console.print(f"[bold green]Saving on :[/bold green] {output_file}")
    save_file(blocks, output_file)
    console.print("[bold green]¡Done! Traslation completed with success. 🎉[/bold green]")


if __name__ == "__main__":
    app()

