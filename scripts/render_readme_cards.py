#!/usr/bin/env python3
import base64
import math
import os
import random
import re
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "cards")
FONTS = os.path.join(ROOT, "fonts")

INK = "#eef2f8"
INK_SOFT = "#cfd7e3"
MUTED = "#a9b3c4"
GOLD = "#e6b325"
GOLD_BRIGHT = "#ffcf3a"
STEEL = "#6b86b8"
GREEN = "#3ddc84"
W = 880

SERIF = "'Instrument Serif', Georgia, serif"
SANS = "Montserrat, system-ui, -apple-system, sans-serif"

FONT_FILES = {
    "serif": ("Instrument Serif", "normal", 400, "serif-400.woff"),
    "sans": ("Montserrat", "normal", "100 900", "montserrat.woff2"),
}

BASE_CSS = """
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes pop{0%{opacity:0;transform:scale(.3)}70%{opacity:1;transform:scale(1.1)}100%{opacity:1;transform:none}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes twinkle{0%,100%{opacity:.15}50%{opacity:.95}}
@keyframes flap{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.55)}}
.r{opacity:0;animation:rise .9s cubic-bezier(.2,.7,.2,1) both;transform-box:fill-box}
.f{opacity:0;animation:fade 1s ease-out both}
.g{transform-box:fill-box;transform-origin:left;transform:scaleX(0);animation:grow 1s cubic-bezier(.2,.7,.2,1) both}
.p{opacity:0;transform-box:fill-box;transform-origin:center;animation:pop .5s ease-out both}
.pu{animation:pulse 2.4s ease-in-out infinite}
.tw{animation:twinkle 3.5s ease-in-out infinite}
.bat{transform-box:fill-box;transform-origin:center;animation:flap .8s ease-in-out infinite}
@media (prefers-reduced-motion: reduce){.r,.f,.g,.p,.pu,.tw,.bat{animation:none!important;opacity:1!important;transform:none!important}}
"""


def font_face(keys):
    out = []
    for k in keys:
        fam, style, weight, fn = FONT_FILES[k]
        b64 = base64.b64encode(open(os.path.join(FONTS, fn), "rb").read()).decode()
        fmt = "woff2" if fn.endswith("woff2") else "woff"
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{weight};"
            f"src:url(data:font/{fmt};base64,{b64}) format('{fmt}')}}"
        )
    return "".join(out)


def svg(w, h, body, fonts, label):
    css = re.sub(r"\s*\n\s*", "", font_face(fonts) + BASE_CSS)
    if os.environ.get("STATIC"):
        css += ".r,.f,.g,.p,.pu,.tw{animation:none!important;opacity:1!important;transform:none!important}"
    body = re.sub(r">\s+<", "><", body).strip()
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" '
        f'role="img" aria-label="{escape(label)}"><title>{escape(label)}</title>'
        f"<style>{css}</style>{body}</svg>"
    )


def write(name, content):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"wrote cards/{name} ({len(content) // 1024} KB)")


def d(s):
    return f'style="animation-delay:{s:.2f}s"'


