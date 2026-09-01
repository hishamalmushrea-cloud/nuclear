/* progress.js — يدمج progress/profile.json مع graph/knowledge_graph.json */
(function () {
  var PASS = 80;
  var graph = null, prof = null;
  var sortKey = "pct", sortDir = -1;

  var tbody = document.querySelector("#tbl tbody");
  var qEl = document.getElementById("q");
  var lvlEl = document.getElementById("lvl");
  var doneEl = document.getElementById("onlyDone");
  var statsEl = document.getElementById("stats");
  var kpisEl = document.getElementById("kpis");

  function get(o, k, d) { return o && o[k] !== undefined && o[k] !== null ? o[k] : d; }

  function pctOf(t) {
    var p = get(t, "mastery", 0);
    return typeof p === "number" ? p : 0;
  }

  function levelColor(l) {
    return { L0: "#8b98ab", L1: "#7fb6ff", L2: "#5fd0a8", L3: "#c58bff", L4: "#ffb347", L5: "#ff7b7b" }[l] || "#8b98ab";
  }

  function rows() {
    var out = graph.nodes.map(function (n) {
      var t = get(prof, "topics", {})[n.id] || {};
      return {
        id: n.id,
        title: n.ar || n.en || n.id,
        domain: n.domain_ar || n.domain || "",
        level: get(t, "level", "L0"),
        stage: n.stage_ar || ("مرحلة " + n.stage),
        pct: pctOf(t),
        quiz: get(t, "best_quiz", get(t, "quiz", "—")),
        updated: get(t, "updated", ""),
        status: get(t, "status", "🔴 غير معروف"),
        hours: n.hours || 0,
        diff: n.difficulty || 0
      };
    });
    var q = (qEl.value || "").trim().toLowerCase();
    var lv = lvlEl.value;
    return out.filter(function (r) {
      if (lv && r.level !== lv) return false;
      if (doneEl.checked && r.pct < PASS) return false;
      if (!q) return true;
      return (r.id + " " + r.title + " " + r.domain).toLowerCase().indexOf(q) >= 0;
    }).sort(function (a, b) {
      var x = a[sortKey], y = b[sortKey];
      if (typeof x === "number" && typeof y === "number") return (x - y) * sortDir;
      return String(x).localeCompare(String(y), "ar") * sortDir;
    });
  }

  function render() {
    var data = rows();
    var html = "";
    data.forEach(function (r) {
      var w = Math.max(0, Math.min(100, r.pct));
      html += "<tr>" +
        "<td class='mono'>" + r.id + "</td>" +
        "<td>" + r.title + "</td>" +
        "<td>" + r.domain + "</td>" +
        "<td style='color:" + levelColor(r.level) + "'>" + r.level + "</td>" +
        "<td>" + r.pct + "٪</td>" +
        "<td><span class='barwrap'><span class='barfill' style='width:" + w +
          "٪;background:" + (r.pct >= PASS ? "#5fd0a8" : "#ffd166") + "'></span></span></td>" +
        "<td>" + r.stage + "</td>" +
        "<td>" + r.quiz + "</td>" +
        "<td class='mono'>" + r.updated + "</td></tr>";
    });
    tbody.innerHTML = html || "<tr><td colspan='9'>لا نتائج.</td></tr>";

    var all = graph.nodes.length;
    var done = 0, partial = 0, hoursDone = 0;
    graph.nodes.forEach(function (n) {
      var t = get(prof, "topics", {})[n.id] || {};
      if (pctOf(t) >= PASS) { done++; hoursDone += n.hours || 0; }
      else if (pctOf(t) > 0) partial++;
    });
    kpisEl.innerHTML =
      "<div class='kpi'><div class='v'>" + done + " / " + all + "</div><div class='l'>مواضيع مكتملة (≥" + PASS + "٪)</div></div>" +
      "<div class='kpi'><div class='v'>" + (100 * done / all).toFixed(1) + "٪</div><div class='l'>نسبة إنجاز الخريطة</div></div>" +
      "<div class='kpi'><div class='v'>" + partial + "</div><div class='l'>قيد التعلّم (0–" + (PASS - 1) + "٪)</div></div>" +
      "<div class='kpi'><div class='v'>" + hoursDone + " س</div><div class='l'>ساعات مُتقنة</div></div>";
    statsEl.textContent = data.length + " صف · آخر تحديث للملف: " + (get(prof, "updated", "—"));
  }

  document.querySelectorAll("#tbl th[data-k]").forEach(function (th) {
    th.addEventListener("click", function () {
      var k = th.getAttribute("data-k");
      if (sortKey === k) sortDir *= -1; else { sortKey = k; sortDir = 1; }
      render();
    });
  });
  ["input", "change"].forEach(function (ev) {
    qEl.addEventListener(ev, render);
    lvlEl.addEventListener(ev, render);
    doneEl.addEventListener(ev, render);
  });

  Promise.all([
    fetch("../graph/knowledge_graph.json", { cache: "no-store" }).then(function (r) { return r.json(); }),
    fetch("../progress/profile.json", { cache: "no-store" }).then(function (r) { return r.json(); })
  ]).then(function (res) {
    graph = res[0]; prof = res[1];
    var seen = {};
    graph.nodes.forEach(function (n) {
      var t = get(prof, "topics", {})[n.id] || {};
      seen[get(t, "level", "L0")] = 1;
    });
    ["L0", "L1", "L2", "L3", "L4", "L5"].forEach(function (l) {
      var o = document.createElement("option");
      o.value = l; o.textContent = l + (seen[l] ? " ✓" : "");
      lvlEl.appendChild(o);
    });
    render();
  }).catch(function (e) {
    tbody.innerHTML = "<tr><td colspan='9'>تعذّر تحميل البيانات: " + e + "</td></tr>";
  });
})();
