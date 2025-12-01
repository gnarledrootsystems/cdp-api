import linecache
import tracemalloc
from .colors import RED, GREEN, MAGENTA, CYAN, RESET

# https://docs.python.org/3/library/tracemalloc.html

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print(MAGENTA + "#### Memory Snapshot - Top %s lines ####" % limit + RESET)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print(CYAN + "#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024) + RESET)
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print(GREEN + '    %s' % line + RESET)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print(CYAN + "%s other: %.1f KiB" % (len(other), size / 1024) + RESET)
    total = sum(stat.size for stat in top_stats)
    print(MAGENTA + "Total allocated size: %.1f KiB" % (total / 1024) + RESET)
    
def start():
    tracemalloc.start()
    
def stop(func_name):
    snapshot = tracemalloc.take_snapshot()
    print(RED + f"Snapshot of: {func_name}" + RESET)
    display_top(snapshot)