import sys

def patch(input_path: str, output_path: str):
    # Ganti dengan logic patch kamu
    # Contoh pake library Python (install dulu di workflow):
    # from moviepy import VideoFileClip
    # clip = VideoFileClip(input_path)
    # ... lakukan patch ...
    # clip.write_videofile(output_path)

    # Sementara cuma copy file
    with open(input_path, 'rb') as f:
        data = f.read()
    with open(output_path, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python patcher.py <input.mp4> <output.mp4>")
        sys.exit(1)
    patch(sys.argv[1], sys.argv[2])
