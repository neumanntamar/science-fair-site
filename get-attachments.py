import mailparser
import eml_parser
import json
import ast
import pickle
import shutil

emlFilePath = 'submissions/Test Submission.eml'
attachmentsFilePath = 'attachments'

with open(emlFilePath, 'rb') as fhdl:
    raw_email = fhdl.read()

parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email, include_raw_body=True)
emailBody = ast.literal_eval(json.dumps(parsed_eml['body'][0]['content'], indent=4))
authorName = emailBody.split('Author:')[1].split('Team Name:')[0].strip().replace(' ','_').lower()
posterTitle = emailBody.split('Poster Title:')[1].split('Short Bio:')[0].strip().replace(' ','_').lower()

mail = mailparser.parse_from_file(emlFilePath)

# Remove inline attachments from email
for index, item in enumerate(mail.attachments):
    if 'inline' in item['content-disposition']:
        mail.attachments.pop(index)

# Check for headshot by png extension and poster by pdf extension
for index, item in enumerate(mail.attachments):
    if 'png' in item['mail_content_type']:
        headshotFileName = item['filename']
    elif 'pdf' in item['mail_content_type']:
        posterFileName = item['filename']


mail.write_attachments('data/attachments')

shutil.copyfile(f'data/attachments/{headshotFileName}', f'content/authors/{authorName}/avatar.png')
shutil.copyfile(f'data/attachments/{posterFileName}', f'content/project/{posterTitle}/{posterFileName}')
shutil.rmtree('data/attachments')