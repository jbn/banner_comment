import subprocess


def banner_comment(text, font='ogre', width=79, 
                   border_top=True, border_bottom=True, border_right=True):
    """
    Generate a ASCII Banner comment for separating code blocks via FIGlet.

    :param text: The text to banner-ize.
    :param font: the figlet font
    :param width: the column width of the banner
    :param border_top: print a octothorp border on the top
    :param border_bottom: print a octothorp border on the bottom
    :param border_right: print a octothorp border on the right
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

    return "\n".join(lines) + "\n"
