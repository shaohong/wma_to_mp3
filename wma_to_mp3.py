from __future__ import print_function
import argparse
import os

import ffmpeg


def convert_audio(wma_file, mp3_file):
    print("converting {} to {}".format(wma_file, mp3_file))
    # ffmpeg.input(wma_file).output(mp3_file).run()
    stream = ffmpeg.input(wma_file)
    stream = ffmpeg.output(stream, mp3_file)
    ffmpeg.run(stream, overwrite_output=True)


def main():
    parser = argparse.ArgumentParser(description='convert wma files under a given directory to mp3 format')
    parser.add_argument('--idir', type=str, required=True,
                        help='Input dir for wma files')
    parser.add_argument('--odir', type=str, required=True,
                        help='Output dir for mp3 files')
    args = parser.parse_args()

    idir = args.idir
    odir = args.odir

    wma_files = sorted([fname for fname in os.listdir(idir)
                        if fname.lower().endswith(".wma")])
    print(wma_files)

    for ifname in wma_files:
        wma_file = os.path.join(idir, ifname)
        wma_file_renamed = os.path.join(idir, ifname.replace(' ', '_'))
        os.rename(wma_file, wma_file_renamed)

        of_name = ifname.replace(' ', '_').replace('.wma', '.mp3')
        mp3_file = os.path.join(odir, of_name)
        convert_audio(wma_file_renamed, mp3_file)


    # list all the '.wma' files under idir
if __name__ == "__main__":
    main()
