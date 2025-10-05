import streamlit as st
import random
import joblib
import pandas as pd
from pathlib import Path
import time
from streamlit.components.v1 import html

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Exoura - Game",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ GLOBAL STYLES ------------------
st.markdown("""
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Urbanist:wght@500;700;900&family=Azeret+Mono:wght@500;700&display=swap" rel="stylesheet">

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
</style>
""", unsafe_allow_html=True)

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
        if c3.button("Demo", use_container_width=True):
            st.switch_page("pages/demo.py")
        if c4.button("Methods", use_container_width=True):
            st.switch_page("pages/methods.py")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ------------------ GAME FUNCTIONS ------------------
def generate_values():
    return {
        'koi_period': round(random.uniform(0.5, 500.0), 3),
        'koi_duration': round(random.uniform(0.5, 20.0), 3),
        'koi_depth': round(random.uniform(10.0, 15000.0), 1),
        'koi_prad': round(random.uniform(0.1, 30.0), 2),
        # Ratio of orbital semi-major axis to stellar radius (a/R*), unitless
        'koi_dor': round(random.uniform(2.0, 100.0), 2),
    }

def get_parameter_info():
    return {
        'koi_period': {'name': 'Orbital Period', 'unit': 'days', 'description': 'Time taken for one complete orbit around the star.'},
        'koi_duration': {'name': 'Transit Duration', 'unit': 'hours', 'description': 'Duration of the transit event in hours.'},
        'koi_depth': {'name': 'Transit Depth', 'unit': 'ppm', 'description': 'Depth of the transit in parts per million.'},
        'koi_prad': {'name': 'Planet Radius', 'unit': 'Earth radii', 'description': 'Radius of the planet in Earth radii.'},
        'koi_dor': {'name': 'Orbit Ratio (a/R*)', 'unit': 'unitless', 'description': 'Ratio of orbital distance to stellar radius.'},
    }

def load_model():
    """
    Load the trained Random Forest model.
    """
    # Try common locations relative to this file and the repo root
    here = Path(__file__).parent
    repo_root = here.parents[2] if len(here.parents) >= 2 else Path.cwd()
    candidates = [
        here / 'random_forest_model.joblib',
        here.parent / 'pages' / 'random_forest_model.joblib',
        repo_root / 'web' / 'pages' / 'random_forest_model.joblib',
        repo_root / 'src' / 'models' / 'trained_models' / 'random_forest_model.joblib',
    ]
    for p in candidates:
        if p.exists():
            return joblib.load(p)
    st.error("Couldn't find random_forest_model.joblib. Tried: " + ", ".join(str(p) for p in candidates))
    raise FileNotFoundError("random_forest_model.joblib not found in expected locations")

def predict_planet(model, planet_data):
    # Model trained on 5 features in this exact order:
    # ['koi_prad','koi_dor','koi_period','koi_duration','koi_depth']
    x = [[
        planet_data.get('koi_prad', 0.0),
        planet_data.get('koi_dor', 0.0),
        planet_data.get('koi_period', 0.0),
        planet_data.get('koi_duration', 0.0),
        planet_data.get('koi_depth', 0.0),
    ]]
    pred_raw = model.predict(x)[0]
    proba = model.predict_proba(x)[0]
    classes = list(getattr(model,'classes_',[]))
    try: cls_index = classes.index(pred_raw)
    except ValueError: cls_index = 1 if str(pred_raw).lower().startswith('false') else 0
    confidence = float(proba[cls_index]) if len(proba) > cls_index else float(max(proba) if len(proba) else 0.0)
    label = 'FALSE POSITIVE' if str(pred_raw).lower().startswith('false') else 'CONFIRMED'
    return label, confidence

