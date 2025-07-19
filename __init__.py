from .image_output_switch import ImageOutputSwitch
from .image_input_switch import ImageInputSwitch
from .int_compare import IntCompare
from .image_count import ImageCount

NODE_CLASS_MAPPINGS = {
    "ImageOutputSwitch": ImageOutputSwitch,
    "ImageInputSwitch": ImageInputSwitch,
    "Int Compare": IntCompare,
    "ImageCount": ImageCount     
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageOutputSwitch": "Image Output Switch (Boolean)",
    "ImageInputSwitch": "Image Input Switch (Boolean)",
    "Int Compare": "Int Compare",
    "ImageCount": "Image Count"
}