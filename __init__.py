from .image_output_switch import ImageOutputSwitch
from .image_input_switch import ImageInputSwitch
from .image_count import ImageCount

NODE_CLASS_MAPPINGS = {
    "ImageOutputSwitch": ImageOutputSwitch,
    "ImageInputSwitch": ImageInputSwitch,
    "ImageCount": ImageCount     
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageOutputSwitch": "Image Output Switch (Boolean)",
    "ImageInputSwitch": "Image Input Switch (Boolean)",
    "ImageCount": "Image Count"
}