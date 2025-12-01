<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 360" width="100%" preserveAspectRatio="xMidYMid meet">
  <rect width="100%" height="100%" fill="#000000"/>
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="#00FF3C"/>
      <stop offset="1" stop-color="#33FF88"/>
    </linearGradient>

    <style type="text/css"><![CDATA[
      .name { font: 700 48px 'Courier New', monospace; fill: url(#g); letter-spacing:1px; }
      .role { font: 400 26px 'Courier New', monospace; fill: #00FF3C; opacity:0.0; }
      .shadow { fill: rgba(0,255,60,0.06); }
    ]]></style>
  </defs>

  <!-- Big bold name -->
  <text x="50%" y="90" class="name" text-anchor="middle" dominant-baseline="middle">Vyom Nagpal</text>
  <text x="50%" y="110" class="shadow" text-anchor="middle" dominant-baseline="middle">Vyom Nagpal</text>

  <!-- Matrix bar -->
  <rect x="0" y="128" width="1000" height="6" fill="#001100" opacity="0.7"/>
  <rect x="0" y="128" width="1000" height="6">
    <animate attributeName="fill" values="#001100;#002200;#001100" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- Role 1: Cybersecurity Student (typing effect via per-char opacity) -->
  <g id="r1" transform="translate(0,0)">
    <text x="50%" y="180" text-anchor="middle" class="role" >
      <tspan x="50%" dy="0" font-family="Courier New" font-size="26">
        <tspan opacity="0">C</tspan>
        <tspan opacity="0">y</tspan>
        <tspan opacity="0">b</tspan>
        <tspan opacity="0">e</tspan>
        <tspan opacity="0">r</tspan>
        <tspan opacity="0">s</tspan>
        <tspan opacity="0">e</tspan>
        <tspan opacity="0">c</tspan>
        <tspan opacity="0">u</tspan>
        <tspan opacity="0">r</tspan>
        <tspan opacity="0">i</tspan>
        <tspan opacity="0">t</tspan>
        <tspan opacity="0">y</tspan>
        <tspan opacity="0"> </tspan>
        <tspan opacity="0">S</tspan>
        <tspan opacity="0">t</tspan>
        <tspan opacity="0">u</tspan>
        <tspan opacity="0">d</tspan>
        <tspan opacity="0">e</tspan>
        <tspan opacity="0">n</tspan>
        <tspan opacity="0">t</tspan>
      </tspan>
    </text>

    <!-- staggered typing: each char fades in -->
    <animate xlink:href="#r1 text tspan tspan[1]" attributeName="opacity" from="0" to="1" begin="1s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[2]" attributeName="opacity" from="0" to="1" begin="1.06s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[3]" attributeName="opacity" from="0" to="1" begin="1.12s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[4]" attributeName="opacity" from="0" to="1" begin="1.18s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[5]" attributeName="opacity" from="0" to="1" begin="1.24s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[6]" attributeName="opacity" from="0" to="1" begin="1.30s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[7]" attributeName="opacity" from="0" to="1" begin="1.36s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[8]" attributeName="opacity" from="0" to="1" begin="1.42s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[9]" attributeName="opacity" from="0" to="1" begin="1.48s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[10]" attributeName="opacity" from="0" to="1" begin="1.54s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[11]" attributeName="opacity" from="0" to="1" begin="1.60s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[12]" attributeName="opacity" from="0" to="1" begin="1.66s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[13]" attributeName="opacity" from="0" to="1" begin="1.72s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[14]" attributeName="opacity" from="0" to="1" begin="1.78s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[15]" attributeName="opacity" from="0" to="1" begin="1.84s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[16]" attributeName="opacity" from="0" to="1" begin="1.90s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[17]" attributeName="opacity" from="0" to="1" begin="1.96s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[18]" attributeName="opacity" from="0" to="1" begin="2.02s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[19]" attributeName="opacity" from="0" to="1" begin="2.08s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[20]" attributeName="opacity" from="0" to="1" begin="2.14s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r1 text tspan tspan[21]" attributeName="opacity" from="0" to="1" begin="2.20s" dur="0.06s" fill="freeze"/>

    <!-- visible window for r1 -->
    <animate attributeName="opacity" from="0" to="1" begin="1s" dur="2.4s" fill="freeze" />
    <animate attributeName="opacity" from="1" to="0" begin="5.4s" dur="0.1s" fill="freeze" />
  </g>

  <!-- Role 2: Security Researcher -->
  <g id="r2">
    <text x="50%" y="180" text-anchor="middle" class="role">
      <tspan x="50%" dy="0" font-family="Courier New" font-size="26">
        <tspan opacity="0">S</tspan><tspan opacity="0">e</tspan><tspan opacity="0">c</tspan><tspan opacity="0">u</tspan><tspan opacity="0">r</tspan><tspan opacity="0">i</tspan><tspan opacity="0">t</tspan><tspan opacity="0">y</tspan>
        <tspan opacity="0"> </tspan>
        <tspan opacity="0">R</tspan><tspan opacity="0">e</tspan><tspan opacity="0">s</tspan><tspan opacity="0">e</tspan><tspan opacity="0">a</tspan><tspan opacity="0">r</tspan><tspan opacity="0">c</tspan><tspan opacity="0">h</tspan><tspan opacity="0">e</tspan><tspan opacity="0">r</tspan>
      </tspan>
    </text>

    <!-- typing for r2 with shifted begin -->
    <animate xlink:href="#r2 text tspan tspan[1]" attributeName="opacity" from="0" to="1" begin="5.6s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[2]" attributeName="opacity" from="0" to="1" begin="5.66s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[3]" attributeName="opacity" from="0" to="1" begin="5.72s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[4]" attributeName="opacity" from="0" to="1" begin="5.78s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[5]" attributeName="opacity" from="0" to="1" begin="5.84s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[6]" attributeName="opacity" from="0" to="1" begin="5.90s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[7]" attributeName="opacity" from="0" to="1" begin="5.96s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[8]" attributeName="opacity" from="0" to="1" begin="6.02s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[9]" attributeName="opacity" from="0" to="1" begin="6.08s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[10]" attributeName="opacity" from="0" to="1" begin="6.14s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[11]" attributeName="opacity" from="0" to="1" begin="6.20s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[12]" attributeName="opacity" from="0" to="1" begin="6.26s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[13]" attributeName="opacity" from="0" to="1" begin="6.32s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[14]" attributeName="opacity" from="0" to="1" begin="6.38s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r2 text tspan tspan[15]" attributeName="opacity" from="0" to="1" begin="6.44s" dur="0.06s" fill="freeze"/>
    <animate attributeName="opacity" from="0" to="1" begin="5.6s" dur="2.2s" fill="freeze" />
    <animate attributeName="opacity" from="1" to="0" begin="10.0s" dur="0.1s" fill="freeze" />
  </g>

  <!-- Role 3: CTF Player -->
  <g id="r3">
    <text x="50%" y="180" text-anchor="middle" class="role">
      <tspan x="50%" dy="0" font-family="Courier New" font-size="26">
        <tspan opacity="0">C</tspan><tspan opacity="0">T</tspan><tspan opacity="0">F</tspan><tspan opacity="0"> </tspan><tspan opacity="0">P</tspan><tspan opacity="0">l</tspan><tspan opacity="0">a</tspan><tspan opacity="0">y</tspan><tspan opacity="0">e</tspan><tspan opacity="0">r</tspan>
      </tspan>
    </text>

    <animate xlink:href="#r3 text tspan tspan[1]" attributeName="opacity" from="0" to="1" begin="10.2s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[2]" attributeName="opacity" from="0" to="1" begin="10.26s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[3]" attributeName="opacity" from="0" to="1" begin="10.32s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[4]" attributeName="opacity" from="0" to="1" begin="10.38s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[5]" attributeName="opacity" from="0" to="1" begin="10.44s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[6]" attributeName="opacity" from="0" to="1" begin="10.50s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[7]" attributeName="opacity" from="0" to="1" begin="10.56s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[8]" attributeName="opacity" from="0" to="1" begin="10.62s" dur="0.06s" fill="freeze"/>
    <animate xlink:href="#r3 text tspan tspan[9]" attributeName="opacity" from="0" to="1" begin="10.68s" dur="0.06s" fill="freeze"/>

    <animate attributeName="opacity" from="0" to="1" begin="10.2s" dur="1.0s" fill="freeze" />
    <animate attributeName="opacity" from="1" to="0" begin="13.0s" dur="0.1s" fill="freeze" />
  </g>

  <!-- Glitch effect: small jitter + color flicker on the active group after ~5s -->
  <g id="glitch" opacity="0">
    <animate attributeName="opacity" from="0" to="1" begin="6.8s" dur="0.2s" fill="freeze"/>
    <animate attributeName="opacity" from="1" to="0.5" begin="7s" dur="0.6s" repeatCount="indefinite" values="1;0.6;1" />
  </g>

  <!-- jitter applied to the entire roles area (works intermittently depending on sanitizer) -->
  <animateTransform xlink:href="#r1" attributeName="transform" type="translate" values="0 0;2 -1;0 0;-2 1;0 0" dur="0.18s" begin="6s" repeatCount="indefinite"/>
  <animateTransform xlink:href="#r2" attributeName="transform" type="translate" values="0 0;1 -1;0 0;-1 1;0 0" dur="0.18s" begin="8s" repeatCount="indefinite"/>
  <animateTransform xlink:href="#r3" attributeName="transform" type="translate" values="0 0;1 0;0 0;-1 0;0 0" dur="0.18s" begin="11s" repeatCount="indefinite"/>

  <!-- small green noise lines (matrix vibe) -->
  <g>
    <rect x="120" y="220" width="2" height="40" fill="#00FF3C" opacity="0.06">
      <animate attributeName="opacity" values="0.06;0.4;0.06" dur="3s" begin="2s" repeatCount="indefinite"/>
    </rect>
    <rect x="260" y="220" width="2" height="36" fill="#00FF3C" opacity="0.05">
      <animate attributeName="opacity" values="0.05;0.35;0.05" dur="2.5s" begin="3s" repeatCount="indefinite"/>
    </rect>
    <rect x="640" y="220" width="2" height="46" fill="#00FF3C" opacity="0.04">
      <animate attributeName="opacity" values="0.04;0.3;0.04" dur="2.8s" begin="4s" repeatCount="indefinite"/>
    </rect>
    <rect x="820" y="220" width="2" height="30" fill="#00FF3C" opacity="0.03">
      <animate attributeName="opacity" values="0.03;0.2;0.03" dur="3.2s" begin="1.5s" repeatCount="indefinite"/>
    </rect>
  </g>

</svg>

