import fileSubstitution as fs
import os

fs.fileSubs('FilesForVVCNEW/(4x4)/RdCost(8x8)-4.cpp','/home/luispmendes/VVCSoftware_VTM/source/Lib/CommonLib/')

os.system('cd /home/luispmendes/VVCSoftware_VTM/build/')
os.system('make')
os.system('cd /home/luispmendes/Data-Analyser-for-video-encoding')
os.system('python3 main.py "4x4-RdCost8x8-4"')
