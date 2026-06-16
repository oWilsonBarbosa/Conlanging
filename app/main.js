/* Phonological Inventory Builder — static, no build step.
 * Toggle IPA "blocks" to assemble an inventory; feedback is grounded in a
 * PHOIBLE-derived summary (data/phoible-summary.json). Complexity is gated by
 * level, mirroring the Conlangs University course (Phonology 1..4). v1 fully
 * implements Phonology 1 and scaffolds the later levels.
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
  ["fricative","Fricative"],["latfric","Lateral fric."],
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
  "tap|alveolar":[null,"ɾ"], "tap|retroflex":[null,"ɽ"],
  "fricative|bilabial":["ɸ","β"], "fricative|labiodental":["f","v"], "fricative|dental":["θ","ð"],
  "fricative|alveolar":["s","z"], "fricative|postalveolar":["ʃ","ʒ"], "fricative|retroflex":["ʂ","ʐ"],
  "fricative|palatal":["ç","ʝ"], "fricative|velar":["x","ɣ"], "fricative|uvular":["χ","ʁ"],
  "fricative|pharyngeal":["ħ","ʕ"], "fricative|glottal":["h","ɦ"],
  "latfric|alveolar":["ɬ","ɮ"],
  "approx|labiodental":[null,"ʋ"], "approx|alveolar":[null,"ɹ"], "approx|retroflex":[null,"ɻ"],
  "approx|palatal":[null,"j"], "approx|velar":[null,"ɰ"],
  "latapprox|alveolar":[null,"l"], "latapprox|retroflex":[null,"ɭ"],
  "latapprox|palatal":[null,"ʎ"], "latapprox|velar":[null,"ʟ"],
};
// Common consonants that don't sit in the pulmonic grid (exact PHOIBLE keys).
const C_EXTRAS = [
  ["w","labial-velar approximant"], ["t̠ʃ","voiceless postalveolar affricate"],
  ["d̠ʒ","voiced postalveolar affricate"], ["ts","voiceless alveolar affricate"],
  ["dz","voiced alveolar affricate"], ["kp","voiceless labial-velar stop"],
  ["ɡb","voiced labial-velar stop"], ["ʔ","glottal stop"],
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
  {n:2, id:"phon2", name:"Length & syllables", status:"soon",
   desc:"Phonology 2: weight and phonotactics.",
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
  {name:"Alantian (this repo)", note:"16 C, /a i u/ core",
   set:["p","b","t","d","k","ɡ","f","s","x","h","m","n","l","r","w","j","a","i","u"]},
];

/* ------------------------------------------------------------------ *
 * 4. State + persistence
 * ------------------------------------------------------------------ */
const LS_KEY = "pib.v1";
let DATA = null;                 // PHOIBLE summary
const state = { level:1, selected:new Set() };

