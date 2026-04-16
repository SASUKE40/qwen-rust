litgpt download Qwen/Qwen3-0.6B

litgpt pretrain Qwen/Qwen3-0.6B \
    --tokenizer_dir Qwen/Qwen3-0.6B \
    --initial_checkpoint_dir Qwen/Qwen3-0.6B \
    --data TextFiles \
    --data.train_data_path "rust_stack_data/" \
    --train.max_tokens 10_000_000 \
    --out_dir out/qwen3-rust-model