import torch
from geocalib import GeoCalib

device = "cuda" if torch.cuda.is_available() else "cpu"
model = GeoCalib().to(device)

# load image as tensor in range [0, 1] with shape [C, H, W]
image = model.load_image("/home/sasha/Documents/temp/remove_me_real/blender_moving_camera/0014.jpg").to(device)
result = model.calibrate(image)

print("camera:", result["camera"].numpy())
print("gravity:", result["gravity"].numpy())
