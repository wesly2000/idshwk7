from LSBSteg import LSBSteg
import cv2
# Hiding phase
in_img = cv2.imread('carrier.png')
steg = LSBSteg(in_img)
data = open('info.txt', "rb").read()
res = steg.encode_binary(data)
cv2.imwrite('test.png', res)
# Extracting phase
in_img = cv2.imread('test.png')
steg = LSBSteg(in_img)
raw = steg.decode_binary()
with open('extract.txt', 'wb') as f:
    f.write(raw)