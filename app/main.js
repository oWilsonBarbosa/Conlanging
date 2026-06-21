/* Phonological Inventory Builder — static, no build step.
 * Toggle IPA "blocks" to assemble an inventory; feedback is grounded in a
 * PHOIBLE-derived summary (data/phoible-summary.json). Complexity is gated by
 * level, mirroring the Conlangs University course (Phonology 1..4). Phonology 1
 * (segments) and Phonology 2 (length, nasalization, gemination, diphthongs and
 * syllable structure) are interactive; Phonology 3..4 are scaffolded.
 */
"use strict";

/* ------------------------------------------------------------------ *
 * 1. Chart layouts (curated IPA positions; the "board")
 * ------------------------------------------------------------------ */
const C_PLACES = [
  ["bilabial","Bilabial"],["labiodental","Labiodental"],["dental","Dental"],
  ["alveolar","Alveolar"],["postalveolar","Postalv."],["retroflex","Retroflex"],
  ["palatal","Palatal"],["velar","Velar"],["uvular","Uvular"],
  ["pharyngeal","Pharyngeal"],["glottal","Glottal"],
];
const C_MANNERS = [
  ["plosive","Plosive"],["nasal","Nasal"],["trill","Trill"],["tap","Tap/Flap"],
  ["sibilant","Sibilant fric."],["nonsibilant","Non-sibilant fric."],["latfric","Lateral fric."],
  ["approx","Approximant"],["latapprox","Lateral approx."],
];
// "manner|place": [voiceless, voiced]   (null where IPA has no symbol)
const C_CELLS = {
  "plosive|bilabial":["p","b"], "plosive|alveolar":["t","d"],
  "plosive|retroflex":["ʈ","ɖ"], "plosive|palatal":["c","ɟ"],
  "plosive|velar":["k","ɡ"], "plosive|uvular":["q","ɢ"], "plosive|glottal":["ʔ",null],
  "nasal|bilabial":[null,"m"], "nasal|labiodental":[null,"ɱ"], "nasal|alveolar":[null,"n"],
  "nasal|retroflex":[null,"ɳ"], "nasal|palatal":[null,"ɲ"], "nasal|velar":[null,"ŋ"], "nasal|uvular":[null,"ɴ"],
  "trill|bilabial":[null,"ʙ"], "trill|alveolar":[null,"r"], "trill|uvular":[null,"ʀ"],
  "tap|labiodental":[null,"ⱱ"], "tap|alveolar":[null,"ɾ"], "tap|retroflex":[null,"ɽ"],
  "sibilant|alveolar":["s","z"], "sibilant|postalveolar":["ʃ","ʒ"], "sibilant|retroflex":["ʂ","ʐ"],
  "nonsibilant|bilabial":["ɸ","β"], "nonsibilant|labiodental":["f","v"], "nonsibilant|dental":["θ","ð"],
  "nonsibilant|palatal":["ç","ʝ"], "nonsibilant|velar":["x","ɣ"], "nonsibilant|uvular":["χ","ʁ"],
  "nonsibilant|pharyngeal":["ħ","ʕ"], "nonsibilant|glottal":["h","ɦ"],
  "latfric|alveolar":["ɬ","ɮ"],
  "approx|labiodental":[null,"ʋ"], "approx|alveolar":[null,"ɹ"], "approx|retroflex":[null,"ɻ"],
  "approx|palatal":[null,"j"], "approx|velar":[null,"ɰ"],
  "latapprox|alveolar":[null,"l"], "latapprox|retroflex":[null,"ɭ"],
  "latapprox|palatal":[null,"ʎ"], "latapprox|velar":[null,"ʟ"],
};
// Cells the IPA shades as "articulation judged impossible" (articulatory grounds).
const IMPOSSIBLE = new Set([
  "plosive|pharyngeal",
  "nasal|pharyngeal","nasal|glottal",
  "trill|labiodental","trill|postalveolar","trill|retroflex","trill|palatal","trill|velar","trill|pharyngeal","trill|glottal",
  "tap|bilabial","tap|palatal","tap|velar","tap|pharyngeal","tap|glottal",
  "sibilant|bilabial","sibilant|labiodental","sibilant|dental","sibilant|palatal","sibilant|velar","sibilant|uvular","sibilant|pharyngeal","sibilant|glottal",
  "latfric|bilabial","latfric|labiodental","latfric|pharyngeal","latfric|glottal",
  "latapprox|bilabial","latapprox|labiodental","latapprox|pharyngeal","latapprox|glottal",
]);

// "Derived" cells: possible articulations the IPA writes with a diacritic rather
// than a dedicated letter (dental/labiodental stops, dental nasal, voiceless
// sonorants…). Hidden behind a toggle so the base chart stays clean. Slots fill
// the empty half of a base cell (e.g. voiceless /m̥/ beside /m/).
const DERIVED = {
  "plosive|labiodental":["p̪","b̪"], "plosive|dental":["t̪","d̪"],
  "nasal|bilabial":["m̥",null], "nasal|labiodental":["ɱ̊",null], "nasal|dental":[null,"n̪"],
  "nasal|alveolar":["n̥",null], "nasal|retroflex":["ɳ̊",null], "nasal|palatal":["ɲ̊",null],
  "nasal|velar":["ŋ̊",null], "nasal|uvular":["ɴ̥",null],
  "trill|bilabial":["ʙ̥",null], "trill|alveolar":["r̥",null], "trill|uvular":["ʀ̥",null],
  "tap|labiodental":["ⱱ̥",null], "tap|alveolar":["ɾ̥",null], "tap|retroflex":["ɽ̊",null],
  "approx|bilabial":[null,"β̞"], "approx|dental":[null,"ð̞"], "approx|alveolar":["ɹ̥",null],
  "approx|palatal":["j̊",null],
  "latapprox|dental":[null,"l̪"], "latapprox|alveolar":["l̥",null], "latapprox|retroflex":["ɭ̊",null],
  "latapprox|palatal":["ʎ̊",null], "latapprox|velar":["ʟ̥",null],
};
// Merge base + derived into one lookup (base symbol wins each slot).
const MCELLS = {};
{
  const keys = new Set([...Object.keys(C_CELLS), ...Object.keys(DERIVED)]);
  keys.forEach(k=>{ const b=C_CELLS[k]||[null,null], d=DERIVED[k]||[null,null];
    MCELLS[k] = [b[0]||d[0]||null, b[1]||d[1]||null]; });
}
const isDerived = (k,i) => !(C_CELLS[k] && C_CELLS[k][i]) && !!(DERIVED[k] && DERIVED[k][i]);
// Consonants beyond the pulmonic grid, grouped as on the official IPA chart.
// Exact PHOIBLE keys; /ʔ/ stays in the grid (plosive×glottal), not here.
const C_NONPULM = [   // non-pulmonic: made with a non-lung airstream
  ["Clicks", ["ʘ","ǀ","ǃ","ǂ","ǁ"]],
  ["Voiced implosives", ["ɓ","ɗ","ʄ","ɠ","ʛ"]],
  ["Ejectives", ["pʼ","tʼ","kʼ","qʼ","sʼ"]],
];
const C_OTHER = [     // IPA "Other symbols": co-articulated, affricates, misc.
  ["Co-articulated", ["ʍ","w","ɥ","kp","ɡb"]],
  ["Affricates", ["t̠ʃ","d̠ʒ","ts","dz"]],
  ["Other", ["ɕ","ʑ","ʜ","ʢ","ʡ","ɺ","ɧ"]],
];

