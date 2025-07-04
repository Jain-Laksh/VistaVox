import uvicorn
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run TTS Server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=8060, help='Port to bind to (default: 8000)')
    
    args = parser.parse_args()
    
    print(f"Starting TTS server on {args.host}:{args.port}")
    print(f"Access from other devices: http://YOUR_LAPTOP_IP:{args.port}")
    
    uvicorn.run(
        "tts_server:app", 
        host=args.host, 
        port=args.port, 
        reload=True
    )
