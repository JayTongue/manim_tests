import numpy as np
import os
from tqdm import tqdm
import json

paths = {'enron': '/media/saltlick/cinnabar/corpora/IA_enron/data/decomp', 
         'contracts': '/media/saltlick/cinnabar/corpora/contracts_20240515/home/padelson/production_contracts'}


def get_file_stats(directory):
    # Collect all file sizes
    sizes = []
    
    for root, dirs, files in tqdm(os.walk(directory)):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath)
                sizes.append(size)
            except (OSError, FileNotFoundError):
                continue
    
    if not sizes:
        print("No files found!")
        return None
    
    return sizes

sizes = {}
for corp in ['enron', 'contracts']:
    sizes[corp] = get_file_stats(paths[corp])

bin_count_dict = {'lin': {}, 'log': {}}
for corp in ['enron', 'contracts']:
    counts, bin_edges = np.histogram(sizes[corp], bins=50)
    bin_count_dict['lin'][corp] = counts.tolist()

    data = [s for s in sizes[corp] if s > 0]
    counts, bin_edges = np.histogram(data, bins=np.logspace(np.log10(min(data)), np.log10(max(data)), 50))
    bin_count_dict['log'][corp] = counts.tolist()

json.dump(bin_count_dict, open('data/file_sizes/bin_counts.json', 'w'), indent=4)
print('Done!')