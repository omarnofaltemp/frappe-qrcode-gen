import frappe
import pyqrcode
from frappe.utils import get_url

@frappe.whitelist()
def gen_qrcode(doctype,name,print_format):
    key = str(frappe.get_doc(doctype, name).get_signature())
    url = str(get_url()) + "/" + doctype + "/" + str(name) + "?format=" + str(print_format) + "&key=" + key

    data = pyqrcode.create(url)
    
    return f'data:image/png;base64,{data.png_as_base64_str(scale=5)}'
