import subprocess
from concurrent.futures import ProcessPoolExecutor

# Define your text embeddings and durations
text_embeddings = [
    "TextSequence",
    "ECT",
    "gpt_summary",
    "gpt_summary_overweight",
    "gpt_summary_underweight",
    "gpt_analysis_overweight",
    "gpt_analysis_underweight",
]

durations = [3, 7, 15, 30]


# Define the function to run your command
def run_command(text_embedding, duration):
    cmd = [
        "python",
        "final_series_infer.py",
        "--text_embedding",
        text_embedding,
        "--weight_decay",
        "5e-2",
        "--lr",
        "0.0002",
        "--pid",
        "0.95",
        "--time_model",
        "CondAutoformer",
        "--duration",
        str(duration),
        "--run_mode",
        "reg",
        "--d_layers",
        "2",
        "--mu",
        "0.7",
        "--dataset",
        "ec",
        "--audio_indim",
        "768",
        "--time_model",
        "CondAutoformer",
    ]
    print(f"Processing {text_embedding} with duration {duration}")
    subprocess.run(cmd)


# Use ProcessPoolExecutor to run tasks in parallel
with ProcessPoolExecutor(max_workers=5) as executor:
    # Create a list of tasks
    tasks = [
        executor.submit(run_command, text_embedding, duration)
        for text_embedding in text_embeddings
        for duration in durations
    ]
    # Wait for all tasks to complete (optional here as the context manager takes care of it)

print("All text embeddings and durations processed.")
