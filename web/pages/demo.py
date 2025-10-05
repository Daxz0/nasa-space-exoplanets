import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Demo - Exoura",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ GLOBAL STYLES ------------------
st.markdown("""
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Urbanist:wght@500;700;900&family=Azeret+Mono:wght@500;700&family=Orbitron:wght@700&display=swap" rel="stylesheet">

<style>
/* Hide Streamlit chrome */
#MainMenu, header, footer {visibility: hidden;}
[data-testid="stSidebar"], section[data-testid="stSidebarNav"], div[aria-label^="App pages"] { display: none !important; }

/* Core layout */
.block-container { padding-top: 0 !important; }
.stApp { background: #050510 !important; color: #e5e7eb; font-family: 'DM Sans', sans-serif; }

/* ===== HEADER ===== */
.site-header {
  position: sticky; top: 0; z-index: 999;
  background: rgba(5,5,16,0.92);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding: .75rem 2rem;
  display: flex; justify-content: space-between; align-items: center;
}
.brand-name {
  font-family: 'Urbanist', sans-serif;
  font-weight: 900; font-size: 1.8rem; color: #fff;
  letter-spacing: -0.02em;
}

.nav { display: flex; gap: 1rem; }
.nav .stButton>button {
  background: transparent; border: 1px solid rgba(255,255,255,.15);
  padding: .5rem 1rem; border-radius: 10px;
  color: #fff; font-weight: 600; transition: all .2s ease;
}
.nav .stButton>button:hover { background: rgba(255,255,255,.12); }
.nav .stButton>button:focus { outline: 2px solid #3b82f6; }

/* ===== HERO ===== */
.hero {
  min-height: 60vh; display: flex; align-items: center; justify-content: center;
  text-align: center; padding: 4rem 1rem;
}
.hero-inner { max-width: 900px; }
.hero-title {
  font-family: 'Urbanist', sans-serif;
  font-weight: 900; font-size: clamp(2.5rem, 6vw, 4.5rem);
  background: linear-gradient(90deg, #7aa2ff, #a78bfa);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 1rem;
}
.hero-sub {
  font-size: 1.2rem; opacity: .9; line-height: 1.6;
  margin-bottom: 2.5rem;
}

/* ===== DEMO SPECIFIC STYLES ===== */
h1, h2, h3, h4, h5, h6 {
    color: #aee2ff;
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 2px;
}

/* Style number input label and box */
label, .stNumberInput label {
    color: #aee2ff !important;
    font-weight: 600;
    font-size: 1.1em;
    margin-bottom: 0.2em;
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 1px;
}
.stNumberInput > div > input {
    background: #1a2636 !important;
    color: #aee2ff !important;
    border-radius: 8px !important;
    border: 1px solid #3a506b !important;
    font-size: 1.1em;
    font-family: 'Orbitron', sans-serif;
}
.stButton > button {
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    color: #fff;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    box-shadow: 0 2px 8px rgba(30,60,114,0.2);
}
.stMarkdown, .stDataFrame, .stTable {
    background: transparent !important;
    border-radius: 0 !important;
    padding: 0 !important;
    color: #e0e6ed;
    box-shadow: none !important;
}
.stPlotlyChart, .stImage, .stAltairChart, .stVegaLiteChart, .stPyplot {
    background: transparent !important;
    border-radius: 0 !important;
    padding: 0 !important;
    box-shadow: none !important;
}

/* Animated stars background */
.stars {
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: 0;
    pointer-events: none;
}
.star {
    position: absolute;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
    animation: twinkle 2s infinite ease-in-out;
}
@keyframes twinkle {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 0.2; }
}

@media (max-width: 640px){
  .hero { padding: 2.5rem 1rem; }
}
</style>
""", unsafe_allow_html=True)

# Add animated stars background
import random
star_html = "<div class='stars' style='pointer-events:none; position:fixed; width:100vw; height:100vh; top:0; left:0; z-index:0;'>"
for _ in range(80):
    top = random.randint(0, 100)
    left = random.randint(0, 100)
    size = random.uniform(2, 5)
    star_html += f"<div class='star' style='top:{top}vh; left:{left}vw; width:{size}px; height:{size}px;'></div>"
