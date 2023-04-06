<h1>Chess Recognition Project</h1>
This project is aimed at developing a web-based application for recognizing chessboards and individual figures on them. The application is implemented in Python using the Django framework and OpenCV computer vision library.

Working project can be found at the following link: http://mikitadaroshkin.pythonanywhere.com/

<h2>Project Description</h2>
The project consists of several parts:

* Chessboard recognition algorithm
* Piece recognition algorithm
* Web application for uploading images and visualizing results

The chessboard recognition algorithm is based on computer vision techniques such as edge detection and hough transform. The algorithm detects the corners of the chessboard and warps the image to get a top-down view of the board.

The figure recognition algorithm is based on image segmentation and pattern matching. The algorithm uses a pre-trained set of patterns for each chess figure and matches them with the segmented figures on the chessboard.

The web application allows users to upload an image of a chessboard and visualize the recognized chessboard with individual figures identified. The application also includes a feature to generate random chessboards with random figures on them.

<h2>Usage Guide</h2>
1. Install Python (version 3.7 or later) and Django (version 3.2 or later).
2. Clone the repository to your local machine.
3. Run the Django development server by typing python manage.py runserver in the terminal in the project's root directory.
4. Open a web browser and navigate to http://localhost:8000/ to access the home page of the application.
5. Upload an image of a chessboard using the file upload form on the home page.
6. Click on the "Recognize" button to visualize the recognized chessboard with individual figures identified.

<h2>Description of the Matching Algorithm</h2>

The figure recognition algorithm is based on image segmentation and pattern matching. The algorithm uses a pre-trained set of patterns for each chess figure and matches them with the segmented figures on the chessboard.

<h3>Segmentation</h3>
The algorithm segments the chessboard image into individual figures using the following steps:

1. Convert the image to grayscale.
2. Apply a binary threshold to the image to obtain a binary image where the chessboard figures are white and the background is black.
3. Find contours in the binary image using OpenCV's findContours function.
4. For each contour, determine the bounding rectangle and crop the image to obtain the individual chessboard figure.

<h3>Pattern Matching</h3>
The algorithm matches the segmented chessboard figures with the pre-trained set of patterns for each chess figure using the following steps:

1. Convert the segmented chessboard figure to grayscale.
2. Apply a binary threshold to the image to obtain a binary image where the chess figure is white and the background is black.
3. For each previously found pattern for the corresponding chess figure, apply a binary threshold to the pattern image to obtain a binary image where the chess figure pattern is white and the background is black.
4. Calculate the cross-correlation between the binary thresholded chess figure image and the binary thresholded chess figure pattern image using OpenCV's matchTemplate function.
5. Determine the positions of the matches in the chess figure image that exceeds predefined threshold.
6. If the correlation values are above a certain threshold, the chess figure is considered a match with the corresponding chess figure pattern.

<h2>Further Steps</h2>

The current implementation of the Chessboard Recognizer uses traditional computer vision techniques to identify chessboard and its pieces. However, the accuracy of this approach can be limited in complex scenarios, where occlusion and noise can significantly impact the performance.

One possible way to improve the recognition algorithm is by using deep learning-based object detectors (for example, YOLO). These models can be trained on large datasets of chessboard and piece images to learn how to accurately detect and classify them.

By using deep learning detectors, the recognizer can be more robust to occlusions, noise, and other challenging scenarios. Additionally, deep learning-based models can learn features that are specific to chessboard and piece recognition, which can lead to better performance compared to traditional computer vision techniques.
