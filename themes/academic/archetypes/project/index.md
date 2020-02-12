---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "{{ .Site.Data.submission.poster | title }}"
summary: "{{.Site.Data.submission.abstract}}"
authors: [{{replace .Site.Data.submission.author " " "_" | lower}}]
tags: [{{.Site.Data.submission.tags}}]
categories: []
date: {{ .Date }}

# Optional external URL for project (replaces project detail page).
external_link: ""

url_code: ""
url_slides: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---
<object data="{{.Site.Data.submission.pdf}}" type="application/pdf" width="100%" height="700px">
    <embed src="{{.Site.Data.submission.pdf}}">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="{{.Site.Data.submission.pdf}}" >Download PDF</a>.</p>
    </embed>
</object>

{{.Site.Data.submission.info}}