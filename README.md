# LiDAR Scene Chunking & Perception Visualization

Interactive, scene-based LiDAR visualization for robotics perception.  
This project splits large `.ply` LiDAR point clouds into **local perception windows**, separates **ground vs. objects**, and visualizes each chunk in an **interactive 3D viewer**.

---

## Demo

- Each window represents a **local perception chunk**
- **Ground** points are shown in **gray**
- **Objects** above ground are **colored by height**
- Visualization is **interactive** (rotate / zoom / pan)

> ℹ️ This repository focuses on **perception-stage visualization** only.  
> It does **not** include model training, detection, or evaluation.

---

## Features

- Load LiDAR point clouds from `.ply`
- Spatial **scene chunking / windowing**
- Simple **ground vs. object separation**
- Interactive 3D visualization (PyVista)
- Curated display of the most informative chunks

---

## How It Works

1. **Load Point Cloud**

Reads a .ply file and extracts XYZ coordinates into a NumPy array.

2. **Scene Chunking**

The large LiDAR scan is split into smaller, overlapping local windows in the X–Y plane.
Each window represents a region a robot would process at one time.

3. **Ground vs. Objects**

For each chunk:

The lowest ~20% of points (by height) are treated as ground

Remaining points are treated as objects

This split is for visual clarity, not semantic labeling

---

## Visualization Notes**

LiDAR data is inherently 3D.
Static images often hide depth and geometry, so this project emphasizes runtime interactive visualization.

For best results:

Rotate, zoom, and pan the scene

Inspect multiple chunks

Adjust configuration parameters if needed

---

## Project Structure
.
<img width="752" height="258" alt="image" src="https://github.com/user-attachments/assets/25883889-445f-4f1c-884b-c96c00b001b6" />


---

## Requirements

- Python 3.9+ (tested with Python 3.11)
- `numpy`
- `pyvista`
- `plyfile`

Install dependencies:

```bash
pip install numpy pyvista plyfile
 

