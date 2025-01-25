import sys
if '-m' not in sys.argv:
    from .summary import Head, Tail
    from .count import Count

__all__ = ['Head', 'Tail', 'Count']