function save(){ localStorage.setItem(LS_KEY, JSON.stringify({level:state.level, selected:[...state.selected]})); }
function load(){
  try{ const o = JSON.parse(localStorage.getItem(LS_KEY)||"{}");
    if(Array.isArray(o.selected)) state.selected = new Set(o.selected);
    if(o.level) state.level = o.level;
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

/* ------------------------------------------------------------------ *
 * 5. Rendering
 * ------------------------------------------------------------------ */
const $ = s => document.querySelector(s);

function pct(x){ return Math.round(x*100); }

function makeBlock(sym, cls, place, manner){
  if(!sym){ const d=document.createElement("div"); d.className="block empty"; return d; }
  register(sym, {cls, place, manner, label:sym});
  const f = freq(sym);
  const b = document.createElement("button");
  b.className = "block" + (state.selected.has(sym) ? " on":"");
  b.style.setProperty("--f", Math.min(1, f/0.9).toFixed(3));
  b.dataset.sym = sym;
  b.innerHTML = `<b class="ipa">${sym}</b><span class="fr">${f? pct(f)+"%":"rare"}</span>`;
  b.title = `/${sym}/ — in ${f?pct(f)+"% of PHOIBLE languages":"<0.1% (rare/unattested)"}`;
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
      const pair = C_CELLS[`${mid}|${pid}`];
      if(!pair) return;
      const wrap = document.createElement("div"); wrap.className="cellpair";
      wrap.appendChild(makeBlock(pair[0],"consonant",pid,mid));
      wrap.appendChild(makeBlock(pair[1],"consonant",pid,mid));
      td.appendChild(wrap);
    });
  });
  // extras
  const ex = $("#consonantExtras"); ex.innerHTML="";
  C_EXTRAS.forEach(([sym,desc])=>{
    register(sym,{cls:"consonant",label:sym,desc});
    ex.appendChild(makeBlock(sym,"consonant","extra","extra"));
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
      state.level=L.n; save(); renderLevels(); renderHeader();
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

function renderTray(){
  const tray=$("#tray");
  const sel=[...state.selected];
  if(!sel.length){ tray.innerHTML='<p class="muted empty">No sounds yet — click blocks on the chart to add them.</p>'; }
  else{
    tray.innerHTML="";
    // order: consonants by frequency then vowels by frequency
    const order=(a,b)=>freq(b)-freq(a);
    const cons=sel.filter(s=>classOf(s)==="consonant").sort(order);
    const vows=sel.filter(s=>classOf(s)==="vowel").sort(order);
    [...cons,...vows].forEach(sym=>{
      const c=document.createElement("button"); c.className="chip"; c.title="Click to remove";
      c.innerHTML=`<span class="ipa">${sym}</span><small>${freq(sym)?pct(freq(sym))+"%":"·"}</small>`;
      c.addEventListener("click",()=>toggle(sym));
      tray.appendChild(c);
    });
  }
  const cons=sel.filter(s=>classOf(s)==="consonant");
  const vows=sel.filter(s=>classOf(s)==="vowel");
  $("#cCount").textContent = cons.length?`· ${cons.length} selected`:"";
  $("#vCount").textContent = vows.length?`· ${vows.length} selected`:"";
  $("#ipaLine").textContent = sel.length? "/ "+[...cons,...vows].join(" ")+" /" : "";
}

/* ------------------------------------------------------------------ *
 * 6. Naturalness engine
 * ------------------------------------------------------------------ */
const NASALS=["m","n","ŋ","ɲ","ɳ","ɱ","ɴ","ʙ"]; // (ʙ harmless)
function has(s){ return state.selected.has(s); }

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
  fb.forEach(f=>{ const li=document.createElement("li"); li.className=f.level;
    li.innerHTML=`<span class="ic">${icon[f.level]}</span><span>${f.html}</span>`; ul.appendChild(li); });
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
  renderTray(); renderFeedback();
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
      const pr=C_CELLS[`${mid}|${pid}`]; return pr&&pr.some(s=>s&&state.selected.has(s));}));
    const usedM=C_MANNERS.filter(([mid])=>C_PLACES.some(([pid])=>{
      const pr=C_CELLS[`${mid}|${pid}`]; return pr&&pr.some(s=>s&&state.selected.has(s));}));
    L.push(`## Consonants (${cons.length})`,"");
    L.push("| | "+usedP.map(p=>p[1]).join(" | ")+" |");
    L.push("|---|"+usedP.map(()=>"---").join("|")+"|");
    usedM.forEach(([mid,ml])=>{
      const row=usedP.map(([pid])=>{ const pr=C_CELLS[`${mid}|${pid}`]||[];
        return pr.filter(s=>s&&state.selected.has(s)).join(" ");});
      L.push(`| **${ml}** | ${row.join(" | ")} |`);
    });
    const extras=C_EXTRAS.map(e=>e[0]).filter(s=>state.selected.has(s));
    if(extras.length) L.push("",`Other: ${extras.map(s=>"/"+s+"/").join(", ")}`);
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
  L.push(`IPA: /${[...cons,...vows].join(" ")}/`);
  return L.join("\n");
}
function exportJSON(){
  return JSON.stringify({
    schema:"phonological-inventory/v1",
    consonants:[...state.selected].filter(s=>classOf(s)==="consonant"),
    vowels:[...state.selected].filter(s=>classOf(s)==="vowel"),
  }, null, 2);
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
  let list=[];
  try{ const o=JSON.parse(raw);
    if(Array.isArray(o)) list=o;
    else list=[...(o.consonants||[]),...(o.vowels||[]),...(o.segments||[])];
  }catch(e){ list=raw.trim().replace(/[\/\[\]]/g,"").split(/\s+/).filter(Boolean); }
  if(list.length) setInventory(list); else toast("Nothing recognised in that input.");
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
  renderLevels(); renderHeader();
  renderConsonants(); renderVowels(); renderPresets();
  // wire toolbar
  $("#btnClear").addEventListener("click",()=>{ if(state.selected.size){ setInventory([]); toast("Inventory cleared."); }});
  $("#btnMd").addEventListener("click",()=>copy(exportMarkdown(),"Markdown"));
  $("#btnJson").addEventListener("click",()=>copy(exportJSON(),"JSON"));
  $("#btnImport").addEventListener("click",importJSON);

  try{
    const res=await fetch("data/phoible-summary.json");
    if(!res.ok) throw new Error(res.status);
    DATA=await res.json();
    const m=DATA.meta;
    $("#metaLine").textContent=`· ${m.n_inventories} inventories · generated ${m.generated}`;
  }catch(e){
    toast("Could not load PHOIBLE summary — serve this folder over http (see README).");
    $("#metaLine").textContent="· PHOIBLE summary not loaded";
  }
  // re-render now that frequencies are available
  renderConsonants(); renderVowels();
  renderTray(); renderFeedback();
}
document.addEventListener("DOMContentLoaded", boot);
