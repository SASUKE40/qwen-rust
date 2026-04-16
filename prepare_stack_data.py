import os
from datasets import load_dataset

# define a directory to save the rust code files
output_dir = "rust_stack_data"
os.makedirs(output_dir, exist_ok=True)

# we'll load a small sample of the stack dataset for demonstration.
# for a real pretraining run, you'd want a much larger subset or the full rust portion.
# the 'data' split for 'bigcode/the-stack' needs `streaming=True` for large datasets.
# let's try a smaller, more manageable subset if possible, or iterate a few.

# load all rust language from the stack dataset using streaming
# this will take a long time and consume a lot of disk space for the full dataset
print("loading all rust code from the stack dataset (this will take a while)...")
rust_dataset = load_dataset(
    "bigcode/the-stack-dedup",
    data_dir="data/rust", # specify the rust language subset
    split="train",
    streaming=True # use streaming to handle large datasets efficiently
)

# save each rust code example as a separate .rs file
print(f"saving rust code files to {output_dir}/\n")
i = 0
for i, example in enumerate(rust_dataset):
    # the 'content' field typically holds the code in the stack dataset
    if "content" in example and example["content"]:
        with open(os.path.join(output_dir, f"rust_code_{i:07d}.rs"), "w", encoding="utf-8") as f:
            f.write(example["content"])
    if i % 1000 == 0: # increased print frequency for a very large dataset
        print(f"processed {i} files...")

print(f"finished preparing {i+1} rust code files in {output_dir}/")