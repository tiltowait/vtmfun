"""Pynecone app configuration."""

import os

import pynecone as pc

PORT = os.getenv("PORT", 8000)

config = pc.Config(
    app_name="app",
    api_url=f"0.0.0.0:{PORT}",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
