# FFmpeg WASM Video Processor 22

A web-based video processing tool that uses FFmpeg WebAssembly to perform video operations directly in the browser. This tool allows you to:
- Convert videos to grayscale
- Trim videos to their first 3 seconds

## Live Demo
The application is live at: [https://comfy-biscochitos-20a742.netlify.app/](https://comfy-biscochitos-20a742.netlify.app/)

## Features

- Browser-based video processing (no server required)
- Drag-and-drop video upload
- Real-time processing status updates
- Supports common video formats
- Processes videos entirely client-side using WebAssembly

## Usage

1. Visit the [live demo](https://comfy-biscochitos-20a742.netlify.app/)
2. Click to select or drag-and-drop a video file
3. Choose between:
   - Converting to grayscale
   - Trimming to first 3 seconds
4. Wait for processing to complete
5. Download or play the processed video

## Technical Details

This project uses:
- FFmpeg.wasm for video processing
- Pure JavaScript for the frontend
- Netlify for hosting with required COOP/COEP headers

## Local Development

To run this project locally:

1. Clone the repository
2. Open `index.html` in a modern web browser
   - Note: Due to CORS policies, you might need to use a local server
   - You can use Python's `http.server`: `python -m http.server 8000`
   - Or Node's `http-server`: `npx http-server`
   - Make sure to set the required COOP/COEP headers

## License

MIT License 