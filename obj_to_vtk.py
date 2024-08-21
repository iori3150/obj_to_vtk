import glob
import json
import os
import sys

import vtk

input_directory = "./"  # Relative path to obj files
output_directory = "./"  # Relative path to save vtu files

script_directory = os.path.dirname(os.path.realpath(__file__))
input_directory = os.path.join(script_directory, input_directory)
output_directory = os.path.join(script_directory, output_directory)

# Check path existance
if not os.path.exists(input_directory):
    print(f"Error: Input directory '{input_directory}' does not exist.")
    sys.exit(1)
if not os.path.exists(output_directory):
    print(f"Error: Output directory '{output_directory}' does not exist.")
    sys.exit(1)

# Get object files
obj_files = glob.glob(os.path.join(input_directory, "*.obj"))
if not obj_files:
    print(f"Error: No .obj files found in the input directory '{input_directory}'.")
    sys.exit(1)

# Convert each obj file to vtk format
for obj_file in obj_files:
    # Use the OBJ reader to load the .obj file
    reader = vtk.vtkOBJReader()
    reader.SetFileName(obj_file)
    reader.Update()

    # Define the output file name for the .vtk file
    base_name = os.path.basename(obj_file)
    vtk_file = os.path.join(output_directory, os.path.splitext(base_name)[0] + ".vtk")

    # Write the data to a .vtk file
    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName(vtk_file)
    writer.SetInputData(reader.GetOutput())
    writer.Write()

    print(f"Converted {obj_file} to {vtk_file}")