// Tabs for the board; each consonant tab counts toward its own group.
const TABS = [
  {id:"pulmonic", label:"Pulmonic"},
  {id:"nonpulm",  label:"Non-pulmonic"},
  {id:"other",    label:"Other / co-art."},
  {id:"vowels",   label:"Vowels"},
];

const V_HEIGHTS = [
  ["close","Close"],["nearclose","Near-close"],["closemid","Close-mid"],
  ["mid","Mid"],["openmid","Open-mid"],["nearopen","Near-open"],["open","Open"],
];
const V_BACK = [["front","Front"],["central","Central"],["back","Back"]];
// "height|back": [unrounded, rounded]
const V_CELLS = {
  "close|front":["i","y"], "close|central":["ɨ","ʉ"], "close|back":["ɯ","u"],
  "nearclose|front":["ɪ","ʏ"], "nearclose|back":[null,"ʊ"],
  "closemid|front":["e","ø"], "closemid|central":["ɘ","ɵ"], "closemid|back":["ɤ","o"],
  "mid|central":["ə",null],
  "openmid|front":["ɛ","œ"], "openmid|central":["ɜ","ɞ"], "openmid|back":["ʌ","ɔ"],
  "nearopen|front":["æ",null], "nearopen|central":["ɐ",null],
  "open|front":["a","ɶ"], "open|back":["ɑ","ɒ"],
};

/* Catalog: every selectable symbol -> metadata (built during render). */
const CATALOG = new Map();
function register(sym, meta){ if(sym) CATALOG.set(sym, meta); }

/* ------------------------------------------------------------------ *
 * 2. Levels (framework; v1 activates level 1, previews 2..4)
 * ------------------------------------------------------------------ */
const LEVELS = [
  {n:1, id:"seg", name:"Segments", status:"active",
   desc:"Pick the contrastive consonants and base vowel qualities. Decide place, manner and voicing — the bones of the inventory.",
   adds:["Pulmonic consonant grid","Vowel quadrilateral","Common affricates & labial-velars"]},
  {n:2, id:"phon2", name:"Length & syllables", status:"active",
   desc:"Add suprasegmental contrasts to your segments — length, nasalization, gemination, diphthongs — then set how syllables are built (onset and coda complexity).",
   adds:["Length (Vː) & gemination","Nasal vowels (Ṽ) & diphthongs","Syllable templates (onset/nucleus/coda)","Cluster & coda constraints"]},
  {n:3, id:"phon3", name:"Prosody", status:"soon",
   desc:"Phonology 3: suprasegmentals.",
   adds:["Stress systems","Mora weight","Vowel harmony"]},
  {n:4, id:"phon4", name:"Tone & pitch", status:"soon",
   desc:"Phonology 4: tonal & pitch-accent systems.",
   adds:["Register & contour tones","Pitch accent","Tone sandhi"]},
];

/* ------------------------------------------------------------------ *
 * 3. Presets
 * ------------------------------------------------------------------ */
const PRESETS = [
  {name:"Cross-linguistic core", note:"the most common small system",
   set:["m","n","p","t","k","b","d","ɡ","s","l","j","w","i","u","a"]},
  {name:"Five-vowel workhorse", note:"/p t k …/ + i e a o u",
   set:["p","t","k","b","d","ɡ","m","n","ŋ","s","l","r","j","w","i","e","a","o","u"]},
  {name:"Polynesian (Hawaiian)", note:"tiny CV system · /ʔ h/ · 5 vowels",
   set:["p","k","ʔ","h","m","n","l","w","i","e","a","o","u"]},
  {name:"Australian (no fricatives)", note:"6 stop series + matching nasals/laterals · /i a u/",
   set:["p","t̪","t","ʈ","c","k","m","n̪","n","ɳ","ɲ","ŋ","l̪","l","ɭ","ʎ","r","ɻ","w","j","i","a","u"]},
  {name:"Arabic / Semitic", note:"back-heavy: uvular /q/ + pharyngeals · fricative-rich",
   set:["b","t","d","k","q","ʔ","f","θ","ð","s","z","ʃ","x","ɣ","ħ","ʕ","h","m","n","l","r","j","w","i","a","u"]},
  {name:"Ejective (Caucasian/Andean)", note:"ejective series /pʼ tʼ kʼ qʼ/ + /q/",
   set:["p","t","k","q","pʼ","tʼ","kʼ","qʼ","ts","s","ʃ","x","m","n","l","r","j","w","i","a","u"]},
  {name:"West African (Gbe)", note:"labial-velars kp ɡb · implosives ɓ ɗ · 7 vowels",
   set:["b","t","d","k","ɡ","kp","ɡb","ɓ","ɗ","f","s","ʃ","h","m","n","l","r","j","w","i","e","ɛ","a","ɔ","o","u"]},
  {name:"Vowel-rich (Turkic)", note:"front-rounded y ø · 8-vowel harmony",
   set:["p","b","t","d","c","ɟ","k","ɡ","f","v","s","z","ʃ","ʒ","ɣ","h","m","n","l","r","j","i","y","ɯ","u","e","ø","o","a"]},
  {name:"Alantian (this repo)", note:"16 C, /a i u/ core",
   set:["p","b","t","d","k","ɡ","f","s","x","h","m","n","l","r","w","j","a","i","u"]},
];

/* ------------------------------------------------------------------ *
 * 4. State + persistence
 * ------------------------------------------------------------------ */
const LS_KEY = "pib.v1";
let DATA = null;                 // PHOIBLE summary
let WALS = null;                 // WALS phonology summary (typological cross-check)
const state = {
  level:1, tab:"pulmonic", derived:false, selected:new Set(),
  // Phonology 2 — suprasegmental contrasts + syllable phonotactics
  supra:{ length:false, nasal:false, gemination:false, diphthong:false },
  syll:{ onset:1, coda:0 },  // max consonants in onset / coda (0..3)
};

function save(){ localStorage.setItem(LS_KEY, JSON.stringify({
  level:state.level, tab:state.tab, derived:state.derived, selected:[...state.selected],
  supra:state.supra, syll:state.syll })); }
function load(){
  try{ const o = JSON.parse(localStorage.getItem(LS_KEY)||"{}");
    if(Array.isArray(o.selected)) state.selected = new Set(o.selected);
    if(o.level) state.level = o.level;
    if(o.tab) state.tab = o.tab;
    if(typeof o.derived==="boolean") state.derived = o.derived;
    if(o.supra) Object.assign(state.supra, o.supra);
    if(o.syll)  Object.assign(state.syll,  o.syll);
  }catch(e){}
}

