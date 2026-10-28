# Manual de formación: Sculpt & Burn · Barre · Block Burn Pilates

Libro de estudio (aprendizaje personal desde cero) con los 28 módulos en el orden del programa,
147 fichas técnicas de ejercicios, diagramas anatómicos, tablas, rutinas y evaluaciones con solucionario.

## Archivos finales
- `dist/Manual_Sculpt_Barre_BlockBurn.docx` — Word editable (al abrirlo, Word ofrece actualizar el índice: responde «Sí»).
- `dist/Manual_Sculpt_Barre_BlockBurn.pdf` — PDF tamaño carta listo para imprimir.

## Regenerar
```bash
python3 src/build.py --force      # figuras + build/book.json (requiere matplotlib)
node src/build_docx.js            # Word (requiere el paquete npm docx)
python3 src/finalize.py dist/Manual_Sculpt_Barre_BlockBurn.docx build/lo.docx dist/Manual_Sculpt_Barre_BlockBurn.pdf  # índice + PDF (LibreOffice)
```

El contenido vive en `src/sculpt_*.py`, `src/barre_*.py`, `src/block_*.py` y `src/appendix.py`.
Los temas que dependen del material oficial del método TBM están marcados con el recuadro «Material oficial».

---

# Manual de estudio: Pilates Reformer — Repertorio clásico

- `dist/Manual_Pilates_Reformer.docx` — Word editable.
- `dist/Manual_Pilates_Reformer.pdf` — PDF listo para imprimir.

12 módulos en 3 partes (Fundamentos, Repertorio clásico, Enseñanza), 48 fichas con el ejercicio dibujado sobre el reformer,
resortes y montaje orientativos, evaluaciones y apéndices.

```bash
python3 src/build_reformer.py
node src/build_docx.js build/reformer.json dist/Manual_Pilates_Reformer.docx
python3 src/finalize.py dist/Manual_Pilates_Reformer.docx build/lo_rf.docx dist/Manual_Pilates_Reformer.pdf
```
