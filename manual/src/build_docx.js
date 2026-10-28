// Maquetador del manual: build/book.json -> dist/*.docx
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType,
  BorderStyle, AlignmentType, HeadingLevel, PageBreak, Header, Footer, PageNumber, TableOfContents,
  LevelFormat, VerticalAlign, TableLayoutType, PageOrientation,
} = require("docx");

const ROOT = path.resolve(__dirname, "..");
const IMG = path.join(ROOT, "build", "img");
const book = JSON.parse(fs.readFileSync(path.join(ROOT, "build", "book.json"), "utf8"));
const OUT = process.argv[2] || path.join(ROOT, "dist", "Manual_Sculpt_Barre_BlockBurn.docx");

const NAVY = "1F3A5F", GOLD = "B08D57", TEAL = "5E8C8A", INK = "222222", GRAY = "6B6B6B", LIGHT = "F3F0EA";
const BODY = "Cambria", HEAD = "Calibri";
const W = 9360; // ancho útil (DXA) con márgenes de 1.25"/1"

// ---------------------------------------------------------------- texto
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let last = 0, m;
  const s = String(text);
  while ((m = re.exec(s))) {
    if (m.index > last) out.push(new TextRun({ text: s.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith("**")) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < s.length) out.push(new TextRun({ text: s.slice(last), ...base }));
  return out;
}

const P = (text, opts = {}) => new Paragraph({ children: runs(text, opts.run || {}), spacing: { after: 100, line: 276 }, ...opts.p });

function bullet(text, level = 0, ref = "bul", size) {
  return new Paragraph({ numbering: { reference: ref, level }, children: runs(text, size ? { size } : {}), spacing: { after: 40, line: 264 } });
}

let olCount = 0;
function olist(items, size) {
  olCount += 1;
  const ref = "ol" + olCount;
  numberingConfigs.push({ reference: ref, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 400, hanging: 280 } } } }] });
  return items.map((t) => new Paragraph({ numbering: { reference: ref, level: 0 }, children: runs(t, size ? { size } : {}), spacing: { after: 40, line: 264 } }));
}

const numberingConfigs = [
  { reference: "bul", levels: [
    { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 260 } } } },
    { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 800, hanging: 260 } } } } ] },
  { reference: "bulx", levels: [
    { level: 0, format: LevelFormat.BULLET, text: "✗", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 300, hanging: 220 } } } } ] },
  { reference: "bulup", levels: [
    { level: 0, format: LevelFormat.BULLET, text: "▲", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 300, hanging: 220 } } } } ] },
  { reference: "buldn", levels: [
    { level: 0, format: LevelFormat.BULLET, text: "▼", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 300, hanging: 220 } } } } ] },
];

// ---------------------------------------------------------------- imágenes
function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20), data: b };
}

function image(name, widthIn) {
  const f = path.join(IMG, name + ".png");
  const { w, h, data } = pngSize(f);
  let wpx = widthIn * 96;
  let hpx = wpx * h / w;
  const maxH = 8.2 * 96;
  if (hpx > maxH) { hpx = maxH; wpx = hpx * w / h; }
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 80, after: 40 }, keepNext: true,
    children: [new ImageRun({ type: "png", data, transformation: { width: Math.round(wpx), height: Math.round(hpx) },
      altText: { title: name, description: name, name } })] });
}

const caption = (t) => new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 180 },
  children: runs(t, { italics: true, size: 17, color: GRAY }) });

// ---------------------------------------------------------------- tablas
const thin = { style: BorderStyle.SINGLE, size: 4, color: "C9C2B6" };
const borders = { top: thin, bottom: thin, left: thin, right: thin };

function cell(content, width, opts = {}) {
  const paras = (Array.isArray(content) ? content : [content]).map((c) =>
    c instanceof Paragraph ? c : new Paragraph({ children: runs(c, { size: opts.size || 18, color: opts.color, bold: opts.bold }), spacing: { after: 20, line: 252 },
      alignment: opts.align, keepNext: !!opts.keep }));
  return new TableCell({ children: paras, width: { size: width, type: WidthType.DXA }, borders,
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 }, verticalAlign: opts.valign || VerticalAlign.TOP });
}

function scaleWidths(rel, total = W) {
  const s = rel.reduce((a, b) => a + b, 0);
  const out = rel.map((r) => Math.floor(total * r / s));
  out[out.length - 1] += total - out.reduce((a, b) => a + b, 0);
  return out;
}

