
# pygradientify

make terminal UI'S beautiful.



## Installation

```bash
pip install pygradientify

pacman -S python-pygradientify
```
    
## Usage / examples

```python
from pygradientify import Colors

# ps: dir is horizontal by default.
"""
Normal
"""
print(Colors.red_to_blue("Hello World!", dir="h"))
print(Colors.mystic("Hello World!", dir="h"))

"""
ascii
"""
art = """
╔═╗╦ ╦╔═╗╦═╗╔═╗╔╦╗╦╔═╗╔╗╔╔╦╗╦╔═╗╦ ╦
╠═╝╚╦╝║ ╦╠╦╝╠═╣ ║║║║╣ ║║║ ║ ║╠╣ ╚╦╝
╩   ╩ ╚═╝╩╚═╩ ╩═╩╝╩╚═╝╝╚╝ ╩ ╩╚   ╩  
"""

print(Colors.blue_to_cyan(art, dir="h"))
print(Colors.purple_to_white(art, dir="h"))
print(Colors.orange_to_pink(art, dir="h"))
print(Colors.rainbow(art, dir="h")) # Rainbow gradient

"""
vertical will not work with rainbow it will fallback to horizontal
"""
print(Colors.rainbow(art, dir="v"))

"""
all gradients.
"""
for gradient_name in Colors.ls():
    grad = getattr(Colors, gradient_name)
    print(grad(f"{gradient_name}: The quick brown fox jumps over the lazy dog", dir="h"))


```
