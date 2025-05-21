from cuneiform import TypedDocxTemplate
import os
import json

tpl = TypedDocxTemplate(
    "/Users/nathanrockell/Dropbox/career/Rockell Group/cuneiform/cuneiform/tests/templates/cuneiform_template.docx")
print(tpl.get_typed_undeclared_template_variables(), indent=2)
