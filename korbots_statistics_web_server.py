import flask
from flask import request
import pandas as pd
import numpy as np
import seaborn as sns
import pickle
from io import BytesIO
import asyncio
import matplotlib
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings("ignore")
# matplotlib.use('TkAgg')
# plt.figure(figsize=[16, 9])
sns.set(rc={'figure.figsize': (16, 9)})

with open("server/db/serversdata.bin", "rb") as ff:
    servers_count_list = pickle.load(ff)


def out():
    global servers_count_list
    with open("server/db/serversdata.bin", "rb") as ff:
        servers_count_list = pickle.load(ff)
    df = pd.DataFrame(dict(time=([i + 1 for i in range(len(servers_count_list))]), servers=servers_count_list))
    # g = sns.lineplot(x="time", y="servers", data=df)
    g = sns.relplot(x="time", y="servers", kind="line", data=df, height=5, aspect=1.7)  # , col="servers", col_wrap=8
    # g.set(xlim=(0, 200))
    # g.fig.autofmt_xdate()

    bytesio = BytesIO()
    g.savefig(bytesio, dpi=300, format='png')
    bytesio.seek(0)
    return bytesio


app = flask.Flask(__name__)


@app.route("/get")
def web_get_image():
    if request.args.get('type') == 'image':
        return flask.send_file(out(), mimetype='image/png')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888")
