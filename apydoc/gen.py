# apydoc.gen: generate apydocs

import json, os, sys
from glob import glob
import inspect, importlib

def gen_docs(object):
    """for a given object, generate and return documents for it."""
    return 

if __name__ == "__main__":
    path = os.path.realpath(sys.argv[1])
    apydoc_json_fn = os.path.join(path, "apydoc.json")
    if not os.path.exists(apydoc_json_fn):
        apydoc_json_fn = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "apydoc.json.TEMPLATE"
        )
    with open(apydoc_json_fn, "rb") as f:
        j = json.loads(f.read())
    pys = []
    for src in j["srcs"]:
        src_path = os.path.realpath(os.path.join(path, src))
        os.chdir(src_path)
        pys = sorted(glob(os.path.join(src_path, "**", "*.py")))
        for py in pys:
            rp = os.path.splitext(os.path.normpath(os.path.relpath(py, src_path)))[0].split(os.path.sep)
            module_path = ".".join(rp)
            module = importlib.import_module(module_path)
            module_docs = gen_docs(module)

