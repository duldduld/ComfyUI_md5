import hashlib

class StringToMD5:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_string": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "case": (["lower", "upper"], {"default": "lower"}),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("md5_hash",)
    FUNCTION = "convert_string_to_md5"
    CATEGORY = "utils/hash"
    OUTPUT_NODE = True

    def convert_string_to_md5(self, input_string, case):
        md5_hash = hashlib.md5()
        md5_hash.update(input_string.encode('utf-8'))
        full_hash = md5_hash.hexdigest()

        if case == "lower":
            result_hash = full_hash.lower()
        else:
            result_hash = full_hash.upper()

        return (result_hash,)

NODE_CLASS_MAPPINGS = {
    "StringToMD5": StringToMD5
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringToMD5": "String to MD5"
}