function table(b) {
  const n = b.head.length;
  const widths = scaleWidths(b.widths || Array(n).fill(1));
  const size = b.small ? 16 : 18;
  const rows = [new TableRow({ tableHeader: true, cantSplit: true,
    children: b.head.map((h, i) => cell(h, widths[i], { fill: NAVY, color: "FFFFFF", bold: true, size })) })];
  b.rows.forEach((r, ri) => rows.push(new TableRow({ cantSplit: true,
    children: r.map((c, i) => cell(c === "" ? " " : c, widths[i], { size, fill: ri % 2 ? LIGHT : undefined })) })));
  const out = [new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths, rows, layout: TableLayoutType.FIXED })];
  if (b.caption) out.push(caption(b.caption));
  else out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
  return out;
}

// ---------------------------------------------------------------- recuadros
const BOX = {
  general: { fill: "EAF0F5", bar: NAVY, label: "FUNDAMENTO GENERAL" },
  oficial: { fill: "FBF1DE", bar: "C38A2E", label: "◆ MATERIAL OFICIAL" },
  seguridad: { fill: "F8E6E1", bar: "B5452F", label: "⚠ SEGURIDAD" },
  cue: { fill: "E7F1EC", bar: "3C7A5A", label: "“ CUE CLAVE" },
  tip: { fill: "F4EFE4", bar: GOLD, label: "★ DATO ÚTIL" },
  practica: { fill: "EEEAF4", bar: "7E6B8F", label: "✎ PRÁCTICA" },
};

function box(b) {
  const k = BOX[b.kind] || BOX.tip;
  const inner = [new Paragraph({ spacing: { after: 60 }, children: [
    new TextRun({ text: k.label + "  ", bold: true, size: 15, color: k.bar, font: HEAD }),
    new TextRun({ text: b.title, bold: true, size: 20, color: INK, font: HEAD })] })];
  b.body.forEach((x) => inner.push(...renderBlock(x, { inBox: true })));
  const bar = { style: BorderStyle.SINGLE, size: 24, color: k.bar };
  const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  return [new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], rows: [new TableRow({ cantSplit: false, children: [
    new TableCell({ children: inner, width: { size: W, type: WidthType.DXA }, shading: { fill: k.fill, type: ShadingType.CLEAR, color: "auto" },
      borders: { left: bar, top: none, bottom: none, right: none }, margins: { top: 120, bottom: 100, left: 200, right: 200 } })] })] }),
    new Paragraph({ spacing: { after: 140 }, children: [] })];
}

// ---------------------------------------------------------------- ficha técnica
function ficha(e) {
  const out = [];
  out.push(new Paragraph({ heading: HeadingLevel.HEADING_4, keepNext: true, spacing: { before: 280, after: 40 },
    children: [new TextRun({ text: e.name }), ...(e.en ? [new TextRun({ text: "  ·  " + e.en, italics: true, color: GRAY, size: 20, bold: false })] : [])] }));
  out.push(new Paragraph({ keepNext: true, spacing: { after: 40 }, children: [
    new TextRun({ text: "FICHA TÉCNICA", bold: true, size: 15, color: GOLD, font: HEAD }),
    new TextRun({ text: "   Nivel: " + e.level, size: 17, color: GRAY, font: HEAD })] }));
  out.push(image(e.img, e.img_narrow ? 2.5 : 6.5));
  if (e.img_narrow) out.push(caption("Mapa muscular (rojo = principal; salmón = secundario/estabilizador). Ver la descripción para la posición."));
  const L = 1900, R = W - L;
  const lab = (t) => cell(t, L, { fill: "E8E2D7", bold: true, size: 17, color: NAVY, keep: true });
  const val = (c) => cell(c, R, { size: 18, keep: true });
  const lst = (items, ref) => items.map((t) => new Paragraph({ keepNext: true, numbering: { reference: ref, level: 0 }, children: runs(t, { size: 18 }), spacing: { after: 20, line: 252 } }));
  olCount += 1;
  const ref = "ol" + olCount;
  numberingConfigs.push({ reference: ref, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 300, hanging: 240 } } } }] });
  const rows = [
    ["Objetivo", e.obj], ["Posición inicial", e.start], ["Ejecución", lst(e.steps, ref)], ["Respiración", e.breath],
    ["Músculos principales", e.prim_txt], ["Secundarios / estabilizadores", e.sec_txt || "—"],
    ["Errores frecuentes", lst(e.errors, "bulx")], ["Regresión (más fácil)", lst(e.regress, "buldn")],
    ["Progresión (más difícil)", lst(e.progress, "bulup")], ["Dosificación sugerida", e.dose],
  ];
  const trs = rows.map(([a, b]) => new TableRow({ cantSplit: true, children: [lab(a), Array.isArray(b) ? new TableCell({ children: b, width: { size: R, type: WidthType.DXA }, borders, margins: { top: 60, bottom: 60, left: 100, right: 100 } }) : val(b)] }));
  trs.push(new TableRow({ cantSplit: true, children: [cell("Cue clave", L, { fill: "3C7A5A", color: "FFFFFF", bold: true, size: 17 }),
    cell(e.cue, R, { fill: "E7F1EC", size: 18, bold: true, color: "2F5E46" })] }));
  out.push(new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [L, R], rows: trs, layout: TableLayoutType.FIXED }));
  out.push(new Paragraph({ spacing: { after: 160 }, children: [] }));
  return out;
}

