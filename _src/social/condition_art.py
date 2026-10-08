"""Custom illustrations (viewBox 640x400) for fatty liver, IBS, IBD and pancreatitis catalogue images."""

LIVER = "M28 114 C32 90 96 80 130 96 C126 104 120 108 114 112 C112 134 92 152 62 154 C40 156 24 138 28 114 Z"
STOMACH = "M124 98 C150 84 192 98 190 128 C188 154 160 168 138 160 C120 154 122 134 138 130 C152 126 152 112 128 112 Z"
PANCREAS = "M96 182 C118 172 160 172 196 166 C203 172 197 181 182 184 C158 188 124 191 104 192 C94 192 90 186 96 182 Z"
DUO = "M126 150 C104 152 80 162 78 180 C76 198 98 204 122 198"
BILE = "M112 118 C110 144 98 164 84 182"
COLON = "M62 286 V216 Q62 204 74 204 H176 Q190 204 190 218 V262 Q190 282 164 286 Q140 290 132 302"
COLON_DISTAL = "M190 230 V262 Q190 282 164 286 Q140 290 132 302"

STYLE = """<style>
.lb{font-family:FT,sans-serif;font-size:22px;font-weight:600;fill:#4A615D}
.lbb{font-family:FT,sans-serif;font-size:24px;font-weight:600;fill:#12302C}
</style>"""

def fatty_liver():
    drops = [(55,108,7),(75,100,6),(96,104,7),(48,128,6),(68,122,8),(90,124,6),(108,114,5),(62,141,6),(82,141,5),(40,114,5)]
    d = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFF6DE" stroke="#C9851F" stroke-width="1.2"/>' for x, y, r in drops)
    return f"""<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg">{STYLE}
<g transform="translate(-30 -80) scale(2)"><path d="{LIVER}" fill="#F1DDB4" stroke="#C9851F" stroke-width="1.5"/>{d}</g>
<g transform="translate(330 -80) scale(2)"><path d="{LIVER}" fill="#CFE6E1" stroke="#0D7466" stroke-width="1.5"/></g>
<path d="M262 160 H352" stroke="#0D7466" stroke-width="5" stroke-linecap="round"/><path d="M340 148 L354 160 L340 172" fill="none" stroke="#0D7466" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<text x="306" y="136" text-anchor="middle" class="lbb">7–10%</text><text x="306" y="198" text-anchor="middle" class="lb">weight loss</text>
<text x="128" y="290" text-anchor="middle" class="lb">Fat in the liver</text><text x="488" y="290" text-anchor="middle" class="lb">Healthier liver</text>
</svg>"""

def ibs():
    gyri = ["M118 92 C128 78 146 80 150 94","M160 84 C172 72 192 76 194 92","M110 120 C122 108 140 112 142 126","M150 116 C162 104 182 108 186 122","M198 108 C210 98 226 104 226 118","M124 146 C138 136 156 140 160 152","M170 140 C184 130 202 134 206 146"]
    g = "".join(f'<path d="{p}" fill="none" stroke="#0D7466" stroke-width="3" stroke-linecap="round"/>' for p in gyri)
    wave = "M244 150 C262 130 276 190 294 170 S326 130 344 160 S376 210 394 190"
    sig = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#C9851F"/>' for x, y in [(262,147),(310,152),(358,178)])
    return f"""<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg">{STYLE}
<ellipse cx="168" cy="118" rx="80" ry="58" fill="#DDEEEA" stroke="#0D7466" stroke-width="3"/>{g}
<path d="M176 174 v24" stroke="#0D7466" stroke-width="10" stroke-linecap="round"/>
<path d="{wave}" fill="none" stroke="#C9851F" stroke-width="4" stroke-dasharray="2 9" stroke-linecap="round"/>{sig}
<g transform="translate(386 168)">
 <rect x="0" y="0" width="200" height="150" rx="40" fill="#CADDD8" stroke="#0D7466" stroke-width="18"/>
 <path d="M40 46 H158 Q172 46 172 60 Q172 74 158 74 H44 Q30 74 30 88 Q30 102 44 102 H156" fill="none" stroke="#0D7466" stroke-width="7" stroke-linecap="round"/>
 <path d="M-26 40 q-12 12 0 24 M-36 28 q-20 24 0 48 M226 40 q12 12 0 24 M236 28 q20 24 0 48" fill="none" stroke="#B0362B" stroke-width="3.5" stroke-linecap="round" opacity=".75"/>
</g>
<text x="168" y="234" text-anchor="middle" class="lb">Brain</text><text x="486" y="360" text-anchor="middle" class="lb">Gut</text>
<text x="270" y="304" text-anchor="middle" class="lbb">Over-sensitive</text><text x="270" y="330" text-anchor="middle" class="lbb">gut-brain link</text>
</svg>"""

