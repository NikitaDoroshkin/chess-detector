import cv2
import os
import base64
import numpy as np
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from .chessboard_recognizer import ChessboardRecognizer
from .pattern_extractor import PatternExtractor


def initialize_recognizer():
    reference_dir = os.path.join(settings.BASE_DIR, 'static', settings.REFERENCE_IMAGES_DIR)
    pattern_dir = os.path.join(settings.BASE_DIR, 'static', settings.PATTERN_IMAGES_DIR)

    pattern_extractor = PatternExtractor(pattern_dir)
    pattern_extractor.extract_patterns(reference_dir)

    # Load the threshold for pattern matching similarity score from configuration
    matching_threshold = settings.PATTERN_MATCHING_THRESHOLD

    # Instantiate the ChessboardRecognizer object
    recognizer = ChessboardRecognizer(pattern_dir=pattern_dir, threshold=matching_threshold)
    return recognizer


recognizer = initialize_recognizer()


# Define the view functions
def home(request):
    return render(request, 'home.html')


def recognize_chessboard(request):
    if request.method == 'POST':
        # Get uploaded image file or choose random
        if 'image' in request.FILES:
            image_file = request.FILES['image']

            # Read the image file into a NumPy array
            image_bytes = image_file.read()
            image_array = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_UNCHANGED)
        else:
            example_images_dir = os.path.join(settings.BASE_DIR, 'static', settings.EXAMPLE_IMAGES_DIR)
            image_filename = np.random.choice(os.listdir(example_images_dir))
            image_array = cv2.imread(os.path.join(example_images_dir, image_filename), cv2.IMREAD_UNCHANGED)

        # Call the ChessboardRecognizer object to recognize the chessboard
        response_image = recognizer.recognize(image_array)

        # Encode the image to bytes and render it on the same page
        img_encoded = cv2.imencode('.png', response_image)[1].tobytes()
        img_encoded = base64.b64encode(img_encoded).decode('utf-8')
        context = {'processed_image': img_encoded}
        return render(request, 'home.html', context)
    else:
        return HttpResponse('Sorry, invalid request')
