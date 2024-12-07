import torch

def report_gpu_status():
    if torch.cuda.is_available():
        print("CUDA is available. Listing GPU details:")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
            print(f"  Memory Allocated: {torch.cuda.memory_allocated(i) / 1e9} GB")
            print(f"  Memory Cached: {torch.cuda.memory_reserved(i) / 1e9} GB")
    else:
        print("CUDA is not available. Please check your installation.")
