from barcode import EAN13
from barcode.writer import ImageWriter



from barcode import EAN13
from barcode.writer import ImageWriter

with open('claude.png', 'wb') as f:
    EAN13('4564567891094', writer=ImageWriter()).write(f)