/* frequency proportion of a symbol from the summary (0 if unattested) */
function freq(sym){
  if(!DATA) return 0;
  const n = DATA.consonants[sym] ?? DATA.vowels[sym] ?? DATA.tones[sym];
  return n ? n / DATA.meta.n_inventories : 0;
}
function classOf(sym){ return CATALOG.get(sym)?.cls
  || (DATA && DATA.vowels[sym] ? "vowel" : "consonant"); }

/* Display info: the direct PHOIBLE proportion, or an aggregate fallback for
   symbols stored only inside composites (e.g. clicks → /kǀ/), flagged approx. */
function segInfo(sym){
  if(!DATA) return {p:0, approx:false, note:null};
  const direct = DATA.consonants[sym] ?? DATA.vowels[sym] ?? DATA.tones[sym];
  if(direct!=null) return {p: direct/DATA.meta.n_inventories, approx:false, note:null};
  const agg = DATA.aggregates && DATA.aggregates[sym];
  if(agg) return {p: agg.n/DATA.meta.n_inventories, approx:true, note:agg.note};
  return {p:0, approx:false, note:null};
}
function fmtPct(p){ const x=p*100;
  if(x>=1) return Math.round(x)+"%";
  if(x>=0.1) return x.toFixed(1)+"%";
  if(x>0) return "<0.1%";
  return null;
}

/* ------------------------------------------------------------------ *
 * 4b. Phonology 2 — suprasegmental contrasts + syllable phonotactics
 * ------------------------------------------------------------------ */
const NFD = s => s.normalize("NFD");
const LONG = "ː", TILDE = "̃", NONSYL = "̯"; // ː · combining tilde · inverted breve below

function selConsonants(){ return [...state.selected].filter(s=>classOf(s)==="consonant"); }
function selVowels(){ return [...state.selected].filter(s=>classOf(s)==="vowel"); }

/* Suprasegmental variants are built from the *base* inventory and normalised to
   NFD so the keys line up with the PHOIBLE summary (e.g. /aː/, /ĩ/, /mː/). */
function longVowels(){ return selVowels().map(v=>NFD(v+LONG)); }
function nasalVowels(){ return selVowels().map(v=>NFD(v+TILDE)); }
/* Geminate only consonants that realistically take a length contrast: exclude
   clicks, implosives, ejectives and the labial-velar stops /kp ɡb/, which
   effectively never geminate (and are unattested as geminates in PHOIBLE). */
const NON_GEMINABLE = new Set([...C_NONPULM.flatMap(([,s])=>s), "kp", "ɡb"]);
function geminates(){ return selConsonants().filter(c=>!NON_GEMINABLE.has(c)).map(c=>NFD(c+LONG)); }
/* Closing diphthongs (the commonest type): a non-high nucleus + a high offglide
   /i̯ u̯/, only when that high vowel is itself in the inventory. */
function diphthongs(){
  const vs=new Set(selVowels()), out=[];
  const glides=[["i",NFD("i"+NONSYL)],["u",NFD("u"+NONSYL)]];
  ["a","e","o","ɛ","ɔ","ə"].forEach(v=>{ if(!vs.has(v)) return;
    glides.forEach(([h,gl])=>{ if(vs.has(h)) out.push(NFD(v+gl)); }); });
  return out;
}
/* Map a suprasegmental key to the segments it contributes (for preview/export). */
const SUPRA = [
  {key:"length",    label:"Vowel length",       sym:"Vː", gen:longVowels,
   blurb:"a length contrast on every vowel quality (e.g. /a/ vs /aː/)"},
  {key:"nasal",     label:"Nasal vowels",        sym:"Ṽ",  gen:nasalVowels,
   blurb:"a phonemic oral/nasal contrast on the vowels"},
  {key:"gemination",label:"Geminate consonants", sym:"Cː", gen:geminates,
   blurb:"a short/long (singleton/geminate) contrast on the consonants"},
  {key:"diphthong", label:"Diphthongs",          sym:"ai̯", gen:diphthongs,
   blurb:"closing diphthongs as complex nuclei (e.g. /ai̯ au̯/)"},
];

/* Syllable template + WALS-12A class from onset/coda maximum consonant counts. */
function syllableTemplate(){
  const opt=n=>"(C)".repeat(n);
  const nuc=state.supra.diphthong ? "V(V)" : "V";
  return `${opt(state.syll.onset)}${nuc}${opt(state.syll.coda)}`;
}
function syllableClass(){
  const on=state.syll.onset, co=state.syll.coda;
  if(on<=1 && co===0) return "Simple";
  if(on<=2 && co<=1)  return "Moderately complex";
  return "Complex";
}

/* ------------------------------------------------------------------ *
 * 5. Rendering
 * ------------------------------------------------------------------ */
const $ = s => document.querySelector(s);

function pct(x){ return Math.round(x*100); }

function makeBlock(sym, cls, place, manner, derived){
  if(!sym){ const d=document.createElement("div"); d.className="block empty"; return d; }
  register(sym, {cls, place, manner, label:sym});
  const info = segInfo(sym);
  let lab = info.p ? fmtPct(info.p) : "rare";
  if(info.approx && lab && lab[0] !== "<") lab = "~"+lab;
  const b = document.createElement("button");
  b.className = "block" + (state.selected.has(sym) ? " on":"") + (derived ? " derived":"");
  b.style.setProperty("--f", Math.min(1, info.p/0.9).toFixed(3));
  b.dataset.sym = sym;
  b.innerHTML = `<b class="ipa">${sym}</b><span class="fr">${lab}</span>`;
  const base = info.p
    ? `/${sym}/ — ${info.approx?"≈":"in "}${fmtPct(info.p)} of PHOIBLE inventories${info.note?` (${info.note})`:""}`
    : `/${sym}/ — <0.1% of PHOIBLE inventories (rare/unattested)`;
  b.title = derived ? base + " · derived (written with a diacritic)" : base;
  b.addEventListener("click", ()=>toggle(sym));
  return b;
}

function renderConsonants(){
  const table = $("#consonantChart"); table.innerHTML="";
  // header
  const thead = table.createTHead().insertRow();
  thead.insertCell().outerHTML = "<th></th>";
  C_PLACES.forEach(([id,label])=> thead.insertCell().outerHTML = `<th>${label}</th>`);
  const tb = table.createTBody();
  C_MANNERS.forEach(([mid,mlabel])=>{
    const tr = tb.insertRow();
    tr.insertCell().outerHTML = `<th class="row">${mlabel}</th>`;
    C_PLACES.forEach(([pid])=>{
      const td = tr.insertCell();
      const key = `${mid}|${pid}`;
      const pair = MCELLS[key];
      if(pair && (pair[0] || pair[1])){
        const wrap = document.createElement("div"); wrap.className="cellpair";
        wrap.appendChild(makeBlock(pair[0],"consonant",pid,mid, isDerived(key,0)));
        wrap.appendChild(makeBlock(pair[1],"consonant",pid,mid, isDerived(key,1)));
        td.appendChild(wrap);
      } else if(IMPOSSIBLE.has(key)){
        td.className = "imp"; td.title = "Articulation judged impossible";
      }
    });
  });
}

