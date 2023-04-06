import os
import cv2


class PatternExtractor:
    def __init__(self, pattern_dir, threshold=127):
        self.pattern_dir = pattern_dir
        self.threshold = threshold

    def extract_patterns(self, reference_dir):
        if not os.path.exists(self.pattern_dir):
            os.makedirs(self.pattern_dir)
        img_files = os.listdir(reference_dir)
        classes = list(set([os.path.splitext(f)[0] for f in img_files]))
        for cls in classes:
            pattern_file = os.path.join(self.pattern_dir, f"{cls}.png")
            if os.path.exists(pattern_file):
                continue  # skip already extracted patterns

            img_file = os.path.join(reference_dir, f"{cls}.png")
            img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
            pattern = self.create_pattern(img)
            cv2.imwrite(pattern_file, pattern)

    def create_pattern(self, img):
        img_new = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        _, thresh = cv2.threshold(img_new, self.threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        x, y, w, h = cv2.boundingRect(contours[-1])
        mask = thresh[y:y + h, x:x + w]
        return mask
