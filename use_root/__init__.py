
import sys

def inject(os, prefix = "/src"):
    file_path = (
        os.path.realpath('.')
        if "ipykernel_launcher" in sys.argv[0]
        else "/".join(os.path.split(os.path.realpath(__file__))[0].split("/"))
    )

    project_path = file_path[: file_path.rindex(prefix)] if prefix in file_path else file_path

    if project_path not in sys.path:
        sys.path.insert(1, project_path)
