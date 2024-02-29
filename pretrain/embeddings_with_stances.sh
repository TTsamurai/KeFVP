# List of file types to process
file_types=(
    "TextSequence"
    "ECT"
    "gpt_summary"
    "gpt_summary_overweight"
    "gpt_summary_underweight"
    "gpt_analysis_overweight"
    "gpt_analysis_underweight"
)

# Loop through each file type and run the Python script with it as an argument
for file_type in "${file_types[@]}"; do
    echo "Processing $file_type"
    python generatePtmEmbeddings.py "$file_type"
done

echo "All file types processed."
