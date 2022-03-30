from dataclasses import dataclass

@dataclass
class Product:
  id: str
  name: str
  colors: list
  sizes: list
  color_size_combinations: list


def get_product() -> Product:
  """
  Simulates a service REST call
  :return:
  """
  return Product(1,
     'Jeans',
     ['red', 'green', 'blue'],
     ['XS', 'S', 'M', 'L'],
     ['red_XS', 'red_S', 'red_L', 'green_S', 'green_M', 'blue_XS', 'blue_S', 'blue_M', 'blue_L']
   )


def main():
  product = get_product()

  # User selects RED color.
  selected_color = 'red'

  # UI needs to show the sizes that are available
  available_sizes = []
  for color_size in product.color_size_combinations:
    (color, size) = color_size.split('_')
    if color == selected_color:
      available_sizes.append(size)

  # These are the sizes to show on the UI
  print(available_sizes)

if __name__ == '__main__':
  main()