/* Render grouped block rows (non-pulmonic, other/co-articulated). */
function renderGroups(containerId, groups){
  const c = $("#"+containerId); c.innerHTML="";
  groups.forEach(([label, syms])=>{
    const g = document.createElement("div"); g.className="cgroup";
    const h = document.createElement("div"); h.className="cgroup-h"; h.textContent=label;
    const row = document.createElement("div"); row.className="cgroup-row";
    syms.forEach(s=> row.appendChild(makeBlock(s,"consonant",label,label)));
    g.appendChild(h); g.appendChild(row); c.appendChild(g);
  });
}

/* Board tabs (Pulmonic / Non-pulmonic / Other / Vowels). */
function tabSyms(id){
  if(id==="pulmonic") return Object.values(MCELLS).flat().filter(Boolean);
  if(id==="nonpulm")  return C_NONPULM.flatMap(([,s])=>s);
  if(id==="other")    return C_OTHER.flatMap(([,s])=>s);
  if(id==="vowels")   return Object.values(V_CELLS).flat().filter(Boolean);
  return [];
}
function renderTabs(){
  const bar = $("#chartTabs"); bar.innerHTML="";
  TABS.forEach(t=>{
    const b = document.createElement("button");
    b.className = "tab"; b.dataset.tab = t.id; b.setAttribute("role","tab");
    b.innerHTML = `${t.label} <span class="cnt"></span>`;
    b.addEventListener("click", ()=>setTab(t.id));
    bar.appendChild(b);
  });
  setTab(state.tab || "pulmonic");
}
function setTab(id){
  state.tab = id; save();
  document.querySelectorAll("#chartTabs .tab").forEach(b=>b.classList.toggle("active", b.dataset.tab===id));
  document.querySelectorAll(".tabpanel").forEach(p=>p.classList.toggle("active", p.id===`tab-${id}`));
  updateTabCounts();
}
function applyDerived(){
  const t=$("#consonantChart"); if(t) t.classList.toggle("show-derived", !!state.derived);
}
function updateTabCounts(){
  TABS.forEach(t=>{
    const n = tabSyms(t.id).filter(s=>state.selected.has(s)).length;
    const el = document.querySelector(`#chartTabs .tab[data-tab="${t.id}"] .cnt`);
    if(el){ el.textContent = n; el.style.visibility = n ? "visible" : "hidden"; }
  });
}

function renderVowels(){
  const table = $("#vowelChart"); table.innerHTML="";
  const thead = table.createTHead().insertRow();
  thead.insertCell().outerHTML="<th></th>";
  V_BACK.forEach(([,label])=> thead.insertCell().outerHTML=`<th>${label}</th>`);
  const tb = table.createTBody();
  V_HEIGHTS.forEach(([hid,hlabel])=>{
    const tr = tb.insertRow();
    tr.insertCell().outerHTML=`<th class="row">${hlabel}</th>`;
    V_BACK.forEach(([bid])=>{
      const td=tr.insertCell();
      const pair=V_CELLS[`${hid}|${bid}`];
      if(!pair) return;
      const wrap=document.createElement("div"); wrap.className="cellpair";
      wrap.appendChild(makeBlock(pair[0],"vowel",bid,hid));
      wrap.appendChild(makeBlock(pair[1],"vowel",bid,hid));
      td.appendChild(wrap);
    });
  });
}

function renderLevels(){
  const nav=$("#levelNav"); nav.innerHTML="";
  LEVELS.forEach(L=>{
    const b=document.createElement("button");
    b.className="lvl"+(L.n===state.level?" active":"")+(L.status==="soon"?" locked":"");
    b.innerHTML=`<span class="n">${L.n}</span> ${L.name}`+(L.status==="soon"?` <span class="lock">soon</span>`:"");
    b.addEventListener("click",()=>{
      if(L.status==="soon"){ toast(`Level ${L.n} (“${L.name}”) is on the roadmap — see the cards below.`); $("#lockedLevels").scrollIntoView({behavior:"smooth"}); return; }
      state.level=L.n; save(); renderLevels(); renderHeader(); renderLevel2();
    });
    nav.appendChild(b);
  });
  // locked previews
  const wrap=$("#lockedLevels"); wrap.innerHTML="";
  LEVELS.filter(L=>L.status==="soon").forEach(L=>{
    const c=document.createElement("div"); c.className="lvlcard";
    c.innerHTML=`<span class="pill">Level ${L.n} · Phonology ${L.n}</span>
      <h4>${L.name}</h4><div class="muted small">${L.desc}</div>
      <ul>${L.adds.map(a=>`<li>${a}</li>`).join("")}</ul>`;
    wrap.appendChild(c);
  });
}

function renderHeader(){
  const L=LEVELS.find(x=>x.n===state.level);
  $("#levelTitle").textContent=`Phonology ${L.n} — ${L.name}`;
  $("#levelDesc").textContent=L.desc;
}

