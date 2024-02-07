# Compute the re-projection error
import Metashape
import math
import statistics
import csv

doc = Metashape.app.document
chunk = doc.chunk
point_cloud = chunk.point_cloud
points = point_cloud.points
error, tie_points = [], []
cam_list, cam_rmse, cam_std, cam_min, cam_max, cam_std = [], [], [], [], [], []
for camera in [cam for cam in doc.chunk.cameras if cam.transform]:
    point_index = 0
    photo_num = 0
    cam_error=[]
    for proj in doc.chunk.point_cloud.projections[camera]:
        track_id = proj.track_id
        while point_index < len(points) and points[point_index].track_id < track_id:
            point_index += 1
        if point_index < len(points) and points[point_index].track_id == track_id:
            if not points[point_index].valid:
                continue
            dist = camera.error(points[point_index].coord, proj.coord).norm() ** 2
            error.append(dist)
            cam_error.append(dist)
            photo_num += 1       
    tie_points.append(photo_num)
    cam_list.append(camera.label)
    cam_rmse.append(round(math.sqrt(sum(error) / len(error)), 3))
    cam_std.append(round(statistics.stdev(error), 3))
    cam_max.append(round(max(error) , 3))
    cam_min.append(round(min(error) , 3))

print("Camera_errors",cam_error)
print("Cam_RMSE_error",cam_rmse)
print("Cam_std_error",cam_std)
print("Cam_max_and_min_error",cam_max, cam_min)

with open("Reprojection_Error.csv","w",newline='') as cam_log:
    fieldnames = ['cam_error', 'cam_rmse', 'cam_std']
    writer = csv.DictWriter(cam_log, fieldnames = fieldnames, delimiter=',', escapechar="\\", quoting=csv.QUOTE_NONE)
    
    writer.writeheader()
    writer.writerow({'cam_error':cam_error, 'cam_rmse':cam_rmse, 'cam_std':cam_std})