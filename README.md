# wma to mp3 converting tool

Convert wma files under a given directory to mp3 format.
It uses  ffmpeg to do media codec conversion and use python to the manage the rest pieces.


## prerequisite
ffmpeg is installed.

## usage:
```wma_to_mp3.py [-h] --idir IDIR --odir ODIR```
where the **IDIR** is the input directory that contains some *.wma files. Those *.wma files will be transcoded to *.mp3 files and saved under **ODIR** folder.
