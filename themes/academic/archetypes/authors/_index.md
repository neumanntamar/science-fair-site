---
# Display name
name: "{{ .Site.Data.submission.author | title }}"

# Username (this should match the folder name and the name on publications)
authors:
- Name "{{ .Site.Data.submission.author | title }}"

# Is this the primary user of the site?
superuser: false

# Role/position (e.g., Professor of Artificial Intelligence)
role: {{.Site.Data.submission.title}}

# Name of team at Cigna/ESI
teamName: {{.Site.Data.submission.teamName}}

# Short bio (displayed in user profile at end of posts)
bio: "{{.Site.Data.submission.biography}}"

# Contact Info
email: "{{.Site.Data.submission.email}}"
---
