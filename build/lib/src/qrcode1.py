# Importando biblioteca
import qrcode
 
# Dados a serem codificados
data = 'https://www.linkedin.com/in/mncodedev/'
 
# Codificando dados usando a função make()
img = qrcode.make(data)
 
# Salvando como arquivo de imagem
img.save('linkedin_mncodedev.png')