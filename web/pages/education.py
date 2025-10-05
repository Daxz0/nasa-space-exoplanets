# web/pages/education.py
# Exoura — Education (Section 1 only) with Home/Demo/methods nav (copied from Home)
# - Nav copied 1:1 from Home, but "Education" button becomes "Home" -> home.py
# - Section 1: "What is an exoplanet?" + exoplanet_rotation.gif
# - Sections 2+ left as TODOs

from pathlib import Path
from typing import Optional
import streamlit as st
import base64

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Exoura • Education",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ GLOBAL STYLES (copied from Home) ------------------
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

/* Content wrap for sections */
.main-wrap { max-width: 1200px; margin: 1.2rem auto 2rem auto; padding: 0 1rem; }
.lead { font-size: 1.05rem; opacity: .92; }
.callout { padding: .75rem 1rem; border: 1px solid rgba(255,255,255,0.12); border-radius: 12px; background: rgba(255,255,255,0.04); }
.kicker { text-transform: uppercase; letter-spacing: .12em; font-weight: 700; font-size: .8rem; color: #9ca3af; }
.small { font-size: .9rem; opacity: .85; }
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER (Home / Demo / methods) ------------------
with st.container():
    st.markdown('<div class="site-header">', unsafe_allow_html=True)
    left, right = st.columns([2,4], vertical_alignment="center")

    with left:
        st.markdown('<h1 class="brand-name">Exoura</h1>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        if c1.button("Home", use_container_width=True):
            st.switch_page("home.py")
        if c2.button("Demo", use_container_width=True):
            st.switch_page("pages/demo.py")
        if c3.button("Methods", use_container_width=True):
            st.switch_page("pages/methods.py")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ HELPERS ------------------
def find_gif(filename: str) -> Optional[Path]:
    """
    Look for the GIF in common repo locations:
    - current file directory (web/pages/)
    - parent (web/)
    - assets folder (web/assets/ or web/pages/assets/)
    - repo root
    """
    here = Path(__file__).parent
    # also check the repo root (two levels up from web/pages) and web/ root
    repo_root = Path(__file__).resolve().parents[2]
    candidates = [
        here / filename,                         # web/pages/exoplanet_rotation.gif
        here.parent / filename,                  # web/exoplanet_rotation.gif
        repo_root / filename,                    # <repo_root>/exoplanet_rotation.gif
        repo_root / 'web' / filename,            # <repo_root>/web/exoplanet_rotation.gif
        here / "assets" / filename,            # web/pages/assets/...
        here.parent / "assets" / filename,     # web/assets/...
        Path.cwd() / filename                    # current working dir, just in case
    ]
    for p in candidates:
        if p.is_file():
            return p
    return None

# ------------------ SECTION 1: What is an exoplanet? ------------------
st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

st.markdown("### What is an exoplanet?")
st.markdown(
    "<p class='lead'>An <strong>exoplanet</strong> is a planet orbiting a star other than the Sun. "
    "Because planets are faint and close to bright stars, we usually can’t see them directly. "
    "Instead, we watch the <em>star’s brightness over time</em>, also known as a <strong>light curve</strong>, "
    "for patterns a planet would create.</p>",
    unsafe_allow_html=True
)

col_text, col_media = st.columns([7,5], vertical_alignment="center")

with col_text:
    st.markdown("#### Key terms (you’ll see these in the game)")
    st.markdown("- **Light curve**: the star’s brightness plotted against time.")
    st.markdown("- **Dip**: a brief, tiny drop in brightness.")
    st.markdown("- **Transit**: when a planet crosses its star and causes a repeating dip.")

    st.markdown("<div class='callout small'>Why this matters: In Exoura you’ll classify light curves — "
                "<strong>planet</strong> or <strong>not a planet</strong> — by reading these tiny dips.</div>",
                unsafe_allow_html=True)

with col_media:
    gif_path = find_gif("exoplanet_rotation.gif")
    if gif_path:
        st.image(str(gif_path), caption="Exoplanet orbiting a star (concept).", use_container_width=True)
    else:
        st.warning("Couldn’t find `exoplanet_rotation.gif`. Place it next to this file (`web/pages/`) or in `web/` or `web/assets/`.")

st.markdown("---")

# ------------------ PLACEHOLDERS for next sections (to add later) ------------------
# st.markdown("### What is transit photometry?")  # TODO: Section 2
# st.markdown("### Planet vs False Positive — how to tell")  # TODO: Section 3
# st.markdown("### Common False Positives")  # TODO: Section 4
# st.markdown("### Ready? → Try the Demo")  # TODO: CTA

st.markdown("</div>", unsafe_allow_html=True)  # close .main-wrap

# ------------------ SECTION 2: What is transit photometry? ------------------
# (Append-only; safe to paste at the end of your current file)

st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

st.markdown("### What is transit photometry?")
st.markdown(
    "<p class='lead'>When a planet crosses (transits) its star, it blocks a tiny fraction of light. "
    "On a light curve, that shows up as a small, repeating <strong>dip</strong>. "
    "By measuring how <em>deep</em> the dip is, how often it <em>repeats</em> (the period), and its <em>shape</em>, "
    "we can tell planet-like signals from look-alikes.</p>",
    unsafe_allow_html=True
)

txt, media = st.columns([7, 5], vertical_alignment="center")

with txt:
    st.markdown("#### The three cues you’ll use")
    st.markdown("**1) Depth — how deep is the dip?**")
    st.latex(r"\text{depth} \;\approx\; \left(\frac{R_p}{R_\star}\right)^2")
    st.markdown(
        "- **$R_p$** = planet radius (size of the planet)\n"
        "- **$R_\\star$** = stellar radius (size of the star; the ★ symbol means “star”)\n"
        "- Bigger planets block more light → a deeper dip."
    )

    st.markdown("**Rules of thumb (depth examples):**")
    st.markdown(
        "- **Hot Jupiter** ($R_p/R_\\star \\approx 0.10$) → depth ≈ **1%** (10,000 ppm)\n"
        "- **Neptune-size** ($R_p/R_\\star \\approx 0.035$) → depth ≈ **0.12%** (≈1,200 ppm)\n"
        "- **Earth–Sun** ($R_p/R_\\star \\approx 0.009$) → depth ≈ **0.008%** (≈80 ppm)"
    )

    st.markdown("**What depths look planet-like?**")
    st.markdown(
        "- **Typically ≤ 2–3%** is consistent with planets (depends on star size).\n"
        "- **≫ 5–10%** is usually **too deep** for a planet → often an **eclipsing binary** (two stars)."
    )

    st.markdown("**2) Period — does it repeat steadily?**")
    st.markdown(
        "- Measure the time from one dip to the next: that’s the **orbital period**.\n"
        "- Real planets produce dips that **repeat at regular intervals**."
    )

    st.markdown("**3) Duration & shape — does it look like a transit?**")
    st.markdown(
        "- A transit is **short** compared to the period and **smooth** with a fairly **symmetric** U-shape "
        "(a shallow V can also be fine).\n"
        "- Jagged, step-like, or single one-off dips are **suspicious** (often noise or star activity)."
    )

    st.markdown(
        "<div class='callout small'>Why this matters: in Exoura, most quick, correct calls come from reading "
        "<strong>Depth + Period + Shape</strong>. If any of these don’t look right, consider "
        "<strong>Not a planet</strong> and let follow-up data decide.</div>",
        unsafe_allow_html=True
    )

    st.markdown("**Unit translator (handy):**")
    st.markdown(
        "- **1%** drop = **10,000 ppm**  •  **0.1%** = **1,000 ppm**  •  **0.01%** = **100 ppm**"
    )

with media:
    gif2 = find_gif("transit_rotation.gif")
    if gif2:
        # Embed as base64 data URI to preserve GIF animation reliably
        try:
            with open(gif2, 'rb') as f:
                data = f.read()
            b64 = base64.b64encode(data).decode('ascii')
            img_html = (
                f'<img src="data:image/gif;base64,{b64}" '
                f'alt="Transit animation" style="width:100%;height:auto;border-radius:8px;" />'
            )
            st.markdown(img_html, unsafe_allow_html=True)
        except Exception:
            # fallback to st.image if embedding fails
            st.image(str(gif2), caption="Transit photometry: a planet crossing its star creates a repeating dip.", use_container_width=True)
    else:
        st.warning("Couldn’t find `transit_rotation.gif`. Place it in `web/pages/`, `web/`, or `web/assets/`.")

st.markdown("---")
st.markdown("</div>", unsafe_allow_html=True)  # close .main-wrap for Section 2