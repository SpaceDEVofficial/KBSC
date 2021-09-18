import flask
from flask import request
import pickle
from io import BytesIO
import asyncio
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import warnings

sns.set(rc={'figure.figsize': (16, 9)})
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

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.xaxis.grid(True, which="minor")

    ax.xaxis.set_major_locator(MultipleLocator(round(scl_length / 10)))
    ax.xaxis.set_major_formatter('{x:.0f}')
    ax.xaxis.set_minor_locator(AutoMinorLocator())

    d = scl_length / 50
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
