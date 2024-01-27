import argparse, os, logging, re

from vosk import Model, SetLogLevel
from sharetape import Sharetape


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
        help='verbose')
    parser.add_argument('-m', '--model', type=str, default=os.environ['HOME'] + '/vosk/vosk-model-en-us-0.42-gigaspeech',
        help='path of model file')
    parser.add_argument('avfile',
        help='audio or video file, with extension .mp4, .mov, or .wav')
    args = parser.parse_args()

    SetLogLevel(-1)
    model = Model(model_path=args.model)
    logging.info('sp2t setup')

    match = re.search(r'([^/]+)\.(\w+)$', args.avfile)
    out_dir, file_type = match.group(1), match.group(2)
    os.makedirs(f'{out_dir}')
    if file_type in ['mp4', 'mov']:
        audio = f'{out_dir}/audio.wav'
    elif file_type in ['wav']:
        audio = args.avfile
    else:
        print(f'unsupported file type {file_type}')
        exit()

    if args.verbose:
        print(f'processing a {file_type} file, output to {out_dir}/, using model {args.model}')
    shartape = Sharetape(
        args.avfile,
        audio,
        f'{out_dir}/mono_audio.wav',
        f'{out_dir}/transcript.txt',
        f'{out_dir}/words.json',
        f'{out_dir}/captions.srt',
        model,
    )
    shartape.extract_transcript()


if __name__ == '__main__':
    main()
