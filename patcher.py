import sys
import subprocess

def patch(input_path: str, output_path: str):
    # Ganti dengan logic patch kamu sendiri
    # Contoh: konversi pakai ffmpeg (tanpa perubahan)
    subprocess.run([
        "ffmpeg", "-i", input_path,
        "-c", "copy",
        output_path
    ], check=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python patcher.py <input.mp4> <output.mp4>")
        sys.exit(1)
    patch(sys.argv[1], sys.argv[2])
