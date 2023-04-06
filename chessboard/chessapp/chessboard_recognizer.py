import cv2
import numpy as np

from . import utils


class ChessboardRecognizer:
    def __init__(self, pattern_dir, threshold):
        # Load the pattern images for each chess piece
        self.pattern_images, self.piece_classes = utils.load_piece_patterns(pattern_dir=pattern_dir)
        self.threshold = threshold

    @staticmethod
    def _preprocess_image(image):
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return processed_image

    def recognize(self, image_array):
        # Define a dictionary to map pattern class to chess piece class
        pattern_to_piece_class = {piece_class: piece_class for piece_class in self.piece_classes}

        # Convert the input image to grayscale
        processed_image = self._preprocess_image(image_array)

        # Define a list to hold the detected bounding boxes
        bounding_boxes = []

        # Loop over each pattern image and perform template matching
        for pattern_class, pattern_image in self.pattern_images.items():
            # Convert the pattern image to grayscale
            # pattern_gray = cv2.cvtColor(pattern_image, cv2.COLOR_BGR2GRAY)
            pattern_gray = pattern_image
            # Perform template matching
            res = cv2.matchTemplate(processed_image, pattern_gray, cv2.TM_CCOEFF_NORMED)

            # Get the locations of the correlations in the result map which are above threshold
            locations = np.where(res >= self.threshold)

            for top_left in zip(*locations[::-1]):
                # Calculate the bounding box for the detected pattern
                bottom_right = (top_left[0] + pattern_image.shape[1], top_left[1] + pattern_image.shape[0])
                bounding_box = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])

                # Append the bounding box and the corresponding piece class to the list
                piece_class = pattern_to_piece_class[pattern_class]
                bounding_boxes.append((bounding_box, piece_class))

        # Draw the bounding boxes on the original image
        response_image = image_array.copy()
        for bounding_box, piece_class in bounding_boxes:
            response_image = utils.draw_bounding_box(response_image, bounding_box, piece_class)

        # Return the response image
        return response_image
