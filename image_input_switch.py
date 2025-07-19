class ImageInputSwitch:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_true": ("IMAGE",),
                "image_false": ("IMAGE",),
                "condition": ("BOOLEAN",)
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "switch_inputs"
    CATEGORY = "DeanLogic"

    def switch_image(self, image_true, image_false, condition):
        def is_valid(image_input):
            if image_input is None:
                return False
            if isinstance(image_input, list) and len(image_input) == 0:
                return False
            return True

        chosen = image_true if condition else image_false
        return (chosen if is_valid(chosen) else None,)