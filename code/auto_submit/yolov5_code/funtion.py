from PIL import Image as im
import torch

model = torch.hub.load('yolov5_code', 'custom',path='yolov5_code/yolov5s.pt', source='local')
results = model('2person.png')
results.render()
img_base64 = im.fromarray(results.ims[0])
img_base64.save("image1.jpg", format="JPEG")
inference_img = "image1.jpg"