BAT = ("M500.8 304.4L494.4 285.2L486.8 268.6L475.4 250.2L463.1 235.0L444.4 217.2L427.3 204.9L401.3 190.7L384.7 184.1L360.5 176.5L326.9 169.4L296.6 165.6L267.2 164.2L231.7 165.1L205.6 168.0L173.4 174.1L149.3 181.2L155.2 165.9L157.1 156.9L158.0 146.4L157.1 131.7L153.8 118.0L149.0 105.7L143.3 95.3L132.9 80.6L110.0 57.1L92.9 43.9L75.4 32.5L56.0 22.1L34.6 12.6L0.8 1.5L315.5 1.2L320.0 17.1L327.1 32.3L332.4 39.8L341.1 49.1L353.4 58.1L370.0 65.7L394.7 71.8L419.8 74.7L444.9 74.7L449.6 73.7L455.1 70.2L460.7 58.3L463.6 44.6L469.0 1.2L481.8 40.1L490.3 39.1L519.2 40.1L532.0 0.8L537.0 42.2L542.2 64.0L545.5 69.7L551.5 73.7L568.0 75.1L588.9 74.2L615.9 69.9L633.4 64.7L649.0 57.1L661.4 47.7L673.4 32.7L680.5 18.1L685.5 1.2L1000.8 1.5L984.9 6.0L958.8 15.9L925.2 33.0L907.7 44.3L893.0 55.7L868.6 80.1L853.0 103.8L848.2 115.2L844.4 128.9L843.5 153.5L845.9 165.9L851.3 181.2L825.7 173.7L792.6 167.5L762.3 164.7L731.9 164.2L710.1 165.1L679.8 168.5L645.7 175.1L623.0 181.7L597.9 191.7L577.5 202.6L556.2 217.7L538.4 234.5L522.8 254.4L513.8 269.6L506.2 286.6Z")


def bat_wing(s, f):
    return (
        f"M0 0"
        f"Q{-0.45 * s:.1f} {-s * (0.5 + 0.45 * f):.1f} {-s:.1f} {-s * 0.9 * f:.1f}"
        f"Q{-0.55 * s:.1f} {s * 0.12:.1f} {-0.12 * s:.1f} {s * 0.16:.1f}"
        f"Q{0.55 * s:.1f} {s * 0.12:.1f} {s:.1f} {-s * 0.9 * f:.1f}"
        f"Q{0.45 * s:.1f} {-s * (0.5 + 0.45 * f):.1f} 0 0Z"
    )