# ------------------ MAIN GAME ------------------
def main():
    st.title("Exoplanet Guessing Game")
    st.write("Can you tell if a planet is a **CONFIRMED** candidate or a **FALSE POSITIVE**?")
    st.write("Based on the following data, make your best guess!")

    model = load_model()

    if 'planet_data' not in st.session_state:
        st.session_state.planet_data = generate_values()
        pred_label, pred_conf = predict_planet(model, st.session_state.planet_data)
        st.session_state.model_prediction = pred_label
        st.session_state.model_confidence = pred_conf
        st.session_state.user_guessed = False
        st.session_state.start_time = time.time()
        st.session_state.elapsed_time = 0.0

    planet_data = st.session_state.planet_data
    param_info = get_parameter_info()

    # ------------------ SLEEK FLOATING TIMER ------------------
    start_ms = int(st.session_state.get('start_time', time.time())*1000)
    user_guessed = bool(st.session_state.get('user_guessed', False))
    fixed_time = float(st.session_state.get('elapsed_time', 0.0))
    
    timer_html = f"""
    <div id="timer-box" style="
        position: fixed;
        top: 0px;
        right: 16px;
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding: 12px 16px;
        border-radius: 12px;
        background: rgba(255,255,255,0.1);
        box-shadow: 0 0 15px rgba(255,255,255,0.2);
        font-family: 'DM Sans', sans-serif;
        color: #ffffff;
        font-size: 20px;
        gap: 6px;
        min-width: 120px;
    ">
        <span style="opacity:0.8;">Time</span>
        <strong id="timer-value" style="text-align:right; font-size:28px; font-weight:700;">0.0s</strong>
    </div>

    <script>
        const start = {start_ms};
        const guessed = {str(user_guessed).lower()};
        const fixed = {fixed_time:.3f};
        const el = document.getElementById('timer-value');
        function fmt(s){{ return (Math.round(s*10)/10).toFixed(1) + 's'; }}
        if (guessed) {{
            el.textContent = fmt(fixed);
        }} else {{
            function tick(){{ const now = Date.now(); const sec = (now - start)/1000.0; el.textContent = fmt(sec); }}
            tick();
            window.__exouraTimer && clearInterval(window.__exouraTimer);
            window.__exouraTimer = setInterval(tick, 100);
        }}
    </script>
    """
    html(timer_html, height=48)

    # ------------------ DISPLAY PLANET PARAMETERS ------------------
    cols = st.columns(len(planet_data))
    for i, (param, value) in enumerate(planet_data.items()):
        info = param_info.get(param, {})
        with cols[i]:
            st.metric(label=info.get('name', param), value=f"{value} {info.get('unit','')}", help=info.get('description'))

    st.markdown("---")

    # ------------------ GAME INTERACTIONS ------------------
    if not st.session_state.user_guessed:
        st.subheader("Your Guess:")
        guess_cols = st.columns(2)
        with guess_cols[0]:
            if st.button("CONFIRMED Candidate", use_container_width=True):
                st.session_state.user_guess = "CONFIRMED"
                st.session_state.user_guessed = True
                st.session_state.elapsed_time = time.time() - st.session_state.get('start_time', time.time())
                st.rerun()
        with guess_cols[1]:
            if st.button("FALSE POSITIVE", use_container_width=True):
                st.session_state.user_guess = "FALSE POSITIVE"
                st.session_state.user_guessed = True
                st.session_state.elapsed_time = time.time() - st.session_state.get('start_time', time.time())
                st.rerun()
    else:
        user_guess = st.session_state.user_guess
        correct_answer = st.session_state.model_prediction
        confidence_pct = st.session_state.get('model_confidence',0.0)*100
        if user_guess == correct_answer:
            st.success(f"Correct! You guessed **{user_guess}**, and the model agrees.")
        else:
            st.error(f"Incorrect! You guessed **{user_guess}**, but the model predicted **{correct_answer}**.")
        st.info(f"**Model's Prediction**: **{correct_answer}**  •  **Confidence**: {confidence_pct:.1f}%  •  **Your time**: {st.session_state.get('elapsed_time',0.0):.1f}s")
        
        if st.button("Next Planet", use_container_width=True):
            st.session_state.planet_data = generate_values()
            pred_label, pred_conf = predict_planet(model, st.session_state.planet_data)
            st.session_state.model_prediction = pred_label
            st.session_state.model_confidence = pred_conf
            st.session_state.user_guessed = False
            st.session_state.start_time = time.time()
            st.session_state.elapsed_time = 0.0
            st.rerun()

if __name__ == "__main__":
    main()
