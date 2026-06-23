import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def run_depth_estimation(image_path, output_path):
    print(f"Loading MiDaS model for depth estimation...")
    # 1. Load MiDaS model
    try:
        model_type = "DPT_Large"     # MiDaS v3 - Large
        
        # Load from PyTorch Hub
        midas = torch.hub.load("intel-isl/MiDaS", model_type)
        
        # Move model to GPU if available
        device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        print(f"Using device: {device}")
        midas.to(device)
        midas.eval()
        
        # Load transforms to resize and normalize the image
        midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        transform = midas_transforms.dpt_transform
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

    # 2. Prepare input image
    print(f"Reading input image from {image_path}...")
    if not os.path.exists(image_path):
        print(f"Error: Could not find image at {image_path}. Please place an image there.")
        sys.exit(1)
        
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Failed to load image at {image_path}.")
        sys.exit(1)
        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    input_batch = transform(img).to(device)

    # 3. Run inference
    print("Running depth estimation...")
    with torch.no_grad():
        prediction = midas(input_batch)
        
        # Resize the prediction to match the original image resolution
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()
    
    output = prediction.cpu().numpy()

    # 4. Visualize depth map
    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.axis("off")
    
    plt.subplot(1, 2, 2)
    plt.title("Depth Map")
    plt.imshow(output, cmap='inferno')
    plt.axis("off")
    
    # 5. Save output
    print(f"Saving output to {output_path}...")
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    
    # 6. Print success message
    print(f"Success! Depth map saved to {output_path}")

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sample_img = os.path.join(base_dir, 'sample_image.jpeg')
    out_img = os.path.join(base_dir, 'screenshots', 'depth_map_output.png')
    
    run_depth_estimation(sample_img, out_img)
