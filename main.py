from pathlib import Path
import shutil

download_dir = Path.home() / "Downloads"
tau_dir = Path.home() / "TAU"


def put_file(name):
    path = tau_dir
    name = name.split(".")[0]
    name_parts = name.split("-")

    class_found = False

    for part in name_parts:
        if len(path.parts) - len(tau_dir.parts) >= 3:
            return path

        if not class_found and part in ["micro", "macro", "linear", "discrete", "econ"]:
            path = path / part
            class_found = True

        if class_found and part in ["lec", "rec", "hw"]:
            if part == "lec" or part == "lec":
                part += "s"
            path = path / (part)
            break
        if not class_found:
            return download_dir

    return path


def main():
    for file in download_dir.iterdir():
        name = file.name
        path = put_file(name)
        if path != download_dir:
            if not path.exists():
                raise FileNotFoundError(f"cant find path {path}")
            print(f"moving {file.name} to {path}")
            shutil.move(str(file), str(path / file.name))


if __name__ == "__main__":
    main()
