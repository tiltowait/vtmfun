import pynecone as pc

config = pc.Config(
    app_name="vtmfun",
    api_url="https://vtmfun-production.up.railway.app:8000",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
