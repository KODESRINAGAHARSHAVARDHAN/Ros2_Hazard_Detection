#!/usr/bin/env python3

from ultralytics import YOLO
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from yolov8_msgs.msg import InferenceResult
from yolov8_msgs.msg import Yolov8Inference
from std_msgs.msg import String
from geometry_msgs.msg import Point

bridge = CvBridge()

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')

        self.model = YOLO('~/yolobot/src/yolobot_recognition/scripts/yolov8n.pt')

        self.yolov8_inference = Yolov8Inference()

        self.subscription = self.create_subscription(
            Image,
            'rgb_cam/image_raw',
            self.camera_callback,
            10)
        self.subscription 

        self.yolov8_pub = self.create_publisher(Yolov8Inference, "/Yolov8_Inference", 1)
        self.img_pub = self.create_publisher(Image, "/inference_result", 1)
        self.object_detection_pub = self.create_publisher(Yolov8Inference, "/yolo_detection", 1)
        self.weapon_alert_pub = self.create_publisher(String, "/weapon_alert", 1)
        self.weapon_location_pub = self.create_publisher(Point, "/weapon_location", 1)

    def camera_callback(self, data):
        img = bridge.imgmsg_to_cv2(data, "bgr8")
        results = self.model(img)

        self.yolov8_inference.header.frame_id = "inference"
        self.yolov8_inference.header.stamp = self.get_clock().now().to_msg()

        yolo_detection = Yolov8Inference()
        weapon_detected = False

        for r in results:
            boxes = r.boxes
            for box in boxes:
                inference_result = InferenceResult()
                b = box.xyxy[0].to('cpu').detach().numpy().copy()  # get box coordinates in (top, left, bottom, right) format
                c = box.cls
                inference_result.class_name = self.model.names[int(c)]
                inference_result.top = int(b[0])
                inference_result.left = int(b[1])
                inference_result.bottom = int(b[2])
                inference_result.right = int(b[3])
                self.yolov8_inference.yolov8_inference.append(inference_result)

                # Check if the detected object is a weapon
                if inference_result.class_name == 'bird' and box.conf > 0.5:
                    weapon_detected = True
                    weapon_location = Point()
                    weapon_location.x = (b[1] + b[3]) / 2
                    weapon_location.y = (b[0] + b[2]) / 2
                    self.weapon_location_pub.publish(weapon_location)

        annotated_frame = results[0].plot()
        img_msg = bridge.cv2_to_imgmsg(annotated_frame)  

        self.img_pub.publish(img_msg)
        self.yolov8_pub.publish(self.yolov8_inference)
        self.object_detection_pub.publish(yolo_detection)

        # Publish weapon alert message if a weapon is detected
        if weapon_detected:
            weapon_alert_msg = String()
            weapon_alert_msg.data = "Weapon detected!"
            self.weapon_alert_pub.publish(weapon_alert_msg)

        self.yolov8_inference.yolov8_inference.clear()

if __name__ == '__main__':
    rclpy.init(args=None)
    camera_subscriber = CameraSubscriber()
    rclpy.spin(camera_subscriber)
    rclpy.shutdown()