/* ---- Phonology 2 panel: suprasegmentals + syllable structure ---- */
function dchip(sym){
  const i=segInfo(sym); let l=i.p?fmtPct(i.p):"rare"; if(i.approx&&l&&l[0]!=="<")l="~"+l;
  const t=i.p?`/${sym}/ — in ${fmtPct(i.p)} of PHOIBLE inventories`:`/${sym}/ — rare/unattested`;
  return `<span class="dchip" title="${t}"><b>${sym}</b><small>${l}</small></span>`;
}
function renderSupra(){
  const host=$("#supraList"); if(!host) return; host.innerHTML="";
  SUPRA.forEach(s=>{
    const on=!!state.supra[s.key], segs=s.gen();
    const need=s.key==="gemination"?"consonants":"vowels";
    const preview = !segs.length
      ? `<span class="muted small">pick ${need} above to derive ${s.sym}</span>`
      : segs.slice(0,8).map(dchip).join("")+(segs.length>8?`<span class="muted small more">+${segs.length-8}</span>`:"");
    const row=document.createElement("div"); row.className="supra-item"+(on?" on":"");
    row.innerHTML=`<label class="supra-top">
        <input type="checkbox" ${on?"checked":""} data-supra="${s.key}">
        <span class="supra-name"><b>${s.label}</b> <span class="supra-sym">${s.sym}</span><br><span class="muted small">${s.blurb}</span></span>
        <span class="supra-n">${on&&segs.length?`+${segs.length}`:""}</span>
      </label><div class="supra-prev">${preview}</div>`;
    row.querySelector("input").addEventListener("change",e=>{
      state.supra[s.key]=e.target.checked; save();
      renderSupra(); renderSyllable(); renderTray(); renderFeedback();
    });
    host.appendChild(row);
  });
}
function segButtons(hostSel, val, onPick){
  const host=$(hostSel); if(!host) return; host.innerHTML="";
  [0,1,2,3].forEach(n=>{
    const b=document.createElement("button"); b.type="button";
    b.className="segb"+(n===val?" active":""); b.textContent=String(n);
    b.setAttribute("aria-pressed", n===val?"true":"false");
    b.addEventListener("click",()=>onPick(n));
    host.appendChild(b);
  });
}
function syllableExample(){
  const cons=selConsonants(), vows=selVowels();
  if(!cons.length||!vows.length) return "Add consonants and vowels above to see a worked example.";
  const byFreq=a=>[...a].sort((x,y)=>segInfo(y).p-segInfo(x).p);
  const C=byFreq(cons), V=byFreq(vows);
  const liquids=["l","r","ɾ","ɹ","w","j","ʎ","ɭ"];
  const onset=n=>{ if(!n) return "";
    const obs=C.filter(c=>!liquids.includes(c)), liq=C.filter(c=>liquids.includes(c)), seq=[];
    for(let i=0;i<n;i++){ if(i===n-1 && n>1 && liq.length) seq.push(liq[0]); else seq.push(obs[i]||C[i%C.length]); }
    return seq.join("");
  };
  const coda=n=> n? C.slice(0,n).reverse().join("") : "";
  const nuc = state.supra.diphthong && diphthongs().length ? diphthongs()[0] : V[0];
  const syl = onset(state.syll.onset)+nuc+coda(state.syll.coda);
  return `Worked example: <code>/${syl}/</code> <span class="muted">(${syllableTemplate()})</span>`;
}
function renderSyllable(){
  segButtons("#onsetSeg", state.syll.onset, n=>{ state.syll.onset=n; save(); renderSyllable(); renderFeedback(); });
  segButtons("#codaSeg",  state.syll.coda,  n=>{ state.syll.coda=n;  save(); renderSyllable(); renderFeedback(); });
  const tpl=$("#syllTemplate"); if(tpl) tpl.textContent=syllableTemplate();
  const cls=syllableClass(), cl=$("#syllClass");
  if(cl){ cl.textContent=cls; cl.dataset.cls=cls.split(" ")[0].toLowerCase(); }
  const ex=$("#syllExamples"); if(ex) ex.innerHTML=syllableExample();
}
function renderLevel2(){
  const panel=$("#level2Panel"); if(!panel) return;
  const show = state.level>=2;
  panel.hidden = !show;
  if(show){ renderSupra(); renderSyllable(); }
}

function renderTray(){
  const tray=$("#tray");
  const sel=[...state.selected];
  if(!sel.length){ tray.innerHTML='<p class="muted empty">No sounds yet — click blocks on the chart to add them.</p>'; }
  else{
    tray.innerHTML="";
    // order: consonants by commonness then vowels by commonness
    const order=(a,b)=>segInfo(b).p-segInfo(a).p;
    const cons=sel.filter(s=>classOf(s)==="consonant").sort(order);
    const vows=sel.filter(s=>classOf(s)==="vowel").sort(order);
    [...cons,...vows].forEach(sym=>{
      const c=document.createElement("button"); c.className="chip"; c.title="Click to remove";
      const ti=segInfo(sym); let tl=ti.p?fmtPct(ti.p):"·"; if(ti.approx&&tl&&tl[0]!=="<")tl="~"+tl;
      c.innerHTML=`<span class="ipa">${sym}</span><small>${tl}</small>`;
      c.addEventListener("click",()=>toggle(sym));
      tray.appendChild(c);
    });
  }
  const cons=sel.filter(s=>classOf(s)==="consonant");
  const vows=sel.filter(s=>classOf(s)==="vowel");
  $("#ipaLine").textContent = sel.length? "/ "+[...cons,...vows].join(" ")+" /" : "";
}

/* ------------------------------------------------------------------ *
 * 6. Naturalness engine
 * ------------------------------------------------------------------ */
const NASALS=["m","n","ŋ","ɲ","ɳ","ɱ","ɴ","n̪"]; // include the dental nasal
function has(s){ return state.selected.has(s); }
const any = arr => arr.some(has);

/* Structural groups used to map an inventory onto WALS categories. */
const W = {
  voicedPlos:["b","d","ɖ","ɟ","ɡ","ɢ"], voicelessPlos:["p","t","ʈ","c","k","q","ʔ"],
  voicedFric:["β","v","ð","z","ʒ","ʐ","ʝ","ɣ","ʁ","ʕ","ɦ","ɮ"],
  voicelessFric:["ɸ","f","θ","s","ʃ","ʂ","ç","x","χ","ħ","h","ɬ"],
  uvularStop:["q","ɢ"], uvularCont:["χ","ʁ","ɴ","ʀ"], frHigh:["y","ʏ"], frMid:["ø","œ"],
  nasals:["m","ɱ","n","n̪","ɳ","ɲ","ŋ","ɴ"], bilabials:["p","b","m","ɸ","β","ʙ"],
  labialVelars:["kp","ɡb"], pharyngeals:["ħ","ʕ"], thSounds:["θ","ð"], clicks:["ʘ","ǀ","ǃ","ǂ","ǁ"],
};

/* Cross the inventory against WALS typological classes -> feedback lines. */
function walsItems(cons, vows){
  const items=[]; let pen=0; const F=WALS.features;
  const P=v=>Math.round(v*100)+"%";
  const sh=(pid,cat)=>{ const f=F[pid]; if(!f) return null; return f.n? (f.dist[cat]||0)/f.n : null; };
  const haveShare=pid=>{ const f=F[pid]; if(!f) return null; return (f.n-(f.dist["None"]||0))/f.n; };
  const binName=(pid,x)=>{ const b=F[pid]&&F[pid].bins; if(!b) return null;
    for(const [mx,nm] of b){ if(mx==null||x<=mx) return nm; } return b[b.length-1][1]; };
  const push=(lvl,html,w=0)=>{ items.push({level:lvl,html}); pen+=w; };

  if(cons.length){ const nm=binName("1A",cons.length), s=sh("1A",nm);
    push(nm==="Average"?"good":"info",
      `<b>${cons.length} consonants</b> → a <b>${nm.toLowerCase()}</b> inventory${s!=null?` (${P(s)} of the WALS sample)`:""}.`); }
  if(vows.length){ const nm=binName("2A",vows.length), s=sh("2A",nm);
    push(nm.startsWith("Average")?"good":"info",
      `<b>${vows.length} vowel qualities</b> → a <b>${nm.replace(/\s*\(.*\)/,"").toLowerCase()}</b> vowel system${s!=null?` (${P(s)} of WALS)`:""}.`); }

  if(any(W.voicedPlos)||any(W.voicelessPlos)||any(W.voicedFric)||any(W.voicelessFric)){
    const cp=any(W.voicedPlos)&&any(W.voicelessPlos), cf=any(W.voicedFric)&&any(W.voicelessFric);
    const cat=cp&&cf?"In both plosives and fricatives":cp?"In plosives alone":cf?"In fricatives alone":"No voicing contrast";
    const s=sh("4A",cat); push("info",`Voicing contrast: <b>${cat.toLowerCase()}</b>${s!=null?` — ${P(s)} of WALS languages`:""}.`); }

  if(any(W.uvularStop)||any(W.uvularCont)){ const hv=haveShare("6A");
    push("info",`Uvular consonants present — uncommon: only ${P(hv)} of WALS languages have any uvular.`); }
  if(has("ŋ")){ const f=F["9A"]; const s=f?((f.dist["Initial velar nasal"]||0)+(f.dist["No initial velar nasal"]||0))/f.n:null;
    push("info",`Includes <b>/ŋ/</b>${s!=null?` — ~${P(s)} of WALS languages have a velar nasal`:""}.`); }
  if(any(W.frHigh)||any(W.frMid)){ const hv=haveShare("11A");
    push("info",`<b>Front rounded vowels</b> are cross-linguistically rare — only ${P(hv)} of WALS languages have any.`); }

  if(cons.length){ const fric=W.voicedFric.concat(W.voicelessFric);
    if(!any(W.nasals)) push("info",`No nasals — WALS records none in just ${P(sh("18A","No nasals"))} of languages.`);
    if(!any(fric))     push("warn",`No fricatives at all — a real but uncommon gap (${P(sh("18A","No fricatives"))} of WALS).`,5);
    if(!any(W.bilabials)) push("warn",`No bilabial consonants — extremely rare (${P(sh("18A","No bilabials"))} of WALS).`,6); }

  [["Clicks",W.clicks],["Labial-velars",W.labialVelars],["Pharyngeals",W.pharyngeals],["'Th' sounds",W.thSounds]]
    .forEach(([cat,set])=>{ if(any(set)){ const s=sh("19A",cat);
      push("info",`Uncommon class — <b>${cat.toLowerCase()}</b>: ~${s!=null?P(s):"few"} of WALS languages. Distinctive but attested.`); }});

  return {items, pen};
}