def _skyline(w, base_y, min_h, max_h, min_w, max_w, lit, color, win, rnd):
    out, buildings = [], []
    x = -30.0
    while x < w + 40:
        bw = rnd.uniform(min_w, max_w)
        bh = rnd.uniform(min_h, max_h)
        top = base_y - bh
        cxr = x + bw / 2
        out.append(f'<rect x="{x:.0f}" y="{top:.0f}" width="{bw:.0f}" height="{bh:.0f}" fill="{color}"/>')
        style = rnd.random()
        if style < 0.18:
            rh = bw * rnd.uniform(0.35, 0.75)
            out.append(f'<polygon points="{x:.0f},{top:.0f} {x + bw:.0f},{top:.0f} {cxr:.0f},{top - rh:.0f}" fill="{color}" stroke="rgba(150,182,232,.22)" stroke-width="1"/>')
            out.append(f'<rect x="{cxr - 1:.0f}" y="{top - rh - 2:.0f}" width="2" height="2" fill="rgba(255,210,120,.8)"/>')
        elif style < 0.38:
            rh = bw * rnd.uniform(0.25, 0.5)
            iw = bw * rnd.uniform(0.38, 0.66)
            out.append(
                f'<polygon points="{x:.0f},{top:.0f} {x + bw:.0f},{top:.0f} '
                f'{cxr + iw / 2:.0f},{top - rh:.0f} {cxr - iw / 2:.0f},{top - rh:.0f}" fill="{color}" stroke="rgba(150,182,232,.22)" stroke-width="1"/>'
            )
        elif style < 0.56:
            rh = bw * rnd.uniform(0.3, 0.55)
            out.append(
                f'<polygon points="{cxr:.0f},{top - rh * 1.9:.0f} {cxr + bw * 0.34:.0f},{top - rh * 0.95:.0f} '
                f'{cxr:.0f},{top:.0f} {cxr - bw * 0.34:.0f},{top - rh * 0.95:.0f}" fill="{color}" stroke="rgba(150,182,232,.22)" stroke-width="1"/>'
            )
        elif style < 0.76:
            rh = bw * rnd.uniform(0.2, 0.42)
            iw = bw * rnd.uniform(0.4, 0.72)
            out.append(f'<rect x="{cxr - iw / 2:.0f}" y="{top - rh:.0f}" width="{iw:.0f}" height="{rh:.0f}" fill="{color}" stroke="rgba(150,182,232,.22)" stroke-width="1"/>')
        cols = max(1, int(bw // 17))
        rows = max(1, int(bh // 27))
        for i in range(cols):
            for j in range(rows):
                if rnd.random() < lit:
                    out.append(f'<rect x="{x + 6 + i * 17:.0f}" y="{top + 10 + j * 27:.0f}" width="5" height="8" fill="{win}"/>')
        buildings.append((x, bw, top))
        x += bw + rnd.uniform(3, 16)
    return "".join(out), buildings


def page_scene(w, h, seed=7):
    rnd = random.Random(seed)
    stars = []
    for _ in range(28):
        sx = rnd.uniform(0, w)
        sy = rnd.uniform(0, h * 0.72)
        tw = f' class="tw" style="animation-delay:{rnd.uniform(0, 3.5):.2f}s"' if rnd.random() < 0.25 else ""
        stars.append(f'<circle{tw} cx="{sx:.0f}" cy="{sy:.0f}" r="{rnd.uniform(0.6, 1.7):.1f}" fill="#d7e3ff" opacity="{rnd.uniform(0.12, 0.7):.2f}"/>')
    clouds = []
    for _ in range(4):
        cy = rnd.uniform(h * 0.06, h * 0.34)
        r = rnd.uniform(130, 280)
        x0 = rnd.uniform(-w * 0.3, w)
        dur = rnd.uniform(70, 140)
        clouds.append(
            f'<circle cx="{x0:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="url(#gcloud)" opacity="{rnd.uniform(0.06, 0.12):.2f}">'
            f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{w * 0.5:.0f} 0" '
            f'dur="{dur:.0f}s" repeatCount="indefinite"/></circle>'
        )
    rain = []
    for _ in range(22):
        x = rnd.uniform(-80, w + 140)
        ln = rnd.uniform(14, 30)
        dur = rnd.uniform(0.7, 1.5)
        op = rnd.uniform(0.12, 0.36)
        dx = ln * 0.38
        y0 = rnd.uniform(-h, 0)
        travel = (h - y0) * 0.38
        rain.append(
            f'<line x1="{x:.0f}" y1="{y0:.0f}" x2="{x - dx:.0f}" y2="{y0 + ln:.0f}" stroke="#afc4e4" stroke-width="1" opacity="{op:.2f}">'
            f'<animate attributeName="x1" from="{x:.0f}" to="{x - travel:.0f}" dur="{dur:.2f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="y1" from="{y0:.0f}" to="{h:.0f}" dur="{dur:.2f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="x2" from="{x - dx:.0f}" to="{x - dx - travel:.0f}" dur="{dur:.2f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="y2" from="{y0 + ln:.0f}" to="{h + ln:.0f}" dur="{dur:.2f}s" repeatCount="indefinite"/></line>'
        )
    bats = []
    for i in range(6):
        by = rnd.uniform(h * 0.04, h * 0.42)
        s = rnd.uniform(14, 26)
        drift = rnd.uniform(34, 60)
        phase = rnd.uniform(0, 1)
        flapd = rnd.uniform(0.45, 0.7)
        bats.append(
            f'<g><animateTransform attributeName="transform" type="translate" '
            f'from="{-80} {by:.0f}" to="{w + 80} {by:.0f}" dur="{drift:.0f}s" '
            f'begin="{-drift * phase:.0f}s" repeatCount="indefinite"/>'
            f'<g><animateTransform attributeName="transform" type="translate" '
            f'values="0 0;0 -9;0 0;0 9;0 0" dur="4.2s" repeatCount="indefinite"/>'
            f'<path fill="#111d33" d="{bat_wing(s, 0)}">'
            f'<animate attributeName="d" dur="{flapd:.2f}s" repeatCount="indefinite" '
            f'values="{bat_wing(s, 1)};{bat_wing(s, 0)};{bat_wing(s, -1)};{bat_wing(s, 0)};{bat_wing(s, 1)}"/>'
            f"</path></g></g>"
        )
    far_svg, _ = _skyline(w, h - 170, 450, 820, 34, 92, 0.08, "#0c1424", "rgba(150,178,220,0.34)", rnd)
    near_svg, near_b = _skyline(w, h + 6, 700, 1080, 40, 120, 0.09, "#05080e", "rgba(255,205,80,0.7)", rnd)
    left_side = [b for b in near_b if b[0] + b[1] / 2 < w * 0.45] or near_b
    low = [b for b in left_side if b[2] > 990 and b[0] > 90] or left_side
    host = min(low, key=lambda b: b[0])
    ox, oy = host[0] + host[1] / 2, host[2]
    tx, ty, rx = 646, 190, 138
    ry = rx * 0.5
    dx, dy = tx - ox, ty - oy
    s = (rx * 1.25) / 1002
    lightning = (
        f'<rect width="{w}" height="{h}" fill="#c8dcff" opacity="0">'
        f'<animate attributeName="opacity" values="0;0;0.16;0.02;0.1;0;0" '
        f'keyTimes="0;0.86;0.89;0.91;0.93;0.96;1" dur="13s" repeatCount="indefinite"/></rect>'
    )
    return (
        f'<rect width="{w}" height="{h}" fill="url(#gsky)"/>'
        + "".join(stars) + "".join(clouds) + "".join(bats)
        + far_svg + near_svg
        + f'<rect x="{ox - 6:.0f}" y="{oy:.0f}" width="12" height="16" fill="#04060b"/>'
        + f'<ellipse cx="{ox:.0f}" cy="{oy:.0f}" rx="13" ry="9" fill="#04060b"/>'
        + f'<circle cx="{ox:.0f}" cy="{oy:.0f}" r="24" fill="url(#glens)"/>'
        + (
            f'<g transform="translate({ox:.0f} {oy:.0f})">'
            f'<g><animateTransform attributeName="transform" type="rotate" values="-0.5;0.5;-0.5" '
            f'dur="13s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;1" '
            f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
            f'<path d="M0 0 L{dx - rx:.0f} {dy:.0f} L{dx + rx:.0f} {dy:.0f} Z" fill="url(#gbeam2)"/>'
            f'<g transform="translate({dx:.0f} {dy:.0f})">'
            f'<g><animateTransform attributeName="transform" type="rotate" values="0.5;-0.5;0.5" '
            f'dur="13s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;1" '
            f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
            f'<ellipse cx="0" cy="0" rx="{rx * 2.8:.0f}" ry="{ry * 3.2:.0f}" fill="url(#gsig)">'
            f'<animate attributeName="opacity" values="0.82;1;0.82" dur="3.4s" repeatCount="indefinite"/></ellipse>'
            f'<ellipse cx="0" cy="0" rx="{rx:.0f}" ry="{ry:.0f}" fill="url(#gdisc)"/>'
            f'<path transform="translate({-500.8 * s:.1f} {-152.6 * s:.1f}) scale({s:.5f})" d="{BAT}" fill="#070a12"/>'
            f"</g></g></g></g>"
        )
        + "".join(rain)
        + f'<rect width="{w}" height="{h}" fill="url(#gvig)"/>'
        + f'<rect y="{h * 0.34:.0f}" width="{w}" height="{h * 0.66:.0f}" fill="url(#gbot)"/>'
        + lightning
    )


SCENE_DEFS = f"""
<defs>
  <linearGradient id="gsky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#070c18"/><stop offset="0.35" stop-color="#0a1120"/>
    <stop offset="0.75" stop-color="#080d18"/><stop offset="1" stop-color="#05080f"/>
  </linearGradient>
  <radialGradient id="gsig"><stop offset="0" stop-color="#ffd54a" stop-opacity=".22"/><stop offset="1" stop-color="#ffd54a" stop-opacity="0"/></radialGradient>
  <linearGradient id="gbeam2" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#e8c25c" stop-opacity=".04"/><stop offset="0.55" stop-color="#f7dc85" stop-opacity=".24"/><stop offset="1" stop-color="#fff0b8" stop-opacity=".78"/></linearGradient>
  <radialGradient id="glens"><stop offset="0" stop-color="#fffce0" stop-opacity=".95"/><stop offset="0.45" stop-color="#ffee8c" stop-opacity=".5"/><stop offset="1" stop-color="#ffe65f" stop-opacity="0"/></radialGradient>
  <radialGradient id="gdisc"><stop offset="0" stop-color="#fff0b8"/><stop offset="1" stop-color="#e8c25c"/></radialGradient>
  <radialGradient id="gvig" cx="0.5" cy="0.42" r="0.9">
    <stop offset="0.4" stop-color="#03040a" stop-opacity="0"/><stop offset="1" stop-color="#020308" stop-opacity="0.9"/>
  </radialGradient>
  <linearGradient id="gbot" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#02030a" stop-opacity="0"/><stop offset="0.5" stop-color="#02030a" stop-opacity="0.45"/>
    <stop offset="1" stop-color="#010208" stop-opacity="0.97"/>
  </linearGradient>
</defs>
"""


def shine_def(w, h, begin, dur=14.0):
    D = 1000
    return (
        f'<defs><linearGradient id="shn" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{D}" y2="{D}">'
        f'<stop offset="0" stop-color="{INK}"/><stop offset="0.47" stop-color="{INK}"/>'
        f'<stop offset="0.5" stop-color="{GOLD}"/><stop offset="0.53" stop-color="{INK}"/>'
        f'<stop offset="1" stop-color="{INK}"/>'
        f'<animateTransform attributeName="gradientTransform" type="translate" '
        f'from="{-D} {-D}" to="{D} {D}" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>'
        f'</linearGradient></defs>'
    )


def count_up(num, x, y, attrs, begin, dur=1.3, frames=5, group=False):
    m = re.match(r"([\d.]+)(.*)", num)
    val, suf = float(m.group(1)), m.group(2)
    dec = len(m.group(1).split(".")[1]) if "." in m.group(1) else 0

    def fmt(v):
        return (f"{v:,.{dec}f}" if group else f"{v:.{dec}f}") + suf

    if os.environ.get("STATIC"):
        return f'<text x="{x}" y="{y}" {attrs}>{escape(num)}</text>'
    out = []
    for i in range(frames + 1):
        e = 1 - (1 - i / frames) ** 3
        txt = num if i == frames else fmt(val * e)
        on = begin + dur * i / frames
        off = "" if i == frames else f'<set attributeName="opacity" to="0" begin="{begin + dur * (i + 1) / frames:.3f}s"/>'
        out.append(f'<text x="{x}" y="{y}" {attrs} opacity="0">{escape(txt)}'
                   f'<set attributeName="opacity" to="1" begin="{on:.3f}s"/>{off}</text>')
    return "".join(out)


def hero():
    h = 396
    inner = (
        f'<text class="f" {d(0.05)} x="44" y="86" font-family="{SANS}" font-weight="700" font-size="21" letter-spacing="0.8" fill="{GREEN}">TheWildEye</text>'
        f'<text class="r" {d(0.15)} x="42" y="176" font-family="{SERIF}" font-size="76" letter-spacing="-1.5" fill="url(#shn)">Vyom <tspan fill="{GOLD_BRIGHT}">Nagpal</tspan></text>'
        f'<text class="f" {d(0.4)} x="46" y="230" font-family="{SANS}" font-weight="600" font-size="16" fill="{INK_SOFT}">Security Researcher &#183; <tspan fill="{GOLD_BRIGHT}">Certified Ethical Hacker</tspan></text>'
        f'<text class="f" {d(0.5)} x="46" y="262" font-family="{SANS}" font-weight="600" font-size="16" fill="{INK_SOFT}">National Forensic Sciences University</text>'
        f'<text class="r" {d(0.7)} x="46" y="332" font-family="{SANS}" font-size="19" fill="{INK}">I <tspan fill="{GOLD_BRIGHT}" font-weight="600">break</tspan> web &amp; mobile apps before attackers do,</text>'
        f'<text class="r" {d(0.78)} x="46" y="360" font-family="{SANS}" font-size="19" fill="{INK}">and <tspan fill="{GOLD_BRIGHT}" font-weight="600">build</tspan> offensive security tooling.</text>'
    )
    return h, inner


def kpi():
    h = 120
    tiles = [("VULNERABILITIES", "100+", False), ("APPS SECURED", "20+", False), ("CVE RECORDS", "6\u00d7", False),
             ("RECORDS PROTECTED", "4000", True), ("TARGETS RECONNED", "1000+", True)]
    n = len(tiles)
    gap = 14
    tw = (W - 80 - gap * (n - 1)) / n
    parts = []
    for i, (label, num, group) in enumerate(tiles):
        x = 40 + i * (tw + gap)
        begin = 0.4 + i * 0.14
        parts.append(count_up(num, x, 62, f'font-family="{SERIF}" font-size="44" fill="{GOLD_BRIGHT}"', begin, group=group))
        parts.append(f'<rect class="g" style="animation-delay:{begin:.2f}s" x="{x}" y="76" width="32" height="3" rx="1.5" fill="{GOLD}"/>')
        parts.append(f'<text class="f" style="animation-delay:{begin - 0.25:.2f}s" x="{x}" y="100" font-family="{SANS}" font-weight="700" font-size="11.5" letter-spacing="0.3" fill="{INK}">{label}</text>')
    return h, "".join(parts)


ORBIT = ["Offensive Security", "Web AppSec", "Mobile AppSec", "API Security", "OSINT & Recon",
         "Secure Code Review", "Threat Modelling", "GRC \u00b7 NIST/ISO", "AI Security", "VAPT"]


def hexpts(cx, cy, r):
    return " ".join(
        f"{cx + r * math.cos(math.radians(60 * k - 30)):.1f},{cy + r * math.sin(math.radians(60 * k - 30)):.1f}"
        for k in range(6)
    )


def orbital():
    h = 490
    cx, cy = W / 2, 260
    rx, ry = 300, 172
    n = len(ORBIT)
    body = [
        f'<circle cx="{cx}" cy="{cy}" r="150" fill="url(#coreglow)"/>',
        f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{GOLD}" stroke-opacity=".16" stroke-dasharray="2 9"/>',
    ]
    amp, wave_dur = 11, 5.0
    for i, name in enumerate(ORBIT):
        a = math.radians(-90 + i * 360 / n)
        nx, ny = cx + rx * math.cos(a), cy + ry * math.sin(a)
        ux, uy = nx - cx, ny - cy
        ul = math.hypot(ux, uy) or 1
        ux, uy = ux / ul, uy / ul
        bw, bh = 100.0, 25.0
        tt = min(bw / abs(ux) if ux else 1e9, bh / abs(uy) if uy else 1e9)
        ex, ey = cx + ux * tt, cy + uy * tt
        qx, qy = (nx + ex) / 2 - uy * 30, (ny + ey) / 2 + ux * 30
        pid = f"cn{i}"
        anchor = "start" if ux > 0.3 else ("end" if ux < -0.3 else "middle")
        pdat = f"M{nx:.0f} {ny:.0f} Q{qx:.0f} {qy:.0f} {ex:.0f} {ey:.0f}"
        lx, ly = nx + ux * 30, ny + uy * 20 + 4
        wave = (f'<animateTransform attributeName="transform" type="translate" '
                f'values="0 0;{-ux * amp:.1f} {-uy * amp:.1f};0 0" '
                f'dur="{wave_dur}s" begin="{-wave_dur * i / n:.2f}s" repeatCount="indefinite"/>')
        body.append(
            f'<path id="{pid}" d="{pdat}" fill="none"/>'
            f'<path d="{pdat}" fill="none" stroke="{GOLD}" stroke-opacity=".16" stroke-width="4.5"/>'
            f'<path d="{pdat}" fill="none" stroke="{GOLD_BRIGHT}" stroke-opacity=".6" stroke-width="1"/>'
            f'<g>{wave}'
            f'<polygon points="{hexpts(nx, ny, 12)}" fill="#0d1526" stroke="{GOLD}" stroke-opacity=".85" stroke-width="1.3"/>'
            f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="3" fill="{GOLD_BRIGHT}"/>'
            f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="{anchor}" font-family="{SANS}" '
            f'font-size="13.5" fill="{INK}">{escape(name)}</text></g>'
            f'<circle r="2.8" fill="{GOLD_BRIGHT}">'
            f'<animateMotion dur="{3.4 + i * 0.21:.1f}s" begin="{-i * 0.34:.2f}s" repeatCount="indefinite" rotate="0">'
            f'<mpath xlink:href="#{pid}"/></animateMotion></circle>'
        )
    body.append(f'<text x="{cx}" y="{cy + 12}" text-anchor="middle" font-family="{SERIF}" font-size="38" letter-spacing="0.5" fill="{GOLD_BRIGHT}">TheWildEye</text>')
    head = f'<text class="r" {d(0.2)} x="42" y="40" font-family="{SERIF}" font-size="30" fill="{INK}">Skills, <tspan font-style="italic" fill="{GOLD}">in orbit</tspan></text>'
    return h, f'<defs><radialGradient id="coreglow"><stop offset="0" stop-color="{GOLD}" stop-opacity=".2"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient></defs>' + head + "".join(body)


CVES = [
    ("CVE-2026-119731", "Payment Bypass"),
    ("CVE-2026-119732", "BOLA / IDOR"),
    ("CVE-2026-119733", "Missing Authorization"),
    ("CVE-2026-119734", "BOLA / IDOR"),
    ("CVE-2026-119735", "Stored XSS"),
    ("CVE-2026-119736", "Hard-coded Credentials"),
]


def cvelog():
    h = 268
    rows = []
    for i, (cid, cls) in enumerate(CVES):
        y = 82 + i * 32
        rows.append(
            f'<g class="r" style="animation-delay:{0.5 + i * 0.13:.2f}s">'
            f'<circle cx="52" cy="{y - 5}" r="4.5" fill="{GOLD}"/>'
            f'<text x="74" y="{y}" font-family="{SANS}" font-weight="600" font-size="14.5" fill="{INK}">{escape(cid)}</text>'
            f'<text x="320" y="{y}" font-family="{SANS}" font-weight="600" font-size="15.5" fill="{GOLD_BRIGHT}">{escape(cls)}</text>'
            f'<text x="{W - 44}" y="{y}" text-anchor="end" font-family="{SANS}" font-weight="500" font-size="13.5" fill="{MUTED}">2026</text></g>'
        )
    head = f'<text class="r" {d(0.2)} x="42" y="40" font-family="{SERIF}" font-size="30" fill="url(#shn)">6 published <tspan font-style="italic" fill="{GOLD}">CVEs</tspan></text>'
    return h, head + "".join(rows)


REPOS = [
    ("MrHunter", "MrHunter2", "AI-assisted appsec & compliance agent: SAST, DAST and risk scoring.", "Python", GOLD),
    ("TheWildEyeFW", "TheWildEyeFW", "Unified recon & OSINT framework: DNS, SSL, WHOIS, WAF detection, email harvesting.", "Python", STEEL),
    ("QuantumShield", "QuantumShield", "Post-quantum secure OpenID Connect built on KEMTLS with ML-KEM-768.", "Python", GOLD_BRIGHT),
]


def repos(stars):
    h = 190
    left, gap = 16, 12
    rw = (W - 2 * left - 2 * gap) / 3
    out = []
    for i, (name, slug, desc, lang, color) in enumerate(REPOS):
        x = left + i * (rw + gap)
        meta = f"{lang}  \u00b7  \u2605 {stars[slug]}" if slug in stars else f"{lang}  \u00b7  live"
        words = desc.split()
        lines, line = [], ""
        for wd in words:
            if line and len(line) + 1 + len(wd) > 32:
                lines.append(line)
                line = wd
            else:
                line = f"{line} {wd}".strip()
        if line:
            lines.append(line)
        body_lines = "".join(
            f'<text x="{x + 22:.1f}" y="{y0}" font-family="{SANS}" font-size="14.5" fill="{INK_SOFT}">{escape(l)}</text>'
            for y0, l in zip(range(100, 100 + 24 * len(lines), 24), lines)
        )
        out.append(
            f'<g class="r" style="animation-delay:{2.4 + i * 0.15:.2f}s">'
            f'<rect x="{x:.1f}" y="0" width="{rw:.1f}" height="3" rx="1.5" fill="{color}"/>'
            f'<text x="{x + 22:.1f}" y="38" font-family="{SANS}" font-size="12" letter-spacing="1" fill="{color}">&#9656; REPO</text>'
            f'<text x="{x + 22:.1f}" y="68" font-family="{SANS}" font-weight="600" font-size="19" fill="{GOLD_BRIGHT}">{escape(name)}</text>'
            f'{body_lines}'
            f'<text x="{x + 22:.1f}" y="{h - 12}" font-family="{SANS}" font-size="13" fill="{MUTED}">{escape(meta)}</text></g>'
        )
    return h, "".join(out)


LINKS = [
    ("cve", "CVE", "linktr.ee"),
    ("portfolio", "Portfolio", "vyomnagpal.in"),
    ("linkedin", "LinkedIn", "in/vyomnagpal"),
    ("medium", "Medium", "@TheWildEye"),
    ("email", "Email", "contact@vyomnagpal.in"),
]


def link_cards():
    for slug, label, sub in LINKS:
        body = (
            f'<rect x="0" y="0" width="168" height="54" rx="12" fill="#0f1626" stroke="{GOLD}" stroke-opacity=".45"/>'
            f'<circle cx="14" cy="27" r="3" fill="{GOLD_BRIGHT}"/>'
            f'<text x="94" y="26" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\',Helvetica,Arial,sans-serif" font-weight="600" font-size="15" fill="{GOLD_BRIGHT}">{label}</text>'
            f'<text x="94" y="43" text-anchor="middle" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="10.5" fill="{MUTED}">{sub}</text>'
        )
        write(f"link-{slug}.svg", svg(176, 54, body, [], f"{label} link"))


def repo_stars():
    stars = {}
    try:
        import requests
        for _n, slug, *_ in REPOS:
            r = requests.get(f"https://api.github.com/repos/TheWildEye/{slug}", timeout=10)
            if r.ok:
                stars[slug] = r.json().get("stargazers_count", 0)
    except Exception as e:
        print(f"stars unavailable: {e}")
    return stars


if __name__ == "__main__":
    stars = repo_stars()
    sections = [hero(), kpi(), cvelog(), repos(stars), orbital()]
    TOP, GAP, BOTTOM = 30, 60, 30
    y = TOP
    placed = []
    for h, inner in sections:
        placed.append((y, h, inner))
        y += h + GAP
    total = y - GAP + BOTTOM
    body = SCENE_DEFS + page_scene(W, total) + shine_def(W, total, 0)
    for yy, hh, inner in placed:
        body += (
            f'<rect x="16" y="{yy - 22:.0f}" width="{W - 32}" height="{hh + 44:.0f}" rx="24" '
            f'fill="none" stroke="{GOLD}" stroke-width="1.2" stroke-opacity=".5"/>'
        )
        body += f'<g transform="translate(0 {yy:.0f})">{inner}</g>'
    write("page.svg", svg(W, total, body, ["serif", "sans"],
                          "Vyom Nagpal - security researcher and ethical hacker. 6x CVE, 100+ vulnerabilities disclosed."))
    link_cards()
