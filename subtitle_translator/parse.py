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

def parse_