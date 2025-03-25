import goran
import marina
import yoyo
import sandie

name = input('Vad är ditt namn?' )

print(f'Hej {name}')

if name == "Goran":
    goran.hello()

elif name == "Marina":
    marina.hello()

elif name == "Chabbe":
    yoyo.hello()

elif name == "Sandie":
    sandie.hello()
