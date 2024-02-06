#!/bin/bash

# Array of durations
durations=(3 7 15 30)

# Loop over each duration
for duration in "${durations[@]}"
do
    # Run the command with the current duration
    CUDA_VISIBLE_DEVICES=0 python final_series_infer.py --weight_decay 5e-2 --lr 0.0002 --pid 0.95 --time_model CondAutoformer --duration $duration --run_mode reg --d_layers 2 --mu 0.7 --dataset ec --audio_indim 768  --time_model CondAutoformer --epochs 10 &
done

wait