// ---------------------------------------------------------------- bloques
function heading(text, level, opts = {}) {
  const map = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3, 4: HeadingLevel.HEADING_4 };
  return new Paragraph({ heading: map[level], keepNext: true, children: runs(text), pageBreakBefore: !!opts.pageBreak });
}

function renderBlock(b, ctx = {}) {
  switch (b.t) {
    case "h": return [heading(b.x, b.l)];
    case "p": return [P(b.x, ctx.inBox ? { p: { spacing: { after: 60, line: 264 } } } : {})];
    case "ul": return b.items.map((t) => bullet(t));
    case "ol": return olist(b.items);
    case "table": return table(b);
    case "fig": return [image(b.name, b.width || 6.3), caption(b.caption)];
    case "box": return box(b);
    case "ex": return ficha(b);
    default: return [];
  }
}

function quiz(m) {
  const out = [heading(`Evaluación del Módulo ${m.num}`, 3)];
  out.push(P("Responde sin consultar el texto y después revisa el **Apéndice B · Solucionario**.", { run: { color: GRAY } }));
  m.quiz.forEach((q, i) => {
    out.push(new Paragraph({ keepNext: true, spacing: { before: 120, after: 40 }, children: [
      new TextRun({ text: `${i + 1}. `, bold: true, color: NAVY }), ...runs(q.q)] }));
    if (q.opts) {
      q.opts.forEach((o, j) => out.push(new Paragraph({ indent: { left: 400 }, spacing: { after: 20 }, keepNext: j < q.opts.length - 1,
        children: runs(`${"abcdefgh"[j]}) ${o}`) })));
    } else if (q.a === "V" || q.a === "F") {
      out.push(new Paragraph({ indent: { left: 400 }, children: [new TextRun({ text: "(   ) Verdadero        (   ) Falso", color: GRAY })] }));
    } else {
      for (let k = 0; k < 3; k++) out.push(new Paragraph({ indent: { left: 400 }, spacing: { after: 0, line: 360 }, keepNext: k < 2,
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "C9C2B6", space: 1 } }, children: [new TextRun(" ")] }));
    }
  });
  return out;
}

// ---------------------------------------------------------------- portada y preliminares
function cover() {
  const out = [];
  out.push(new Paragraph({ spacing: { before: 1400, after: 0 }, alignment: AlignmentType.LEFT,
    children: [new TextRun({ text: "MANUAL DE FORMACIÓN", font: HEAD, size: 26, color: GOLD, bold: true, characterSpacing: 60 })] }));
  out.push(new Paragraph({ spacing: { before: 120, after: 0 }, children: [new TextRun({ text: "Sculpt & Burn", font: HEAD, size: 76, bold: true, color: NAVY })] }));
  out.push(new Paragraph({ spacing: { before: 0, after: 0 }, children: [new TextRun({ text: "Barre", font: HEAD, size: 76, bold: true, color: NAVY })] }));
  out.push(new Paragraph({ spacing: { before: 0, after: 200 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 8 } },
    children: [new TextRun({ text: "Block Burn Pilates", font: HEAD, size: 76, bold: true, color: NAVY })] }));
  out.push(new Paragraph({ spacing: { before: 200, after: 120 }, children: [new TextRun({ text: "Guía de estudio para el aprendizaje personal desde cero", font: BODY, size: 30, italics: true, color: INK })] }));
  out.push(new Paragraph({ spacing: { after: 400 }, children: [new TextRun({ text: "Anatomía · técnica · fichas de ejercicios · rutinas · cueing · evaluaciones", font: HEAD, size: 22, color: GRAY })] }));
  out.push(image("d_anatomy", 4.6));
  out.push(new Paragraph({ spacing: { before: 400 }, children: [new TextRun({ text: "Preparado para Ethérea Pilates", font: HEAD, size: 22, color: NAVY, bold: true })] }));
  out.push(new Paragraph({ children: [new TextRun({ text: "Material de estudio complementario. No sustituye ni reproduce el material oficial del método TBM.", font: HEAD, size: 18, color: GRAY, italics: true })] }));
  return out;
}

