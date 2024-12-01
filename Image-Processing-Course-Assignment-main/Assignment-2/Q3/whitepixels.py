import cv2

def calculate_white_pixel_percentage(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to create a binary image
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Count white pixels
    total_pixels = img.shape[0] * img.shape[1]
    white_pixels = cv2.countNonZero(thresh)

    # Calculate the percentage of white pixels
    white_percentage = (white_pixels / total_pixels) * 100

    return white_percentage

# Replace 'input_image.jpg' with your image path
percentage = calculate_white_pixel_percentage('r13.jpg')
print(f"Percentage of white pixels: {percentage:.2f}%")
