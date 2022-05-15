import os
import sys
import time
import numpy as np
import skimage
from skimage import io
from PIL import Image
import pathlib
from pyDF import *

save_dir = 'negative_imgs'
imgs_folder = str(os.path.dirname(os.path.realpath(__file__))) + "/imgs"

def list_imgs(rootdir):
    """ Lista os nomes dos arquivos de imagens """
    file_names = []
    for current, directories, files in os.walk(rootdir):
        for f in files:
            file_names.append(current + '/' + f)

    file_names.sort()
    return file_names

def get_negative(args):
    """ Converte a imagem no seu negativo """
    fname = args[0]
    splitname = fname.split('/')[-1]

    img = io.imread(fname)
    
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]

    img_ch0_R_neg = 255-red
    img_ch1_G_neg = 255-green
    img_ch2_B_neg = 255-blue

    new_image = np.stack((img_ch0_R_neg, img_ch1_G_neg, img_ch2_B_neg), axis=-1)

    splitname = save_dir + '/' + 'negative_' + splitname.split('.')[0]  + '.png'
    Image.fromarray(new_image).convert("RGB").save(splitname)

    return splitname


def print_name(args):
    """ Formata e imprime os nomes """
    fname = args[0]

    print("Convertido %s" %fname)

def sucuri(n_procs):
    """ Aplica comandos da lib Sucuri """
    nprocs = n_procs
    image_path = list_imgs(imgs_folder)
    
    graph = DFGraph()
    sched = Scheduler(graph, nprocs, mpi_enabled = False)
    
    feed_files = Source(image_path)
    
    convert_file = FilterTagged(get_negative, 1)  
    
    pname = Serializer(print_name, 1)
    
    graph.add(feed_files)
    graph.add(convert_file)
    graph.add(pname)

    feed_files.add_edge(convert_file, 0)
    convert_file.add_edge(pname, 0)

    t0 = time.time()
    sched.start()
    t1 = time.time()
    print( "Tempo de execucao: %.3f" %(t1-t0))


sucuri(int(sys.argv[1]))
