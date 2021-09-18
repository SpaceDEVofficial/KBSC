import flask
from flask import request
import pickle
from io import BytesIO
import asyncio
from matplotlib import pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import warnings

warnings.filterwarnings("ignore")

with open("server/db/serversdata.bin", "rb") as ff:
    servers_count_list = pickle.load(ff)


def out():
    global servers_count_list
    with open("server/db/serversdata.bin", "rb") as ff:
        servers_count_list = pickle.load(ff)
    x = [i + 1 for i in range(len(servers_count_list))]
    y = servers_count_list
    scl_length = len(servers_count_list)
    # https://matplotlib.org/stable/gallery/ticks_and_spines/major_minor_demo.html

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.xaxis.grid(True, which="minor")

    ax.xaxis.set_major_locator(MultipleLocator(round(scl_length / 10)))
    ax.xaxis.set_major_formatter('{x:.0f}')

    # For the minor ticks, use no labels; default NullFormatter.
    # ax.xaxis.set_minor_locator(MultipleLocator(3000))

    ax.xaxis.set_minor_locator(AutoMinorLocator())

    # ax.xaxis.set_visible(False)
    d = scl_length / 50  # 기본 Location 10 + 마이너 5
    d = round(d / 1440, 2)
    plt.xlabel(f"{scl_length} minutes | Grid per {d} day")
    ax.xaxis.set_ticklabels([])

    bytesio = BytesIO()

    fig.savefig(bytesio, dpi=300, format='png')
    bytesio.seek(0)
    return bytesio

app = flask.Flask(__name__)


@app.route("/get")
def web_get_image():
    if request.args.get('type') == 'image':
        return flask.send_file(out(), mimetype='image/png')

@app.route("/total")
def web_get_total():
    return str(len(servers_count_list))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888")
