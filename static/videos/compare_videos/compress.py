import os
from pathlib import Path
from tqdm import tqdm

for file in tqdm(list(Path('.').rglob('*.mp4'))):
    os.system(f"ffmpeg -i {file} -vcodec libx264 -crf 28 {file.as_posix().replace('.mp4', '_crf28.mp4').replace('combined_', '')}")

# for file in tqdm(list(Path('.').rglob('*.mp4_crf28.mp4'))):
#     file.rename(file.as_posix().replace('.mp4_crf28.mp4', '_crf28.mp4'))