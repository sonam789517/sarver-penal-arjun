from flask import Flask, render_template_string

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>【🌹🦋𝐎𝐅𝐅𝐋𝐈𝐍𝐄 𝐀𝐋𝐋 𝐒𝐀𝐑𝐕𝐄𝐑 𝐀𝐑𝐉𝐔𝐍 𝐓𝐇𝐀𝐊𝐔𝐑 𝐖𝐄𝐁🦋🌹】</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"/>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: "Poppins", sans-serif;
      background-color: #ffcc;
      color: black;
      padding: 20px;
    }
    h1, h2, h3, h4 {
      text-align: center;
      color: black;
      margin-bottom: 15px;
    }
    .image-container {
      width: 330px;
      height: 200px;
      margin: 20px auto;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
      border-radius: 10px;
      overflow: hidden;
      animation: fadeIn 1.5s ease;
    }
    .image {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .button-34 {
      display: block;
      margin: 12px auto;
      padding: 10px 20px;
      background: black;
      color: white;
      border: none;
      border-radius: 999px;
      font-weight: bold;
      cursor: pointer;
      font-size: 16px;
      text-align: center;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      animation: fadeIn 1.5s ease;
    }
    .button-34:hover {
      background: #333;
      transform: scale(1.05);
      box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .button-34:active {
      animation: pulse 0.3s ease;
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(0.95); }
      100% { transform: scale(1); }
    }
    .footer {
      text-align: center;
      margin-top: 40px;
      font-size: 14px;
    }
    .footer a {
      color: black;
      margin: 0 5px;
      text-decoration: underline;
    }
    .footer i {
      margin: 0 8px;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
<h2>🎋 【🌹🦋𝐎𝐅𝐅𝐋𝐈𝐍𝐄 𝐒𝐀𝐑𝐕𝐄𝐑 𝐏𝐄𝐍𝐀𝐋🦋❤️】 🎋</h2>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <h3>⊲ 【🦋🌹𝐂𝐎𝐍𝐓𝐑𝐀𝐂𝐓 𝐎𝐖𝐍𝐄𝐑 𝐀𝐑𝐉𝐔𝐍 𝐓𝐇𝐀𝐊𝐔𝐑 🌹🦋】⊳ 【❤️𝐌𝐘 𝐁𝐑𝐎𝐓𝐇𝐄𝐑 𝐋𝐎𝐄 𝐘𝐎𝐔 𝐅𝐔𝐋𝐋 𝐈𝐍𝐉𝐎𝐘❤️】</h3>
  <button class="button-34" onclick="window.location.href='https://wa.me/+917543864'">⊲ CONTACT OWNER CLICK HERE ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='http://fi2.bot-hosting.net:20855'">⊲ CONVO+POST+TOKEN CHKER+PASS-Hassan123 ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='http://fi2.bot-hosting.net:21328'">⊲ ID SEYSHTM CHEK+TOKEN CHKER  ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='http://fi4.bot-hosting.net:21777'">⊲ CONVO MULTI TOKEN SARVER ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='http://fi1.bot-hosting.net:5278'">⊲ POST SARVER TOKEN+COOKIES ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='http://fi7.bot-hosting.net:20397'">⊲ CONVO SINGAL TOKEN SARVER ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='http://page-uid-sarver.onrender.com/'">⊲ PAGE TOKEN+GROUP UID ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='http://wp-sarver-arjun1-1.onrender.com/'">⊲ WHATSAPP SARVER ⊳</button>

  <div class="image-container">
    <img src="https://i.ibb.co/BHk1RJGN/1759735913212.jpg" class="image">
  </div>
  <button class="button-34" onclick="window.location.href='https://arjun-ka-bot.onrender.com/'">⊲ GRUPNAME LOCKER BOT ⊳</button>

  <div class="footer">
    <p>
      <a href="/terms">Terms</a> |
      <a href="/privacy">Privacy</a>
    </p>
    <p>
      <a href="https://www.facebook.com/profile.php?id=61574766235"><i class="fab fa-facebook"></i></a>
      <a href="https://wa.me/+917209105433"><i class="fab fa-whatsapp"></i></a>
      <a href="https://github.com/devixayyat/"><i class="fab fa-github"></i></a>
    </p>
    <p>© 2025 【🌹𝐀𝐑𝐉𝐔𝐍 𝐓𝐇𝐀𝐊𝐔𝐑🌹】All RIGHTS RESERVED.</p>
    <p> 【❤️🦋𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐑𝐉𝐔𝐍 𝐓𝐇𝐀𝐊𝐔𝐑 𝐁𝐘❤️🦋】</a></p>
  </div>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
