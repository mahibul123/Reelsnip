from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

HTML = """

<!DOCTYPE html>
<html>
<head>

<title>Reelsnip Offline Video Processor</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<script src="https://cdn.jsdelivr.net/npm/@ffmpeg/ffmpeg@0.12.6/dist/umd/ffmpeg.js"></script>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial;
}

body{
background:#0f172a;
color:white;
overflow:hidden;
}

.main{
display:flex;
height:100vh;
}

.sidebar{
width:280px;
background:#111827;
padding:20px;
overflow-y:auto;
border-right:2px solid #1e293b;
}

.logo{
font-size:28px;
font-weight:bold;
margin-bottom:30px;
color:#3b82f6;
}

.sidebar h2{
font-size:18px;
margin-bottom:20px;
}

.tool-btn{
width:100%;
padding:15px;
margin-bottom:12px;
border:none;
border-radius:15px;
background:#1e293b;
color:white;
font-size:16px;
cursor:pointer;
transition:0.3s;
text-align:left;
}

.tool-btn:hover{
background:#2563eb;
}

.content{
flex:1;
padding:25px;
overflow-y:auto;
}

.title{
font-size:48px;
font-weight:bold;
margin-bottom:25px;
}

.subtitle{
font-size:18px;
color:#60a5fa;
margin-left:10px;
}

.card{
background:#172554;
padding:22px;
border-radius:22px;
margin-bottom:25px;
}

label{
display:block;
margin-bottom:10px;
font-size:15px;
}

input,
select{
width:100%;
padding:14px;
border:none;
border-radius:12px;
background:#0f172a;
color:white;
font-size:15px;
margin-bottom:18px;
}

.range-box{
margin-bottom:20px;
}

.range-label{
margin-top:5px;
font-size:13px;
color:#cbd5e1;
}

input[type=range]{
padding:0;
}

.process-btn{
width:100%;
padding:16px;
background:#2563eb;
border:none;
border-radius:15px;
color:white;
font-size:18px;
font-weight:bold;
cursor:pointer;
transition:0.3s;
}

.process-btn:hover{
background:#1d4ed8;
}

video{
width:200px;
border-radius:15px;
margin-top:15px;
background:black;
}

.output-card{
display:inline-block;
width:220px;
background:#111827;
padding:15px;
margin:12px;
border-radius:18px;
vertical-align:top;
}

.output-card video,
.output-card audio{
width:100%;
border-radius:12px;
}

.download-btn{
display:block;
text-align:center;
margin-top:12px;
padding:12px;
background:#10b981;
border-radius:12px;
text-decoration:none;
color:white;
font-weight:bold;
}

.hidden{
display:none;
}

.loader{
display:none;
margin-top:20px;
padding:20px;
background:#111827;
border-radius:15px;
}

.progress{
width:100%;
height:15px;
background:#1e293b;
border-radius:20px;
overflow:hidden;
margin-top:15px;
}

.fill{
height:100%;
width:0%;
background:#3b82f6;
transition:0.3s;
}

</style>

</head>

<body>

<div class="main">

<div class="sidebar">

<div class="logo">
Reelsnip.com
</div>

<h2>🎬 PRO TOOLS</h2>

<button class="tool-btn" onclick="showTool('cutter')">
✂ Video Cutter
</button>

<button class="tool-btn" onclick="showTool('shorts')">
📱 Multiple Shorts
</button>

<button class="tool-btn" onclick="showTool('compress')">
⚡ Video Compress
</button>

<button class="tool-btn" onclick="showTool('reels')">
📲 Reels Resize
</button>

<button class="tool-btn" onclick="showTool('youtube')">
▶ YouTube Resize
</button>

<button class="tool-btn" onclick="showTool('mute')">
🔇 Remove Audio
</button>

<button class="tool-btn" onclick="showTool('mp3')">
🎵 Extract MP3
</button>

<button class="tool-btn" onclick="showTool('reverse')">
🔄 Reverse Video
</button>

<button class="tool-btn" onclick="showTool('speed')">
🚀 Speed Control
</button>

</div>

<div class="content">

<div class="title">
Ultimate Offline Video Processor
<span class="subtitle">
Made by Reelsnip.com
</span>
</div>

<input type="file" id="videoFile">

<video id="preview" controls></video>

<div class="loader" id="loader">

<h3 id="loaderText">
Loading FFmpeg...
</h3>

<div class="progress">
<div class="fill" id="fill"></div>
</div>

</div>

<!-- CUTTER -->

<div class="card tool-panel" id="cutter">

<h2>✂ Video Cutter</h2>

<div class="range-box">

<label>Start Time</label>

<input type="range" id="cutStart" min="0" max="300" value="0">

<div class="range-label" id="startLabel">
0 sec
</div>

</div>

<div class="range-box">

<label>End Time</label>

<input type="range" id="cutEnd" min="1" max="300" value="30">

<div class="range-label" id="endLabel">
30 sec
</div>

</div>

<select id="quality">

<option value="1080">Full HD 1080p</option>
<option value="720">HD 720p</option>
<option value="480">NON HD 480p</option>
<option value="360">LOW 360p</option>

</select>

<button class="process-btn" onclick="processVideo('cutter')">
🚀 Process Video
</button>

</div>

<!-- SHORTS -->

<div class="card tool-panel hidden" id="shorts">

<h2>📱 Multiple Shorts</h2>

<select id="shortDuration">

<option value="15">15 Seconds</option>
<option value="30">30 Seconds</option>
<option value="60">60 Seconds</option>

</select>

<button class="process-btn" onclick="processVideo('shorts')">
🚀 Create Shorts
</button>

</div>

<!-- COMPRESS -->

<div class="card tool-panel hidden" id="compress">

<h2>⚡ Compress Video</h2>

<select id="compressLevel">

<option value="23">Low Compression</option>
<option value="30">Medium Compression</option>
<option value="38">High Compression</option>

</select>

<button class="process-btn" onclick="processVideo('compress')">
🚀 Compress Video
</button>

</div>

<!-- REELS -->

<div class="card tool-panel hidden" id="reels">

<h2>📲 Reels Resize 9:16</h2>

<button class="process-btn" onclick="processVideo('reels')">
🚀 Convert Reels
</button>

</div>

<!-- YOUTUBE -->

<div class="card tool-panel hidden" id="youtube">

<h2>▶ YouTube Resize 16:9</h2>

<button class="process-btn" onclick="processVideo('youtube')">
🚀 Convert YouTube
</button>

</div>

<!-- MUTE -->

<div class="card tool-panel hidden" id="mute">

<h2>🔇 Remove Audio</h2>

<button class="process-btn" onclick="processVideo('mute')">
🚀 Remove Audio
</button>

</div>

<!-- MP3 -->

<div class="card tool-panel hidden" id="mp3">

<h2>🎵 Extract MP3</h2>

<button class="process-btn" onclick="processVideo('mp3')">
🚀 Extract MP3
</button>

</div>

<!-- REVERSE -->

<div class="card tool-panel hidden" id="reverse">

<h2>🔄 Reverse Video</h2>

<button class="process-btn" onclick="processVideo('reverse')">
🚀 Reverse Video
</button>

</div>

<!-- SPEED -->

<div class="card tool-panel hidden" id="speed">

<h2>🚀 Speed Control</h2>

<select id="speedValue">

<option value="0.5">0.5x Slow</option>
<option value="1">1x Normal</option>
<option value="2">2x Fast</option>

</select>

<button class="process-btn" onclick="processVideo('speed')">
🚀 Change Speed
</button>

</div>

<div id="results"></div>

</div>

</div>

<script>

const { FFmpeg } = FFmpegWASM

const ffmpeg = new FFmpeg()

let loaded = false

async function loadFFmpeg(){

if(loaded) return

document.getElementById("loader").style.display = "block"

await ffmpeg.load({

coreURL:"https://cdn.jsdelivr.net/npm/@ffmpeg/core@0.12.6/dist/umd/ffmpeg-core.js"

})

loaded = true

document.getElementById("loader").style.display = "none"

}

loadFFmpeg()

const preview = document.getElementById("preview")

const input = document.getElementById("videoFile")

input.onchange = ()=>{

const file = input.files[0]

preview.src = URL.createObjectURL(file)

}

function showTool(id){

document.querySelectorAll(".tool-panel").forEach(el=>{

el.classList.add("hidden")

})

document.getElementById(id).classList.remove("hidden")

}

document.getElementById("cutStart").oninput = function(){

document.getElementById("startLabel").innerText =
this.value + " sec"

}

document.getElementById("cutEnd").oninput = function(){

document.getElementById("endLabel").innerText =
this.value + " sec"

}

async function processVideo(tool){

const file = input.files[0]

if(!file){

alert("Please Select Video")

return

}

await loadFFmpeg()

const loader = document.getElementById("loader")

const fill = document.getElementById("fill")

const loaderText = document.getElementById("loaderText")

loader.style.display = "block"

fill.style.width = "10%"

loaderText.innerText = "Processing Video..."

const data = await fetchFile(file)

await ffmpeg.writeFile("input.mp4", data)

let output = "output.mp4"

if(tool === "cutter"){

const start = document.getElementById("cutStart").value
const end = document.getElementById("cutEnd").value

await ffmpeg.exec([
"-i","input.mp4",
"-ss",start,
"-to",end,
"-preset","ultrafast",
output
])

}

else if(tool === "compress"){

const level =
document.getElementById("compressLevel").value

await ffmpeg.exec([
"-i","input.mp4",
"-vcodec","libx264",
"-crf",level,
output
])

}

else if(tool === "reels"){

await ffmpeg.exec([
"-i","input.mp4",
"-vf","scale=1080:1920",
output
])

}

else if(tool === "youtube"){

await ffmpeg.exec([
"-i","input.mp4",
"-vf","scale=1920:1080",
output
])

}

else if(tool === "mute"){

await ffmpeg.exec([
"-i","input.mp4",
"-an",
output
])

}

else if(tool === "reverse"){

await ffmpeg.exec([
"-i","input.mp4",
"-vf","reverse",
"-af","areverse",
output
])

}

else if(tool === "speed"){

const speed =
document.getElementById("speedValue").value

const pts = 1 / speed

await ffmpeg.exec([
"-i","input.mp4",
"-filter:v",`setpts=${pts}*PTS`,
output
])

}

else if(tool === "mp3"){

output = "audio.mp3"

await ffmpeg.exec([
"-i","input.mp4",
"-q:a","0",
"-map","a",
output
])

}

else if(tool === "shorts"){

const duration =
document.getElementById("shortDuration").value

await ffmpeg.exec([
"-i","input.mp4",
"-t",duration,
output
])

}

fill.style.width = "100%"

loaderText.innerText = "Completed"

const resultBox =
document.getElementById("results")

const fileData =
await ffmpeg.readFile(output)

const blob = new Blob(
[fileData.buffer],
{
type:
output.endsWith(".mp3")
? "audio/mp3"
: "video/mp4"
}
)

const url = URL.createObjectURL(blob)

resultBox.innerHTML = `

<div class="output-card">

<h3>Processed File</h3>

${
output.endsWith(".mp3")
?
`<audio controls src="${url}"></audio>`
:
`<video controls src="${url}"></video>`
}

<a class="download-btn"
href="${url}"
download="${output}">
⬇ Download
</a>

</div>

`

setTimeout(()=>{

loader.style.display = "none"

fill.style.width = "0%"

},1500)

}

</script>

</body>
</html>

"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
