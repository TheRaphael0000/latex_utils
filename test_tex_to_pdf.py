import time

from tex_to_pdf import tex_to_pdf


class Stopwatch:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        print(time.perf_counter() - self.start)


if __name__ == '__main__':
    n = 100

    src = r"""
    \documentclass{article}
    % General document formatting
    \usepackage[margin=0.7in]{geometry}

    \begin{document}

    test

    \end{document}
    """

    with Stopwatch() as sw:
        for i in range(n):
            tex_to_pdf(src)
