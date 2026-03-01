from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse("""
    <html>
        <head><title>Ghost Chat</title></head>
        <body>
            <h1>🔒 Ghost Chat</h1>
            <p>If you can see this, Docker is working!</p>
            <p>Server time: <span id="time"></span></p>
            <script>
                document.getElementById('time').textContent = new Date().toString();
            </script>
        </body>
    </html>
    """)

@app.get("/health")
async def health():
    return {"status": "alive", "message": "Your Docker container is running"}
