AutoProcessing.py
Description:

Use this Python script in Agisoft Metashape Professional to automate photogrammetry processing tasks.

Workflow for Processing:

Read Images (geotagged): This step involves reading geotagged images as input for the photogrammetry processing.

Coordinate System Definition: By default, the script defines the EPSG::4326 coordinate system, but you can modify it as per your requirements.

Define Expected Camera Accuracy: By default, the script sets the expected camera accuracy to 0.02 cm. You can modify this value based on your equipment specifications.

Image Alignment: Aligns the input images to establish correspondences between them and create a sparse point cloud.

Camera Optimization: Optimizes the camera parameters to minimize the reprojection error and improve the accuracy of the reconstruction.

Depth Map Generation: Generates depth maps from the aligned images to estimate the depth information for each pixel.

Dense Cloud Generation: Creates a dense point cloud by triangulating the depth information from multiple images.

Save Project: Saves the processed project with the generated dense cloud and other relevant information.

Orthomosaic Generation: Generates an orthomosaic (orthophoto) from the dense point cloud. You can define your desired Ground Sampling Distance (GSD) for the output orthomosaic.

Compute_re-projection_error.py
Description:

This Python script computes the re-projection error in a photogrammetry project using the Metashape library.

Re-projection Error:

Re-projection error is a measure of how accurately the cameras in a photogrammetry project reproduce the positions of points in the scene. This script calculates the re-projection error for each camera in the project and generates a CSV file with the results.
