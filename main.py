

# pip install tensorflow
# conda activate tensorflow { this is the same as -} C:\Users\DELL\anaconda3\Scripts\conda.exe activate tensorflow
# pip install opencv-contrib-python # some people ask the difference between this and opencv-python
                                    # and opencv-python contains the main packages wheras the other
                                    # contains both main modules and contrib/extra modules
# pip install cvlib # for object detection

# # pip install gtts
# # pip install playsound // i installed this version instead - pip install playsound==1.2.2
# use `pip3 install PyObjC` if you want playsound to run more efficiently.
# pip install opencv-contrib-python cvlib gtts playsound PyObjC
#

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound



def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/audio.mp3")
    playsound("./sounds/audio.mp3")

    # output.save("audio.mp3")
    # playsound("audio.mp3")
    # os.remove("C:/Users/DELL/Downloads/object_detection/audio.mp3")    #LINE ADDED

video = cv2.VideoCapture(0)

labels = []

while video.isOpened():
    print('cam opened')
    ret, frame = video.read()
    # Bounding box.
    # the cvlib library has learned some basic objects using object learning
    # usually it takes around 800 images for it to learn what a phone is.

    # bbox, label, conf = cv.detect_common_objects(frame)
    bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4-tiny')
    # bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4-tiny')
    # bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny')

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", frame)

    # to record items once
    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

i = 0
new_sentence = []
for label in labels:
    if i == 0:
        new_sentence.append(f"I found a {label} ")
    else:
        new_sentence.append(f"and, a {label},")

    i += 1

speech(" ".join(new_sentence))


