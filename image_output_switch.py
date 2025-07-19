class ImageOutputSwitch:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "condition": ("BOOLEAN",)
            }
        }

    RETURN_TYPES = ("IMAGE", "IMAGE")
    RETURN_NAMES = ("images_true", "images_false")
    FUNCTION = "switch_outputs"
    CATEGORY = "DeanLogic"

    def switch_outputs(self, images, condition):
        if condition:
            return (images, None)
        else:
            return (None, images)