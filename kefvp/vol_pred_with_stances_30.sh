#!/bin/bash

# List of file types to process
text_embeddings=(
    "TextSequence"
    "ECT"
    "gpt_summary"
    "gpt_summary_overweight"
    "gpt_summary_underweight"
    "gpt_analysis_overweight"
    "gpt_analysis_underweight"
)

# List of durations to process
durations=(30)

# Loop through each text embedding
for text_embedding in "${text_embeddings[@]}"; do
    # Loop through each duration for the current text embedding
    for duration in "${durations[@]}"; do
        echo "Processing $text_embedding with duration $duration"
        python final_series_infer.py --text_embedding "$text_embedding" --weight_decay 5e-2 --lr 0.0002 --pid 0.95 --time_model CondAutoformer --duration "$duration" --run_mode reg --d_layers 2 --mu 0.7 --dataset ec --audio_indim 768 --time_model CondAutoformer
    done
done

echo "All text embeddings and durations processed."
