class IntCompare:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "a": ("INT", {"default": 0}),
                "b": ("INT", {"default": 0}),
                "comparison": (["<", ">", "=="],)
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("result",)
    FUNCTION = "compare"
    CATEGORY = "DeanLogic"

    def compare(self, a, b, comparison):
        if comparison == "<":
            return (a < b,)
        elif comparison == ">":
            return (a > b,)
        elif comparison == "==":
            return (a == b,)
        else:
            # Sicher ist sicher: Bei unbekannter Option false
            return (False,)