# library import
import PhotoScan
import Metashape
import os

doc = PhotoScan.app.document
chunk = doc.chunk

project_path = "E:\\42L_R&D\\08-11-2022\\Images_geotagged\\"
project_name = "42L_Test_07112022"

# image list
image_list = os.listdir(project_path)
photo_list = []

for photo in image_list:
    if photo.rsplit('.',1)[1] .lower() in ['jpg', 'jpeg', 'tif', 'tiff']:
        photo_list.append(project_path + photo)
    else:
        print('Sorry! No photo available')
print(photo_list)
PhotoScan.app.update()
chunk.addPhotos(photo_list)

# Coordinate System
chunk.crs = Metashape.CoordinateSystem("EPSG::4326")
chunk.updateTransform
PhotoScan.app.update()

# Reference Settings | Import camera locations from EXIF meta data
chunk.loadReferenceExif(load_rotation=True, load_accuracy=True)


# save
location ="E:\\42L_R&D\\08-11-2022\\Processing_file\\42L_Test_08112022.psx" 

# Expected camera location accuracy
chunk.camera_location_accuracy= Metashape.Vector([0.02,0.02,0.02])
PhotoScan.app.update()

#Align photos
chunk.matchPhotos(downscale=2, generic_preselection=True, reference_preselection=True,filter_mask = False, keypoint_limit = 40000, tiepoint_limit = 4000) 
chunk.alignCameras()

#Optimize Cameras
chunk.optimizeCameras(fit_f=True, fit_cx=True, fit_cy=True, fit_b1=True, fit_b2=True, fit_k1=True,fit_k2=True, fit_k3=True, fit_k4=True, fit_p1=True, fit_p2=True, fit_p3=False,fit_p4=False)

#build dense cloud
chunk.buildDepthMaps(downscale= 2, filter_mode = Metashape.ModerateFiltering)
chunk.buildDenseCloud(point_colors = True)

#Export Points
#chunk.exportPoints(project_path + project_name + ".las", binary=True, save_colors=True, format=PhotoScan.PointsFormatLAS)

#Save Project
doc.save(location)
chunk = doc.chunk

#DEM
chunk.buildDem(source_data=PhotoScan.DenseCloudData, interpolation=PhotoScan.EnabledInterpolation)

#Build Ortho
chunk.buildOrthomosaic(surface_data=PhotoScan.ElevationData, blending_mode=PhotoScan.MosaicBlending, fill_holes=True, resolution=0.015)

#Save Project
doc.save(location)
chunk = doc.chunk

print("Done")