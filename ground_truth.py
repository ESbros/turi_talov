import turicreate as tc

dir_sframe = '/Users/erik/Desktop/turi/ig02.sframe'#'directory_to_.sframe exm: (desktop/annotation.sframe)'

data = tc.SFrame(dir_sframe)

data['image_with_ground_truth'] = tc.object_detector.util.draw_bounding_boxes(data["image"], data["annotations"])

data.explore()