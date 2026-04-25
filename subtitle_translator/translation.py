import time
from rich.progress import track
from deep_translator import GoogleTranslator

def translate_batches(blocks, target_lang="es"):
    translator = GoogleTranslator(source='auto', target=target_lang)

    current_batch = []
    current_chars = 0

    #Recorremos los bloques para crear los lotes
    for block in track(blocks, description="[cyan]Proscessing subttitles...[/cyan]"):
        # Unimos las líneas del subtítulo por si tiene varias
        text = " ".join(block.content)