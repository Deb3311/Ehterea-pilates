"""Abre el .docx en LibreOffice, actualiza el índice y exporta .docx final y .pdf."""
import os
import subprocess
import sys
import time

import uno
from com.sun.star.beans import PropertyValue

src, out_docx, out_pdf = [os.path.abspath(a) for a in sys.argv[1:4]]


def prop(n, v):
    p = PropertyValue()
    p.Name, p.Value = n, v
    return p


port = 2002
proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--nologo", "--norestore",
                         f"--accept=socket,host=localhost,port={port};urp;"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
local = uno.getComponentContext()
resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
for _ in range(60):
    try:
        ctx = resolver.resolve(f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext")
        break
    except Exception:
        time.sleep(1)
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(src), "_blank", 0, (prop("Hidden", True),))
idx = doc.getDocumentIndexes()
for _ in range(2):  # dos pasadas: los números de página se estabilizan
    for i in range(idx.getCount()):
        idx.getByIndex(i).update()
    doc.refresh()
print("índices:", idx.getCount(), "páginas:", doc.getCurrentController().getPropertyValue("PageCount"))
doc.storeToURL(uno.systemPathToFileUrl(out_docx), (prop("FilterName", "MS Word 2007 XML"),))
doc.storeToURL(uno.systemPathToFileUrl(out_pdf), (prop("FilterName", "writer_pdf_Export"),
                                                    prop("FilterData", uno.Any("[]com.sun.star.beans.PropertyValue", tuple([
                                                        prop("ExportBookmarks", True), prop("UseLosslessCompression", False),
                                                        prop("Quality", 92), prop("ReduceImageResolution", False)])))))
doc.close(True)
try:
    desktop.terminate()
except Exception:
    pass
proc.wait(timeout=30)
