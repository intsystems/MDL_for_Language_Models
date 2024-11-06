# this script was generated by ChatGPT with minor fixes
import xml.etree.ElementTree as ET


def get_coverage():
    tree = ET.parse("coverage.xml")
    root = tree.getroot()
    line_rate = float(root.get("line-rate", 0)) * 100
    return round(line_rate, 2)


def generate_badge(coverage):
    color = "red"
    if coverage >= 90:
        color = "lightgreen"
    elif coverage >= 75:
        color = "yellowgreen"
    elif coverage >= 50:
        color = "olive"
    badge = f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="20">
        <rect width="100" height="20" fill="{color}" />
        <text x="50%" y="14" fill="#fff" font-family="Arial" font-size="11" text-anchor="middle">
            Coverage: {coverage}%
        </text>
    </svg>
    """
    with open("coverage-badge.svg", "w") as badge_file:
        badge_file.write(badge)


if __name__ == "__main__":
    coverage = get_coverage()
    generate_badge(coverage)
