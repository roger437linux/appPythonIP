from flask import Flask
import platform
import subprocess
import socket

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Docker Container</title>

        <!-- Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

        <!-- Bootstrap Icons -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.css" rel="stylesheet">

        <style>
            body {{
                background: linear-gradient(135deg, #DBDCDD, #AAABAC);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
            .main-card {{
                width: 100%;
                max-width: 900px;
                background: rgba(255,255,255,0.10);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.15);
            }}
            .title {{
                text-align: center;
                font-size: 4rem;
                font-weight: bold;
                color: #0d5e6d;
                margin-bottom: 40px;
            }}
            .info-card {{
                background: #111;
                border-radius: 12px;
                padding: 25px;
                margin-bottom: 20px;
                box-shadow: 0 5px 18px rgba(0,0,0,0.08);
                transition: 0.3s;
            }}
            .info-card:hover {{
                transform: translateY(-4px);
            }}
            .label {{
                font-size: 1rem;
                color: #6c757d;
                margin-bottom: 8px;
            }}
            .value {{
                font-size: 2rem;
                font-weight: bold;
                word-break: break-word;
            }}
            .python {{
                color: #0d8efd;
            }}
            .linux {{
                color: #fd7e14;
            }}
            .ip {{
                color: #19e754;
            }}
            .refresh-box {{
                text-align: center;
                margin-top: 35px;
            }}
            .refresh-box label {{
                font-size: 1.4rem;
                font-weight: bold;
                color: #495057;
                cursor: pointer;
            }}
            .refresh-box input {{
                width: 24px;
                height: 24px;
                margin-right: 12px;
                cursor: pointer;
            }}
            .footer {{
                margin-top: 30px;
                text-align: center;
                color: #6c757d;
                font-size: 1rem;
            }}
        </style>

        <script>
            var ref;
            function checkRefresh() {{
                if (document.cookie == "refresh=1") {{
                    document.getElementById("check").checked = true;
                    ref = setTimeout(function () {{
                        location.reload();
                    }}, 1000);
                }}
            }}

            function changeCookie() {{
                if (document.getElementById("check").checked) {{
                    document.cookie = "refresh=1";
                    ref = setTimeout(function () {{
                        location.reload();
                    }}, 1000);
                }} else {{
                    document.cookie = "refresh=0";
                    clearTimeout(ref);
                }}
            }}
        </script>
    </head>

    <body onload="checkRefresh();">
        <div class="main-card">

            <div class="title">
                <i class="bi bi-box-seam"></i>
                Docker Container
            </div>

            <div class="info-card">
                <div class="label">
                    <i class="bi bi-rocket"></i>
                    Python Version
                </div>

                <div class="value python">
                    {python_version}
                </div>
            </div>

            <div class="info-card">
                <div class="label">
                    <i class="bi bi-cpu"></i>
                    Linux Distribution
                </div>

                <div class="value linux">
                    {distro}
                </div>
            </div>

            <div class="info-card">
                <div class="label">
                    <i class="bi bi-hdd-network"></i>
                    IPv4 Container
                </div>

                <div class="value ip">
                    {ipv4}
                </div>
            </div>

            <div class="refresh-box">
                <label>
                    <input type="checkbox"
                        id="check"
                        onchange="changeCookie()">

                    Auto Refresh
                </label>
            </div>

            <div class="footer">
                Flask + Docker
            </div>
        </div>
    </body>
</html>
"""

@app.route("/")
def home():

    os = 'head -n 1 /etc/os-release | cut -d"=" -f2'

    distro = subprocess.run(
        os,
        shell=True,
        text=True,
        capture_output=True
    ).stdout.strip().replace('"', '')

    return HTML.format(
        python_version=platform.python_version(),
        distro=distro,
        ipv4=socket.gethostbyname(socket.gethostname())
    )

app.run(host="0.0.0.0", port=5000, debug=True)
