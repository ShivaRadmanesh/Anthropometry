
import trimesh
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure


def project(img_path, output_path):
    mesh = trimesh.load_mesh(img_path)
    filename = img_path.split('/')[-1:][0].split("-")[0]

    plane = trimesh.points.project_to_plane(mesh.vertices, plane_normal=[0,0,1],plane_origin=[0,0,0])

    data = np.array(plane)
    x, y = data.T
    diffy = math.ceil(np.amax(y)) - math.floor(np.amin(y))
    diffx =  math.ceil(np.amax(x)) - math.floor(np.amin(x))
    margin_percentage = 20
    margin_x = margin_percentage / 100 * diffx
    margin_y = margin_percentage / 100 * diffy



    px = 1/plt.rcParams['figure.dpi']  # pixel in inches

    pixel_size_in_mm = 4
    plt.subplots(figsize=((diffx+margin_x)*px*pixel_size_in_mm, (diffy+margin_y)*px*pixel_size_in_mm))


    plt.xlim([math.floor(np.amin(x)) - margin_x/2, math.ceil(np.amax(x))  + margin_x/2])
    plt.ylim([math.floor(np.amin(y)) - margin_y/2, math.ceil(np.amax(y))  + margin_y/2])
    plt.scatter(x,y)

    plt.axis('off')
    plt.tight_layout(pad=0)

    plt.savefig(f"{output_path}/{filename}.png")




