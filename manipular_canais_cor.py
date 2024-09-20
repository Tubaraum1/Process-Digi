import cv2
import numpy as np
# Carregar a imagem
imagem = cv2.imread('cavalo.jpg')
# Separando os canais de cor, na ordem azul, verde e vermelho
azul, verde, vermelho = cv2.split(imagem)
# Mesclando os canais de cor, na ordem azul, verde e vermelho
imagem_mesclada = cv2.merge((azul, verde, vermelho))
# Invertendo os canais de cor
imagem_invertida = cv2.merge((vermelho, verde, azul))
# criando uma imagem branca nas dimensões da imagem lida
blank = np.zeros(imagem.shape[:2], dtype='uint8')
#abindo as imagens por canais e mesclando com as matrizes de zeros
canal_azul = cv2.merge([azul, blank, blank])
canal_azul_gimp = cv2.merge([azul, azul, azul])
canal_verde = cv2.merge([blank, verde, blank])
canal_verde_gimp = cv2.merge([verde, verde, verde])
canal_vermelho = cv2.merge([blank, blank, vermelho])
canal_vermelho_gimp = cv2.merge([vermelho, vermelho, vermelho])
# Salvando as imagens
cv2.imwrite('Azul.png', canal_azul)
cv2.imwrite('Azul_gimp.png', canal_azul_gimp)
cv2.imwrite('Verde.png', canal_verde)
cv2.imwrite('Verde_gimp.png', canal_verde_gimp)
cv2.imwrite('Vermelho.png', canal_vermelho)
cv2.imwrite('Vermelho_gimp.png', canal_vermelho_gimp)
cv2.imwrite('imagem_mesclada.jpg', imagem_mesclada)
cv2.imwrite('imagem_invertida.jpg', imagem_invertida)
