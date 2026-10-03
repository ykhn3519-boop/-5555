import os
from flask import Flask, request
import yt_dlp

app = Flask(__name__)

@app.route('/process_audio', methods=['GET', 'POST'])
def process_audio():
    # מקבל את הטקסט שהמאזין הקליש/אמר
    search_query = request.args.get('search_text', '').strip()
    
    # אם לא נשלח טקסט לחיפוש
    if not search_query:
        return "id_list_message=t-לא הוכנס טקסט לחיפוש"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{search_query}", download=False)
            if 'entries' in info and len(info['entries']) > 0:
                audio_url = info['entries'][0]['url']
                return f"playfile={audio_url}"
    except Exception as e:
        pass

    return "id_list_message=t-לא נמצאו תוצאות"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
