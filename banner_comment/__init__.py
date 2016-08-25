from __future__ import print_function
import subprocess


def banner_comment(text, font='standard', width=79, print_to_stdout=True,
                   border_top=True, border_bottom=True, border_right=True):
    """
    Generate a ASCII Banner comment for separating code blocks via FIGlet.

    :param text: The text to banner-ize.
    :param font: the figlet font
    :param width: the column width of the banner
    :param print_to_stdout: if True (default) print the banner comment to
        stdout. Otherwise, print nothing.
    :param border_top: print a octothorp border on the top
    :param border_bottom: print a octothorp border on the bottom
    :param border_right: print a octothorp border on the right
    :return: the banner_comment, if print_to_stdout is False
    """
    cmd = ['figlet', '-c', '-w', str(width), '-f', font, text]
    s = subprocess.check_output(cmd).decode()

    lines = ("#" + line for line in s.splitlines())
    if border_right:
        lines = (l.ljust(width-1, " ") + "#" for l in lines)
    lines = list(lines)

    if border_top or border_bottom:
        border = "#" * 79
        if border_top:
            lines.insert(0, border)
        if border_bottom:
            lines.append(border)

    banner_str = "\n".join(lines) + "\n"
    if print_to_stdout:
        print(banner_str, end='')
    else:
        return banner_str


def cli():
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Make Bannerized Code Comments")
    parser.add_argument('text', metavar='COMMENT', help='the comment string')
    parser.add_argument('--font', metavar='FONT', required=False,
                        default='standard')

    border_ks = ['border_top', 'border_bottom', 'border_right']
    for k in border_ks:
        parser.add_argument("--no-" + k.replace("_", "-"),
                            dest=k, action='store_false')

    banner_comment(**vars(parser.parse_args()))


if __name__ == '__main__':
    cli()