function front() {
  const out = [];
  out.push(heading("Aviso importante", 1, { pageBreak: true }));
  out.push(...box({ kind: "seguridad", title: "Salud y seguridad", body: [
    { t: "p", x: "Este libro es educativo. Antes de comenzar un programa de ejercicio, consulta con un profesional de la salud, especialmente si tienes lesiones, embarazo, posparto reciente, enfermedad cardiovascular, hipertensión, diabetes u otra condición médica." },
    { t: "p", x: "Detén cualquier ejercicio ante dolor agudo, mareo, dolor en el pecho o falta de aire desproporcionada." }] }));
  out.push(...box({ kind: "oficial", title: "Relación con el método TBM", body: [
    { t: "p", x: "Los nombres de los módulos siguen exactamente el orden del programa proporcionado. Este libro desarrolla **fundamentos generales** de anatomía, ciencia del ejercicio, ballet, Pilates y diseño de clases. **No inventa ni reproduce contenido propietario del método TBM.** Cuando un tema requiere información oficial (historia y filosofía del método, formatos y coreografías oficiales, playlists, criterios de certificación) se indica con este recuadro y una lista de lo que debes completar con el material oficial." },
    { t: "p", x: "Las rutinas de práctica son **propuestas didácticas**, no coreografías oficiales." }] }));
  out.push(heading("Cómo usar este libro", 2));
  out.push(P("El libro está dividido en tres partes —una por disciplina— que respetan el orden de módulos del programa. Cada módulo contiene objetivos, teoría con diagramas y tablas, fichas técnicas de ejercicios y una evaluación. Al final encontrarás glosario, solucionario, plantillas, rúbrica y referencias."));
  out.push(heading("Leyenda de recuadros", 3));
  const leg = [["general", "Fundamento general", "Definiciones y bases que provienen de la ciencia del ejercicio o del programa."],
    ["oficial", "Material oficial", "Lo que debes completar con el manual o la capacitación oficial del método TBM."],
    ["seguridad", "Seguridad", "Precauciones, contraindicaciones y señales de alarma."],
    ["cue", "Cue clave", "Indicación verbal modelo para enseñar."], ["tip", "Dato útil", "Mitos, matices y consejos prácticos."],
    ["practica", "Práctica", "Ejercicios para ti como estudiante o futura instructora."]];
  const widths = scaleWidths([1.4, 1.5, 3.6]);
  out.push(new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths, rows: leg.map(([k, t, d]) => new TableRow({ children: [
    cell(BOX[k].label, widths[0], { fill: BOX[k].fill, color: BOX[k].bar, bold: true, size: 15 }), cell(t, widths[1], { bold: true, size: 18 }), cell(d, widths[2], { size: 18 })] })) }));
  out.push(new Paragraph({ spacing: { after: 160 }, children: [] }));
  out.push(heading("Cómo leer una ficha técnica", 3));
  out.push(...olist(["**Figura:** posición inicial → final (la pierna o brazo más claro es el del lado lejano).",
    "**Mapa muscular:** rojo = músculos principales; salmón = secundarios o estabilizadores; la línea discontinua en el abdomen indica el transverso.",
    "**Tabla:** objetivo, posición inicial, ejecución paso a paso, respiración, músculos, errores frecuentes (✗), regresión (▼), progresión (▲), dosificación y cue clave."]));
  out.push(heading("Índice", 1, { pageBreak: true }));
  out.push(new TableOfContents("Índice", { hyperlink: true, headingStyleRange: "1-3" }));
  return out;
}

const ROMAN = ["I", "II", "III", "IV"];

