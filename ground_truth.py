import turicreate as tc

data = tc.SFrame('directory_to_.sframe')

data['image_with_ground_truth'] = tc.object_detector.util.draw_bounding_boxes(data["image"], data["annotations"])

data.explore()