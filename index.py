import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Holi 🌈",
    page_icon="🎨",
    layout="centered",
)

# ----------- Custom CSS -------------
st.markdown("""
<style>

/* Mobile Optimization */
@media only screen and (max-width: 600px) {
    .main-title { font-size: 36px !important; }
    .wish-text { font-size: 18px !important; }
    .signature { font-size: 18px !important; }
}

/* Animated Gradient Background */
body {
    background: linear-gradient(-45deg, #ff4e50, #f9d423, #24c6dc, #ff0080);
    background-size: 400% 400%;
    animation: gradientMove 10s ease infinite;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Center Container */
.main-container {
    text-align: center;
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    background: rgba(255, 255, 255, 0.15);
    margin-top: 40px;
}

/* Glowing Title */
.main-title {
    font-size: 60px;
    font-weight: bold;
    color: white;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #fff, 0 0 20px #ff0080; }
    to { text-shadow: 0 0 20px #fff, 0 0 40px #24c6dc; }
}

/* Wish Text */
.wish-text {
    font-size: 22px;
    color: white;
    margin-top: 20px;
    animation: fadeIn 2s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Signature */
.signature {
    margin-top: 25px;
    font-size: 22px;
    color: white;
    font-weight: bold;
}

/* Floating Color Bubbles */
.bubble {
    position: fixed;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    animation: floatUp 8s infinite;
    opacity: 0.7;
}

@keyframes floatUp {
    0% { transform: translateY(100vh) scale(0); }
    100% { transform: translateY(-10vh) scale(1); }
}

</style>
""", unsafe_allow_html=True)

# Floating Bubbles (Decorative)
components.html("""
<script>
function createBubble() {
    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.style.left = Math.random() * 100 + "vw";
    bubble.style.background = "hsl(" + Math.random()*360 + ", 100%, 50%)";
    bubble.style.animationDuration = (5 + Math.random() * 5) + "s";
    document.body.appendChild(bubble);

    setTimeout(() => {
        bubble.remove();
    }, 8000);
}
setInterval(createBubble, 500);
</script>
""", height=0)

# Main Content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="main-title">🌈 Happy Holi 🌈</div>', unsafe_allow_html=True)

st.markdown("""
<div class="wish-text">
May this Holi bring vibrant colors of happiness,  
success, love, and positivity into your life.  

Let every splash of color remind you  
that life is beautiful when filled with joy and kindness. ✨  

Celebrate safely, smile brightly,  
and spread happiness everywhere! 🎨💖
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="signature">With Love ❤️ <br> ~ Sachin</div>', unsafe_allow_html=True)

if st.button("🎉 Tap for Surprise 🎉"):
    st.balloons()
    st.success("Wishing You a Colorful, Joyful & Prosperous Holi! 🌈✨")

st.markdown('</div>', unsafe_allow_html=True)

# Auto Confetti
components.html("""
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<script>
setTimeout(function() {
    confetti({
        particleCount: 250,
        spread: 120,
        origin: { y: 0.6 }
    });
}, 1500);
</script>
""", height=0)