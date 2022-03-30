from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
  val: Optional[int]
  left: Optional['Node']
  right: Optional['Node']

def compare_nodes(a: Optional[Node], b: Optional[Node]) -> bool:
  return False
