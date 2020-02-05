# wma to mp3 converting tool

Convert wma files under a given directory to mp3 format.
It uses  **ffmpeg** to do the media transcoding and uses python to manage the rest pieces.


## Prerequisite
'ffmpeg' is installed. And 'ffmpeg-python' python package is installed.

## Usage
```wma_to_mp3.py [-h] --idir IDIR --odir ODIR```

Where the **IDIR** is the input directory that contains some *.wma files. Those *.wma files will be transcoded to *.mp3 files and saved under **ODIR** folder.
