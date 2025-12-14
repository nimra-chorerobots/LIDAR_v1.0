import pyvista as pv
import plyfile
import numpy as np
import os

# ============================================================
# CONFIGURATION (EDIT ONLY THESE IF NEEDED)
# ============================================================

DATA_DIR = r"D:\Chorerobotics\codes\lidar_dataset1"
WINDOW_RADIUS = 20.0        # meters (local perception radius)
STEP_SIZE = 15.0            # sliding window step
MAX_POINTS = 180_000        # safety cap for rendering
MIN_POINTS_PER_CHUNK = 800  # ignore tiny/noisy chunks
MAX_CHUNKS_TO_SHOW = 8      # boss-friendly number

# ============================================================
# LOAD LiDAR (.ply)
# ============================================================

def load_ply(path):
    ply = plyfile.PlyData.read(path)
    v = ply["vertex"].data
    points = np.vstack((v["x"], v["y"], v["z"])).T
    return points

# ============================================================
# SPLIT INTO LOCAL PERCEPTION WINDOWS
# ============================================================

def extract_local_chunks(points):
    xy = points[:, :2]

    xs = np.arange(xy[:, 0].min(), xy[:, 0].max(), STEP_SIZE)
    ys = np.arange(xy[:, 1].min(), xy[:, 1].max(), STEP_SIZE)

    chunks = []

    for cx in xs:
        for cy in ys:
            mask = (
                (np.abs(xy[:, 0] - cx) < WINDOW_RADIUS) &
                (np.abs(xy[:, 1] - cy) < WINDOW_RADIUS)
            )

            chunk = points[mask]
            if chunk.shape[0] >= MIN_POINTS_PER_CHUNK:
                chunks.append(chunk)

    return chunks

# ============================================================
# SHOW ONE PERCEPTION CHUNK (GROUND vs OBJECTS)
# ============================================================

def show_chunk(chunk, title):
    # Downsample if needed
    if chunk.shape[0] > MAX_POINTS:
        idx = np.random.choice(chunk.shape[0], MAX_POINTS, replace=False)
        chunk = chunk[idx]

    # Ego-centric normalization
    chunk = chunk - chunk.mean(axis=0)

    # --- Simple ground separation (height-based) ---
    z = chunk[:, 2]
    ground_thresh = np.percentile(z, 20)
    ground_mask = z <= ground_thresh
    object_mask = ~ground_mask

    ground = chunk[ground_mask]
    objects = chunk[object_mask]

    # --- Create PyVista objects ---
    p = pv.Plotter(window_size=(1200, 900))
    p.add_text(
        f"{title}\nGray = Ground | Colored = Objects",
        font_size=11
    )

    if ground.shape[0] > 0:
        p.add_points(
            pv.PolyData(ground),
            color="lightgray",
            point_size=2,
            render_points_as_spheres=True
        )

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
# MAIN
# ============================================================

files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".ply")])
scene = files[0]

print(f"Loading {scene}")

points = load_ply(os.path.join(DATA_DIR, scene))

chunks = extract_local_chunks(points)
print(f"Generated {len(chunks)} local scene chunks")

# Sort chunks by usefulness (largest first)
chunks_sorted = sorted(chunks, key=lambda x: x.shape[0], reverse=True)

# Show only curated chunks
for i, chunk in enumerate(chunks_sorted[:MAX_CHUNKS_TO_SHOW]):
    show_chunk(chunk, f"Local Perception Chunk {i+1}")

print("✅ Done — perception chunks displayed successfully")
