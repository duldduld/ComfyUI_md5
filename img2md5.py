import torch
import hashlib

class ImgToMD5:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE", {"forceInput": True}),
                "case": (["lower", "upper"], {"default": "lower"}),
            },
            "optional": {
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("md5_hash",)
    FUNCTION = "convert_image_to_md5"
    CATEGORY = "utils/hash"
    OUTPUT_NODE = True

    def convert_image_to_md5(self, image, case):                
        try:
            md5_hash = hashlib.md5()
            content = image.numpy().tobytes()            
            md5_hash.update(content)
            full_hash = md5_hash.hexdigest()
            
            if case == "lower":
                result_hash = full_hash.lower()
            else:
                result_hash = full_hash.upper()
                
            return (result_hash,)
            
        except Exception as e:
            error_msg = f"Error while making md5: {e}"
            print(error_msg)
            return (f"error: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "ImgToMD5": ImgToMD5
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImgToMD5": "Image to MD5"
}
