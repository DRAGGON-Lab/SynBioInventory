# SynBioInventory Backend

FastAPI backend for SynBioInventory MVP.

## Run locally

```bash
cd server
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload --port 8000
```

Default mode uses `SYNBIOHUB_USE_STUB=true`, so no live SynBioHub is required.
