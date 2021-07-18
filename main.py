import uvicorn

if __name__ == '__main__':
    debug = True

    uvicorn.run('omni:app', host='0.0.0.0', port=8000, debug=debug, reload=debug)
