import urllib.request
import urllib.error
import PyPDF2

url = "https://dspace.hansung.ac.kr/bitstream/2024.oak/7612/2/200000806828.pdf"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open("temp.pdf", 'wb') as out_file:
        out_file.write(response.read())

    with open("temp.pdf", "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(len(reader.pages)):
            text = reader.pages[i].extract_text()
            if text and "어려움" in text and "전환" in text:
                print(f"--- Page {i+1} ---")
                print(text)
except Exception as e:
    print(f"Error: {e}")
