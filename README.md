## uv setup
- [install uv](https://docs.astral.sh/uv/getting-started/installation/)
- `uv init demoserver`  (intializing uv project)
- `cd demoserver`
- `uv venv`  (setting up virtual environment)
- `source .venv/bin/activate` (macOS) (activating virtual environment)
- `uv add mcp['cli']`  (installing mcp related dependencies)

## Commands for running mcp servers
- `uv run mcp dev servers/weather.py  # mcp inspector`
- `uv run mcp install servers/weather.py # claude desktop`
- `uv run --with mcp[cli] mcp run <full-path>  # GHC`
- `uv run mcpserver/server.py   # this is for sse`

