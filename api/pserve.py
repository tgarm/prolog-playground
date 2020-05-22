#!/usr/bin/env python3
import uvicorn

if __name__ == "__main__":
    uvicorn.run("pstore:app", host="127.0.0.1", port=8000, log_level="info",reload=True)
