import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(
        description="Change extension of files in directory"
    )

    parser.add_argument("work_dir", type=str)
    parser.add_argument("old_ext", type=str)
    parser.add_argument("new_ext", type=str)

    return parser


def batch_rename(work_dir, old_ext, new_ext):
    print(type(work_dir))
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        name, ext = split_file
        if ext == old_ext:
            newfile = name + new_ext
            print("find successfully")
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))
    print("rename done")
    print(os.listdir(work_dir))


def main():
    parser = get_parser()
    # args = vars(parser.parse_args())
    args = parser.parse_args()

    work_dir = args.work_dir
    old_ext = args.old_ext
    new_ext = args.new_ext
    # work_dir = args['work_dir'][0]
    # old_ext = args['old_ext'][0]
    # new_ext = args['new_ext'][0]

    if old_ext and old_ext[0] != ".":
        old_ext = "." + old_ext

    if new_ext and new_ext[0] != ".":
        new_ext = "." + new_ext
    # print(work_dir, old_ext, new_ext)

    batch_rename(work_dir, old_ext, new_ext)


if __name__ == "__main__":
    main()
