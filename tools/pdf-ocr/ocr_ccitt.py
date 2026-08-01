"""OCR de PDFs que são só imagem CCITT G3/G4, sem renderizador externo.

Extrai o fluxo CCITT de cada página, envelopa num TIFF mínimo (o codec é o
mesmo: CCITT G4 = compressão TIFF 4) e passa ao tesseract.
"""
import struct, subprocess, sys, warnings, pathlib
warnings.filterwarnings("ignore")
import pypdf

def tiff_wrap(data, width, height, k):
    comp = 4 if k < 0 else (3 if k > 0 else 2)      # G4 / G3-2D / G3-1D
    tags = [
        (256, 3, 1, width), (257, 3, 1, height), (258, 3, 1, 1),
        (259, 3, 1, comp),  (262, 3, 1, 0),      (273, 4, 1, 8 + 2 + 12 * 9 + 4),
        (277, 3, 1, 1),     (278, 3, 1, height), (279, 4, 1, len(data)),
    ]
    out = bytearray(b"II*\x00" + struct.pack("<I", 8))
    out += struct.pack("<H", len(tags))
    for tag, typ, cnt, val in sorted(tags):
        out += struct.pack("<HHI", tag, typ, cnt)
        out += struct.pack("<I", val) if typ == 4 else struct.pack("<HH", val, 0)
    out += struct.pack("<I", 0)
    out += data
    return bytes(out)


def ocr_pdf(path, out_txt, lang="eng"):
    reader = pypdf.PdfReader(path)
    chunks = []
    for i, page in enumerate(reader.pages):
        xo = (page.get("/Resources", {}) or {}).get("/XObject")
        if not xo:
            continue
        for name in xo.keys():
            img = xo[name].get_object()
            if img.get("/Filter") != "/CCITTFaxDecode":
                continue
            parms = img.get("/DecodeParms") or {}
            w = int(img["/Width"]); h = int(img["/Height"])
            k = int(parms.get("/K", 0))
            tif = tiff_wrap(img._data, w, h, k)
            p = subprocess.run(
                ["tesseract", "stdin", "stdout", "-l", lang, "--psm", "1"],
                input=tif, capture_output=True)
            txt = p.stdout.decode("utf-8", "replace")
            chunks.append(f"\n\n=== [p.{i+1}] ===\n{txt}")
        print(f"  p.{i+1}/{len(reader.pages)}", end="\r", file=sys.stderr)
    text = "".join(chunks)
    pathlib.Path(out_txt).write_text(text)
    return len(text)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    lang = sys.argv[3] if len(sys.argv) > 3 else "eng"
    n = ocr_pdf(src, dst, lang)
    print(f"{n:8d} chars -> {dst}")
