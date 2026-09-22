/* docs.js — عارض الوثائق: يبني شجرة الملفات ويحوّل Markdown إلى HTML */
(function () {
  var BASE = "../";           /* المجلد الجذري للمستودع بالنسبة لـ site/ */
  var sidebar = document.getElementById("sidebar");
  var content = document.getElementById("content");
  var filter = document.getElementById("filter");
  var countEl = document.getElementById("count");
  var index = null;

  function md2html(text) {
    if (typeof marked !== "undefined" && typeof marked.parse === "function") {
      try {
        marked.setOptions({ gfm: true, breaks: false });
        return marked.parse(text);
      } catch (e) { /* يسقط إلى المحوّل المحلي */ }
    }
    if (window.miniMarkdown) return window.miniMarkdown.render(text);
    return "<pre class='raw'>" + text.replace(/[<>&]/g, function (c) {
      return { "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c];
    }) + "</pre>";
  }

  function titleOf(path) {
    for (const g of index.groups) {
      const it = g.items.find(x => x.path === path);
      if (it) return it.title;
    }
    return path;
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function mark(text, q) {
    const i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return esc(text);
    return esc(text.slice(0, i)) + "<mark>" + esc(text.slice(i, i + q.length)) +
           "</mark>" + esc(text.slice(i + q.length));
  }

  async function contentSearch(q) {
    const paths = [];
    index.groups.forEach(g => g.items.forEach(it => paths.push(it.path)));
    sidebar.innerHTML = "<div class='empty'>يبحث في " + paths.length + " ملفاً…</div>";
    const texts = await Promise.all(paths.map(p =>
      fetch(BASE + p, { cache: "no-store" }).then(r => (r.ok ? r.text() : "")).catch(() => "")
    ));
    const hits = [];
    paths.forEach((p, i) => {
      const lines = texts[i].split(/\r?\n/);
      let count = 0; const samples = [];
      lines.forEach((ln, k) => {
        if (ln.toLowerCase().indexOf(q.toLowerCase()) >= 0) {
          count++;
          if (samples.length < 2) samples.push({ n: k + 1, t: ln.trim().slice(0, 160) });
        }
      });
      if (count) hits.push({ path: p, count: count, samples: samples });
    });
    hits.sort((a, b) => b.count - a.count);
    if (!hits.length) {
      sidebar.innerHTML = "<div class='empty'>لا نتائج في المحتوى عن «" + esc(q) + "».</div>";
      return;
    }
    let html = "<div class='group'><div class='glabel'>🔍 نتائج المحتوى — " +
      esc(q) + " (" + hits.length + " ملفاً)</div><ul>";
    hits.forEach(h => {
      html += "<li><a href='#" + encodeURIComponent(h.path) + "' data-path='" + h.path + "'>" +
        esc(titleOf(h.path)) + "</a><span class='p'>" + h.count + " تطابقاً في " + h.path + "</span>";
      h.samples.forEach(s => {
        html += "<span class='snip'>س" + s.n + ": " + mark(s.t, q) + "</span>";
      });
      html += "</li>";
    });
    html += "</ul></div>";
    sidebar.innerHTML = html;
    countEl.textContent = hits.length + " ملف";
  }

  function renderIndex(q) {
    q = (q || "").trim().toLowerCase();
    var html = "", n = 0;
    index.groups.forEach(function (g) {
      var items = g.items.filter(function (it) {
        return !q || (it.path + " " + it.title).toLowerCase().indexOf(q) >= 0;
      });
      if (!items.length) return;
      html += "<div class='group'><div class='glabel'>" + g.icon + " " + g.label + "</div><ul>";
      items.forEach(function (it) {
        n++;
        html += "<li><a href='#" + encodeURIComponent(it.path) + "' data-path='" +
                it.path + "'>" + it.title + "</a>" +
                "<span class='p'>" + it.path + "</span></li>";
      });
      html += "</ul></div>";
    });
    sidebar.innerHTML = html || "<div class='empty'>لا نتائج.</div>";
    countEl.textContent = n + " ملف";
  }

  function show(path) {
    content.innerHTML = "<div class='empty'>جارٍ التحميل…</div>";
    fetch(BASE + path, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.text();
      })
      .then(function (txt) {
        content.innerHTML = "<div class='paper'>" + md2html(txt) + "</div>";
        content.scrollTop = 0;
        window.scrollTo(0, 0);
        document.title = path + " — النظام النووي المعرفي";
        location.hash = encodeURIComponent(path);
      })
      .catch(function (e) {
        content.innerHTML = "<div class='empty'><h2>تعذّر فتح الملف</h2><p>" +
          path + "</p><p>" + e + "</p></div>";
      });
  }

  sidebar.addEventListener("click", function (ev) {
    var a = ev.target.closest("a[data-path]");
    if (!a) return;
    ev.preventDefault();
    Array.prototype.forEach.call(sidebar.querySelectorAll("a.active"),
      function (x) { x.classList.remove("active"); });
    a.classList.add("active");
    show(a.getAttribute("data-path"));
  });

  filter.addEventListener("input", function () { renderIndex(filter.value); });
  document.getElementById("deepSearch").addEventListener("click", function () {
    const q = filter.value.trim();
    if (q.length < 2) { countEl.textContent = "اكتب كلمتين على الأقل"; return; }
    contentSearch(q);
  });
  filter.addEventListener("keydown", function (ev) {
    if (ev.key === "Enter" && filter.value.trim().length >= 2) contentSearch(filter.value.trim());
  });

  fetch("docs_index.json", { cache: "no-store" })
    .then(function (r) { return r.json(); })
    .then(function (data) {
      index = data;
      renderIndex("");
      var h = decodeURIComponent((location.hash || "").replace(/^#/, ""));
      var first = null;
      index.groups.forEach(function (g) {
        g.items.forEach(function (it) {
          if (it.path === h) first = it;
        });
      });
      if (!first) {
        var g0 = index.groups[0];
        first = g0 && g0.items[0];
      }
      if (first) {
        var link = sidebar.querySelector("a[data-path='" + first.path + "']");
        if (link) link.classList.add("active");
        show(first.path);
      }
    })
    .catch(function () {
      sidebar.innerHTML = "<div class='empty'>تعذّر تحميل <code>docs_index.json</code>." +
        "<br>شغّل: <code>python3 tools/site_index.py</code></div>";
    });
})();
