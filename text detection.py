import cv2
import easyocr
import matplotlib.pyplot as plt


image_path = r'C:\speed estimation\Data\test2.png'

img = cv2.imread(image_path)


reader = easyocr.Reader(['en'], gpu=False)


text = reader.readtext(img)

threshold = 0.25

for i in text:
    print(i)

    bbox, text, score = i

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()