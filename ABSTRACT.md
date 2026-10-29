# Abstract — Harvesta

Harvesta is a mini project demonstrating how artificial intelligence can support access to basic agricultural information. Developed using Python and Streamlit, it contains two main sections: crop-leaf image analysis and agricultural market-price information. Users can upload a leaf image and, when a Gemini API key is configured, request AI-generated observations about visible symptoms and cautious next steps. Without a key, the application runs in demo mode and offers general leaf-observation tips without claiming to diagnose the image. The market section displays illustrative crop-price values to demonstrate how such information can be presented; the values are clearly marked as sample data and are not live prices. Harvesta is an educational prototype that can be expanded with verified market data, regional-language support, and links to agricultural experts. It does not replace professional crop diagnosis or official market information.

## Objectives
- Build a simple web interface for agricultural information.
- Demonstrate image upload and optional AI-assisted observations.
- Present crop-price information in a readable table.
- Keep the project easy to run and extend.

## Technologies
Python, Streamlit, Pillow, and optionally the Google Gemini API.

## Methodology
1. The user opens the Streamlit app.
2. The user uploads a crop-leaf image.
3. If a Gemini key is configured, the image is sent for cautious AI observations; otherwise, demo guidance is shown.
4. The user opens the market section to view illustrative sample values.
5. The app encourages verification with official sources and agricultural experts.

## Limitations
- Market prices are sample values and are not connected to a live data source.
- AI observations may be inaccurate and need expert confirmation.
- Gemini analysis requires a valid API key and internet access.

## Conclusion
Harvesta demonstrates how a web application can combine image-based AI assistance with an agricultural information display. Future work can include official live market-price integration and regional-language support.
