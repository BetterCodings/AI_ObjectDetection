from PIL import Image as im
import torch

def yolo(file):
    model = torch.hub.load('yolov5_code', 'custom',path='yolov5_code/yolov5s.pt', source='local')
    results = model(file)
    results.render()
    img_base64 = im.fromarray(results.ims[0])
    img_base64.save(file, format="JPEG")
yolo("submit/2person.png")

