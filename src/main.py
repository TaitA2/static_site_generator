import os
import shutil

# recursively copy contents of source dir to destination dir
def recursive_copy(source, dest):
    # make destination dir if none exists
    if not os.path.exists(dest):
        os.mkdir(dest)
    # iterate over contents of source dir
    for file in os.listdir(source):
        # set paths to be source/file and dest/file
        from_path = os.path.join(source, file)
        dest_path = os.path.join(dest, file)
        # print paths for insight and debugging
        print(f"* {from_path} -> {dest_path}")
        # copy files across and call this func on dirs
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            recursive_copy(from_path, dest_path)

def main():
    # call recursive copy func from static/ to public/
    recursive_copy("static/", "public/")

if __name__ == "__main__":
    main()