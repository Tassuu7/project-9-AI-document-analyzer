"""Native Pure-Python OpenXML DOCX Document Builder."""
import io
import zipfile
import xml.sax.saxutils as saxutils
from typing import List, Dict, Any, Optional

class DocxBuilder:
    """Builds valid Microsoft Word .docx files using pure Python standard library zipfile and XML."""

    @classmethod
    def create_document_bytes(cls, title: str, paragraphs: List[Dict[str, Any]]) -> bytes:
        """
        paragraphs: List of dicts with keys:
            - type: "heading_1", "heading_2", "heading_3", "paragraph", "bullet", "table"
            - text: str
            - bold: bool (optional)
            - italic: bool (optional)
            - rows: List[List[str]] (for table type)
        """
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as docx:
            # 1. [Content_Types].xml
            docx.writestr("[Content_Types].xml", cls._get_content_types_xml())

            # 2. _rels/.rels
            docx.writestr("_rels/.rels", cls._get_root_rels_xml())

            # 3. word/_rels/document.xml.rels
            docx.writestr("word/_rels/document.xml.rels", cls._get_doc_rels_xml())

            # 4. word/styles.xml
            docx.writestr("word/styles.xml", cls._get_styles_xml())

            # 5. word/document.xml
            docx.writestr("word/document.xml", cls._build_document_xml(title, paragraphs))

        buffer.seek(0)
        return buffer.getvalue()

    @classmethod
    def text_to_docx_bytes(cls, full_text: str, title: str = "Document Analysis & Export") -> bytes:
        """Converts raw text with paragraphs and headings into a DOCX document."""
        paragraphs = []
        raw_paras = full_text.split("\n")
        for line in raw_paras:
            clean = line.strip()
            if not clean:
                continue
            if clean.startswith("# "):
                paragraphs.append({"type": "heading_1", "text": clean[2:].strip()})
            elif clean.startswith("## "):
                paragraphs.append({"type": "heading_2", "text": clean[3:].strip()})
            elif clean.startswith("### "):
                paragraphs.append({"type": "heading_3", "text": clean[4:].strip()})
            elif clean.startswith("- ") or clean.startswith("* "):
                paragraphs.append({"type": "bullet", "text": clean[2:].strip()})
            else:
                paragraphs.append({"type": "paragraph", "text": clean})
        return cls.create_document_bytes(title, paragraphs)

    @classmethod
    def _build_document_xml(cls, title: str, paragraphs: List[Dict[str, Any]]) -> str:
        body_xml = []

        # Title
        if title:
            body_xml.append(f"""
            <w:p>
                <w:pPr><w:pStyle w:val="Title"/><w:jc w:val="center"/></w:pPr>
                <w:r><w:rPr><w:b/><w:sz w:val="48"/></w:rPr><w:t>{saxutils.escape(title)}</w:t></w:r>
            </w:p>
            """)

        for p in paragraphs:
            ptype = p.get("type", "paragraph")
            text = saxutils.escape(p.get("text", ""))

            if ptype == "heading_1":
                body_xml.append(f"""
                <w:p>
                    <w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
                    <w:r><w:rPr><w:b/><w:sz w:val="36"/></w:rPr><w:t>{text}</w:t></w:r>
                </w:p>
                """)
            elif ptype == "heading_2":
                body_xml.append(f"""
                <w:p>
                    <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
                    <w:r><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:t>{text}</w:t></w:r>
                </w:p>
                """)
            elif ptype == "heading_3":
                body_xml.append(f"""
                <w:p>
                    <w:pPr><w:pStyle w:val="Heading3"/></w:pPr>
                    <w:r><w:rPr><w:b/><w:sz w:val="24"/></w:rPr><w:t>{text}</w:t></w:r>
                </w:p>
                """)
            elif ptype == "bullet":
                body_xml.append(f"""
                <w:p>
                    <w:pPr><w:pStyle w:val="ListBullet"/></w:pPr>
                    <w:r><w:t>&bull; {text}</w:t></w:r>
                </w:p>
                """)
            elif ptype == "table":
                rows_xml = []
                for row in p.get("rows", []):
                    cells_xml = []
                    for cell in row:
                        cell_text = saxutils.escape(str(cell))
                        cells_xml.append(f"""
                        <w:tc>
                            <w:tcPr><w:tcW w:w="2500" w:type="dxa"/></w:tcPr>
                            <w:p><w:r><w:t>{cell_text}</w:t></w:r></w:p>
                        </w:tc>
                        """)
                    rows_xml.append(f"<w:tr>{''.join(cells_xml)}</w:tr>")
                body_xml.append(f"""
                <w:tbl>
                    <w:tblPr><w:tblBorders><w:top w:val="single" w:sz="4"/><w:left w:val="single" w:sz="4"/><w:bottom w:val="single" w:sz="4"/><w:right w:val="single" w:sz="4"/><w:insideH w:val="single" w:sz="4"/><w:insideV w:val="single" w:sz="4"/></w:tblBorders></w:tblPr>
                    {''.join(rows_xml)}
                </w:tbl>
                """)
            else:
                body_xml.append(f"""
                <w:p>
                    <w:pPr><w:spacing w:after="160" w:line="276" w:lineRule="auto"/></w:pPr>
                    <w:r><w:t>{text}</w:t></w:r>
                </w:p>
                """)

        body_content = "\n".join(body_xml)
        return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
    <w:body>
        {body_content}
        <w:sectPr>
            <w:pgSz w:w="12240" w:h="15840"/>
            <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>
        </w:sectPr>
    </w:body>
</w:document>"""

    @classmethod
    def _get_content_types_xml(cls) -> str:
        return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
    <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

    @classmethod
    def _get_root_rels_xml(cls) -> str:
        return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    @classmethod
    def _get_doc_rels_xml(cls) -> str:
        return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

    @classmethod
    def _get_styles_xml(cls) -> str:
        return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:docDefaults>
        <w:rPrDefault>
            <w:rPr>
                <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>
                <w:sz w:val="22"/>
                <w:szCs w:val="22"/>
                <w:lang w:val="en-US"/>
            </w:rPr>
        </w:rPrDefault>
    </w:docDefaults>
    <w:style w:type="paragraph" w:styleId="Normal" w:default="1">
        <w:name w:val="Normal"/>
    </w:style>
    <w:style w:type="paragraph" w:styleId="Heading1">
        <w:name w:val="heading 1"/>
        <w:rPr><w:b/><w:sz w:val="36"/></w:rPr>
    </w:style>
    <w:style w:type="paragraph" w:styleId="Heading2">
        <w:name w:val="heading 2"/>
        <w:rPr><w:b/><w:sz w:val="28"/></w:rPr>
    </w:style>
    <w:style w:type="paragraph" w:styleId="Heading3">
        <w:name w:val="heading 3"/>
        <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
    </w:style>
</w:styles>"""
