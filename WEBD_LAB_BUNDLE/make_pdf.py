import os, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, Preformatted, Image, KeepTogether, Flowable)
from build import EXPS, NAME, ROLL, FACULTY, SUBJECT, live, repo

ROOT = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(ROOT, "screenshots")   # put exp1_1.png, exp1_2.png ... here and re-run
LOGO = os.path.join(ROOT, "assets", "logo-000.png")
OUTFILE = os.path.join(ROOT, "WEBD_FILE_ANIKET_CHAUDHARY.pdf")

NAVY = colors.HexColor("#1F4E79")
base = dict(fontName="Times-Roman", fontSize=11, leading=14)
sty = {
    "body": ParagraphStyle("body", alignment=TA_JUSTIFY, spaceAfter=4, **base),
    "bullet": ParagraphStyle("bullet", leftIndent=14, bulletIndent=2, spaceAfter=1, **base),
    "h": ParagraphStyle("h", fontName="Times-Bold", fontSize=12.5, leading=16, spaceBefore=8, spaceAfter=3),
    "exp": ParagraphStyle("exp", fontName="Times-Bold", fontSize=20, leading=24, textColor=NAVY, spaceAfter=6),
    "file": ParagraphStyle("file", fontName="Courier-Bold", fontSize=9, leading=11, spaceBefore=6, spaceAfter=2),
    "code": ParagraphStyle("code", fontName="Courier", fontSize=7.5, leading=9, backColor=colors.HexColor("#F5F6F8"),
                           borderPadding=3, leftIndent=2),
    "cap": ParagraphStyle("cap", fontName="Times-Italic", fontSize=10, alignment=TA_CENTER, spaceBefore=2, spaceAfter=8),
    "ph": ParagraphStyle("ph", fontName="Times-Italic", fontSize=10, alignment=TA_CENTER, textColor=colors.HexColor("#888888")),
    "ctr": ParagraphStyle("ctr", alignment=TA_CENTER, **base),
}


def P(t, s="body"):
    return Paragraph(t, sty[s])


def wrap_code(src, width=104):
    out = []
    for line in src.rstrip("\n").split("\n"):
        line = line.replace("\t", "    ")
        if len(line) <= width:
            out.append(line)
        else:
            indent = len(line) - len(line.lstrip())
            parts = textwrap.wrap(line, width=width, subsequent_indent=" " * (indent + 4),
                                  break_long_words=True, replace_whitespace=False, drop_whitespace=False)
            out.extend(parts)
    return "\n".join(out)


class Placeholder(Flowable):
    def __init__(self, text, w=150 * mm, h=55 * mm):
        super().__init__()
        self.text, self.w, self.h = text, w, h
        self.width, self.height = w, h

    def draw(self):
        c = self.canv
        c.setStrokeColor(colors.HexColor("#AAAAAA"))
        c.setDash(4, 3)
        c.rect(0, 0, self.w, self.h)
        c.setFillColor(colors.HexColor("#888888"))
        c.setFont("Times-Italic", 10)
        c.drawCentredString(self.w / 2, self.h / 2 + 4, "[ Paste screenshot here ]")
        c.drawCentredString(self.w / 2, self.h / 2 - 9, self.text)


def shot(n, k, caption):
    for ext in ("png", "jpg", "jpeg"):
        p = os.path.join(SHOTS, "exp%d_%d.%s" % (n, k, ext))
        if os.path.exists(p):
            from PIL import Image as PI
            w, h = PI.open(p).size
            maxw, maxh = 150 * mm, 95 * mm
            sc = min(maxw / w, maxh / h)
            img = Image(p, width=w * sc, height=h * sc)
            img.hAlign = "CENTER"
            return [img, P("-" + caption, "cap")], True
    ph = Placeholder(caption)
    ph.hAlign = "CENTER"
    return [ph, P("-" + caption, "cap")], False


def header_footer(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 8)
    canv.setFillColor(colors.HexColor("#555555"))
    canv.drawCentredString(A4[0] / 2, A4[1] - 12 * mm, "JCS 308  |  WEB DESIGNING LAB")
    canv.drawCentredString(A4[0] / 2, 10 * mm, "Web Designing Lab Manual • %d" % doc.page)
    canv.restoreState()


