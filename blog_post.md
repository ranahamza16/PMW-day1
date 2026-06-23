# Exploring the Intersection of AI and Heritage: My Journey into 3D Reconstruction

As a Computer Science student, I've always been fascinated by how software can solve real-world problems. Recently, my focus has shifted toward the intersection of Artificial Intelligence and digital preservation—specifically, 3D reconstruction.

I am thrilled to be participating in the **PreserveMy.World** initiative, a track dedicated to using cutting-edge technology to digitize and preserve cultural heritage.

## Why 3D Reconstruction Matters for Heritage Preservation

Cultural heritage sites, historical artifacts, and ancient architecture are constantly under threat from natural disasters, climate change, and time itself. Once these physical objects are lost or damaged, they are often gone forever.

3D reconstruction matters because it allows us to create highly accurate, immersive digital twins of these artifacts. By transforming 2D images into 3D models, we can:
1. **Preserve History Indefinitely**: Creating digital backups that immune to physical decay.
2. **Increase Accessibility**: Allowing researchers, students, and the general public worldwide to study and experience heritage sites in Virtual Reality or via the web without risking physical damage.
3. **Aid in Restoration**: Providing precise baseline blueprints for restoration teams if physical damage does occur.

## What I've Learned So Far

During my initial research phase, I've learned that modern 3D reconstruction isn't just about manual 3D modeling anymore. We are now leveraging complex Machine Learning algorithms to deduce 3D geometry and view-dependent lighting from a simple set of 2D photographs. 

I've been particularly amazed by the evolution from traditional photogrammetry (like Structure-from-Motion using COLMAP) to neural-based approaches. 

## The Road Ahead: Exploring Gaussian Splatting

The method I am most excited to explore next is **3D Gaussian Splatting**. While Neural Radiance Fields (NeRFs) revolutionized the field by using neural networks to represent scenes, Gaussian Splatting represents the 3D scene using millions of 3D Gaussians (splats). This allows for incredibly fast, real-time rendering of complex scenes without the heavy computational overhead during the inference phase that NeRFs require.

### My Planned Experiment for This Week

Since I am still setting up my environment, I haven't run any code locally yet. However, this week I plan to:
1. Find an open-source Google Colab notebook implementing a baseline Gaussian Splatting pipeline (such as the original Inria implementation or Nerfstudio).
2. Take a dataset of overlapping photographs of an object (perhaps a small statue or artifact).
3. Run COLMAP to extract the camera poses.
4. Train a Gaussian Splatting model on the dataset and render a new camera trajectory.

I will be documenting my terminal outputs, Colab links, and final rendered videos right here on my blog. Stay tuned as I dive deeper into the code!

---
*Follow my progress on [GitHub](https://github.com/ranahamza16) and check out my [Portfolio](https://github.com/ranahamza16/PMW-day1).*
