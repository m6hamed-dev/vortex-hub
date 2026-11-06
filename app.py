from flask import Flask, request, session, redirect, send_file
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = 'vortex_ultimate_2006'
PASSWORD = "2006"

if not os.path.exists('files'):
    os.makedirs('files')

@app.route('/', methods=['GET', 'POST'])
def main():
    if not session.get('ok'):
        err = ""
        if request.method == 'POST':
            if request.form.get('pass') == PASSWORD:
                session['ok'] = True
                return redirect('/')
            else:
                err = "كلمة السر خطأ!"
        return f'''
        <html dir="rtl">
        <head><title>Vortex Hub - Login</title></head>
        <body style="background:#090d16; color:#fff; font-family:Tahoma; text-align:center; padding-top:100px; margin:0;">
            <div style="background:#111827; max-width:340px; margin:auto; padding:35px; border-radius:14px; border:1px solid #1f2937; box-shadow:0 10px 25px rgba(0,0,0,0.7);">
                <h2 style="color:#38bdf8; margin-top:0;">Vortex Ultimate Hub</h2>
                <p style="color:#9ca3af; font-size:13px;">أدخل كلمة السر الخاصة للوصول للأداة</p>
                <form method="POST">
                    <input type="password" name="pass" placeholder="الباسورد (2006)" style="width:100%; padding:12px; margin:12px 0; background:#030712; color:#fff; border:1px solid #374151; text-align:center; border-radius:8px; outline:none; font-size:16px;" required>
                    <button style="width:100%; padding:12px; background:#0284c7; color:#fff; border:none; font-weight:bold; border-radius:8px; cursor:pointer; font-size:15px;">دخول النظام</button>
                    <p style="color:#ef4444; font-size:14px; margin-top:10px;">{err}</p>
                </form>
            </div>
        </body>
        </html>
        '''

    return '''
    <html dir="rtl">
    <head><title>Vortex Ultimate Hub</title></head>
    <body style="background:#090d16; color:#fff; font-family:Tahoma; padding:15px; margin:0;">
        <div style="max-width:550px; margin:auto; background:#111827; padding:25px; border-radius:14px; border:1px solid #1f2937; box-shadow: 0 15px 30px rgba(0,0,0,0.6);">
            
            <!-- شريط العنوان -->
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1f2937; padding-bottom:12px; margin-bottom:20px;">
                <h2 style="margin:0; color:#38bdf8; font-size:20px;">⚡ Vortex Ultimate Hub</h2>
                <span style="font-size:12px; background:#065f46; color:#34d399; padding:5px 10px; border-radius:6px; font-weight:bold;">متصل 24/7 سحابياً</span>
            </div>
            
            <!-- قسم التحميل والترجمة -->
            <div style="background:#030712; padding:18px; border-radius:10px; margin-bottom:20px; border:1px solid #1f2937;">
                <h4 style="margin:0 0 12px 0; color:#10b981; font-size:16px;">📥 التحميل والترجمة العربية الفورية</h4>
                <form action="/get" method="POST">
                    <input type="text" name="link" placeholder="الصق الرابط هنا (يوتيوب، تيك توك، فيسبوك)..." style="width:100%; padding:12px; margin-bottom:12px; background:#111827; color:#fff; border:1px solid #374151; border-radius:8px; outline:none; font-size:14px;" required>
                    <select name="kind" style="width:100%; padding:12px; margin-bottom:12px; background:#111827; color:#fff; border:1px solid #374151; border-radius:8px; outline:none; font-size:14px;">
                        <option value="vid">فيديو عادي (جودة عالية)</option>
                        <option value="sub_ar">🎬 فيديو مع ترجمة عربية (أفلام أجنبية)</option>
                        <option value="mp3">صوت MP3 فقط (أغاني، قرآن)</option>
                    </select>
                    <button style="width:100%; padding:12px; background:#10b981; color:#fff; border:none; font-weight:bold; border-radius:8px; cursor:pointer; font-size:15px;">بدء التحميل والترجمة</button>
                </form>
            </div>

            <!-- قسم المتصفح والمنصات السريعة -->
            <div style="background:#030712; padding:18px; border-radius:10px; border:1px solid #1f2937;">
                <h4 style="margin:0 0 12px 0; color:#f59e0b; font-size:16px;">🌐 المتصفح السريع والمنصات الترفيهية</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                    <a href="https://www.tiktok.com" target="_blank" style="background:#1f2937; color:#fff; padding:12px; text-decoration:none; text-align:center; border-radius:8px; font-size:14px; font-weight:bold;">🎵 تيك توك</a>
                    <a href="https://m.youtube.com" target="_blank" style="background:#1f2937; color:#fff; padding:12px; text-decoration:none; text-align:center; border-radius:8px; font-size:14px; font-weight:bold;">📺 يوتيوب</a>
                    <a href="https://m.facebook.com" target="_blank" style="background:#1f2937; color:#fff; padding:12px; text-decoration:none; text-align:center; border-radius:8px; font-size:14px; font-weight:bold;">👥 فيسبوك</a>
                    <a href="https://www.instagram.com" target="_blank" style="background:#1f2937; color:#fff; padding:12px; text-decoration:none; text-align:center; border-radius:8px; font-size:14px; font-weight:bold;">📸 انستغرام</a>
                    <a href="https://x.com" target="_blank" style="background:#1f2937; color:#fff; padding:12px; text-decoration:none; text-align:center; border-radius:8px; font-size:14px; font-weight:bold;">💬 منصة X</a>
                    <a href="https://www.google.com" target="_blank" style="background:#1f2937; color:#fff; padding:12px; text-decoration:none; text-align:center; border-radius:8px; font-size:14px; font-weight:bold;">🔍 محرك جوجل</a>
                </div>
            </div>
            
            <p style="text-align:center; color:#6b7280; font-size:12px; margin-top:20px;">تم التطوير بواسطة محمد فريد - مخصص لعائلة فريد 💙</p>
        </div>
    </body>
    </html>
    '''

@app.route('/get', methods=['POST'])
def get_file():
    if not session.get('ok'): return redirect('/')
    link = request.form.get('link')
    kind = request.form.get('kind')
    
    opts = {'outtmpl': 'files/%(title)s.%(ext)s'}
    
    if kind == 'mp3':
        opts['format'] = 'bestaudio/best'
        opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
    elif kind == 'sub_ar':
        opts['format'] = 'best[height<=360]'
        opts['writesubtitles'] = True
        opts['writeautomaticsub'] = True
        opts['subtitleslangs'] = ['ar']
        opts['postprocessors'] = [{'key': 'FFmpegEmbedSubtitle'}]
    else:
        opts['format'] = 'best[height<=360]'
    
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(link, download=True)
            f = ydl.prepare_filename(info)
            if kind == 'mp3': 
                f = os.path.splitext(f)[0] + '.mp3'
            elif kind == 'sub_ar':
                f = os.path.splitext(f)[0] + '.mkv' if os.path.exists(os.path.splitext(f)[0] + '.mkv') else f
        return send_file(f, as_attachment=True)
    except Exception as e:
        return f"خطأ أثناء التحميل: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)