import tempfile
import subprocess
import shutil

LATEX_PROCESSOR = "latexmk"

if not shutil.which(LATEX_PROCESSOR):
    raise Exception(f"{LATEX_PROCESSOR} is not installed in global path")


def tex_to_pdf(input_tex, capture_output=True):
    with tempfile.TemporaryDirectory() as tmpdir:
        _, tmpfilename = tempfile.mkstemp(dir=tmpdir)
        latex_filename = f"{tmpfilename}.tex"
        with open(latex_filename, "w") as latex_file:
            latex_file.write(input_tex)
        subprocess.run(
            [LATEX_PROCESSOR, "-pdf", latex_filename],
            capture_output=capture_output,
            check=True,
            cwd=tmpdir
        )
        pdf_filename = f"{tmpfilename}.pdf"
        with open(pdf_filename, "rb") as pdf_file:
            return pdf_file.read()
