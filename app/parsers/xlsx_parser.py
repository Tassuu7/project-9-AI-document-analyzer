"""Pure-Python OpenXML Excel Spreadsheet Parser (.xlsx)."""
import zipfile
import io
import xml.etree.ElementTree as ET
from typing import Dict, Any, List

class XLSXParser:
    @classmethod
    def parse_bytes(cls, file_bytes: bytes) -> Dict[str, Any]:
        try:
            with zipfile.ZipFile(io.BytesIO(file_bytes)) as zf:
                # 1. Read shared strings
                shared_strings = []
                if "xl/sharedStrings.xml" in zf.namelist():
                    tree = ET.fromstring(zf.read("xl/sharedStrings.xml"))
                    for si in tree.findall("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si"):
                        t = si.find("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")
                        shared_strings.append(t.text if t is not None and t.text else "")

                # 2. Read sheet1.xml
                sheet_data = []
                sheet_path = "xl/worksheets/sheet1.xml"
                if sheet_path in zf.namelist():
                    tree = ET.fromstring(zf.read(sheet_path))
                    rows_xml = tree.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row")
                    for r in rows_xml:
                        row_vals = []
                        for c in r.findall("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c"):
                            t_attr = c.get("t")
                            v = c.find("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v")
                            val = v.text if v is not None and v.text else ""
                            if t_attr == "s" and val.isdigit():
                                idx = int(val)
                                val = shared_strings[idx] if idx < len(shared_strings) else val
                            row_vals.append(val)
                        sheet_data.append(row_vals)

                if not sheet_data:
                    return {"clean_text": "", "headers": [], "rows": [], "row_count": 0, "column_count": 0, "tables": []}

                headers = sheet_data[0]
                rows = sheet_data[1:]
                text_repr = "\n".join(["\t".join(r) for r in sheet_data[:100]])
                
                return {
                    "clean_text": text_repr,
                    "headers": headers,
                    "rows": rows,
                    "row_count": len(rows),
                    "column_count": len(headers),
                    "word_count": sum(len(r) for r in sheet_data),
                    "page_count": max(1, len(rows) // 40),
                    "tables": [{"name": "Worksheet 1", "headers": headers, "rows": rows[:200]}]
                }
        except Exception as e:
            return {"clean_text": f"Excel Workbook Extraction Error: {str(e)}", "headers": [], "rows": [], "row_count": 0, "column_count": 0, "error": str(e), "tables": []}
