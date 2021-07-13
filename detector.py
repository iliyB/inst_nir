from imageai.Detection import ObjectDetection, VideoObjectDetection
import os

class detector_photo:



    def __init__(self):
        current_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(current_path + "/resnet50_coco_best_v2.1.0.h5")
        self.detector.loadModel()

    def detectorRetinaNet_from_photo(self, input_file):

        image, list = self.detector.detectObjectsFromImage(
            input_image=str(input_file),
            output_type="array",
            minimum_percentage_probability=45
        )
        list_object = {}
        for object in list:
            if object['name'] in list_object:
                list_object[object['name']] += 1
            else:
                list_object.update({object['name']: 1})

        return list_object






def forSecond(frame2_number, output_arrays, count_arrays, average_count, returned_frame):
    print("FOR FRAME ", frame2_number)
    print("Output for each object : ", output_arrays)
    print("Output count for unique objects : ", count_arrays)
    print(returned_frame)
    print("------------END OF A FRAME --------------")

def forFull(output_arrays, count_arrays, average_output_count):
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the entire video: ", average_output_count)
    print("------------END OF THE VIDEO --------------")

def detectorRetinaNet_from_video(input):

    current_path = os.getcwd()
    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(current_path + "/resnet50_coco_best_v2.1.0.h5")
    detector.loadModel()

    print()
    print("RetinaNet")
    #list =
    print(detector.detectObjectsFromVideo(
        input_file_path=current_path + "/" + input,
        #output_file_path=current_path + "/" + "time_file.mp4",
        minimum_percentage_probability=45,
        frames_per_second=2,
        #per_second_function=forSecond,
        video_complete_function=forFull,
        save_detected_video=False

    ))
    # print(list)
    # list_object = {}
    # for object in list:
    #     if object['name'] in list_object:
    #         list_object[object['name']] += 1
    #     else:
    #         list_object.update({object['name']: 1})

    #return list_object

def detectorYolo(input):

    current_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(current_path + "/yolo.h5")
    detector.loadModel()

    print()
    print("Yolo")
    list = detector.detectObjectsFromImage(
        input_image='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + input,
        #output_image_path='C:/Users/iliy-/PycharmProjects/instaApi/venv/images/' + output,
        minimum_percentage_probability=45,

    )

    return list

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