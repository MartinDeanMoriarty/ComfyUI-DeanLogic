class ImageCount:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",)
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("count",)
    FUNCTION = "count_images"
    CATEGORY = "DeanLogic"

    def count_images(self, images):
        if images is None or not isinstance(images, list) or len(images) == 0:
            return (0,)
        return (len(images),)
