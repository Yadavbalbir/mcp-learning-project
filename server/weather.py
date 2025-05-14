from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# initialize the FastMCP instance
mcp = FastMCP("weather")


NWS_API_BASE = "https://api.weather.gov/"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """
    Make a request to the NWS API and return the JSON response.
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json",
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
        except httpx.RequestError as e:
            mcp.logger.error(f"Request error: {e}")
            return None

        return response.json()
    
def format_alert(feature:dict) -> str:
    """
    Format the alert data into a string.
    """
    props = feature["properties"]
    Event = props.get("event", "Unknown Event")
    title = props.get("headline", "No Title")
    description = props.get("description", "No Description")
    area_desc = props.get("areaDesc", "No Area Description")
    effective = props.get("effective", "No Effective Date")
    expires = props.get("expires", "No Expiration Date")
    instruction = props.get("instruction", "No Instruction")

    return f"""
        **{Event}**
        **Title:** {title}
        **Description:** {description}
        **Area:** {area_desc}
        **Effective:** {effective}
        **Expires:** {expires}
        **Instruction:** {instruction}
            """.strip()


@mcp.tool()
async def get_alerts(state: str) -> str:
    """ Get weather alerts for a given state.
    Args:
        state (str): The state to get alerts for (e.g., "CA" for California).
    Returns:
        str: A formatted string containing the weather alerts.
    """

    url = f"{NWS_API_BASE}alerts/active/area/{state}"
    data = await make_nws_request(url)
    if data is None:
        return "Error fetching alerts."
    if not data["features"]:
        return "No active alerts."
    alerts = []
    for feature in data["features"]:
        alerts.append(format_alert(feature))
    return "\n\n".join(alerts)


#prompt are basically reusable templates that helps LLMs to interact with the server 
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

# rosources helps in exposing data to the LLMs. They are similar to get endpoints in a REST API
@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


