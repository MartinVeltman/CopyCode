import os
import pyperclip
import argparse
import yaml


def gather_files(root_dir, exclude_paths, filetypes):
    collected_code = []
    files_count = 0
    lines_count = 0
    processed_files = []
    for current_dir, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if os.path.join(current_dir, d) not in exclude_paths]
        for file in files:
            full_path = os.path.join(current_dir, file)
            if full_path in exclude_paths:
                continue
            if any(file.endswith(ext) for ext in filetypes):
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.readlines()
                    files_count += 1
                    lines_count += len(content)
                    processed_files.append(full_path)
                    header = "# " + os.path.basename(full_path) + "\n"
                    combined_content = "".join(content)
                    collected_code.append(header + combined_content + "\n")
                except:
                    pass
    return "\n".join(collected_code), files_count, lines_count, processed_files


def main():
    parser = argparse.ArgumentParser(description="Copy your code to the clipboard or a file.")
    parser.add_argument("path", nargs="?", default=".", help="Root folder to scan.")
    parser.add_argument("--exclude", type=str, help="Comma-separated files or folders to exclude.")
    parser.add_argument("--outfile", type=str, help="Destination file for the combined output.")
    parser.add_argument("--filetypes", type=str, help="Comma-separated list of file extensions.")
    args = parser.parse_args()
    default_config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    config_excludes = []
    config_filetypes = []
    if os.path.exists(default_config_path):
        try:
            with open(default_config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f) or {}
                config_excludes = config.get("exclude", [])
                config_filetypes = config.get("filetypes", [])
        except:
            pass
    abs_exclude_paths = []
    for item in config_excludes:
        abs_exclude_paths.append(os.path.abspath(os.path.join(args.path, item)))
    if args.exclude:
        cli_excludes = [x.strip() for x in args.exclude.split(",")]
        for ex in cli_excludes:
            abs_exclude_paths.append(os.path.abspath(os.path.join(args.path, ex)))
    used_filetypes = config_filetypes if config_filetypes else [".py", ".js", ".html"]
    if args.filetypes:
        used_filetypes = [ft.strip() for ft in args.filetypes.split(",")]
    combined, files_count, lines_count, processed_files = gather_files(
        os.path.abspath(args.path),
        abs_exclude_paths,
        used_filetypes
    )
    if args.outfile:
        try:
            with open(args.outfile, "w", encoding="utf-8") as out:
                out.write(combined)
            print("All code has been written to", args.outfile)
        except:
            print("Could not write to", args.outfile)
    else:
        pyperclip.copy(combined)
        print("Your code has been copied to the clipboard.")
    print("----------------------------------------")
    print("Processed files:", files_count)
    print("Total lines of code:", lines_count)
    print("Files:")
    for f in processed_files:
        print(f)
    print("----------------------------------------")