def ibd():
    ulcers = [(40,-30,16,10),(-34,-6,14,9),(10,34,18,10),(-20,-48,11,7),(46,18,10,6),(-44,36,10,7)]
    u = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#F7EBDD" stroke="#B0362B" stroke-width="3"/>' for x, y, rx, ry in ulcers)
    spots = "".join(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#B0362B"/>' for x, y in [(0,-20),(26,6),(-12,14),(30,-54),(-56,-20),(60,-6),(-6,60)])
    return f"""<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg">{STYLE}
<defs><clipPath id="mag"><circle cx="0" cy="0" r="96"/></clipPath><radialGradient id="lum" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#D98C7E"/><stop offset="1" stop-color="#E9AFA2"/></radialGradient></defs>
<g transform="translate(-128 -540) scale(2.8)">
 <path d="{COLON}" fill="none" stroke="#97B6AF" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>
 <path d="{COLON}" fill="none" stroke="#CADDD8" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
 <path d="{COLON_DISTAL}" fill="none" stroke="#B0362B" stroke-width="15" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/>
</g>
<path d="M414 140 L430 150" stroke="#4A615D" stroke-width="3" stroke-dasharray="6 6"/>
<g transform="translate(528 165)"><circle r="100" fill="#FFFFFF" stroke="#4A615D" stroke-width="5"/><g clip-path="url(#mag)"><circle r="96" fill="url(#lum)"/>{u}{spots}</g></g>
<text x="528" y="300" text-anchor="middle" class="lb">Inflamed lining</text><text x="528" y="326" text-anchor="middle" class="lb">with ulcers</text>
<text x="212" y="380" text-anchor="middle" class="lb">Large bowel</text>
</svg>"""

def pancreatitis():
    rays = "".join(f'<path d="{d}" stroke="#B0362B" stroke-width="4" stroke-linecap="round" opacity=".8"/>' for d in
                   ["M150 280 l-8 22","M200 286 l-2 24","M250 284 l4 24","M300 276 l8 22","M344 262 l14 16","M210 214 l-4 -18","M280 208 l4 -18"])
    return f"""<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg">{STYLE}
<g transform="translate(-170 -200) scale(2.6)">
 <path d="{STOMACH}" fill="#E6EFEC" stroke="#C3D5D0" stroke-width="1.2"/>
 <path d="{DUO}" fill="none" stroke="#C3D5D0" stroke-width="12" stroke-linecap="round"/>
 <path d="{DUO}" fill="none" stroke="#E6EFEC" stroke-width="9" stroke-linecap="round"/>
 <path d="{PANCREAS}" fill="#B0362B" opacity=".12" stroke="#B0362B" stroke-width="9" stroke-opacity=".12"/>
 <path d="{PANCREAS}" fill="#F3C3B9" stroke="#B0362B" stroke-width="2"/>
 <path d="{BILE}" fill="none" stroke="#C9851F" stroke-width="3" stroke-linecap="round"/>
 <circle cx="90" cy="174" r="5" fill="#6F7F7B"/>
</g>
{rays}
<path d="M368 240 H410" stroke="#4A615D" stroke-width="2.5"/><text x="420" y="248" class="lbb">Inflamed pancreas</text>
<path d="M60 264 L48 300" stroke="#4A615D" stroke-width="2.5"/><text x="14" y="330" class="lb">Gallstone in the duct</text>
<text x="420" y="300" class="lb">Pain often spreads</text><text x="420" y="326" class="lb">to the back</text>
<text x="262" y="52" text-anchor="middle" class="lb">Stomach</text>
</svg>"""
