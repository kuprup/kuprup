
from dataclasses import dataclass

@dataclass
class Engine:
    volume:int
    pistons:int

Engine(volume=5,pistons=7)