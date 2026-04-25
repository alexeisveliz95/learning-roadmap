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

        # Si este texto supera los 2000 caracteres, traducimos lo que llevamos
        if current_chars + len(text) > 2000:
            process_batch(current_batch, translator)
            time.sleep(0)
            current_batch = []
            current_chars = 0

        current_batch.append(block)
        current_chars += len(text)
    
    # Traducimos el último lote que quedó pendiente
    if current_batch:
        process_batch(current_batch, translator)

def process_batch(batch_blocks, translator):
    # Unimos todos los textos del lote con un delimitador único
    to_translate = " ||| ".join([" ".join(b.content) for b in batch_blocks])

    # Llamada a la API
    translated_text = translator.translate(to_translate)

    # Separamos el resultado usando el mismo delimitador
    translated_parts = translated_text.split(" ||| ")

    # Repartimos cada parte traducida de vuelta a su objeto original
    for i, block in enumerate(batch_blocks):
        if i < len(translated_parts):
            # Guardamos como lista para mantener la estructura original
            block.translated_content = [translated_parts[i].strip()]