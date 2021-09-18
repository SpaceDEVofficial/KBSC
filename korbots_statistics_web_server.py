from datetime import datetime
import matplotlib.pyplot as plt
import flask
import quart
from quart import request
from io import BytesIO
import aiosqlite
import math
import config

if config.env:
    host_ip = "0.0.0.0"
    host_port = 80
else:
    host_ip = "127.0.0.1"
    host_port = 80
async def out():
    async with aiosqlite.connect("db/db.db") as con:
        data = list(await (await con.execute("SELECT * FROM guild_count")).fetchall())
        x = []
        y = []
        for i in data:
            x.append(i[1][:-3])
            y.append(i[0])
        fig, ax = plt.subplots()
        ax.set(title='Konosuba bot Server chart!')
        plt.plot_date(x, y, linestyle='solid')
        plt.margins(0)
        plt.gcf().set_size_inches(20, 10)
        new_list = range(math.floor(min(y))-3, math.ceil(max(y)) + 3)
        plt.yticks(new_list)
        fig.autofmt_xdate(rotation=65)
        plt.grid(True)
        bytesio = BytesIO()
        plt.savefig(bytesio, dpi=300, format='png',bbox_inches='tight')
        bytesio.seek(0)
        return bytesio

async def vote_out():
    async with aiosqlite.connect("db/db.db") as con:
        data = list(await (await con.execute("SELECT * FROM vote_count")).fetchall())
        x = []
        y = []
        for i in data:
            x.append(i[1][:-3])
            y.append(i[0])
        fig, ax = plt.subplots()
        ax.set(title='Konosuba bot Heart❤ chart! ')
        plt.plot_date(x, y, linestyle='solid',color="red")
        plt.margins(0)
        plt.gcf().set_size_inches(20, 10)
        new_list = range(math.floor(min(y))-2, math.ceil(max(y)) + 3)
        plt.yticks(new_list)
        ax.set_xticklabels(x)
        fig.autofmt_xdate(rotation=65)
        plt.grid(True)
        bytesio = BytesIO()
        plt.savefig(bytesio, dpi=300, format='png',bbox_inches='tight')
        bytesio.seek(0)
        return bytesio

app = quart.Quart(__name__)


@app.route("/get")
async def web_get_image():
    if request.args.get('type') == 'image':
        return await quart.send_file(filename_or_io=await out(), mimetype='image/png')

@app.route("/voteget")
async def vote_get_image():
    if request.args.get('type') == 'image':
        return await quart.send_file(filename_or_io=await vote_out(), mimetype='image/png')


if __name__ == "__main__":
    app.run(host=host_ip, port=host_port)