/* Phonology-2 layer: suprasegmental contrasts + syllable phonotactics. */
function phon2Items(){
  const items=[]; let pen=0;
  const add=(lvl,html,w=0)=>{ items.push({level:lvl,html}); pen+=w; };
  const vows=selVowels(), cons=selConsonants();
  // examples ordered by real PHOIBLE prevalence, each tagged with its own share
  const egF=arr=>[...arr].sort((a,b)=>segInfo(b).p-segInfo(a).p).slice(0,3)
    .map(s=>{ const p=segInfo(s).p; return `/${s}/${p?` ${fmtPct(p)}`:""}`; }).join(", ");

  if(state.supra.length){
    const segs=longVowels();
    if(!segs.length) add("warn","Vowel length is on, but there are no vowels to lengthen yet.",3);
    else add("info",`<b>Vowel length</b> → ${segs.length} long vowel${segs.length>1?"s":""}; commonest: ${egF(segs)}.`);
  }
  if(state.supra.nasal){
    const segs=nasalVowels();
    if(!segs.length) add("warn","Nasal vowels are on, but there are no vowels to nasalize yet.",3);
    else{ add("info",`<b>Nasal vowels</b> → ${segs.length} contrast${segs.length>1?"s":""}; commonest: ${egF(segs)}.`);
      if(!NASALS.some(has)) add("info","Nasal vowels typically pattern with nasal consonants — you have none (attested, e.g. via lost nasals, but unusual).",2); }
  }
  if(state.supra.gemination){
    const segs=geminates();
    if(!segs.length) add("warn","Gemination is on, but there are no geminable consonants yet.",3);
    else add("info",`<b>Geminate consonants</b> → a length contrast on ${segs.length} consonant${segs.length>1?"s":""}; commonest: ${egF(segs)} — geminates are uncommon phonemes.`);
  }
  if(state.supra.diphthong){
    const segs=diphthongs();
    if(!segs.length) add("warn","Diphthongs are on, but none can be formed — add a non-high vowel plus /i/ or /u/.",2);
    else add("good",`<b>Diphthongs</b> → ${segs.length} closing diphthong${segs.length>1?"s":""} (${segs.slice(0,3).map(s=>"/"+s+"/").join(" ")}); the commonest type cross-linguistically, though any single one is individually rare.`);
  }

  // ---- syllable structure → WALS 12A
  const cls=syllableClass();
  let share=null;
  if(WALS&&WALS.features&&WALS.features["12A"]){ const f=WALS.features["12A"]; share=f.dist[cls]!=null?f.dist[cls]/f.n:null; }
  add(cls==="Moderately complex"?"good":"info",
    `Syllable template <code>${syllableTemplate()}</code> → <b>${cls.toLowerCase()}</b> structure${share!=null?` — ${Math.round(share*100)}% of WALS languages`:""}.`);
  const liquids=["l","r","ɾ","ɹ","w","j","ʎ","ɭ","ʀ","ʁ"];
  if(state.syll.onset>=2 && cons.length && !cons.some(c=>liquids.includes(c)))
    add("warn","Onset clusters but no liquids or glides — most cluster systems are built around /l r w j/.",4);
  if(state.syll.coda>=2 && state.syll.onset===0)
    add("warn","Complex codas with no onset at all is a very marked, near-unattested combination.",5);
  if(state.syll.onset===0 && state.syll.coda===0 && cons.length)
    add("info","Onset 0 / coda 0 makes every syllable a bare V — even minimal systems usually allow (C)V.",1);

  return {items, pen};
}

