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

{{.Site.Data.submission.info}}