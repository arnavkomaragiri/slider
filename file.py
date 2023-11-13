import skvideo.io
import numpy as np
import subprocess
import os

def m3u8_to_mp4(path: str) -> None:
    print('Converting m3u8 files to mp4 in', path)
    if not os.path.exists(path):
        os.mkdir(path)
    # get every file in the directory
    files = os.listdir(path)
    # filter out the m3u8 file
    files = [file for file in files if file.endswith('.m3u8')]
    # convert every m3u8 file to mp4 in the output directory
    output_dir = os.path.join(path, 'output')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for file in files:
        print('=' * 30)
        print('Converting', file, 'to mp4')
        # ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i [insert m3u8 file] -c copy -bsf:a aac_adtstoasc [output file]
        subprocess.run([
            'ffmpeg', 
            '-protocol_whitelist', 
            'file,http,https,tcp,tls,crypto', 
            '-i', 
            os.path.join(path, file), 
            '-c', 
            'copy', 
            '-bsf:a', 
            'aac_adtstoasc', 
            os.path.join(output_dir, file[:-5] + '.mp4')
        ])
        print('Done converting', file, 'to mp4')
        print('=' * 30)

def load_video(path: str) -> np.ndarray:
    return skvideo.io.vread(path) 

def get_keyframes(video: np.ndarray) -> np.ndarray:
    per_frame_diffs = np.diff(video, axis=0)
    per_frame_diff_norms = np.linalg.norm(per_frame_diffs, axis=(-3, -2, -1))
    pass
    
if __name__ == '__main__':
    m3u8_to_mp4('videos')