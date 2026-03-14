
import os
from datetime import datetime


BASE_DIR = "generated_projects"


def create_project(project_name: str, code: str):
    """
    Create a new FastAPI project from generated AI code
    """

    # unique folder name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    project_folder = f"{project_name}_{timestamp}"

    project_path = os.path.join(BASE_DIR, project_folder)

    os.makedirs(project_path, exist_ok=True)

    # create main.py
    main_file = os.path.join(project_path, "main.py")

    with open(main_file, "w") as f:
        f.write(code)

    return {
        "project_name": project_folder,
        "path": project_path,
        "file": "main.py"
    }
