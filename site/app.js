/* عارض تفاعلي لخريطة المعرفة النووية — بدون مكتبات خارجية.
   التخطيط: طبقات حسب «عمق الرسم» (أطول مسار من الجذور)، أي أن كل عمود يلي شروطه. */
(async function () {
  const canvas = document.getElementById('graph');
  const ctx = canvas.getContext('2d');
  const panel = document.getElementById('panelBody');
  const search = document.getElementById('search');
  const domainFilter = document.getElementById('domainFilter');
  const levelFilter = document.getElementById('levelFilter');
  const statsEl = document.getElementById('stats');

  let DATA = null, nodes = [], byId = new Map(), edges = [];
  let view = { x: 0, y: 0, k: 0.8 };
  let hover = null, selected = null, prevHighlight = new Set();

  const COLORS = {};
  const PALETTE = ['#4f8ef7','#f78c4f','#4fc3a1','#c17ef7','#f76f8e','#8ad24f','#f7c948',
                   '#4fd0e0','#e07a5f','#9b8cf7','#5fb0f7','#7ad07a','#d98cc0','#f7a35f',
                   '#63c7b2','#b0a34f','#e35f7a','#6fa8dc','#a2d06f','#7f8ce0','#d0a05f','#5fc9c9'];

  function fit() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = canvas.clientWidth * dpr;
    canvas.height = canvas.clientHeight * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  function layout() {
    const levels = new Map();
    nodes.forEach(n => {
      const l = n.graph_level || 0;
      if (!levels.has(l)) levels.set(l, []);
      levels.get(l).push(n);
    });
    const keys = [...levels.keys()].sort((a, b) => a - b);
    let maxCount = 0;
    keys.forEach(k => {
      const arr = levels.get(k).sort((a, b) => (a.domain === b.domain ? a.id.localeCompare(b.id)
        : a.domain.localeCompare(b.domain)));
      maxCount = Math.max(maxCount, arr.length);
    });
    const COL = 250, ROW = 44;
    keys.forEach(k => {
      const arr = levels.get(k);
      const offset = (maxCount - arr.length) * ROW / 2;
      arr.forEach((n, i) => { n._x = 90 + k * COL; n._y = 70 + offset + i * ROW; });
    });
    return { width: 120 + (keys.length) * COL, height: 140 + maxCount * ROW };
  }

  function fitToView() {
    if (!nodes.length) return;
    let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    nodes.forEach(n => {
      minX = Math.min(minX, n._x); maxX = Math.max(maxX, n._x);
      minY = Math.min(minY, n._y); maxY = Math.max(maxY, n._y);
    });
    const h = (maxY - minY) + 120;
    const k = Math.max(0.35, Math.min(0.85, canvas.clientHeight / h));
    view.k = k;
    view.x = 40 - minX * k;
    view.y = (canvas.clientHeight - (maxY + minY) * k) / 2;
  }

  function domainColor(d) {
    if (!COLORS[d]) COLORS[d] = PALETTE[Object.keys(COLORS).length % PALETTE.length];
    return COLORS[d];
  }

  function highlightSet() {
    const s = new Set();
    if (selected) {
      s.add(selected.id);
      (byId.get(selected.id).prereqs || []).forEach(p => s.add(p));
      (byId.get(selected.id).dependents || []).forEach(p => s.add(p));
    }
    if (search.value.trim()) {
      const q = search.value.trim().toLowerCase();
      nodes.forEach(n => {
        if ((n.ar + ' ' + n.en + ' ' + n.id).toLowerCase().includes(q)) s.add(n.id);
      });
    }
    return s;
  }

  function draw() {
    if (!DATA) return;
    ctx.save();
    ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);
    ctx.translate(view.x, view.y);
    ctx.scale(view.k, view.k);

    const hl = highlightSet();
    const hasHL = hl.size > 0;
    const dim = hasHL ? 0.12 : 1;

    // الحواف
    edges.forEach(e => {
      const a = byId.get(e.from), b = byId.get(e.to);
      if (!a || !b) return;
      const hot = selected && (e.from === selected.id || e.to === selected.id);
      ctx.globalAlpha = hot ? 0.95 : (hasHL ? (hl.has(e.from) && hl.has(e.to) ? 0.35 : 0.05) : 0.18);
      ctx.strokeStyle = hot ? '#ffd166' : '#8899aa';
      ctx.lineWidth = hot ? 2.2 : 1;
      ctx.beginPath();
      const x1 = a._x + 34, y1 = a._y, x2 = b._x - 34, y2 = b._y;
      ctx.moveTo(x1, y1);
      ctx.bezierCurveTo(x1 + 70, y1, x2 - 70, y2, x2, y2);
      ctx.stroke();
    });

    // العقد
    nodes.forEach(n => {
      const inHL = !hasHL || hl.has(n.id);
      ctx.globalAlpha = inHL ? 1 : dim;
      const r = 6 + (n.difficulty || 1) * 1.6;
      ctx.fillStyle = domainColor(n.domain);
      if (n.depth === 'research') { ctx.strokeStyle = '#fff'; ctx.lineWidth = 2; }
      else if (n.depth === 'advanced' || n.depth === 'specialized') { ctx.strokeStyle = 'rgba(255,255,255,.65)'; ctx.lineWidth = 1.4; }
      else { ctx.strokeStyle = 'rgba(255,255,255,.25)'; ctx.lineWidth = 1; }
      ctx.beginPath(); ctx.arc(n._x, n._y, r, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

      if (n === hover || (selected && n.id === selected.id)) {
        ctx.globalAlpha = 1;
        ctx.strokeStyle = '#ffd166'; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.arc(n._x, n._y, r + 5, 0, Math.PI * 2); ctx.stroke();
      }

      const showLabel = view.k > 0.55 || inHL && hasHL;
      if (showLabel) {
        ctx.globalAlpha = inHL ? 0.95 : dim;
        ctx.fillStyle = '#e8edf5';
        ctx.font = '12px "Noto Naskh Arabic", "Segoe UI", Tahoma, sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText(n.ar.length > 30 ? n.ar.slice(0, 28) + '…' : n.ar, n._x - 12, n._y + 4);
      }
    });
    ctx.restore();
  }

  function pick(mx, my) {
    const x = (mx - view.x) / view.k, y = (my - view.y) / view.k;
    let best = null, bd = 400;
    nodes.forEach(n => {
      const d = (n._x - x) ** 2 + (n._y - y) ** 2;
      if (d < bd) { bd = d; best = n; }
    });
    return best;
  }

  let dragging = false, last = null;
  canvas.addEventListener('mousedown', e => { dragging = true; last = { x: e.clientX, y: e.clientY }; });
  window.addEventListener('mouseup', () => { dragging = false; });
  window.addEventListener('mousemove', e => {
    if (dragging && last) {
      view.x += e.clientX - last.x; view.y += e.clientY - last.y;
      last = { x: e.clientX, y: e.clientY }; draw();
    } else {
      const r = canvas.getBoundingClientRect();
      const n = pick(e.clientX - r.left, e.clientY - r.top);
      if (n !== hover) { hover = n; canvas.style.cursor = n ? 'pointer' : 'default'; draw(); }
    }
  });
  canvas.addEventListener('wheel', e => {
    e.preventDefault();
    const r = canvas.getBoundingClientRect();
    const mx = e.clientX - r.left, my = e.clientY - r.top;
    const k2 = Math.min(2.5, Math.max(0.2, view.k * (e.deltaY < 0 ? 1.12 : 0.89)));
    view.x = mx - (mx - view.x) * (k2 / view.k);
    view.y = my - (my - view.y) * (k2 / view.k);
    view.k = k2; draw();
  }, { passive: false });
  canvas.addEventListener('click', e => {
    const r = canvas.getBoundingClientRect();
    const n = pick(e.clientX - r.left, e.clientY - r.top);
    if (n) { selected = n; renderPanel(n); draw(); }
  });
  canvas.addEventListener('dblclick', e => {
    const r = canvas.getBoundingClientRect();
    const n = pick(e.clientX - r.left, e.clientY - r.top);
    if (n) { center(n); }
  });

  function center(n) {
    view.k = 1.1;
    view.x = canvas.clientWidth / 2 - n._x * view.k;
    view.y = canvas.clientHeight / 2 - n._y * view.k;
    draw();
  }

  function chip(id, cls) {
    const n = byId.get(id);
    return `<button class="chip ${cls || ''}" data-goto="${id}">${n ? n.ar : id}</button>`;
  }

  function renderPanel(n) {
    const srcs = (n.sources || []).map(s => {
      const meta = (DATA.meta.sources || {})[s];
      if (!meta) return `<li>${s}</li>`;
      const lvl = meta.level ? `<span class="lvl${meta.level}">${meta.level}</span>` : '';
      const link = meta.url ? ` <a href="${meta.url}" target="_blank" rel="noopener">رابط</a>` : '';
      return `<li>${lvl} ${meta.ar || s}${link}</li>`;
    }).join('');

    panel.innerHTML = `
      <h2>${n.ar}</h2>
      <div class="muted">${n.en} · <code>${n.id}</code></div>
      <div class="badges">
        <span class="badge">${n.domain_ar}</span>
        <span class="badge">المستوى ${n.level_0_14} — ${n.level_0_14_ar}</span>
        <span class="badge">المرحلة ${n.stage}</span>
        <span class="badge depth-${n.depth}">${n.depth_ar}</span>
        <span class="badge">صعوبة ${n.difficulty}/5</span>
        <span class="badge">${n.hours} ساعة</span>
        <span class="badge">عمق الرسم ${n.graph_level}</span>
      </div>

      <h3>المفاهيم</h3>
      <ul>${(n.concepts || []).map(c => `<li>${c}</li>`).join('')}</ul>

      ${(n.equations || []).length ? `<h3>معادلات</h3><ul class="eq">${n.equations.map(e => `<li><code>${e}</code></li>`).join('')}</ul>` : ''}
      ${(n.applications || []).length ? `<h3>تطبيقات</h3><ul>${n.applications.map(a => `<li>${a}</li>`).join('')}</ul>` : ''}

      <h3>الشروط المسبقة</h3>
      <div class="chips">${(n.prereqs || []).length ? n.prereqs.map(p => chip(p, 'pre')).join('') : '<span class="muted">لا شيء — نقطة بداية</span>'}</div>

      <h3>يفتح الطريق إلى</h3>
      <div class="chips">${(n.dependents || []).length ? n.dependents.map(p => chip(p, 'next')).join('') : '<span class="muted">—</span>'}</div>

      ${(n.related || []).length ? `<h3>روابط مقترحة</h3><div class="chips">${n.related.map(p => chip(p)).join('')}</div>` : ''}
      ${(n.tools || []).length ? `<h3>أدوات</h3><div class="chips">${n.tools.map(t => `<span class="chip static">${t}</span>`).join('')}</div>` : ''}
      ${(n.tags || []).length ? `<h3>وسوم</h3><div class="chips">${n.tags.map(t => `<span class="chip static">${t}</span>`).join('')}</div>` : ''}
      <h3>مصادر</h3><ul class="src">${srcs}</ul>
    `;
    panel.querySelectorAll('[data-goto]').forEach(b => b.addEventListener('click', () => {
      const t = byId.get(b.dataset.goto);
      if (t) { selected = t; renderPanel(t); center(t); }
    }));
    panel.parentElement.scrollTop = 0;
  }

  function applyFilters() {
    const d = domainFilter.value, l = levelFilter.value;
    nodes = DATA.nodes.filter(n => (!d || n.domain === d) && (!l || String(n.level_0_14) === l));
    edges = DATA.edges.filter(e => byId.has(e.from) && byId.has(e.to) &&
      (!d || byId.get(e.from).domain === d) && (!l || String(byId.get(e.from).level_0_14) === l));
    layout();
    statsEl.textContent = `${nodes.length} موضوع · ${edges.length} رابط`;
    draw();
  }

  try {
    const res = await fetch('graph_data.json');
    DATA = await res.json();
    byId = new Map(DATA.nodes.map(n => [n.id, n]));
    const doms = [...new Set(DATA.nodes.map(n => n.domain))].sort();
    doms.forEach(d => {
      const o = document.createElement('option');
      o.value = d;
      o.textContent = (DATA.meta.domains[d] && DATA.meta.domains[d].ar) || d;
      domainFilter.appendChild(o);
    });
    for (let i = 0; i <= 14; i++) {
      const o = document.createElement('option');
      o.value = String(i);
      o.textContent = `${i} — ${(DATA.meta.levels_0_14 && DATA.meta.levels_0_14[i]) || ''}`;
      levelFilter.appendChild(o);
    }
    const legend = document.getElementById('legend');
    legend.innerHTML = doms.map(d =>
      `<span class="lg"><i style="background:${domainColor(d)}"></i>${(DATA.meta.domains[d] || {}).ar || d}</span>`).join('');
    nodes = DATA.nodes.slice();
    edges = DATA.edges.slice();
    layout();
    statsEl.textContent = `${nodes.length} موضوع · ${edges.length} رابط`;
    document.getElementById('resetView').addEventListener('click', () => { fitToView(); draw(); });
    search.addEventListener('input', draw);
    domainFilter.addEventListener('change', applyFilters);
    levelFilter.addEventListener('change', applyFilters);
    window.addEventListener('resize', () => { fit(); });
    fit();
    fitToView();
    draw();
  } catch (err) {
    panel.innerHTML = `<p style="color:#ff8a8a">تعذّر تحميل البيانات: ${err.message}<br>
      شغّل <code>python3 tools/build.py</code> ثم افتح الصفحة عبر خادم محلي.</p>`;
  }
})();
