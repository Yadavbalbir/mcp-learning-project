FROM python:3.11-slim

WORKDIR /app
RUN pip install uv

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies using uv
RUN uv venv
RUN uv pip install -r requirements.txt

# Copy application code
COPY server.py server.py

# Expose the port the app runs on
EXPOSE 8050

# Command to run the server
CMD ["uv", "run", "server.py"]