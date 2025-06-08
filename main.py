from ultralytics import YOLO
import cv2
import numpy as np


def draw_bbox(frame, boxes, confs):
    """
    Отрисовка объектов класса person и confidence
    """
    for i, (box, conf) in enumerate(zip(boxes, confs), start=1):
        x1, y1, x2, y2 = box
        bbox_color = (255, 0, 0)
        text_color = (0, 0, 255)
        cv2.rectangle(frame, (x1, y1), (x2, y2), bbox_color, 2)
        label = f"Person {i}. Conf: {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 2)
    return frame


if __name__ == '__main__':
    user_input = input("Показывать видео во время обработки? (y/n): ").strip().lower()
    show_video = user_input in ['да', 'yes', 'y', 'true', '1']
    model = YOLO('yolov8n.pt')
    input_video_path = 'crowd.mp4'
    capture = cv2.VideoCapture(input_video_path)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    output_video_path = 'detect.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break

        results = model(frame, classes=[0])[0]
        boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)
        confs = results.boxes.conf.cpu().numpy()

        indices = np.where(confs > 0.25)[0]
        filtered_boxes = boxes[indices]
        filtered_confs = confs[indices]

        frame = draw_bbox(frame, filtered_boxes, filtered_confs)
        writer.write(frame)

        if show_video:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    capture.release()
    writer.release()
    cv2.destroyAllWindows()
