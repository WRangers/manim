import os
import hashlib

from manimlib.constants import TEX_TEXT_TO_REPLACE
from manimlib.constants import TEX_USE_CTEX
import manimlib.constants as consts


def tex_hash(expression, template_tex_file_body):
    id_str = str(expression + template_tex_file_body)
    hasher = hashlib.sha256()
    hasher.update(id_str.encode())
    # Truncating at 16 bytes for cleanliness
    return hasher.hexdigest()[:16]


def tex_to_svg_file(expression, template_tex_file_body):
    tex_file = generate_tex_file(expression, template_tex_file_body)
    dvi_or_pdf_file = tex_to_dvi_or_pdf(tex_file)
    return dvi_or_pdf_to_svg(dvi_or_pdf_file)


def generate_tex_file(expression, template_tex_file_body):
    result = os.path.join(
        consts.TEX_DIR,
        tex_hash(expression, template_tex_file_body)
    ) + ".tex"
    if not os.path.exists(result):
        print("Writing \"%s\" to %s" % (
            "".join(expression), result
        ))
        new_body = template_tex_file_body.replace(
            TEX_TEXT_TO_REPLACE, expression
        )
        with open(result, "w", encoding="utf-8") as outfile:
            outfile.write(new_body)
    return result


def tex_to_dvi_or_pdf(tex_file):
    result = tex_file.replace(".tex", ".dvi" if not TEX_USE_CTEX else ".pdf")
    if not os.path.exists(result):
        commands = [
            "latex",
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-output-directory=\"{}\"".format(consts.TEX_DIR),
            "\"{}\"".format(tex_file),
            ">",
            os.devnull
        ] if not TEX_USE_CTEX else [
            "xelatex",
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-output-directory=\"{}\"".format(consts.TEX_DIR),
            "\"{}\"".format(tex_file),
            ">",
            os.devnull
        ]
        exit_code = os.system(" ".join(commands))
        if exit_code != 0:
            log_file = tex_file.replace(".tex", ".log")
            raise Exception(
                ("Latex error converting to dvi. " if not TEX_USE_CTEX
                 else "Xelatex error converting to xdv. ") +
                "See log output above or the log file: %s" % log_file)
    return result


def dvi_or_pdf_to_svg(dvi_or_pdf_file, regen_if_exists=False):
    """
    Converts a dvi, which potentially has multiple slides, into a
    directory full of enumerated pngs corresponding with these slides.
    Returns a list of PIL Image objects for these images sorted as they
    where in the dvi
    """
    if 'pdf' in dvi_or_pdf_file:
        result = dvi_or_pdf_file.replace(".pdf", ".svg")
        pdf_name = get_pdf_name(dvi_or_pdf_file)
        old_path = os.getcwd()
        if not os.path.exists(result):
            commands = [
                "dvisvgm",
                "-P",
                # "-n",
                # "-v",
                # "0",
                # "-o",
                "\"{}\"".format(pdf_name),
                # pdf_file,
                ">",
                os.devnull
            ]
            os.chdir(consts.TEX_DIR)
            os.system(" ".join(commands))
            os.chdir(old_path)
        return result
    else:
        result = dvi_or_pdf_file.replace(".dvi", ".svg")
        if not os.path.exists(result):
            commands = [
                "dvisvgm",
                "\"{}\"".format(dvi_or_pdf_file),
                "-n",
                "-v",
                "0",
                "-o",
                "\"{}\"".format(result),
                ">",
                os.devnull
            ]
            os.system(" ".join(commands))
        return result


def get_pdf_name(pdf_file):
    de_n = len(consts.TEX_DIR)+1
    return pdf_file[de_n::]
