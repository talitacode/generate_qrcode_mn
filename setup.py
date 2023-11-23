from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'gerador de imagens de QRcode'
LONG_DESCRIPTION = 'gerador de imagens de QRcode utilizando a biblioteca “ qrcode ”'

# Setting up
setup(
        name="generate_qrcode_mn", 
        version=VERSION,
        author="mncodedev",
        author_email="mncodedev@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        
)