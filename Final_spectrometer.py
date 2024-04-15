import cv2
import numpy as np
import matplotlib.pyplot as plt

# index 0 for laptop cam,1 for external cam
camera_index = 1

# Create video capture object
cap = cv2.VideoCapture(camera_index)

# Set video capture parameters
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Adjust resolution if needed
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

calib = 23

# Set up plot
plt.figure()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.xlim([100, 1000])

# Initialize intensity array and wavelength vector
intensity_array = []

while True:
    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", frame)  # to see the video in separate window

    # Calculate intensity (sum of each row)
    intensity = np.sum(gray_image, axis=0)

    wavelength = np.linspace(100 + calib, 1000 + calib, len(intensity))

    # Update intensity array and plot: adding current intensity values to array
    intensity_array.append(intensity)

    plt.plot(wavelength, intensity)
    plt.draw()

    plt.pause(0.001)  # Adjust delay as needed

# Release resources
cap.release()
plt.show()
