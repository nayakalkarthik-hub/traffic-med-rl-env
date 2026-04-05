FROM python:3.10

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --no-cache-dir numpy

# If you want GUI in Docker, you need extra X11 setup (optional)
# For terminal-only RL simulation, above is enough

CMD ["python", "run.py"]