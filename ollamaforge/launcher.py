import subprocess
import time
from pathlib import Path

import typer

app = typer.Typer(help="OllamaForge: simple launcher for local Ollama coder models")


def start_ollama_server():
    # try to start ollama serve in background; ignore errors if already running
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)


@app.command()
def run(model: str = "qwen2.5-coder:3b"):
    """
    Start Ollama server if needed, then run the given model.
    """
    typer.echo(f"Starting Ollama with model: {model}")
    start_ollama_server()
    # replace current process with `ollama run model`
    subprocess.call(["ollama", "run", model])


if __name__ == "__main__":
    app()

