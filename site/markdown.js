/* markdown.js — مُحوِّل Markdown مصغّر ومستقل (بدون أي اعتماد على الإنترنت).
   يغطي ما نستخدمه فعلاً في هذا المستودع: العناوين، الجداول، القوائم، الاقتباسات،
   كتل الشفرة، الخطوط، الروابط، والفواصل. إن وُجدت مكتبة marked فهي تتولى العمل. */
(function (global) {
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function inline(s) {
    s = esc(s);
    s = s.replace(/`([^`]+)`/g, function (_, c) { return "<code>" + c + "</code>"; });
    s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    s = s.replace(/(^|[\s(])\*([^*\n]+)\*/g, "$1<em>$2</em>");
    s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g,
      function (_, t, u) { return '<a href="' + u + '">' + t + "</a>"; });
    return s;
  }

  function splitRow(line) {
    return line.replace(/^\s*\|/, "").replace(/\|\s*$/, "").split("|").map(function (c) {
      return c.trim();
    });
  }

  function render(src) {
    var lines = String(src).replace(/\r\n?/g, "\n").split("\n");
    var out = [], i = 0, inList = null, para = [];

    function flushPara() {
      if (para.length) {
        out.push("<p>" + inline(para.join(" ")) + "</p>");
        para = [];
      }
    }
    function closeList() {
      if (inList) { out.push("</" + inList + ">"); inList = null; }
    }

    while (i < lines.length) {
      var ln = lines[i];

      /* كتلة شفرة ``` */
      if (/^\s*```/.test(ln)) {
        flushPara(); closeList();
        var lang = ln.replace(/^\s*```/, "").trim();
        var buf = [];
        i++;
        while (i < lines.length && !/^\s*```/.test(lines[i])) { buf.push(lines[i]); i++; }
        i++;
        out.push("<pre" + (lang ? ' class="lang-' + lang + '"' : "") + "><code>" +
          esc(buf.join("\n")) + "</code></pre>");
        continue;
      }

      /* فاصل */
      if (/^\s*(-{3,}|\*{3,}|_{3,})\s*$/.test(ln)) {
        flushPara(); closeList(); out.push("<hr>"); i++; continue;
      }

      /* عنوان */
      var h = /^(#{1,6})\s+(.*)$/.exec(ln);
      if (h) {
        flushPara(); closeList();
        var lvl = Math.min(6, h[1].length);
        out.push("<h" + lvl + ">" + inline(h[2].trim()) + "</h" + lvl + ">");
        i++; continue;
      }

      /* جدول */
      if (/\|/.test(ln) && i + 1 < lines.length && /^\s*\|?[\s:|-]+\|[\s:|-]*$/.test(lines[i + 1])) {
        flushPara(); closeList();
        var head = splitRow(ln);
        i += 2;
        var body = [];
        while (i < lines.length && /\|/.test(lines[i]) && lines[i].trim() !== "") {
          body.push(splitRow(lines[i])); i++;
        }
        var t = "<table><thead><tr>" + head.map(function (c) {
          return "<th>" + inline(c) + "</th>";
        }).join("") + "</tr></thead><tbody>";
        body.forEach(function (r) {
          t += "<tr>" + r.map(function (c) { return "<td>" + inline(c) + "</td>"; }).join("") + "</tr>";
        });
        out.push(t + "</tbody></table>");
        continue;
      }

      /* قائمة */
      var li = /^\s*([-*+]|\d+[.)])\s+(.*)$/.exec(ln);
      if (li) {
        flushPara();
        var ordered = /\d/.test(li[1]);
        var tag = ordered ? "ol" : "ul";
        if (inList !== tag) { closeList(); out.push("<" + tag + ">"); inList = tag; }
        out.push("<li>" + inline(li[2]) + "</li>");
        i++; continue;
      }

      /* اقتباس */
      if (/^\s*>\s?/.test(ln)) {
        flushPara(); closeList();
        out.push("<blockquote>" + inline(ln.replace(/^\s*>\s?/, "")) + "</blockquote>");
        i++; continue;
      }

      /* سطر فارغ */
      if (ln.trim() === "") { flushPara(); closeList(); i++; continue; }

      para.push(ln.trim()); i++;
    }
    flushPara(); closeList();
    return out.join("\n");
  }

  global.miniMarkdown = { render: render };
})(window);
