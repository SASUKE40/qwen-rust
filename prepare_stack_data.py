import os
from datasets import load_dataset

# define a directory to save the rust code files
output_dir = "rust_stack_data"
os.makedirs(output_dir, exist_ok=True)

# we'll load a small sample of the stack dataset for demonstration.
# for a real pretraining run, you'd want a much larger subset or the full rust portion.
# the 'data' split for 'bigcode/the-stack' needs `streaming=True` for large datasets.
# let's try a smaller, more manageable subset if possible, or iterate a few.

# load a small portion of the rust language from the stack dataset
# this might take a moment depending on your internet connection and the dataset size
print("loading a small sample of rust code from the stack dataset...")
rust_dataset = load_dataset(
    "bigcode/the-stack-dedup",
    data_dir="data/rust", # specify the rust language subset
    split="train",
    streaming=True # use streaming to handle large datasets efficiently
).take(1000) # take the first 1000 examples for a quick demo

# save each rust code example as a separate .rs file
print(f"saving rust code files to {output_dir}/")
for i, example in enumerate(rust_dataset):
    # the 'content' field typically holds the code in the stack dataset
    if "content" in example and example["content"]:
        with open(os.path.join(output_dir, f"rust_code_{i:05d}.rs"), "w", encoding="utf-8") as f:
            f.write(example["content"])
    if i % 100 == 0:
        print(f"processed {i} files...")

print(f"finished preparing {i+1} rust code files in {output_dir}/")