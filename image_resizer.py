import cv2

# Load the image from the file
src = cv2.imread("krishna-arjun.jpg", cv2.IMREAD_UNCHANGED)

# Set the scale percentage for resizing
scale_percent = 50

# Calculate the new dimensions based on the scale percentage
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Resize the image
output = cv2.resize(src, (new_width, new_height))

# Save the resized image to a new file
cv2.imwrite("newkrishnaimage.jpeg", output)

# Wait for a key press to close the window (optional)
cv2.waitKey(0)
