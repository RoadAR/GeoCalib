import json
from contextlib import redirect_stdout
from io import StringIO

from gradio_client import Client, handle_file


IMAGE_PATH = "/home/sasha/Documents/temp/frame_000001.jpg"


with redirect_stdout(StringIO()):
    client = Client("http://localhost:7860")

metrics, result_image = client.predict(
    image_path=handle_file(IMAGE_PATH),
    camera_model="pinhole",
    plot_up=True,
    plot_up_confidence=False,
    plot_latitude=True,
    plot_latitude_confidence=False,
    plot_undistort=False,
    api_name="/process_results",
)

result = {
    "input_image": IMAGE_PATH,
    "metrics": metrics,
    "result_image": result_image,
}

print(json.dumps(result, ensure_ascii=False, indent=2))
