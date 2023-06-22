"""Pynecone app configuration."""

import os

import pynecone as pc

PORT = os.getenv("PORT", 8000)

config = pc.Config(
    app_name="vtmfun",
    api_url=f"https://0.0.0.0:{PORT}",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
