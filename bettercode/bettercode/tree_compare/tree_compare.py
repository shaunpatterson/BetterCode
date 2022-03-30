from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
  val: Optional[int]
  left: Optional['Node']
  right: Optional['Node']

def compare_nodes(a: Optional[Node], b: Optional[Node]) -> bool:
  if not a and not b:
    return True

  if not a and b:
    return False
  if not b and a:
    return False

  left = compare_nodes(a.left, b.left)
  right = compare_nodes(a.right, b.right)

  return left and right and a.val == b.val
