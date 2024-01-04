from main import c, conn

def get_prefix():
    c.execute("SELECT key FROM keys WHERE service=?", ("prefix",))
    return c.fetchone()[0]
