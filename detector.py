from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag
from imageai.Detection import ObjectDetection
import os


def detectorRetinaNet(input, output):

    current_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(current_path + "/resnet50_coco_best_v2.1.0.h5")
    detector.loadModel()

    print()
    print("RetinaNet")
    list = detector.detectObjectsFromImage(
        input_image='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + input,
        output_image_path='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + output,
        minimum_percentage_probability=45

    )
    print(list)

def detectorYolo(input, output):

    current_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(current_path + "/yolo.h5")
    detector.loadModel()

    print()
    print("Yolo")
    list = detector.detectObjectsFromImage(
        input_image='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + input,
        output_image_path='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + output,
        minimum_percentage_probability=45

    )
    print(list)

def detectorYoloTiny(input, output):

    current_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(current_path + "/yolo-tiny.h5")
    detector.loadModel()

    print()
    print("YoloTiny")
    list = detector.detectObjectsFromImage(
        input_image='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + input,
        output_image_path='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + output,
        minimum_percentage_probability=45

    )
    print(list)