"""Original illustrations for the special guide pages (drawn for drlochab.com, no outside images)."""

def pregnancy(alt):
    """A pregnant woman with a bowl of fruit and a glass of water (viewBox 0 0 400 300)."""
    return f'''<svg viewBox="0 0 400 300" role="img" aria-label="{alt}" xmlns="http://www.w3.org/2000/svg">
<circle cx="200" cy="160" r="128" fill="var(--accent-soft)"/>
<path d="M150 272 C150 230 152 170 168 128 C174 112 186 106 200 106 C214 106 224 114 226 128 C228 142 226 150 232 158 C258 168 276 196 272 226 C270 248 262 262 252 272 Z" fill="#0D7466"/>
<ellipse cx="246" cy="204" rx="14" ry="28" fill="#FFFFFF" opacity=".14" transform="rotate(-18 246 204)"/>
<rect x="190" y="88" width="18" height="22" rx="6" fill="#C98B6B"/>
<circle cx="200" cy="70" r="27" fill="#C98B6B"/>
<path d="M174 66 C172 40 210 34 224 54 C214 50 196 52 186 62 C182 70 182 80 186 90 C178 86 174 76 174 66 Z" fill="#2E2420"/>
<circle cx="168" cy="58" r="13" fill="#2E2420"/>
<circle cx="214" cy="70" r="2.6" fill="#2E2420"/>
<path d="M218 82 q-5 4 -10 2" fill="none" stroke="#7A4A36" stroke-width="2.4" stroke-linecap="round"/>
<path d="M188 126 C176 160 186 196 222 214" fill="none" stroke="#B87C5E" stroke-width="15" stroke-linecap="round"/>
<path d="M196 124 C196 156 206 176 236 184" fill="none" stroke="#C98B6B" stroke-width="15" stroke-linecap="round"/>
<g transform="translate(70 214)">
 <ellipse cx="0" cy="36" rx="54" ry="10" fill="#0B2A26" opacity=".08"/>
 <path d="M-50 6 H50 C48 30 26 42 0 42 C-26 42 -48 30 -50 6 Z" fill="#FFFFFF" stroke="#0D7466" stroke-width="3"/>
 <circle cx="-22" cy="0" r="12" fill="#F7D046"/><circle cx="-2" cy="-4" r="13" fill="#5E9B4B"/><circle cx="22" cy="0" r="12" fill="#E0503D"/>
 <path d="M-2 -17 q6 -10 14 -8" fill="none" stroke="#3F8A3A" stroke-width="3" stroke-linecap="round"/>
</g>
<g transform="translate(328 226)"><path d="M-16 -34 H16 L12 30 H-12 Z" fill="#E8F4F1" stroke="#0D7466" stroke-width="3" stroke-linejoin="round"/><path d="M-14 -14 H14 L11 27 H-11 Z" fill="#9BD3EA"/></g>
<path d="M300 92 c14 -18 34 -16 40 -6 c-12 10 -30 14 -40 6 Z" fill="#5E9B4B"/><path d="M300 92 c12 -6 22 -8 34 -8" stroke="#3F8A3A" stroke-width="2" fill="none"/>
<path d="M92 104 c-6 -18 4 -32 16 -32 c4 14 -4 28 -16 32 Z" fill="#9CCB6B"/>
</svg>'''

ART = {"pregnancy-digestive-health": pregnancy}
