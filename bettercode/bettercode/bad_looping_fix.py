from typing import List, Dict
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class ProductRaw:
  id: str
  name: str
  colors: list
  sizes: list
  color_size_combinations: list

@dataclass
class Product(ProductRaw):
  sizes_by_color = Dict[str, List[str]]


def get_product() -> Product:
  """
  Simulates a service REST call
  :return:
  """
  product = Product(1,
     'Jeans',
     ['red', 'green', 'blue'],
     ['XS', 'S', 'M', 'L'],
     ['red_XS', 'red_S', 'red_L', 'green_S', 'green_M', 'blue_XS', 'blue_S', 'blue_M', 'blue_L']
   )

  # Post-processing
  product.sizes_by_color = defaultdict(list)
  for color_size in product.color_size_combinations:
    (color, size) = color_size.split('_')
    product.sizes_by_color[color].append(size)

  return product


def main():
  product = get_product()

  # User selects RED color.
  selected_color = 'gray'

  # UI needs to show the sizes that are available
  available_sizes = product.sizes_by_color[selected_color]

  # These are the sizes to show on the UI
  print(available_sizes)

# HIDES MESSY DETAILS
# MAKES THE CODE CLEANER

# COUNTERARGUMENT -- you could just put a function somewhere to do that

if __name__ == '__main__':
  main()


