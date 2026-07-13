# LiDAR Scene Chunking & Perception Visualization

### Interactive LiDAR Perception Pipeline for Local Scene Analysis and 3D Visualization

This repository provides an interactive LiDAR perception pipeline for robotics and autonomous systems. It processes large **LiDAR point clouds** stored in `.ply` format by dividing them into smaller local perception windows, separating ground from elevated objects, and visualizing each region in an interactive 3D viewer.

Unlike traditional perception pipelines that generate static outputs, this project focuses on **interactive qualitative visualization**, allowing users to explore LiDAR scenes dynamically for perception research, robotics development, and autonomous navigation.

---

# 📌 Overview

LiDAR sensors generate dense three-dimensional point clouds that capture detailed geometric information about the surrounding environment. Processing an entire scene simultaneously can be computationally expensive and difficult to interpret.

This project demonstrates a lightweight visualization pipeline that divides large LiDAR scans into smaller overlapping regions, representing the local perception windows typically processed by autonomous robots.

The pipeline performs:

- LiDAR point-cloud loading
- XYZ coordinate extraction
- Scene chunking and windowing
- Ground–object separation
- Height-based object coloring
- Interactive 3D visualization
- Selection of representative local perception windows

The repository is intended for:

- LiDAR perception research
- Robotics education
- Dataset exploration
- Autonomous navigation research
- Point-cloud preprocessing
- Sensor fusion development

---

# 🚀 Features

- Load LiDAR point clouds from `.ply` files
- Extract XYZ coordinates into NumPy arrays
- Divide large scenes into overlapping perception windows
- Perform simple ground–object separation
- Color elevated objects according to height
- Interactive PyVista visualization
- Runtime exploration using rotation, zooming, and panning
- Lightweight qualitative perception analysis

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

> **Note:** This approach is intended for visualization and qualitative inspection. It is not a semantic segmentation or production-grade ground extraction algorithm.

---

## 4️⃣ Interactive Visualization

Each selected perception window is rendered using **PyVista**, providing a fully interactive 3D environment for scene exploration.

The visualization supports:

- Rotation
- Zooming
- Panning
- Multi-angle inspection
- Depth perception
- Interactive exploration of local scene geometry

---

# 🖥 Interactive Visualization

Unlike conventional computer vision projects that generate static output images, this repository provides a **live interactive visualization experience**.

During execution, the pipeline automatically:

- Loads the LiDAR point cloud
- Generates local perception windows
- Separates ground from elevated objects
- Applies height-based coloring
- Opens interactive PyVista visualization windows

Users can freely rotate, zoom, and inspect each perception chunk in real time, providing a much deeper understanding of the scene geometry than static screenshots.

The number of displayed scene chunks can be configured within the source code, allowing representative regions to be explored without rendering the complete point cloud.

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
- Ground–object separation
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
- Camera–LiDAR sensor fusion
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

Install the required dependencies:

```bash
pip install -r requirements.txt
```

or manually:

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

Run the visualization pipeline:

```bash
python src/lidar_visualization.py
```

Update the input `.ply` file path inside the script before execution.

During runtime, interactive visualization windows will automatically open, allowing exploration of the generated perception chunks.

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
- Interactive perception debugging

---

# 🔮 Future Work

Future versions of this repository will include:

- Semantic segmentation
- Object clustering
- Dynamic obstacle detection
- Multi-sensor fusion
- ROS 2 integration
- NVIDIA Isaac Sim integration
- Real-time LiDAR processing
- Occupancy mapping
- SLAM integration
- Autonomous navigation support

 
