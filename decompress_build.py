import brotli
import os

build_dir = "Build"

for filename in os.listdir(build_dir):
    if filename.endswith(".br"):
        filepath = os.path.join(build_dir, filename)
        output_path = filepath[:-3]  # strip ".br"
        
        with open(filepath, "rb") as f:
            compressed_data = f.read()
        
        decompressed_data = brotli.decompress(compressed_data)
        
        with open(output_path, "wb") as f:
            f.write(decompressed_data)
        
        print(f"Decompressed: {filename} -> {os.path.basename(output_path)}")