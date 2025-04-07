import streamlit as st
import pyshorteners
import qrcode
from io import BytesIO
import base64

# --- Streamlit page config ---
st.set_page_config(page_title="🔗 URL Tools Hub", page_icon="✨", layout="centered")

# --- Session State for history ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- Title ---
st.title("🔗 URL Shortener & Tools")
st.markdown("Choose a service below to get started 👇")

# --- Sidebar for Navigation ---
service = st.sidebar.radio("📌 Select a Service", [
    "🔗 Basic URL Shortener",
    "📱 QR Code Generator",
    "📊 View Shortening History",
    "🌐 Custom Domain Shortener"
])

# --- Basic URL Shortener ---
if service == "🔗 Basic URL Shortener":
    st.header("🔗 Basic URL Shortener")
    long_url = st.text_input("📥 Enter a long URL")

    if st.button("🚀 Shorten"):
        if long_url:
            try:
                s = pyshorteners.Shortener()
                short_url = s.tinyurl.short(long_url)

                # Store in history
                st.session_state.history.append((long_url, short_url))

                st.success("✅ Shortened URL:")
                st.code(short_url, language="text")

                # Copy button
                st.markdown(
                    f'<a href="#" onClick="navigator.clipboard.writeText(\'{short_url}\')">📋 Copy to Clipboard</a>',
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please enter a valid URL.")

# --- QR Code Generator ---
elif service == "📱 QR Code Generator":
    st.header("📱 Generate QR Code for any URL")
    qr_url = st.text_input("🔗 Enter a URL for QR Code")

    if st.button("📸 Generate QR Code"):
        if qr_url:
            try:
                qr = qrcode.make(qr_url)
                buffer = BytesIO()
                qr.save(buffer)
                img_bytes = buffer.getvalue()

                st.image(img_bytes, caption="Scan Me!", use_column_width=False)

                # Download option
                b64 = base64.b64encode(img_bytes).decode()
                href = f'<a href="data:image/png;base64,{b64}" download="qrcode.png">⬇️ Download QR Code</a>'
                st.markdown(href, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error generating QR: {e}")
        else:
            st.warning("⚠️ Please enter a URL.")

# --- History ---
elif service == "📊 View Shortening History":
    st.header("📊 Shortening History")
    if st.session_state.history:
        for i, (long, short) in enumerate(reversed(st.session_state.history), 1):
            st.markdown(f"**{i}.** 🔗 `{long}` → 🌐 [{short}]({short})")
    else:
        st.info("No history yet. Start shortening URLs!")

# --- Custom Domain Shortener ---
elif service == "🌐 Custom Domain Shortener":
    st.header("🌐 Custom Domain Shortener (e.g., dev.ly/my-link)")
    custom_url = st.text_input("🔗 Enter your long URL")
    custom_alias = st.text_input("✍️ Choose your custom alias (e.g., my-link)")

    if st.button("🎯 Create Custom Short URL"):
        if custom_url and custom_alias:
            try:
               
                custom_short = f"https://dev.ly/{custom_alias}"
                st.success("✅ Your custom short URL:")
                st.code(custom_short)

                st.markdown(
                    f'<a href="#" onClick="navigator.clipboard.writeText(\'{custom_short}\')">📋 Copy to Clipboard</a>',
                    unsafe_allow_html=True
                )

                # Add to history
                st.session_state.history.append((custom_url, custom_short))
            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Enter both a URL and a custom alias.")

# --- Footer ---
st.markdown("""
---
Made with ❤️ by **Dev-Ice**  
[🌐 GitHub](https://github.com/Dev-comett) | [💼 LinkedIn](https://www.linkedin.com/in/dev-ice/)
""", unsafe_allow_html=True)


##Code enhanced & beautified with the help of [ChatGPT](https://chat.openai.com) 