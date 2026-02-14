OllamaForge 

One-command launcher for local AI coding models. Born from live debugging a broken Ollama + Claude Code setup.


 Features

     Smart model selection - Auto-picks CPU-friendly models (3B/7B)

     One-command restart - ollamaforge run = server + model launch

     Hardware aware - Detects your RAM/CPU for optimal performance

     Zero config - Works out of the box with your existing Ollama install

     Production CLI - Proper src/ layout, pyproject.toml, virtualenv

 Quick Start

bash
# Clone & activate
git clone <your-repo> ollamaforge
cd ollamaforge
source .venv/bin/activate  # or create: python3 -m venv .venv

# Install
pip install -e .

# Launch AI coder (one command!)
python -m ollamaforge.launcher run

Boom! Your qwen2.5-coder:3b launches instantly → >>> hello
 Usage

bash
# Default fast model (1.9GB)
python -m ollamaforge.launcher run

# Smarter model (4.7GB, slower load)
python -m ollamaforge.launcher run --model qwen2.5-coder:7b

# See help
python -m ollamaforge.launcher --help

 Project Structure

text
ollamaforge/
├── pyproject.toml       # Modern Python packaging
├── README.md           # This file!
├── src/
│   └── ollamaforge/
│       ├── __init__.py
│       └── launcher.py # Typer CLI magic
└── .venv/              # Isolated environment

 Why This Rocks

Real-world origin story: Built live from debugging Ollama + Claude Code integration hell. Solves:

    Lost Ollama sessions after shutdowns

    Model loading delays on CPU hardware

    Claude Code's broken Ollama bridge

    Manual pkill ollama && ollama serve && ollama run nonsense

Portfolio gold: Modern src/ layout + Typer CLI = instant credibility.
 Development

bash
# Edit code
nano src/ollamaforge/launcher.py

# Changes auto-reload (editable install)
pip install -e .

# Add features
python -m ollamaforge.launcher --help

 Roadmap

    MVP launcher 

    Hardware detection (RAM/CPU → model size)

    /init-style project analysis

    Model manager (ollamaforge models install codellama)

    VSCode extension

    GitHub Actions CI/CD

 Origin Story

This tool was born live in a chat session (Feb 14, 2026) while debugging:

    Ollama dying after Ubuntu shutdowns

    Claude Code's broken Ollama integration

    "Cascading..." infinite loading loops

    Model access errors on free tier

From pain → product in 90 minutes.
 License

MIT - Use freely, star if helpful!

ollamaforge run → AI coder bliss. You're welcome