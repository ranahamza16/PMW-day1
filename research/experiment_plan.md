# 3D Reconstruction Experiment Plan - Day 1

**Chosen Method**: Monocular Depth Estimation (Beginner-Safe)
**Goal**: Implement a basic pipeline to extract depth information from a single 2D image to understand AI-driven spatial understanding.

## Expected Timeline (Week-long progression)

- **Day 1**: Set up environment, research methods, and run a pre-trained monocular depth model (MiDaS) on a single test image.
- **Day 2**: Expand to batch processing multiple images; explore different MiDaS model variants.
- **Day 3**: Convert 2D depth maps into 3D point clouds using Open3D.
- **Day 4**: Try capturing a video and applying depth estimation frame-by-frame.
- **Day 5**: Document findings and prepare a mini-portfolio of reconstructed depth maps for PreserveMy.World.

## Folder Structure for Outputs

```text
/PMW-day1
├── /scripts
│   └── simple_3d_reconstruction.py
├── /notebooks
│   └── 3d_exploration.ipynb
├── /screenshots
│   └── depth_map_output.png (Visualization of depth)
├── /outputs
│   └── run_log.txt (Terminal/Console outputs)
```

## Expected Outputs

1. **`depth_map_output.png`**: A side-by-side or combined visual showing the original image and its grayscale/inferno depth map representation.
2. **`run_log.txt`**: Standard output confirming the model loaded successfully and the inference time.

## Success Criteria

- The Python script executes without throwing runtime errors.
- The depth map output accurately reflects near objects as lighter/brighter and far objects as darker (or vice versa depending on the colormap).
- The output files are successfully generated and saved in their respective directories.

## Fallback Options

- **Failure**: PyTorch fails to install or recognize hardware.
  - *Fallback*: Switch to using a Google Colab notebook to bypass local hardware/environment issues.
- **Failure**: MiDaS model fails to download via `torch.hub`.
  - *Fallback*: Download the model weights manually from GitHub/HuggingFace and load them locally, or use the `transformers` library pipeline instead.
