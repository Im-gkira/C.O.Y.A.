from gevent import monkey

monkey.patch_all()

import os
from coya import create_app, db, socketio

app = create_app()


@app.shell_context_processors
def make_shell_context():
    return {"db": db}


if __name__ == '__main__':
    socketio.run(app)
