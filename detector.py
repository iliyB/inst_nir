from imageai.Detection import ObjectDetection, VideoObjectDetection
import os
from moviepy.editor import VideoFileClip
import utils

class detector_photo:

    def __init__(self):
        current_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(current_path + "/resnet50_coco_best_v2.1.0.h5")
        self.detector.loadModel()

    def detectorRetinaNet_from_photo(self, input_file, delete_file=False):

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

        if delete_file:
            utils.delete_file(input_file)

        return list_object

class detector_video:

    def __init__(self):
        current_path = os.getcwd()
        self.detector = VideoObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(current_path + "/resnet50_coco_best_v2.1.0.h5")
        self.detector.loadModel(detection_speed='fastest')
        self.result = None

    def detectorRetinaNet_from_video(self, input_file, delete_file=False):

        def forFull(output_arrays, count_arrays, average_output_count):
            # print("Array for the outputs of each frame ", output_arrays)
            # print("Array for output count for unique objects in each frame : ", count_arrays)
            # print("Output average count for unique objects in the entire video: ", average_output_count)
            # print("------------END OF THE VIDEO --------------")
            self.result = average_output_count

        new_file = str(input_file[:-4]) + 'fix' + str(input_file[-4:])

        clip = VideoFileClip(str(input_file))
        clip.write_videofile(new_file, fps=3, logger=None)
        clip.reader.close()

        self.detector.detectObjectsFromVideo(input_file_path=str(new_file)
                                                     , frames_per_second=3, video_complete_function=forFull,
                                                     minimum_percentage_probability=45,
                                                     save_detected_video=False)
        if delete_file:
            utils.delete_file(input_file)
        utils.delete_file(new_file)

        result = {}
        for key in self.result.keys():
            if self.result.get(key):
                result.update({key: self.result.get(key)})
            else:
                result.update({key: 1})

        return result
