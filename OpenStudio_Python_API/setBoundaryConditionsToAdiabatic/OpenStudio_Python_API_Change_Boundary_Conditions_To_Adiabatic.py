# Developed by Mohammad Heidarinejad, PhD, PE 
# Updated on: 03/18/2024
# Contact: muh182@iit.edu

# // Copyright (c) 2023-2024 The Built Environment Research Group (BERG)
# // Distributed under the MIT software license, see the accompanying
# // file LICENSE or http://www.opensource.org/licenses/mit-license.php.

# import libraries used
import os
from os import system
import openstudio
from pathlib import Path

# set the current and OSM paths
current_path = Path(__file__).parent.absolute()
osm_path = current_path / "testModel.osm"
#print(type(osm_path))f

# import an existing model 
translator = openstudio.osversion.VersionTranslator()
model = translator.loadModel(osm_path)
assert model.is_initialized()
model = model.get()
#print(model)

# get surfaces
surfaces = model.getSurfaces()

# print surfaces for checking purposes - uncomment if needed
# print(surfaces)

# loop through the surfaces to find the Outdoors and change them to adiabatic
for surface in surfaces:
    #if surface.outsideBoundaryCondition() == "Outdoors": # just for outdoors
    if surface.outsideBoundaryCondition() == "Outdoors" and surface.surfaceType() == "Wall":
        surface.setOutsideBoundaryCondition("Adiabatic")

# set the model to export the updated model
final_path = Path(__file__).parent.absolute()
final_model_out_path = current_path / "output" / "test_output.osm"

# save the final model 
model.save(final_model_out_path, True)