function evaluate(){
  const fb=[]; const warnSyms=new Set();
  const sel=[...state.selected];
  const cons=sel.filter(s=>classOf(s)==="consonant");
  const vows=sel.filter(s=>classOf(s)==="vowel");
  const sizes=DATA.meta.sizes;
  let penalty=0;
  const add=(level,html,weight=0,syms)=>{ fb.push({level,html}); penalty+=weight; if(syms) syms.forEach(s=>warnSyms.add(s)); };

  if(!sel.length){ add("info","Click blocks to start building.",0); return {fb, score:null, warnSyms}; }

  // ---- structural minimums
  if(!cons.length) add("bad","No <b>consonants</b> yet — every known language has them.",20);
  if(!vows.length) add("bad","No <b>vowels</b> yet — add at least one vowel quality.",20);

  // ---- size vs PHOIBLE
  const sizeLine=(label,n,st)=>{
    if(!n) return;
    if(n<st.p10) add("warn",`<b>${n} ${label}</b> is small — only ~10% of languages have ≤${st.p10}.`,8);
    else if(n>st.p90) add("info",`<b>${n} ${label}</b> is large (PHOIBLE p90 = ${st.p90}); attested but elaborate.`,2);
    else if(n>=st.p25&&n<=st.p75) add("good",`<b>${n} ${label}</b> — squarely typical (median ${st.median}).`);
    else add("info",`<b>${n} ${label}</b> — within the normal range (median ${st.median}).`);
  };
  sizeLine("consonants",cons.length,sizes.consonant);
  sizeLine("vowels",vows.length,sizes.vowel);

  // ---- near-universals
  if(vows.length && !NASALS.some(has))
    add("warn","No <b>nasal consonant</b> — &gt;96% of languages have at least one (usually /m/, /n/).",10,[]);
  ["i","a","u"].forEach(v=>{ if(vows.length && !has(v))
    add("info",`Most languages include <b>/${v}/</b> (${pct(freq(v))}%); consider it for a natural vowel core.`,2); });
  if(has("i")&&has("a")&&has("u")) add("good","Has the cross-linguistic vowel core <b>/i a u/</b>.");

  // ---- implicational co-occurrence (data-driven), strongest first
  const fired=DATA.implications
    .filter(im=>has(im.a)&&!has(im.b)&&im.p>=0.6)
    .sort((x,y)=>y.p-x.p);
  fired.slice(0,6).forEach(im=>{
    add("warn",`You have <b>/${im.a}/</b> but not <b>/${im.b}/</b> — ${pct(im.p)}% of PHOIBLE languages with /${im.a}/ also have /${im.b}/.`,
        Math.round(im.p*12),[im.a]);
  });

  // ---- voicing symmetry praise
  const stopVL=["p","t","k"].filter(has), stopVD=["b","d","ɡ"].filter(has);
  if(stopVL.length>=2 && stopVD.length && stopVL.length>=stopVD.length &&
     ["b","d","ɡ"].every(v=>!has(v)|| has({b:"p",d:"t","ɡ":"k"}[v])))
    add("good","Stop voicing is <b>symmetric</b> — no orphaned voiced stops.");

  // ---- average commonness note
  const avg = sel.reduce((a,s)=>a+freq(s),0)/sel.length;
  if(sel.length>=5) add("info",`Mean segment commonness: <b>${pct(avg)}%</b> across your ${sel.length} sounds.`);

  // ---- Phonology 2 layer (only once the level is unlocked)
  if(state.level>=2){
    const {items,pen}=phon2Items();
    if(items.length){
      fb.push({level:"div", html:"Phonology 2 — length & syllables"});
      items.forEach(it=>fb.push({level:it.level, html:it.html}));
      penalty+=pen;
    }
  }

  // ---- WALS typological cross-check (separate source)
  if(WALS && WALS.features){
    const {items,pen}=walsItems(cons,vows);
    if(items.length){
      fb.push({level:"div", html:"WALS typological cross-check"});
      items.forEach(it=>fb.push({level:it.level, html:it.html, src:"wals"}));
      penalty+=pen;
    }
  }

  let score = Math.max(0, Math.min(100, 100-penalty));
  return {fb, score, warnSyms};
}

