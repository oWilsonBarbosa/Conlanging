# `pdf-ocr`

Recupera texto de PDFs que são **só imagem**, sem depender de um renderizador
externo (poppler/`pdftoppm`) — que não está disponível neste ambiente.

## O problema

Alguns dos artigos do corpus são digitalizações sem camada de texto. É fácil se
enganar aqui: o arquivo declara fontes em `/Resources` e um leitor de PDF pode
fazer OCR ao vivo e *parecer* que há texto selecionável. O diagnóstico
definitivo é olhar o fluxo de conteúdo da página:

```
q
829.44 0 0 660.48 0 0 cm
/Im0 Do
Q
```

Trinta e sete bytes. Desenha uma imagem e nada mais — nenhum operador `Tj` ou
`TJ`. A fonte Helvetica declarada nunca é usada; é resíduo do software do
scanner. `pdfminer.six` e `pypdf` devolvem zero caracteres, corretamente.

## A solução

As imagens são **CCITT G4**, que é o mesmo codec da compressão TIFF 4. Dá para
extrair o fluxo bruto e envelopá-lo num TIFF mínimo montado à mão, sem
descomprimir nada, e entregar direto ao `tesseract`.

```bash
python3 ocr_ccitt.py entrada.pdf saida.txt [lang]
```

Requisitos: `tesseract` no PATH e `pypdf`. Sem Pillow, sem poppler.

## Qualidade

Boa o suficiente para leitura e citação. Erros típicos de OCR em fonte
serifada — `*h,` por `*h₁`, `Tibingen` por `Tübingen`, `A;` por `h₂` — então
**confira qualquer citação literal contra a imagem** antes de tratá-la como
canônica. Diacríticos de transliteração (`ḫ`, `š`, `ā`) sofrem bastante.
