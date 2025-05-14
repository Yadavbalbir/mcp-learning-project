## Commands
- uv run mcp dev servers/weather.py  # mcp inspector
- uv run mcp install servers/weather.py # claude desktop
- uv run --with mcp[cli] mcp run <full-path>  # GHC
- uv run mcpserver/server.py   # this is for sse


## uv setup
- install uv  (brew install uv)
- uv init demoserver  (intializing uv project)
- uv venv  (setting up virtual environment)
- source .venv/bin/activate (activate venv)
- uv add mcp['cli']
