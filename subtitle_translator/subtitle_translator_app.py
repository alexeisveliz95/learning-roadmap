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
