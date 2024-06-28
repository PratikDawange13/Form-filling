from markdown_pdf import MarkdownPdf, Section

markdown_content = """
# This is a Title1
## This is a Title2
### This is a Title3

This is some text in markdown format.

* You can use bullet points.
* And even nesting.

---
#hello atish
Here's an image: ![Alt text](image.jpg)
"""


pdf = MarkdownPdf()
pdf.add_section(Section(markdown_content, toc=False))
pdf.save('output2.pdf')