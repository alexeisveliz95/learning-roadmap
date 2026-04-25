from dataclasses import dataclass
from typing import List

@dataclass
class SubtitleBlock:
    index: str
    timestamp: str
    content: List[str]
    translated_content: List[str] = None

    def __post_init__(self):
        if self.translated_content is None:
            self.translated_content = []

def time_mark_detection(line: str)-> bool:
    return ":" in line and line.count(":") == 4 and "-->" in line

def parse_srt(file_path: str)-> List(SubtitleBlock):
    blocks = []

    with open(file_path, "r", encoding="utf-8") as file:
        current_index, current_time, current_text = "", "", []

        for line in file:
            line = line.strip()
            if not line:
                if current_index and current_time:
                    blocks.append(SubtitleBlock(current_index, current_time, current_text))
                    current_index, current_time, current_text = "", "", []
                continue

            if time_mark_detection(line):
                current_time = line
            elif line.isdigit() and not current_time:
                current_index = line
            else:
                current_text.append(line)
        
        if current_index and current_time:
            blocks.append(SubtitleBlock(current_index, current_time, current_text))

    return blocks        