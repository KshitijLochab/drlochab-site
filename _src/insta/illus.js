const IL=(()=>{
  const P={
    eso:"M126 -10 V100",
    stomach:"M124 98 C150 84 192 98 190 128 C188 154 160 168 138 160 C120 154 122 134 138 130 C152 126 152 112 128 112 Z",
    liver:"M28 114 C32 90 96 80 130 96 C126 104 120 108 114 112 C112 134 92 152 62 154 C40 156 24 138 28 114 Z",
    gb:"M98 156 m-9 0 a9 14 -20 1 0 18 0 a9 14 -20 1 0 -18 0",
    pancreas:"M96 182 C118 172 160 172 196 166 C203 172 197 181 182 184 C158 188 124 191 104 192 C94 192 90 186 96 182 Z",
    duo:"M126 150 C104 152 80 162 78 180 C76 198 98 204 122 198",
    colon:"M62 286 V216 Q62 204 74 204 H176 Q190 204 190 218 V262 Q190 282 164 286 Q140 290 132 302",
    si:"M84 236 h88 v40 h-88 Z",
    coil:"M100 246 H156 Q164 246 164 254 Q164 261 156 261 H102 Q94 261 94 268",
    bile:"M112 118 C110 144 98 164 84 182"
  };
  const tube=(d,w,on)=>`<path d="${d}" class="il-edge${on?" on":""}" stroke-width="${w+4}"/><path d="${d}" class="il-tube${on?" on":""}" stroke-width="${w}"/>`;
  const fill=(d,on)=>`<path d="${d}" class="il-fill${on?" on":""}"/>`;
  const label=(x,y,t,a)=>`<text x="${x}" y="${y}" class="il-lbl"${a?` text-anchor="${a}"`:""}>${t}</text>`;
  const tip=(x,y)=>`<circle cx="${x}" cy="${y}" r="4.2" class="il-tip"/>`;
  const scope=d=>`<path d="${d}" class="il-scope"/>`;
  const svg=(vb,body,alt)=>`<svg viewBox="${vb}" role="img" aria-label="${alt}">${body}</svg>`;

  // the view through the scope: a circle of lining with a dark lumen
  const scopeView=(inner,alt,id)=>svg("0 0 200 150",`
    <defs><radialGradient id="lum${id}" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#3B1A17"/><stop offset=".35" stop-color="#8E4A40"/><stop offset="1" stop-color="#E9AFA2"/></radialGradient>
    <clipPath id="cv${id}"><circle cx="100" cy="75" r="62"/></clipPath></defs>
    <rect x="18" y="3" width="164" height="144" rx="20" fill="#101A19"/>
    <circle cx="100" cy="75" r="62" fill="url(#lum${id})"/>
    <g clip-path="url(#cv${id})">${inner}</g>
    <circle cx="100" cy="75" r="62" fill="none" stroke="#2A3634" stroke-width="2"/>`,alt);


  /* three-step side views: lining at the bottom, open space above */
  const wall=()=>`<path d="M0 150 H100 V176 H0Z" class="il-fill"/>`;
  const ulcer=()=>`<path d="M0 150 H28 C34 150 36 168 50 168 C64 168 66 150 72 150 H100 V176 H0Z" class="il-fill"/><path d="M30 152 C36 165 64 165 70 152" fill="none" stroke="#E8DCC8" stroke-width="3"/>`;
  const scopeDown=y=>`<path d="M50 -6 V${y}" stroke="var(--ink)" stroke-width="15" stroke-linecap="round"/><circle cx="50" cy="${y}" r="3.5" class="il-tip"/>`;
  const scopeSide=y=>`<path d="M-6 ${y} H40" stroke="var(--ink)" stroke-width="15" stroke-linecap="round"/><circle cx="42" cy="${y}" r="3.5" class="il-tip"/>`;
  const clip=(x,y,r=0)=>`<g transform="translate(${x} ${y}) rotate(${r})"><rect x="-4" y="-16" width="8" height="18" rx="2" fill="#8E9CA1"/><path d="M-3 2 L-6 22 M3 2 L6 22" stroke="#8E9CA1" stroke-width="3.2" stroke-linecap="round"/></g>`;
  const steps=(panels,alt)=>svg("0 0 312 234",panels.map(([art,cap],i)=>`
    <g transform="translate(${i*106} 0)">
      <svg x="0" y="26" width="100" height="150" viewBox="0 34 100 150" overflow="hidden">${art}</svg>
      <circle cx="12" cy="14" r="10" fill="var(--accent)"/><text x="12" y="18" text-anchor="middle" class="il-num">${i+1}</text>
      <text x="50" y="198" text-anchor="middle" class="il-cap">${cap[0]}</text>
      <text x="50" y="212" text-anchor="middle" class="il-cap">${cap[1]}</text>
    </g>${i<2?`<path d="M${i*106+101} 108 l4 5 l-4 5" class="il-arrow"/>`:""}`).join(""),alt);
  return {
    gastro:svg("20 -8 210 182",
      tube(P.eso,14,true)+fill(P.liver)+tube(P.duo,12)+fill(P.stomach,true)+
      scope("M126 -10 V100 C126 112 156 104 170 116 C184 128 180 148 162 154 C150 158 140 156 132 152")+tip(132,152)+
      label(196,104,"Stomach")+label(134,40,"Food pipe")+label(56,128,"Liver","middle"),
      "Upper GI endoscopy: the scope passes through the food pipe into the stomach"),
    colono:svg("20 186 210 140",
      fill(P.si)+`<path d="${P.coil}" class="il-coil"/>`+tube(P.colon,16,true)+
      scope("M131 318 L132 302 Q140 290 164 286 Q190 282 190 262 V218 Q190 204 176 204 H74 Q62 204 62 216 V272")+tip(62,272)+
      `<circle cx="120" cy="204" r="4.5" class="il-polyp"/>`+
      label(120,195,"Polyp","middle")+label(228,318,"Large bowel","end"),
      "Colonoscopy: the scope travels around the large bowel, where polyps can be removed"),
    eus:svg("44 62 204 154",
      tube(P.eso,14)+tube(P.duo,12)+fill(P.pancreas,true)+fill(P.stomach)+
      `<path d="M150 150 L124 192 A48 48 0 0 0 178 192 Z" class="il-fan"/>`+
      scope("M126 60 V100 C126 112 156 104 170 116 C184 128 176 148 150 150")+tip(150,150)+
      label(200,186,"Pancreas")+label(194,104,"Stomach")+label(151,212,"Ultrasound view","middle"),
      "Endoscopic ultrasound: an ultrasound probe on the scope looks through the stomach wall at the pancreas"),
    ercp:svg("0 0 200 150",
      `<path d="M60 -10 C90 -14 196 -12 210 6 C204 24 160 30 126 30 C96 30 74 20 60 -10Z" class="il-fill"/>`+
      `<path d="M58 112 C70 98 120 102 204 94 V118 C150 122 96 130 72 128 C60 126 52 120 58 112Z" class="il-fill"/>`+
      `<path d="M66 108 C110 110 150 104 204 104" fill="none" stroke="var(--organ-line)" stroke-width="2"/>`+
      tube("M106 20 C64 22 36 46 36 82 C36 124 66 140 126 136",22)+
      `<path d="M116 26 C116 56 94 92 66 106" class="il-duct"/>`+
      `<path d="M52 104 H64 C84 96 98 80 104 66" class="il-cath"/>`+
      `<circle cx="110" cy="56" r="5" class="il-stone"/>`+
      scope("M100 -8 C76 6 46 30 42 62 C40 84 44 98 50 104")+tip(50,104)+
      label(176,18,"Liver","middle")+label(124,84,"Bile duct")+label(120,58,"Stone")+label(150,142,"Pancreas","middle")+label(14,146,"Intestine"),
      "ERCP: from the intestine, a thin tube enters the bile duct to remove a stone"),
    evl:steps([
      [wall()+`<path d="M14 150 C32 150 34 112 50 112 C66 112 68 150 86 150Z" fill="#5B6FB5"/><path d="M38 124 C44 116 56 116 62 124" fill="none" stroke="#AEB9E4" stroke-width="3" stroke-linecap="round"/>`,["Swollen vein","in the food pipe"]],
      [wall()+scopeDown(84)+`<path d="M34 150 C40 150 40 104 50 100 C60 104 60 150 66 150Z" fill="#5B6FB5"/><rect x="36" y="84" width="28" height="56" rx="4" fill="var(--surface)" fill-opacity=".35" stroke="var(--ink)" stroke-width="1.5" stroke-dasharray="3 2"/><rect x="38" y="134" width="24" height="7" rx="3.5" class="il-band"/>`,["Vein sucked in,","band put on"]],
      [wall()+`<circle cx="50" cy="132" r="13" fill="#5B6FB5" fill-opacity=".55"/><rect x="40" y="141" width="20" height="7" rx="3.5" class="il-band"/>`,["Vein shrinks and","falls off in days"]]
    ],"Variceal banding in three steps: a swollen vein, a band placed on it, and the vein shrinking away"),
    emr:steps([
      [wall()+`<path d="M24 150 C28 124 72 124 76 150Z" fill="#D9806F"/><path d="M36 134 C44 128 56 128 64 134" fill="none" stroke="#EDB0A4" stroke-width="3" stroke-linecap="round"/>`,["Growth (polyp)","on bowel lining"]],
      [wall()+scopeSide(70)+`<path d="M20 150 C22 116 78 116 80 150Z" fill="#B9D6EE"/><path d="M28 124 C32 102 68 102 72 124 C62 130 38 130 28 124Z" fill="#D9806F"/><path d="M44 70 C40 90 24 116 26 124 C30 134 70 134 74 124 C76 116 58 96 52 78" fill="none" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/>`,["Lifted, then","caught in a loop"]],
      [wall()+`<path d="M34 150 C40 144 60 144 66 150" fill="none" stroke="var(--organ-line)" stroke-width="3"/><path d="M34 84 C38 66 62 66 66 84 C56 90 44 90 34 84Z" fill="#D9806F"/><path d="M50 118 V96 m-6 7 l6 -7 l6 7" class="il-arrow"/>`,["Removed and","sent for testing"]]
    ],"Polyp removal in three steps: a growth on the bowel lining, lifted and caught in a wire loop, then removed"),
    stop:steps([
      [ulcer()+`<circle cx="50" cy="160" r="5" fill="#B3261E"/><path d="M50 150 c-5 -8 -5 -12 0 -18 c5 6 5 10 0 18Z M38 136 c-4 -6 -4 -9 0 -13 c4 4 4 7 0 13Z M62 128 c-4 -6 -4 -9 0 -13 c4 4 4 7 0 13Z" fill="#C0392B"/>`,["Ulcer with a","bleeding vessel"]],
      [ulcer()+scopeDown(96)+`<circle cx="50" cy="160" r="5" fill="#B3261E"/><path d="M50 96 V122" stroke="var(--muted)" stroke-width="2"/>`+clip(50,122),["Tiny clip","seals the vessel"]],
      [ulcer()+clip(44,128,-14)+clip(58,128,14)+`<path d="M70 108 l6 7 l12 -16" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`,["Bleeding stops,","clip falls off later"]]
    ],"Bleeding control in three steps: a bleeding ulcer, a clip placed on the vessel, and the bleeding stopped"),
    peg:svg("0 0 200 150",`
      <rect x="-5" y="22" width="210" height="22" class="il-fill"/>
      <path d="M-5 68 H205 V160 H-5Z" class="il-fill on"/>
      <path d="M100 -6 V96" stroke="var(--accent)" stroke-width="8" stroke-linecap="round"/>
      <rect x="80" y="14" width="40" height="7" rx="3.5" fill="var(--accent)"/>
      <ellipse cx="100" cy="98" rx="22" ry="6" fill="var(--accent)"/>
      ${label(130,37,"Belly wall")}${label(130,90,"Stomach")}${label(92,58,"Feeding tube","end")}`,
      "Feeding tube: a soft tube passes through the belly wall into the stomach, held by a small disc on each side"),
    dil:svg("0 0 200 150",`
      <path d="M8 30 H62 C82 30 86 58 100 58 C114 58 118 30 138 30 H192 V12 H8Z" class="il-fill"/>
      <path d="M8 120 H62 C82 120 86 92 100 92 C114 92 118 120 138 120 H192 V138 H8Z" class="il-fill"/>
      <ellipse cx="100" cy="75" rx="42" ry="20" class="il-balloon"/>
      ${scope("M-4 75 H52")}${tip(52,75)}
      <path d="M52 75 H58" class="il-cath"/>
      ${label(100,148,"Balloon gently widens the narrowing","middle")}`,
      "Dilatation: a balloon passed through the scope widens a narrowed section")
  };
})();