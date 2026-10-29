import os
from datetime import date
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Harvesta", page_icon="🌱", layout="wide")
st.title("🌱 Harvesta")
st.subheader("Smart Agriculture Assistant")
st.write("A student mini project demonstrating crop-leaf observations and agricultural market information.")

leaf_tab, market_tab, about_tab = st.tabs(["🍃 Crop Leaf Analysis", "📈 Market Price Demo", "ℹ️ About"])

with leaf_tab:
    st.write("Upload a clear crop-leaf photo for AI-assisted observations when Gemini is configured.")
    uploaded = st.file_uploader("Choose a leaf image", type=["jpg", "jpeg", "png"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded image", use_container_width=True)
        if st.button("Analyze leaf", type="primary"):
            api_key = os.getenv("GEMINI_API_KEY", "").strip()
            if not api_key:
                st.info("Demo mode: GEMINI_API_KEY is not configured, so no AI image analysis was performed.")
                st.markdown("**General observation tips**")
                st.write("- Look for spots, yellowing, curling, holes, or unusual growth.")
                st.write("- Photograph both sides of the leaf in good natural light.")
                st.write("- Compare several plants and note recent weather and watering.")
                st.warning("These are general tips, not a diagnosis of your uploaded image.")
            else:
                try:
                    from google import genai
                    client = genai.Client(api_key=api_key)
                    prompt = ("Inspect this crop-leaf image. Describe visible symptoms only, give cautious possible explanations and safe next steps, and recommend confirmation by a local agricultural expert. If uncertain, say so. Do not claim a definitive diagnosis.")
                    response = client.models.generate_content(model="gemini-2.5-flash", contents=[prompt, image])
                    st.markdown("### AI observations")
                    st.write(response.text or "No text returned. Try another clear image.")
                    st.caption("AI guidance may be wrong. Confirm important decisions with an agricultural expert.")
                except Exception as exc:
                    st.error("AI analysis failed. Check the API key, internet connection, and model access.")
                    st.caption(f"Technical detail: {type(exc).__name__}")
    else:
        st.info("Upload a JPG or PNG image to begin.")

with market_tab:
    st.write("These values are illustrative sample data, not live market prices.")
    rows = [
        {"Crop": "Paddy", "Market": "Demo Market", "Price (₹/quintal)": 2300},
        {"Crop": "Maize", "Market": "Demo Market", "Price (₹/quintal)": 2100},
        {"Crop": "Groundnut", "Market": "Demo Market", "Price (₹/quintal)": 5800},
        {"Crop": "Tomato", "Market": "Demo Market", "Price (₹/quintal)": 1800},
    ]
    st.caption(f"Demo values shown on {date.today().strftime('%d %b %Y')}; not suitable for selling decisions.")
    st.dataframe(rows, use_container_width=True, hide_index=True)
    st.warning("Check an official mandi/APMC source for current prices.")

with about_tab:
    st.write("**Problem:** Farmers may need accessible information when crop leaves look unhealthy.")
    st.write("**Solution:** Harvesta demonstrates image-based AI observations and a simple market-price display.")
    st.write("**Technology:** Python, Streamlit, Pillow, and optionally Google Gemini.")
    st.write("**Limitations:** Sample prices are not live. AI output is not a substitute for professional diagnosis.")
    st.write("**Future work:** Verified live prices, regional languages, crop selection, and agricultural extension links.")

st.divider()
st.caption("Harvesta — Student Mini Project | Smart Agriculture Assistant")
