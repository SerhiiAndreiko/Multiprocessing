from pathlib import Path
from multiprocessing import Pool

CATEGORIES = {
    "Audio": [".mp3", ".aiff", ".wav", ".aac", ".flac"],
    "Documents": [".docx", ".doc", ".txt", ".pdf", ".xls", ".xlsx", ".pptx", ".rtf"],
    "Video": [".avi", ".mp4", ".mov", ".mkv", ".mpeg"],
    "Image": [".jpeg", ".png", ".pcd", ".jpg", ".svg", ".tiff", ".raw", ".gif", ".bmp"],
    "Archive": [".zip", ".7-zip", ".7zip", ".rar", ".gz", ".tar"],
    "Book": [".fb2", ".mobi"]
}


def get_category(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def move_file(file: Path, root_dir: Path, category: str) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir(parents=True)
    new_name = target_dir.joinpath(file.name)
    file.rename(new_name)


def delete_empty_folders(path: Path) -> None:
    for folder in list(path.glob("**/*"))[::-1]:
        if folder.is_dir() and not any(folder.iterdir()):
            is_category_folder = any(cat in CATEGORIES.keys() for cat in folder.name)
            if not is_category_folder:
                folder.rmdir()

    if path.name != "" and not any(path.iterdir()):
        path.rmdir()


def sort_file_and_delete_empty_folders(file):
    folder_path, item = file
    path = Path(folder_path)
    if item.is_file():
        category = get_category(item)
        move_file(item, path, category)

    delete_empty_folders(path)
    return f"Sorting and Cleaning Completed in folder: {path}"


def sort_folder_parallel(folder_path: str) -> str:
    path = Path(folder_path)

    if not path.exists():
        return f"Folder with path {path} doesn't exist."

    files = [(folder_path, item) for item in path.glob("**/*") if item.is_file()]

    with Pool(processes=4) as pool:  
        results = pool.map(sort_file_and_delete_empty_folders, files)

    return "\n".join(results)

if __name__ == "__main__":
    source_folder = "Trash" # Щлях до папки 
    
    result = sort_folder_parallel(source_folder)
    print(result)
