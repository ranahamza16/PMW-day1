# Learning Notes: Day 1 - 3D Reconstruction

### What I Learned About 3D Methods
- **COLMAP**: Traditional photogrammetry is very robust but requires significant computational power and many overlapping images.
- **NeRF**: Neural Radiance Fields create stunning photorealistic views but take a long time to train and are computationally heavy.
- **Gaussian Splatting**: A newer, faster alternative to NeRFs that enables real-time web rendering, highly relevant for immersive digital exhibits.
- **Structure-from-Motion (SfM)**: Good for extracting 3D structure from video, but sparse compared to dense photogrammetry.
- **Monocular Depth**: Uses AI to guess depth from a single image. It's surprisingly effective for quick 2.5D effects without needing a multi-camera setup.

### Why I Chose Monocular Depth First
For Day 1, monocular depth estimation using the MiDaS model was the perfect entry point. It allowed me to work with just a single image (no complex dataset needed), provided immediate visual feedback, and ran locally without requiring a massive multi-GPU cluster.

### What Surprised Me
I was surprised by how accurately the MiDaS model could distinguish foreground from background on a completely flat, 2D image, just by recognizing contextual cues like shadows, perspective, and object sizes.

### Challenges & Solutions
- **Challenge**: PyTorch and dependencies are huge and complex to install.
- **Solution**: Setup a proper isolated Python virtual environment to keep system dependencies clean.
- **Challenge**: PyTorch Hub paused the execution to ask for repository trust.
- **Solution**: Interacted with the CLI to trust `intel-isl/MiDaS` once, which caches the trust for future runs.

### Connection to PreserveMy.World
Our mission is to safeguard cultural heritage. While true 3D archiving will eventually rely on COLMAP or Gaussian Splatting, Monocular Depth Estimation provides a rapid way to add parallax and pseudo-3D interactivity to historical 2D photos in our archive that can never be re-photographed from other angles.

### Next Steps
Explore running the MiDaS model on a short video clip (frame-by-frame) and look into converting depth maps into 3D point clouds using `Open3D`.
