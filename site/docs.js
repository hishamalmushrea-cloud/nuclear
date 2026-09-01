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
