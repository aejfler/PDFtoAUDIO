from gtts import gTTS
import PyPDF2

pdf_file = open('the little prince.pdf', 'rb')
audio_file = open('audio_doc.mp3', 'wb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

for page in range(len(pdf_reader.pages)):
    page_content = pdf_reader.pages[page].extract_text()
    tts = gTTS(page_content, lang='en', slow=False)
    # code below enables to convert all text per page in one file
    tts.write_to_fp(audio_file)

pdf_file.close()
