import os


def main():
    work_dir = "./../image/"

    idx = 0
    for id, filename in enumerate(os.listdir(work_dir)):
        split_file = os.path.splitext(filename)
        root, ext = split_file
        os.rename(
            os.path.join(work_dir, filename), os.path.join(work_dir, str(id) + "." + ext)
        )
    
    print(os.listdir(work_dir))

    print(work_dir)


if __name__ == "__main__":
    main()
