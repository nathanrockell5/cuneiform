from cuneiform import DocxTemplate

tpl = DocxTemplate("templates/comments_tpl.docx")

tpl.render({})
tpl.save("output/comments.docx")