function renderFeedback(){
  if(!DATA) return;
  const {fb,score,warnSyms}=evaluate();
  // mark warn blocks
  document.querySelectorAll(".block.warnat").forEach(b=>b.classList.remove("warnat"));
  warnSyms.forEach(s=>document.querySelector(`.block[data-sym="${cssEsc(s)}"]`)?.classList.add("warnat"));
  // list
  const ul=$("#feedback"); ul.innerHTML="";
  const icon={good:"✓",warn:"!",bad:"✕",info:"i"};
  fb.forEach(f=>{
    if(f.level==="div"){ const li=document.createElement("li"); li.className="divider"; li.textContent=f.html; ul.appendChild(li); return; }
    const li=document.createElement("li"); li.className=f.level;
    const tag = f.src==="wals" ? '<span class="src">WALS</span>' : "";
    li.innerHTML=`<span class="ic">${icon[f.level]}</span><span>${tag}${f.html}</span>`; ul.appendChild(li);
  });
  // badge + gauge
  const badge=$("#scoreBadge"), fill=$("#gaugeFill");
  if(score==null){ badge.textContent="—"; fill.style.width="0"; }
  else{
    const label = score>=85?"Very natural":score>=70?"Natural":score>=50?"Plausible":score>=30?"Marked":"Unusual";
    badge.textContent=`${score} · ${label}`;
    fill.style.width=score+"%";
  }
}
function cssEsc(s){ return (window.CSS&&CSS.escape)?CSS.escape(s):s.replace(/["\\]/g,"\\$&"); }

/* ------------------------------------------------------------------ *
 * 7. Actions
 * ------------------------------------------------------------------ */
function toggle(sym){
  if(state.selected.has(sym)) state.selected.delete(sym); else state.selected.add(sym);
  save(); refreshSelectionUI();
}
function refreshSelectionUI(){
  document.querySelectorAll(".block").forEach(b=>{
    if(b.dataset.sym) b.classList.toggle("on", state.selected.has(b.dataset.sym));
  });
  renderTray(); renderFeedback(); updateTabCounts();
  if(state.level>=2){ renderSupra(); renderSyllable(); } // derived previews track the base inventory
}
function setInventory(list){ state.selected=new Set(list); save(); refreshSelectionUI(); }

/* ------------------------------------------------------------------ *
 * 8. Export / import
 * ------------------------------------------------------------------ */
function exportMarkdown(){
  const sel=[...state.selected];
  const cons=sel.filter(s=>classOf(s)==="consonant");
  const vows=sel.filter(s=>classOf(s)==="vowel");
  const L=[];
  L.push(`# Phonological inventory`,"",
    `*${cons.length} consonants, ${vows.length} vowels. Built with the Phonological Inventory Builder; naturalness checked against PHOIBLE 2.0.*`,"");
  // consonant table — only places/manners in use
  if(cons.length){
    const usedP=C_PLACES.filter(([pid])=>C_MANNERS.some(([mid])=>{
      const pr=MCELLS[`${mid}|${pid}`]; return pr&&pr.some(s=>s&&state.selected.has(s));}));
    const usedM=C_MANNERS.filter(([mid])=>C_PLACES.some(([pid])=>{
      const pr=MCELLS[`${mid}|${pid}`]; return pr&&pr.some(s=>s&&state.selected.has(s));}));
    L.push(`## Consonants (${cons.length})`,"");
    L.push("| | "+usedP.map(p=>p[1]).join(" | ")+" |");
    L.push("|---|"+usedP.map(()=>"---").join("|")+"|");
    usedM.forEach(([mid,ml])=>{
      const row=usedP.map(([pid])=>{ const pr=MCELLS[`${mid}|${pid}`]||[];
        return pr.filter(s=>s&&state.selected.has(s)).join(" ");});
      L.push(`| **${ml}** | ${row.join(" | ")} |`);
    });
    const otherSel=[...C_NONPULM,...C_OTHER].flatMap(([,syms])=>syms).filter(s=>state.selected.has(s));
    if(otherSel.length) L.push("",`Non-pulmonic / other: ${otherSel.map(s=>"/"+s+"/").join(", ")}`);
    L.push("");
  }
  if(vows.length){
    const usedB=V_BACK.filter(([bid])=>V_HEIGHTS.some(([hid])=>{
      const pr=V_CELLS[`${hid}|${bid}`]; return pr&&pr.some(s=>s&&state.selected.has(s));}));
    const usedH=V_HEIGHTS.filter(([hid])=>V_BACK.some(([bid])=>{
      const pr=V_CELLS[`${hid}|${bid}`]; return pr&&pr.some(s=>s&&state.selected.has(s));}));
    L.push(`## Vowels (${vows.length})`,"");
    L.push("| | "+usedB.map(b=>b[1]).join(" | ")+" |");
    L.push("|---|"+usedB.map(()=>"---").join("|")+"|");
    usedH.forEach(([hid,hl])=>{
      const row=usedB.map(([bid])=>{ const pr=V_CELLS[`${hid}|${bid}`]||[];
        return pr.filter(s=>s&&state.selected.has(s)).join(" ");});
      L.push(`| **${hl}** | ${row.join(" | ")} |`);
    });
    L.push("");
  }
  // ---- Phonology 2: suprasegmentals & phonotactics
  if(state.level>=2){
    L.push(`## Suprasegmentals & phonotactics`,"");
    const rows=[];
    const fmt=(name,arr)=>{ if(arr.length) rows.push(`- **${name}** (${arr.length}): ${arr.map(s=>"/"+s+"/").join(" ")}`); };
    if(state.supra.length)     fmt("Vowel length",longVowels());
    if(state.supra.nasal)      fmt("Nasal vowels",nasalVowels());
    if(state.supra.gemination) fmt("Geminate consonants",geminates());
    if(state.supra.diphthong)  fmt("Diphthongs",diphthongs());
    L.push(...(rows.length?rows:["- No suprasegmental contrasts selected."]));
    L.push(`- **Syllable structure**: \`${syllableTemplate()}\` — ${syllableClass()} (WALS 12A).`,"");
  }
  L.push(`IPA: /${[...cons,...vows].join(" ")}/`);
  return L.join("\n");
}
function exportJSON(){
  const o={
    schema:"phonological-inventory/v1",
    consonants:[...state.selected].filter(s=>classOf(s)==="consonant"),
    vowels:[...state.selected].filter(s=>classOf(s)==="vowel"),
  };
  if(state.level>=2){
    o.suprasegmentals={
      length:     state.supra.length     ? longVowels()  : [],
      nasal:      state.supra.nasal      ? nasalVowels() : [],
      gemination: state.supra.gemination ? geminates()   : [],
      diphthongs: state.supra.diphthong  ? diphthongs()  : [],
    };
    o.syllable={ onset:state.syll.onset, coda:state.syll.coda,
      template:syllableTemplate(), class:syllableClass() };
  }
  return JSON.stringify(o, null, 2);
}
async function copy(text,label){
  try{ await navigator.clipboard.writeText(text); toast(`${label} copied to clipboard`); }
  catch(e){ // fallback
    const t=document.createElement("textarea"); t.value=text; document.body.appendChild(t); t.select();
    try{document.execCommand("copy"); toast(`${label} copied`);}catch(_){toast("Copy failed — select & copy manually");}
    t.remove();
  }
}
function importJSON(){
  const raw=prompt("Paste an inventory JSON (or a space-separated IPA list):");
  if(!raw) return;
  let list=[], o=null;
  try{ o=JSON.parse(raw);
    if(Array.isArray(o)){ list=o; o=null; }
    else list=[...(o.consonants||[]),...(o.vowels||[]),...(o.segments||[])];
  }catch(e){ list=raw.trim().replace(/[\/\[\]]/g,"").split(/\s+/).filter(Boolean); }
  if(!list.length){ toast("Nothing recognised in that input."); return; }
  setInventory(list);
  // round-trip the Phonology-2 layer if present (toggles are rederived from the base)
  if(o){
    if(o.syllable){ if(Number.isInteger(o.syllable.onset)) state.syll.onset=Math.max(0,Math.min(3,o.syllable.onset));
                    if(Number.isInteger(o.syllable.coda))  state.syll.coda =Math.max(0,Math.min(3,o.syllable.coda)); }
    if(o.suprasegmentals){ const s=o.suprasegmentals;
      state.supra.length    =!!(s.length     && s.length.length);
      state.supra.nasal     =!!(s.nasal      && s.nasal.length);
      state.supra.gemination=!!(s.gemination && s.gemination.length);
      state.supra.diphthong =!!(s.diphthongs && s.diphthongs.length);
    }
    if((o.syllable||o.suprasegmentals) && state.level<2) state.level=2;
    save(); renderLevels(); renderHeader(); renderLevel2(); renderFeedback();
  }
}

/* ------------------------------------------------------------------ *
 * 9. Misc UI
 * ------------------------------------------------------------------ */
let toastT=null;
function toast(msg){
  const h=$("#hint"); h.textContent=msg; h.hidden=false;
  clearTimeout(toastT); toastT=setTimeout(()=>h.hidden=true, 2600);
}
function renderPresets(){
  const m=$("#presetMenu"); m.innerHTML="";
  PRESETS.forEach(p=>{
    const b=document.createElement("button");
    b.innerHTML=`${p.name}<small>${p.note} · ${p.set.length} sounds</small>`;
    b.addEventListener("click",()=>{ setInventory(p.set); m.closest("details").open=false; toast(`Loaded “${p.name}”.`); });
    m.appendChild(b);
  });
}

/* ------------------------------------------------------------------ *
 * 10. Boot
 * ------------------------------------------------------------------ */
async function boot(){
  load();
  renderLevels(); renderHeader(); renderLevel2();
  renderConsonants();
  renderGroups("nonpulmGroups", C_NONPULM);
  renderGroups("otherGroups", C_OTHER);
  renderVowels(); renderTabs(); renderPresets(); applyDerived();
  // wire toolbar
  const dt=$("#derivedToggle");
  if(dt){ dt.checked=!!state.derived;
    dt.addEventListener("change",()=>{ state.derived=dt.checked; save(); applyDerived();
      toast(state.derived?"Showing derived (diacritic) segments.":"Hiding derived segments."); }); }
  $("#btnClear").addEventListener("click",()=>{ if(state.selected.size){ setInventory([]); toast("Inventory cleared."); }});
  $("#btnMd").addEventListener("click",()=>copy(exportMarkdown(),"Markdown"));
  $("#btnJson").addEventListener("click",()=>copy(exportJSON(),"JSON"));
  $("#btnImport").addEventListener("click",importJSON);

  try{
    const res=await fetch("data/phoible-summary.json");
    if(!res.ok) throw new Error(res.status);
    DATA=await res.json();
    const m=DATA.meta;
    $("#metaLine").textContent=`· PHOIBLE ${m.n_inventories} inventories · generated ${m.generated}`;
  }catch(e){
    toast("Could not load PHOIBLE summary — serve this folder over http (see README).");
    $("#metaLine").textContent="· PHOIBLE summary not loaded";
  }
  try{
    const r2=await fetch("data/wals-phonology.json");
    if(r2.ok){ WALS=await r2.json();
      $("#metaLine").textContent += ` · WALS cross-check (${WALS.features["19A"].n} langs)`; }
  }catch(e){ /* WALS is an optional enhancement */ }
  // re-render now that frequencies are available
  renderConsonants();
  renderGroups("nonpulmGroups", C_NONPULM);
  renderGroups("otherGroups", C_OTHER);
  renderVowels(); applyDerived();
  renderTray(); renderFeedback(); updateTabCounts(); renderLevel2();
}
document.addEventListener("DOMContentLoaded", boot);
