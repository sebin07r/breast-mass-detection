import cv2

from ultralytics import YOLO

# Load the YOLO model
model = YOLO(r"C:\Users\chris\PycharmProjects\PythonProject\sebin.pt")

# Open the video file
video_path = r"C:\Users\chris\Downloads\-098TRTY_jpg.rf.079358b7e0725ad50280befed89702f4 (1).jpg"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(0) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