function partSection(part, idx) {
  const ch = [];
  ch.push(new Paragraph({ spacing: { before: 2000, after: 0 }, children: [new TextRun({ text: `PARTE ${ROMAN[idx]}`, font: HEAD, size: 28, bold: true, color: GOLD, characterSpacing: 80 })] }));
  ch.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 60, after: 300 }, children: [new TextRun({ text: part.title, size: 64 })] }));
  ch.push(...box({ kind: "general", title: `¿Qué es ${part.title}?`, body: [{ t: "p", x: part.intro }] }));
  ch.push(new Paragraph({ spacing: { before: 200, after: 80 }, children: [new TextRun({ text: "Estructura de esta parte", bold: true, font: HEAD, size: 24, color: NAVY })] }));
  const rows = part.modules.map((m) => [`Módulo ${m.num}`, m.topics.map((t) => t.title).join(" · ")]);
  ch.push(...table({ head: ["Módulo", "Temas (en el orden del programa)"], rows, widths: [1.1, 5.4] }));
  part.modules.forEach((m) => {
    ch.push(new Paragraph({ heading: HeadingLevel.HEADING_2, pageBreakBefore: true, children: [new TextRun({ text: `Módulo ${m.num}` })] }));
    ch.push(new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: m.topics.map((t) => t.title).join("  ·  "), font: HEAD, size: 22, color: TEAL, bold: true })] }));
    ch.push(...box({ kind: "tip", title: "Objetivos de aprendizaje", body: [{ t: "ul", items: m.objectives }] }));
    m.topics.forEach((tp) => {
      ch.push(heading(tp.title, 3));
      tp.blocks.forEach((b) => ch.push(...renderBlock(b)));
    });
    ch.push(...quiz(m));
  });
  return ch;
}

function appendixSection() {
  const ch = [];
  book.appendix.forEach((a, i) => {
    ch.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: i > 0, children: [new TextRun(a.title)] }));
    a.blocks.forEach((b) => ch.push(...renderBlock(b)));
  });
  return ch;
}

function hdr(label) {
  return new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD, space: 4 } },
    children: [new TextRun({ text: "Manual de formación  ·  ", size: 16, color: GRAY, font: HEAD }), new TextRun({ text: label, size: 16, color: NAVY, bold: true, font: HEAD })] })] });
}
const ftr = () => new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
  children: [new TextRun({ children: [PageNumber.CURRENT], size: 17, color: GRAY, font: HEAD })] })] });

const page = { size: { width: 12240, height: 15840 }, margin: { top: 1300, bottom: 1200, left: 1440, right: 1440, header: 600, footer: 600 } };

const sections = [
  { properties: { page, titlePage: true }, children: [...cover(), ...front()], headers: { default: hdr("Preliminares"), first: new Header({ children: [] }) }, footers: { default: ftr(), first: new Footer({ children: [] }) } },
  ...book.parts.map((p, i) => ({ properties: { page }, headers: { default: hdr(p.title) }, footers: { default: ftr() }, children: partSection(p, i) })),
  { properties: { page }, headers: { default: hdr("Apéndices") }, footers: { default: ftr() }, children: appendixSection() },
];

const doc = new Document({
  creator: "Ethérea Pilates", title: "Manual de formación: Sculpt & Burn, Barre y Block Burn Pilates",
  description: "Guía de estudio para aprendizaje personal desde cero",
  features: { updateFields: true },
  numbering: { config: numberingConfigs },
  styles: {
    default: { document: { run: { font: BODY, size: 21, color: INK } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD, size: 44, bold: true, color: NAVY }, paragraph: { spacing: { before: 240, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD, size: 40, bold: true, color: NAVY }, paragraph: { spacing: { before: 120, after: 60 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD, size: 30, bold: true, color: NAVY },
        paragraph: { spacing: { before: 360, after: 140 }, outlineLevel: 2, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD, space: 4 } } } },
      { id: "Heading4", name: "Heading 4", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD, size: 24, bold: true, color: "8A6A3A" }, paragraph: { spacing: { before: 220, after: 80 }, outlineLevel: 3 } },
    ],
  },
  sections,
});

Packer.toBuffer(doc).then((buf) => { fs.mkdirSync(path.dirname(OUT), { recursive: true }); fs.writeFileSync(OUT, buf); console.log("OK", OUT, (buf.length / 1e6).toFixed(1) + " MB"); });
