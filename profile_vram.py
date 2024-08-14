import GPUtil
import psutil

def get_vram_info():
    # Get the list of GPUs
    gpus = GPUtil.getGPUs()

    if len(gpus) == 0:
        print("No GPU found.")
        return

    for gpu in gpus:
        print(f"GPU: {gpu.name}")
        print(f"Total VRAM: {gpu.memoryTotal} MB")
        print(f"Available VRAM: {gpu.memoryFree} MB")
        print(f"Used VRAM: {gpu.memoryUsed} MB")
        print(f"Memory utilization: {gpu.memoryUtil * 100}%")
        print()

if __name__ == "__main__":
    get_vram_info()