star_html += "</div>"
st.markdown(star_html, unsafe_allow_html=True)

# ------------------ HEADER ------------------
with st.container():
    st.markdown('<div class="site-header">', unsafe_allow_html=True)
    left, right = st.columns([2,4], vertical_alignment="center")

    with left:
        st.markdown('<h1 class="brand-name">Exoura</h1>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("Home", use_container_width=True):
            st.switch_page("home.py")
        if c2.button("Education", use_container_width=True):
            st.switch_page("pages/education.py")
        if c3.button("Methods", use_container_width=True):
            st.switch_page("pages/methods.py")
        if c4.button("Game", use_container_width=True):
            st.switch_page("pages/game.py")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



st.markdown("""
<div class="hero">
  <div class="hero-inner">
    <h1 class="hero-title">Exouria Demo</h1>
    <p class="hero-sub">
      Try our demo of the random forest model at work, input in values from NASA's exoplanet datasets to the following parameters!
    </p>
</div>
</div>
""", unsafe_allow_html=True)

model = joblib.load('random_forest_model.joblib')


input_cols = st.columns(5)
with input_cols[0]:
    koi_period = st.number_input('Orbital Period (days)', value=0.0, step=1.0, format="%f", key='koi_period', help='Time taken for one complete orbit around the star.')
with input_cols[1]:
    koi_duration = st.number_input('Transit Duration (hours)', value=0.0, step=1.0, format="%f", key='koi_duration', help='Duration of the transit event in hours.')
with input_cols[2]:
    koi_depth = st.number_input('Transit Depth (ppm)', value=0.0, step=1.0, format="%f", key='koi_depth', help='Depth of the transit in parts per million.')
with input_cols[3]:
    koi_prad = st.number_input('Planet Radius (Earth radii)', value=0.0, step=1.0, format="%f", key='koi_prad', help='Radius of the planet in Earth radii.')
with input_cols[4]:
    koi_model_snr = st.number_input('Signal Noise Ratio', value=0.0, step=1.0, format="%f", key='koi_model_snr', help='Signal-to-noise ratio of the model.')

inputs = [koi_period, koi_duration, koi_depth, koi_prad, koi_model_snr]

if any(x != 0.0 for x in inputs):
    input_array = np.array([inputs])
    predicted_index = model.predict(input_array)[0]
    labels = ['Not False Positive', 'False Positive']
    predicted_label = labels[predicted_index]

    probs = model.predict_proba(input_array)[0]
    fig, ax = plt.subplots(figsize=(4,4))
    pie_result = ax.pie(
        probs, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=['#66b3ff','#ff9999'], textprops={'color':'#e0e6ed','fontsize':14})
    ax.axis('equal')
    
    if len(pie_result) == 3:
        patches, texts, autotexts = pie_result
        plt.setp(autotexts, size=16, weight="bold")
    else:
        patches, texts = pie_result
    plt.setp(texts, size=14)
    fig.patch.set_alpha(0)

    color = '#ff9999' if predicted_label == 'False Positive' else '#66b3ff'
    st.markdown(f"""
    <div style='background:rgba(20,30,48,0.85); border-radius:16px; padding:2em 2em 2em 2em; margin-top:1.5em; box-shadow:0 2px 12px rgba(30,60,114,0.12); max-width: 500px; margin-left:auto; margin-right:auto; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;'>
        <h2 style='color:#aee2ff; text-align:center; width:100%;'>Prediction</h2>
        <h3 style='color:{color}; font-size:2em; margin:0.5em 0 0.1em 0; text-align:center; width:100%;'>{predicted_label}</h3>
        <div style='display:flex; justify-content:center; margin-top:0.5em; width:100%;'>
    """, unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown(f"""
        </div>
    </div>
    """, unsafe_allow_html=True)
