# obj_to_vtk
Convert object files to vtk files

## Requirement
```bash
pip install vtk
```

## How to Use
1. Write input and output directories to configuration file.
    ```json
    {
        "input_directory": "path_to_your_obj_files",
        "output_directory": "path_to_save_vtk_files"
    }

    ```
1. Run the python script
    ```bash
    python obj_to_vtk.py
    ```