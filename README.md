# MCP Weather & App Server

## Description
A server application using the MCP framework to provide weather alerts, app ratings, and code review prompts.

## Features
*   Fetches weather alerts for a given state (from NWS API).
*   Provides a simulated average app rating.
*   Offers a code review prompt.
*   Exposes app configuration.
*   Includes different server implementations (`mcpserver/server.py` and `server/weather.py`).

## Prerequisites
*   Python 3.x
*   `uv` (for environment and package management)

## Setup and Installation
1.  **Install `uv`:**
    Follow the instructions at [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/) to install `uv`.

2.  **Initialize the project:**
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```
    (On Windows, use: `.venv\Scripts\activate`)

4.  **Install dependencies:**
    ```bash
    uv add mcp['cli'] httpx
    ```

## Running the Server
There are several ways to run the servers:

*   **MCP Inspector for the weather server:** This allows you to inspect the weather server's tools, prompts, and resources.
    ```bash
    uv run mcp dev servers/weather.py
    ```

*   **Claude Desktop for the weather server:** This provides a desktop interface for interacting with the weather server.
    ```bash
    uv run mcp install servers/weather.py
    ```

*   **GHC for any MCP server:** This is a general-purpose command to run any MCP server. Replace `<full-path-to-server.py>` with the actual path to the server file (e.g., `servers/weather.py` or `mcpserver/server.py`).
    ```bash
    uv run --with mcp[cli] mcp run $(pwd)/servers/weather.py
    ```
    or
    ```bash
    uv run --with mcp[cli] mcp run $(pwd)/mcpserver/server.py
    ```
    *Note: You need to provide the full path to the server file.*

*   **SSE server at `mcpserver/server.py`:** This runs a Server-Sent Events (SSE) server that can be used for real-time updates.
    ```bash
    uv run python mcpserver/server.py
    ```

## Available Tools, Prompts, and Resources

### Tools
*   **`get_alerts(state: str)`**:
    *   **Description:** Retrieves active weather alerts for a specified US state from the National Weather Service (NWS) API.
    *   **Arguments:**
        *   `state` (str): The two-letter abbreviation for the US state (e.g., "CA", "NY").

*   **`get_average_rating()`**:
    *   **Description:** Returns a simulated average app rating. This is a placeholder and does not reflect real user data.

### Prompts
*   **`review_code(code: str)`**:
    *   **Description:** Provides a template to help structure a code review.
    *   **Arguments:**
        *   `code` (str): The code snippet to be reviewed.

### Resources
*   **`config://app`**:
    *   **Description:** Provides access to the static application configuration defined in the server. This typically includes settings and parameters for the application.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
