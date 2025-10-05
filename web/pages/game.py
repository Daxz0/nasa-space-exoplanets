import streamlit as st
import random
import joblib
import pandas as pd
from pathlib import Path
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Exoura • Game",
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



def generate_values():
    """
    Generate random realistic values for exoplanet parameters based on Kepler data ranges.
    Returns a dictionary with parameter names as keys and generated values.
    """
    # Generate realistic random values based on Kepler dataset ranges
    values = {
        'koi_period': round(random.uniform(0.5, 500.0), 3),  # Orbital Period in days (0.5 to ~500 days)
        'koi_duration': round(random.uniform(0.5, 20.0), 3),  # Transit Duration in hours (0.5 to ~20 hours)
        'koi_depth': round(random.uniform(10.0, 15000.0), 1),  # Transit Depth in ppm (10 to ~15,000 ppm)
        'koi_prad': round(random.uniform(0.1, 30.0), 2),  # Planet Radius in Earth radii (0.1 to ~30 Earth radii)
        'koi_model_snr': round(random.uniform(5.0, 500.0), 1)  # Signal-to-Noise Ratio (5 to ~500)
    }
    
    return values


def set_random_values():
    """
    Generate and set random values in Streamlit session state for all exoplanet parameters.
    This function can be called when a "Generate Random Values" button is clicked.
    """
    random_values = generate_values()
    
    # Set the values in Streamlit session state
    for param, value in random_values.items():
        st.session_state[param] = value


def get_parameter_info():
    """
    Returns information about each parameter for educational purposes.
    """
    return {
        'koi_period': {
            'name': 'Orbital Period',
            'unit': 'days',
            'description': 'Time taken for one complete orbit around the star.',
            'typical_range': '0.5 - 500 days'
        },
        'koi_duration': {
            'name': 'Transit Duration',
            'unit': 'hours', 
            'description': 'Duration of the transit event in hours.',
            'typical_range': '0.5 - 20 hours'
        },
        'koi_depth': {
            'name': 'Transit Depth',
            'unit': 'ppm',
            'description': 'Depth of the transit in parts per million.',
            'typical_range': '10 - 15,000 ppm'
        },
        'koi_prad': {
            'name': 'Planet Radius',
            'unit': 'Earth radii',
            'description': 'Radius of the planet in Earth radii.',
            'typical_range': '0.1 - 30 Earth radii'
        },
        'koi_model_snr': {
            'name': 'Signal-to-Noise Ratio',
            'unit': 'unitless',
            'description': 'Signal-to-noise ratio of the transit model.',
            'typical_range': '5 - 500'
        }
    }


def load_model():
    """
    Load the trained Random Forest model.
    """
    # Correctly locate the model file relative to the current script
    model_path = Path(__file__).parent / 'random_forest_model.joblib'
    model = joblib.load(model_path)
    return model

def predict_planet(model, planet_data):
    """
    Predict if a planet is 'CONFIRMED' or 'FALSE POSITIVE' and return confidence.
    This aligns with the trained model that expects 8 features in this order:
    ['koi_prad','koi_dicco_msky','koi_dikco_msky','koi_dor','koi_prad_err2','koi_period','koi_duration','koi_depth']
    Returns: (label: str, confidence: float in [0,1])
    """
    # Build feature vector in the model's training order; fill unknowns with 0.0
    x = [[
        planet_data.get('koi_prad', 0.0),
        planet_data.get('koi_dicco_msky', 0.0),
        planet_data.get('koi_dikco_msky', 0.0),
        planet_data.get('koi_dor', 0.0),
        planet_data.get('koi_prad_err2', 0.0),
        planet_data.get('koi_period', 0.0),
        planet_data.get('koi_duration', 0.0),
        planet_data.get('koi_depth', 0.0),
    ]]

    pred_raw = model.predict(x)[0]
    proba = model.predict_proba(x)[0]
    classes = list(getattr(model, 'classes_', []))
    # Map predicted class to index for confidence
    try:
        cls_index = classes.index(pred_raw)
    except ValueError:
        # Fallback if types differ (e.g., int vs str cast)
        cls_index = 1 if str(pred_raw).lower().startswith('false') or str(pred_raw) == '1' else 0

    confidence = float(proba[cls_index]) if len(proba) > cls_index else float(max(proba) if len(proba) else 0.0)

    # Normalize label to UI terms
    if isinstance(pred_raw, (int, float)):
        label = 'FALSE POSITIVE' if int(pred_raw) == 1 else 'CONFIRMED'
    else:
        low = str(pred_raw).lower()
        label = 'FALSE POSITIVE' if 'false' in low else 'CONFIRMED'

    return label, confidence

def main():
    """
    Main function to run the exoplanet guessing game.
    """
    st.title("Exoplanet Guessing Game")
    st.write("Can you tell if a planet is a **CONFIRMED** candidate or a **FALSE POSITIVE**?")
    st.write("Based on the following data, make your best guess!")

    model = load_model()

    # Initialize or update the planet data in the session state
    if 'planet_data' not in st.session_state:
        st.session_state.planet_data = generate_values()
        pred_label, pred_conf = predict_planet(model, st.session_state.planet_data)
        st.session_state.model_prediction = pred_label
        st.session_state.model_confidence = pred_conf
        st.session_state.user_guessed = False
        st.session_state.start_time = time.time()
        st.session_state.elapsed_time = 0.0

    # Display the planet's parameters
    planet_data = st.session_state.planet_data
    param_info = get_parameter_info()
    
    # Live timer display (top-right)
    timer_col1, timer_col2 = st.columns([3, 1])
    with timer_col2:
        if not st.session_state.get('user_guessed', False):
            elapsed = time.time() - st.session_state.get('start_time', time.time())
            st.metric(label="⏱️ Time", value=f"{elapsed:.1f}s")
        else:
            st.metric(label="⏱️ Time", value=f"{st.session_state.get('elapsed_time', 0.0):.1f}s")
    
    cols = st.columns(len(planet_data))
    for i, (param, value) in enumerate(planet_data.items()):
        info = param_info.get(param, {})
        with cols[i]:
            st.metric(label=info.get('name', param), value=f"{value} {info.get('unit', '')}", help=info.get('description'))

    st.markdown("---")

    # Game interaction
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
        # Provide feedback after the user has guessed
        user_guess = st.session_state.user_guess
        correct_answer = st.session_state.model_prediction
        confidence_pct = st.session_state.get('model_confidence', 0.0) * 100

        if user_guess == correct_answer:
            st.success(f"Correct! You guessed **{user_guess}**, and the model agrees.")
        else:
            st.error(f"Incorrect! You guessed **{user_guess}**, but the model predicted **{correct_answer}**.")
        
        st.info(
            f"**Model's Prediction**: **{correct_answer}**  •  **Confidence**: {confidence_pct:.1f}%  •  **Your time**: {st.session_state.get('elapsed_time', 0.0):.1f}s"
        )

        if st.button("Next Planet", use_container_width=True):
            # Reset the game with new values
            st.session_state.planet_data = generate_values()
            pred_label, pred_conf = predict_planet(model, st.session_state.planet_data)
            st.session_state.model_prediction = pred_label
            st.session_state.model_confidence = pred_conf
            st.session_state.user_guessed = False
            st.session_state.start_time = time.time()
            st.session_state.elapsed_time = 0.0
            st.rerun()

    # Auto-refresh every second to update the live timer while awaiting a guess
    if not st.session_state.get('user_guessed', False):
        time.sleep(1)
        st.rerun()

if __name__ == "__main__":
    main()


