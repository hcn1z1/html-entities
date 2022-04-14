# html-entities
a python lib to encode a whole html src code into entities

# about
have you ever wondered how to convert a whole html script to entities and yeah still everything works so fine? yes, this small module will help you to achieve your needs.

before using the script. please consider reading **rules** section to provide successful convertion from ASCII to entities.

# requirements
- python 3.x
- bs4 (Beautiful Soup 4)

# installation
i have finally added this project to PyPi under [htmltools-hcn1z1](https://pypi.org/project/htmltools-hcn1z1/0.0.1/).

`` pip install htmltools-hcn1z1==0.0.1``
# usage
```
from htmltools.entities import Encrypter,EncryptionHardOne
html = "some html here"
encryptContentOnly = Enctypter(html)
html = encryptContentOnly.encodingLetter()

encryptWholeScript = EncryptionHardOne(html)
html = encryptWholeScript.encodingLetterX()
```
# rules
before encoding the whole letter, please follow the next rules i setted myself:
- remove any unnecessary **#**, it breaks the encryption, for example: **href="#"**.
- consider removing <style> Content </style> and add it after encryption to make the encryption works.
- always use base64 or email-embedded images instead of urls.
- if an image doesnt work when embedded to base64, please remove it from source code then add it later.
