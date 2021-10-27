import time
import math
import sys

from road_side_unit.src import rsu

# Import our config file
import config

#global mainWin

# def main(mapSpecs, vehiclesLock, vehicles, sensors, trafficLightArray, unit_test):
#     # Initialize a simulator with the GUI set to on, cm map, .1s timestep, and vehicle spawn scale of 1 (default)
#     QTapp = gui.QtWidgets.QApplication(sys.argv)
#     mainWin = gui.MainWindow(mapSpecs, vehiclesLock, vehicles, sensors, trafficLightArray, unit_test)
#     mainWin.show()

#     sys.exit(QTapp.exec_())
#     #QTapp.exec_()

# Setup the RSU
sim = rsu.RSU(config)

while(True):
    time.sleep(.1)
    print ( "sleep" )

sys.exit()