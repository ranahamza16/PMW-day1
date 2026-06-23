# PreserveMy.World - Day 1 3D Reconstruction Research

## Mission Statement
PreserveMy.World is dedicated to the digital preservation of our global heritage. Through advanced 3D reconstruction and immersive technologies, we aim to document, share, and safeguard cultural and historical artifacts for future generations, ensuring they are accessible to anyone, anywhere.

## Table of Contents
- [Mission Statement](#mission-statement)
- [Setup Instructions](#setup-instructions)
- [Tools Used](#tools-used)
- [Project Structure](#project-structure)

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd PMW-day1
   ```
2. **Set up the Python Environment:**
   It is recommended to use Python 3.8+ (Python 3.12+ tested).
   ```bash
   python -m venv venv
   source venv/Scripts/activate # On Windows
   # source venv/bin/activate # On macOS/Linux
   ```
3. **Install Dependencies:**
   ```bash
   pip install torch torchvision timm pillow numpy matplotlib opencv-python jupyter
   ```
4. **Run the Notebook or Script:**
   - Execute the script: `python scripts/simple_3d_reconstruction.py`
   - Or start Jupyter: `jupyter notebook` and open `notebooks/3d_exploration.ipynb`

## Tools Used
- **Python (3.12+)**: Core programming language
- **PyTorch & Torchvision**: Deep learning framework for 3D estimation
- **MiDaS**: Pre-trained model for monocular depth estimation
- **OpenCV & Pillow**: Image processing libraries
- **Matplotlib**: Visualization and plotting
- **Jupyter**: Interactive notebooks
- **Git & GitHub CLI**: Version control and repository management

## Project Structure
- `/research`: Documentation and comparisons of 3D reconstruction methods.
- `/scripts`: Python scripts for running reconstruction models.
- `/notebooks`: Interactive Jupyter notebooks for step-by-step exploration.
- `/docs`: Project documentation, learning notes, and blog drafts.
- `/screenshots`: Saved output visualizations and depth maps.
- `/outputs`: Logs and raw outputs from script execution.
