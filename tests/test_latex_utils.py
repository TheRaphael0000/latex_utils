import time
import unittest

from latex_utils import tex_to_pdf


class Stopwatch:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        print("Took:", time.perf_counter() - self.start)


class TestLatexUtils(unittest.TestCase):
    def test_tex_to_pdf(self):
        n = 5

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
                print(i)
                tex_to_pdf(src)


if __name__ == '__main__':
    unittest.main()
