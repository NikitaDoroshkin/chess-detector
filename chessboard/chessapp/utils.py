import cv2
import os


def load_piece_patterns(pattern_dir):
    piece_classes = []
    piece_patterns = {}
    for filename in os.listdir(pattern_dir):
        if filename.endswith('.png'):
            pattern_path = os.path.join(pattern_dir, filename)
            pattern_name = os.path.splitext(filename)[0]
            piece_classes.append(pattern_name)
            pattern = cv2.imread(pattern_path, cv2.IMREAD_GRAYSCALE)
            piece_patterns[pattern_name] = pattern
    return piece_patterns, piece_classes


def draw_bounding_box(image, bounding_box, text):
    cv2.rectangle(image, (bounding_box[0], bounding_box[1]), (bounding_box[2], bounding_box[3]),
                  (0, 255, 0), 2)
    cv2.putText(image, text, (bounding_box[0], bounding_box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2)
    return image
