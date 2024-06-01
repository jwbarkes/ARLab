import os
import numpy as np

def extract_translation_and_rotation(camera_pose_matrix):
    # Extract the translation vector (XYZ) from the transformation matrix
    translation = camera_pose_matrix[:3, 3]

    # Extract the rotation submatrix (3x3) from the transformation matrix
    rotation_submatrix = camera_pose_matrix[:3, :3]

    # Calculate the XYZ Euler angles from the rotation submatrix
    pitch = np.arcsin(-rotation_submatrix[2, 0])              # Rotation around X-axis
    roll = np.arctan2(rotation_submatrix[2, 1], rotation_submatrix[2, 2])  # Rotation around Y-axis
    yaw = np.arctan2(rotation_submatrix[1, 0], rotation_submatrix[0, 0])    # Rotation around Z-axis

    # Convert Euler angles from radians to degrees
    pitch_deg = np.degrees(pitch)
    roll_deg = np.degrees(roll)
    yaw_deg = np.degrees(yaw)

    return translation, (roll_deg, pitch_deg, yaw_deg)

folder = os.listdir("/Users/jbarkes/Desktop/VidToPlace/poses")
folder.sort()

for file in folder:
    with open(os.path.join("poses", file)) as f:
        lines = f.readlines()
        lines = [i.strip().split() for i in lines]
        for i in range(len(lines)):
            lines[i] = [float(j) for j in lines[i]]
        camera_pose_matrix = np.array(lines)
    
    translation, rotation_angles = extract_translation_and_rotation(camera_pose_matrix)
    print("Translation (XYZ):", translation)
    print("Rotation (XYZ Euler Angles):", rotation_angles)