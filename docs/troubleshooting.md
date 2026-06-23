# Troubleshooting & Notes

During our initial setup and execution of the Monocular Depth Estimation script, we encountered and resolved the following issues:

### 1. Missing Dependencies
**Issue**: Running the script directly yielded a `ModuleNotFoundError` for PyTorch.
**Solution**: We initialized a Python virtual environment (`venv`) and installed the required deep learning libraries (`torch`, `torchvision`, `timm`, `opencv-python`, `matplotlib`).

### 2. PyTorch Hub Trust Warning
**Issue**: When downloading the `intel-isl/MiDaS` model for the first time, PyTorch paused execution to ask if we trusted the repository.
**Solution**: We manually sent an input (`y`) to the background task to approve adding the repository to the trusted list. In future runs, this step will be skipped automatically since it's cached in `~/.cache/torch/hub/`.

### 3. File Format Compatibility
**Issue**: The default script expected a `.jpg` image, but the test image provided was a `.jpeg`.
**Solution**: Modified both the Python script and the Jupyter Notebook to point to the correct `.jpeg` extension to prevent file-not-found errors.
