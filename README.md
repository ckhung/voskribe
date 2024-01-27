# voksribe

Create text transcription for a video or audio file. This outputs 3 files, 1 `words.json` file that has all of the words said along with their timing and confidence, 1 `transcript.txt` with just all the words read, and 1 `captions.srt` file which is the captions for that video.

This is a fork of [adhikary97/Sharetape-Speech-To-Text](https://github.com/adhikary97/Sharetape-Speech-To-Text).

## Install requirements

```
$ pip3 install moviepy vosk
```

## Download Vosk models

Choose language models from [vosk model page](https://alphacephei.com/vosk/models) and unzip them in ~/vosk/ or any directory to your liking. You can use the -m option to specify the exact path of the language model at runtime.

## Speech to text with video

Video must be `.mp4` or `.mov`

```
$ python main.py videoname.mp4
```

## Speech to text with audio

Video must be `.wav`

```
$ python main.py audioname.wav
```
