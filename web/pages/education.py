# web/pages/education.py
# Exoura — Education (Section 1 only) with Home/Demo/Results nav (copied from Home)
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

/* Gradient titles (purple -> blue) scoped inside .main-wrap */
.main-wrap h1, .main-wrap h2, .main-wrap h3, .main-wrap .page-hero h1 {
    background: linear-gradient(90deg, #7c3aed 0%, #2563eb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}

/* Explicit class to force gradient on headings rendered by Streamlit markdown */
.gradient-title {
    background: linear-gradient(90deg, #7c3aed 0%, #2563eb 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    color: transparent !important;
    display: inline-block !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER (Home / Demo / Results) ------------------
with st.container():
    st.markdown('<div class="site-header">', unsafe_allow_html=True)
    left, right = st.columns([2,4], vertical_alignment="center")

    with left:
        st.markdown('<h1 class="brand-name">Exoura</h1>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="nav">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        # NOTE: On Education we replace "Education" with "Home"
        if c1.button("Home", use_container_width=True):
            try:
                st.switch_page("home.py")
            except Exception:
                st.experimental_rerun()
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

st.markdown('<h3 class="gradient-title">What is an exoplanet?</h3>', unsafe_allow_html=True)
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

st.markdown('<h3 class="gradient-title">What is transit photometry?</h3>', unsafe_allow_html=True)
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

# ------------------ SECTION 3: What are false positives? ------------------
# (Append-only; safe to paste at the end of your current file)

st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

st.markdown('<h3 class="gradient-title">What are false positives?</h3>', unsafe_allow_html=True)
st.markdown(
    "<p class='lead'>Not every dip in brightness is caused by a planet. "
    "<strong>False positives</strong> are planet look-alikes created by stars, instruments, or nearby sources. "
    "Knowing the usual suspects helps you avoid common traps.</p>",
    unsafe_allow_html=True
)

def fp_card(title: str, what_happens: list[str], how_to_tell: list[str]):
    st.markdown(f"#### {title}")
    st.markdown("**What happens:**")
    for s in what_happens:
        st.markdown(f"- {s}")
    st.markdown("**How to tell apart:**")
    for s in how_to_tell:
        st.markdown(f"- {s}")
    st.divider()

# 1) Eclipsing binaries (EBs)
fp_card(
    "Eclipsing binaries (EBs)",
    ["Two stars orbit each other; one blocks the other’s light, mimicking a transit."],
    [
        "Dips are often **too deep** (≫ 5–10% brightness drop).",
        "**Odd vs even** dips can differ; a **secondary eclipse** may appear at phase ≈ 0.5.",
        "Very large **radial velocities** (km/s) in follow-up indicate stellar masses.",
    ],
)

# 2) Background / blended binaries
fp_card(
    "Background / blended binaries",
    ["A faint binary system aligns behind/near the target; their light blends with the target’s."],
    [
        "Depth appears **diluted**; doesn’t add up once contamination is corrected.",
        "**Centroid shift** during dips; **chromatic** (color-dependent) transit depth.",
        "High-resolution imaging reveals multiple sources.",
    ],
)

# 3) Star spots / stellar activity
fp_card(
    "Star spots / stellar activity",
    ["Dark spots on a rotating star or flares cause brightness dips that mimic transits."],
    [
        "Signals are **not strictly periodic** like planetary orbits.",
        "Dips are **broader** and **evolve** over time; often look sinusoidal.",
        "Spectroscopic monitoring shows activity cycles / rotation.",
    ],
)

# 4) Instrumental / systematic noise
fp_card(
    "Instrumental / systematic noise",
    ["Detector glitches, spacecraft jitter, or cosmic rays can create artificial dips."],
    [
        "Usually **single** or **irregular** events; **don’t repeat** at a steady period.",
        "Often **asymmetric/jagged**; disappear after good **detrending/calibration**.",
    ],
)

# 5) Pulsating / variable stars
fp_card(
    "Pulsating / variable stars",
    ["Some stars naturally vary in brightness due to pulsations or irregular variability."],
    [
        "Variations are **quasi-periodic or multi-periodic**, not a short symmetric transit.",
        "Depth and duration can **change** from cycle to cycle.",
        "Frequency analysis reveals stellar pulsations.",
    ],
)

# 6) Contamination from nearby stars
fp_card(
    "Contamination from nearby stars",
    ["Light from nearby stars in the same pixel/aperture **dilutes** the target’s signal."],
    [
        "**Centroid analysis** shows the dip originates slightly **off-target**.",
        "After **de-blending**, the inferred radius is **too large** (stellar).",
    ],
)

st.markdown(
    "<div class='callout small'>Rule of thumb: planet-like depths are usually **≤ 2–3%**. "
    "If you’re seeing **≫ 5–10%**, suspect an <strong>eclipsing binary</strong> or another non-planet scenario.</div>",
    unsafe_allow_html=True,
)

st.markdown("---")
st.markdown("</div>", unsafe_allow_html=True)  # close .main-wrap for Section 3


# ------------------ SECTION 4: Planet vs False Positive — how to tell ------------------
# (Append-only; follows immediately after Section 3)

st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

st.markdown('<h3 class="gradient-title">Planet vs False Positive — how to tell</h3>', unsafe_allow_html=True)
st.markdown(
    "<p class='lead'>Use this quick checklist to decide if a dip is likely a "
    "<strong>planet</strong> or a <strong>false positive</strong>. "
    "It’s beginner-friendly and maps directly to what you’ll see in the game.</p>",
    unsafe_allow_html=True
)

st.markdown("#### The 60-second checklist")
st.markdown("1) **Repeatability (Period):** Do similar dips repeat at **regular intervals**?  \n"
            " • No → likely **noise/activity**.  \n"
            " • Yes → go to step 2.")
st.markdown("2) **Depth sanity:** Is the dip **planet-sized** (typically **≤ 2–3%**) and **not** ≫ **5–10%**?  \n"
            " • Too deep → suspect **eclipsing binary (EB)**.")
st.markdown("3) **Shape & duration:** Is the dip **short**, **smooth**, and fairly **symmetric** (U or shallow V)?  \n"
            " • Jagged/one-off → **instrumental** or **stellar activity**.")
st.markdown("4) **Odd vs even:** In a phase-folded view, are **odd and even dips the same** depth?  \n"
            " • Different → **EB**.")
st.markdown("5) **Secondary / centroid / color:**  \n"
            " • **Secondary** dip near phase ~0.5 → **EB/blended binary**.  \n"
            " • **Centroid shift** or **color-dependent depth** → **blend/contamination**.")

st.markdown("#### Quick side-by-side tells")
colA, colB = st.columns(2)
with colA:
    st.markdown("**Planet-like usually…**")
    st.markdown("- ✅ Repeats with a steady **period**")
    st.markdown("- ✅ **Small depth** (<~2–3%)")
    st.markdown("- ✅ **Smooth, symmetric** transit shape")
    st.markdown("- ✅ **Odd = even** depths")
    st.markdown("- ✅ **No secondary**, **no centroid shift**")

with colB:
    st.markdown("**False positive-like often…**")
    st.markdown("- ❌ Irregular or **non-repeating**")
    st.markdown("- ❌ **Deep** dips (≫ 5–10%)")
    st.markdown("- ❌ **Odd ≠ even** or clear **secondary**")
    st.markdown("- ❌ **Jagged/sinusoidal** (instrument/stellar)")
    st.markdown("- ❌ **Centroid motion** or **chromatic** depth")

st.markdown("#### Handy numbers (rules of thumb)")
st.latex(r"\text{depth} \;\approx\; \left(\frac{R_p}{R_\star}\right)^2")
st.markdown(
    "- **$R_p$** = planet radius • **$R_\\star$** = star radius  \n"
    "- **Hot Jupiter:** $R_p/R_\\star \\approx 0.10$ → depth ≈ **1%** (10,000 ppm)  \n"
    "- **Neptune-size:** $\\approx 0.035$ → depth ≈ **0.12%** (≈1,200 ppm)  \n"
    "- **Earth–Sun:** $\\approx 0.009$ → depth ≈ **0.008%** (≈80 ppm)"
)

st.markdown(
    "<div class='callout small'><strong>Decision path:</strong> "
    "Repeat? → Size sane? → Shape okay? → Odd = Even? → No secondary/centroid? "
    "If yes to all → <strong>Planet candidate</strong>. Otherwise → <strong>False positive likely</strong>.</div>",
    unsafe_allow_html=True,
)

st.markdown("---")
st.markdown("</div>", unsafe_allow_html=True)  # close .main-wrap for Section 4