def cover():
    s = []
    s.append(Paragraph("JSS University, Noida, Uttar Pradesh", ParagraphStyle("u", fontName="Times-Roman", fontSize=26, leading=30, alignment=TA_CENTER, textColor=NAVY)))
    s.append(Paragraph("C-20/1, SECTOR-62, NOIDA, DISTT. U.P., INDIA-201301", ParagraphStyle("a", fontName="Times-Roman", fontSize=11, leading=14, alignment=TA_CENTER, textColor=NAVY)))
    s.append(Spacer(1, 14 * mm))
    if os.path.exists(LOGO):
        im = Image(LOGO, width=48 * mm, height=48 * mm * 310 / 339)
        im.hAlign = "CENTER"
        s.append(im)
    s.append(Spacer(1, 16 * mm))
    big = ParagraphStyle("b", fontName="Times-Bold", fontSize=18, leading=26, alignment=TA_CENTER, textColor=NAVY)
    s += [Paragraph("Department of CSE-Data Science", big), Paragraph("Academic Session: 2026-27", big),
          Paragraph("B.Tech(CSE-DS) 2<super>nd</super> Year", big), Spacer(1, 14 * mm),
          Paragraph("WEB DESIGNING LAB", ParagraphStyle("w", fontName="Times-Bold", fontSize=26, leading=30, alignment=TA_CENTER, textColor=NAVY)),
          Spacer(1, 4 * mm),
          Paragraph("LABORATORY FILE", ParagraphStyle("l", fontName="Times-Bold", fontSize=18, leading=22, alignment=TA_CENTER)),
          Spacer(1, 14 * mm)]
    cell = ParagraphStyle("c", fontName="Times-Bold", fontSize=10.5, leading=13)
    rows = [[Paragraph("NAME", cell), Paragraph(NAME.upper(), cell)],
            [Paragraph("UNIVERSITY ROLL NO.", cell), Paragraph(ROLL, cell)],
            [Paragraph("SUBJECT CODE", cell), Paragraph(SUBJECT, cell)],
            [Paragraph("FACULTY NAME", cell), Paragraph(FACULTY, cell)]]
    t = Table(rows, colWidths=[85 * mm, 89 * mm], rowHeights=[11 * mm] * 4)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, colors.black), ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#D9E8F5")),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    s += [t, PageBreak()]
    return s


def index():
    s = [Paragraph("List of Experiments", ParagraphStyle("i", fontName="Times-Bold", fontSize=18, leading=22, textColor=NAVY, spaceAfter=8))]
    cell = ParagraphStyle("ic", fontName="Times-Roman", fontSize=10.5, leading=13)
    rows = [[Paragraph("<b>Week</b>", cell), Paragraph("<b>Exp. No.</b>", cell), Paragraph("<b>Experiment</b>", cell)]]
    for e in EXPS:
        rows.append([Paragraph("Week %d" % e["n"], cell), Paragraph(str(e["n"]), cell), Paragraph(escape(e["title"]), cell)])
    t = Table(rows, colWidths=[22 * mm, 22 * mm, 130 * mm], repeatRows=1)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.6, colors.black), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9E8F5")),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    s += [t, PageBreak()]
    return s


def experiment(e):
    n = e["n"]
    s = [P("EXPERIMENT %d" % n, "exp")]
    s += [P("Objective", "h"), P(escape(e["title"])), P("Aim", "h"), P(escape(e["aim"])), P("Description", "h"), P(escape(e["desc"]))]
    s.append(P("Software Required", "h"))
    for sw in e["software"]:
        s.append(Paragraph(escape(sw), sty["bullet"], bulletText="•"))
    s.append(P("Source Code", "h"))
    for rel, content in e["files"]:
        s.append(P(escape(rel), "file"))
        s.append(Preformatted(wrap_code(content), sty["code"]))
    s.append(P("Output", "h"))
    s.append(P(escape(e["output"])))
    missing = 0
    for k, cap in enumerate(e["shots"], 1):
        fl, ok = shot(n, k, cap)
        missing += 0 if ok else 1
        s.append(KeepTogether(fl))
    # links
    s.append(P("Links", "h"))
    if e.get("live"):
        s.append(P("<b>Live Website URL:</b> <link href='%s' color='blue'>%s</link>" % (live(n), live(n))))
    else:
        s.append(P("<b>Live Website URL:</b> %s" % escape(e.get("live_note", "Not applicable."))))
    for label, val in e.get("extra_links", []):
        s.append(P("<b>%s:</b> %s" % (escape(label), escape(val))))
    s.append(P("<b>GitHub Repo URL:</b> <link href='%s' color='blue'>%s</link>" % (repo(n), repo(n))))
    s.append(P("Conclusion", "h"))
    s.append(P(escape(e["conclusion"])))
    s.append(PageBreak())
    return s, missing


def main():
    doc = BaseDocTemplate(OUTFILE, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=20 * mm, bottomMargin=18 * mm,
                          title="Web Designing Lab File - %s" % NAME, author=NAME)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=header_footer)])
    story = cover() + index()
    total_missing = 0
    for e in EXPS:
        s, m = experiment(e)
        story += s
        total_missing += m
    story.pop()  # trailing page break
    doc.build(story)
    print("PDF written:", OUTFILE, "| screenshot slots still empty:", total_missing)


if __name__ == "__main__":
    main()
