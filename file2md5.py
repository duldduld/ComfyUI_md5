import hashlib
import os
import io

class FileToMD5:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "case": (["lower", "upper"], {"default": "lower"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("md5_hash",)
    FUNCTION = "calculate_file_md5"
    CATEGORY = "utils/hash"
    OUTPUT_NODE = True

    def calculate_file_md5(self, file_path, case):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            if not os.path.isfile(file_path):
                raise ValueError(f"Invalid file: {file_path}")
            
            md5_hash = hashlib.md5()
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5_hash.update(chunk)
            
            full_hash = md5_hash.hexdigest()
            
            if case == "lower":
                result_hash = full_hash.lower()
            else:
                result_hash = full_hash.upper()
            
            return (result_hash,)
            
        except Exception as e:
            print(f"Error while making md5: {e}")
            return ("error",)

NODE_CLASS_MAPPINGS = {
    "FileToMD5": FileToMD5,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FileToMD5": "File to MD5", 
}
