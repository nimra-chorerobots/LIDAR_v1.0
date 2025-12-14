"""
============================================================
LiDAR Scene Chunking & Perception Visualization
============================================================

WHAT THIS PROGRAM DOES (IN VERY SIMPLE WORDS):
----------------------------------------------
• Takes a large LiDAR point cloud (millions of points)
• Breaks it into smaller, meaningful local scenes
• Separates flat ground from above-ground objects
• Shows each local scene in an interactive 3D window

WHY THIS IS IMPORTANT:
----------------------
Real robots never look at the whole world at once.
They only look at a small area around themselves.
This code shows EXACTLY how that perception stage works.

This is:
✓ Visualization
✓ Perception-stage processing
✓ Data understanding

This is NOT:
✗ AI training
✗ Object detection
✗ Classification models
"""

# ============================================================
# LIBRARIES (TOOLS WE USE)
# ============================================================

import pyvista as pv
# pyvista:
# Used to show interactive 3D point clouds
# Allows rotating, zooming, and inspecting LiDAR scenes

import plyfile
# plyfile:
# Reads LiDAR .ply files (a common point cloud format)

import numpy as np
# numpy:
# Used for math and array operations on point data

import os
# os:
# Used to work with file paths and folders


# ============================================================
# CONFIGURATION (SAFE TO CHANGE)
# ============================================================

# Folder that contains LiDAR .ply files
DATA_DIR = r"D:\Chorerobotics\codes\lidar_dataset1"

# Size of local perception window (meters)
# Think of this as "how far the robot looks around itself"
WINDOW_RADIUS = 20.0

# Distance between two neighboring windows
STEP_SIZE = 15.0

# Maximum number of points shown at once
# (prevents slow rendering)
MAX_POINTS = 180_000

# Ignore very small chunks (usually noise)
MIN_POINTS_PER_CHUNK = 800

# Show only a few best chunks (boss-friendly)
MAX_CHUNKS_TO_SHOW = 8


# ============================================================
# LOAD ONE LiDAR FILE
# ============================================================

def load_ply(path):
    """
    Reads a .ply LiDAR file and extracts XYZ coordinates.

    Each row returned is one LiDAR point:
    [x position, y position, z height]
    """

    ply = plyfile.PlyData.read(path)
    v = ply["vertex"].data

    # Combine x, y, z into a single array
    points = np.vstack((v["x"], v["y"], v["z"])).T

    return points


# ============================================================
# SPLIT LARGE SCENE INTO LOCAL PERCEPTION WINDOWS
# ============================================================

def extract_local_chunks(points):
    """
    Breaks a huge LiDAR scene into smaller local chunks.

    Each chunk represents what the robot would
    "see" in a local area.
    """

    # Use only X and Y for windowing
    xy = points[:, :2]

    # Create sliding window centers
    xs = np.arange(xy[:, 0].min(), xy[:, 0].max(), STEP_SIZE)
    ys = np.arange(xy[:, 1].min(), xy[:, 1].max(), STEP_SIZE)

    chunks = []

    # Slide window across the entire scene
    for cx in xs:
        for cy in ys:

            # Select points inside this local window
            mask = (
                (np.abs(xy[:, 0] - cx) < WINDOW_RADIUS) &
                (np.abs(xy[:, 1] - cy) < WINDOW_RADIUS)
            )

            chunk = points[mask]

            # Ignore empty or tiny windows
            if chunk.shape[0] >= MIN_POINTS_PER_CHUNK:
                chunks.append(chunk)

    return chunks


# ============================================================
# SHOW ONE LOCAL PERCEPTION CHUNK
# ============================================================

def show_chunk(chunk, title):
    """
    Displays one local LiDAR scene.

    Gray points   → ground
    Colored points → objects above ground
    """

    # Reduce number of points if needed
    if chunk.shape[0] > MAX_POINTS:
        idx = np.random.choice(chunk.shape[0], MAX_POINTS, replace=False)
        chunk = chunk[idx]

    # Move scene center to (0,0,0)
    # This is called ego-centric normalization
    chunk = chunk - chunk.mean(axis=0)

    # --------------------------------------------------------
    # SIMPLE GROUND SEPARATION
    # --------------------------------------------------------
    # Ground is usually the lowest points
    z = chunk[:, 2]

    # Bottom 20% of points = ground
    ground_thresh = np.percentile(z, 20)

    ground_mask = z <= ground_thresh
    object_mask = ~ground_mask

    ground = chunk[ground_mask]
    objects = chunk[object_mask]

    # --------------------------------------------------------
    # VISUALIZATION
    # --------------------------------------------------------
    p = pv.Plotter(window_size=(1200, 900))

    p.add_text(
        f"{title}\nGray = Ground | Colored = Objects",
        font_size=11
    )

    # Draw ground
    if ground.shape[0] > 0:
        p.add_points(
            pv.PolyData(ground),
            color="lightgray",
            point_size=2,
            render_points_as_spheres=True
        )

    # Draw objects
    if objects.shape[0] > 0:
        cloud_obj = pv.PolyData(objects)
        cloud_obj["height"] = objects[:, 2]

        p.add_points(
            cloud_obj,
            scalars="height",
            cmap="turbo",
            point_size=3,
            render_points_as_spheres=True
        )

    p.show_axes()
    p.enable_eye_dome_lighting()
    p.show()


# ============================================================
# MAIN PROGRAM STARTS HERE
# ============================================================

# Find all LiDAR files
files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".ply")])

# Use first file as demo
scene = files[0]
print(f"Loading {scene}")

# Load LiDAR points
points = load_ply(os.path.join(DATA_DIR, scene))

# Split into local scenes
chunks = extract_local_chunks(points)
print(f"Generated {len(chunks)} local scene chunks")

# Sort chunks by size (largest = most informative)
chunks_sorted = sorted(chunks, key=lambda x: x.shape[0], reverse=True)

# Show only a few best chunks
for i, chunk in enumerate(chunks_sorted[:MAX_CHUNKS_TO_SHOW]):
    show_chunk(chunk, f"Local Perception Chunk {i+1}")

print("✅ Done — perception chunks displayed successfully")
