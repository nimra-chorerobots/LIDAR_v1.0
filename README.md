# LiDAR Scene Chunking & Perception Visualization

### Interactive LiDAR Perception Pipeline for Local Scene Analysis and 3D Visualization

This repository provides an interactive LiDAR perception pipeline for robotics and autonomous systems. It processes large **LiDAR point clouds** stored in `.ply` format by dividing them into smaller local perception windows, separating ground from elevated objects, and visualizing each region in an interactive 3D viewer.

The project is designed for qualitative scene inspection, perception research, and preparation for downstream tasks such as obstacle detection, mapping, navigation, and sensor fusion.

---

# 📌 Overview

LiDAR sensors generate dense three-dimensional point clouds that capture detailed geometric information about the surrounding environment. Processing an entire scene simultaneously can be computationally expensive and difficult to interpret.

This project demonstrates a lightweight visualization pipeline that divides large LiDAR scans into smaller overlapping regions, representing the local perception windows typically processed by autonomous robots.

The pipeline performs:

- LiDAR point-cloud loading
- XYZ coordinate extraction
- Scene chunking and windowing
- Ground and object separation
- Height-based object coloring
- Interactive 3D visualization
- Selection of informative local perception windows

The repository is intended for:

- LiDAR perception research
- Robotics education
- Dataset exploration
- Autonomous navigation research
- Preprocessing before machine learning
- Sensor fusion development

---

# 🚀 Features

- Load LiDAR point clouds from `.ply` files
- Extract XYZ coordinates into NumPy arrays
- Divide large scenes into overlapping perception windows
- Perform simple ground–object separation
- Color elevated objects according to height
- Interactive PyVista visualization
- Curated display of representative scene chunks
- Runtime inspection using rotation, zooming, and panning

---

# 📂 Input Data

The pipeline supports LiDAR point clouds stored in the standard **PLY** format.

Example directory structure:

```text
data/
└── sample_point_cloud.ply
```

Supported datasets include:

- KITTI
- SemanticKITTI
- NuScenes LiDAR
- Custom PLY point clouds

---

# 🔄 Processing Pipeline

```text
PLY Point Cloud
        │
        ▼
Point Cloud Loading
        │
        ▼
XYZ Coordinate Extraction
        │
        ▼
Scene Chunking
        │
        ▼
Ground–Object Separation
        │
        ▼
Height-Based Coloring
        │
        ▼
Interactive 3D Visualization
```

---

# ⚙️ How It Works

## 1️⃣ Point Cloud Loading

The pipeline reads a `.ply` file and extracts the X, Y, and Z coordinates into a NumPy array for further processing.

---

## 2️⃣ Scene Chunking

Instead of processing an entire LiDAR scan simultaneously, the scene is divided into smaller overlapping windows across the X–Y plane.

Each chunk represents a local perception region similar to the area processed by a mobile robot at any given time.

---

## 3️⃣ Ground–Object Separation

Within each local chunk:

- Approximately the lowest 20% of points (based on height) are classified as ground.
- Remaining elevated points are treated as objects.
- Ground points are displayed in **gray**.
- Elevated points are color-coded according to their height.

> **Note:** This method is intended for visualization and qualitative inspection only. It is not a semantic segmentation or production-grade ground extraction algorithm.

---

## 4️⃣ Interactive Visualization

Each selected chunk is displayed in an interactive PyVista window.

Supported interactions include:

- Rotation
- Zooming
- Panning
- Multi-angle inspection
- Depth perception

---

# 🖼 Example Results

*(Insert screenshots of your LiDAR visualization here.)*

Recommended images:

- Original Point Cloud
- Scene Chunking
- Ground vs Object Separation
- Interactive 3D Visualization

---

# 🖥 Visualization Notes

LiDAR data is inherently three-dimensional, making interactive visualization significantly more informative than static images.

For the best experience:

- Rotate the scene from different viewpoints
- Zoom into dense object regions
- Inspect multiple scene chunks
- Adjust chunk size and overlap parameters
- Modify the ground threshold if necessary

---

# 📈 Representative Results

The visualization demonstrates:

- Efficient scene chunking
- Clear separation between ground and elevated structures
- Consistent height-based visualization
- Improved local scene interpretability
- Interactive exploration of LiDAR geometry

The displayed windows represent only a subset of the complete point cloud, allowing users to focus on informative regions while maintaining computational efficiency.

---

# 🏗 Architecture

```text
LiDAR Point Cloud (.ply)
        │
        ▼
Point Cloud Loader
        │
        ▼
Scene Chunk Generator
        │
        ▼
Ground Separation
        │
        ▼
Height-Based Coloring
        │
        ▼
Interactive 3D Viewer
```

---

# 🚀 Project Status

🟢 **Prototype**

### Current Features

- PLY point-cloud loading
- Scene chunking
- Ground separation
- Height-based object coloring
- Interactive 3D visualization
- Local perception window generation

### Planned Improvements

- ROS 2 integration
- NVIDIA Isaac Sim integration
- Advanced ground-plane estimation
- Euclidean obstacle clustering
- 3D bounding-box generation
- Real-time LiDAR streaming
- Camera-LiDAR sensor fusion
- Obstacle tracking
- Navigation safety output

---

# 📂 Repository Structure

```text
chore-lidar-perception/
│
├── src/
│   └── lidar_visualization.py
│
├── assets/
│   ├── input/
│   ├── output/
│   └── examples/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── CHANGELOG.md
└── CITATION.cff
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/nimra-chorerobots/chore-lidar-perception.git

cd chore-lidar-perception
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install numpy pyvista plyfile
```

---

# 📦 Requirements

- Python 3.9+
- NumPy
- PyVista
- plyfile

Example `requirements.txt`

```text
numpy
pyvista
plyfile
```

---

# ▶️ Running the Project

```bash
python src/lidar_visualization.py
```

Update the input `.ply` file path inside the script before execution.

---

# 💡 Applications

This visualization pipeline can be used for:

- Autonomous mobile robotics
- LiDAR perception research
- Sensor fusion development
- Point-cloud preprocessing
- Robot navigation
- Educational demonstrations
- Digital twin visualization
- Autonomous vehicle research

---

# 🔮 Future Work

Future versions of this repository will include:

- Semantic segmentation
- Object clustering
- Dynamic obstacle detection
- Multi-sensor fusion
- ROS 2 nodes
- NVIDIA Isaac Sim integration
- Real-time LiDAR processing
- Occupancy mapping
- SLAM integration

 
