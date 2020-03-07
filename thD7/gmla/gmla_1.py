class Preamble(Scene):
    CONFIG = {
        'c_title': '我的第一个视频',
        'e_title': 'My First Video',
        'series': r'\scriptsize The Geometry Meaning of Linear Algebra Series\\ \# \sz{0}',
        'saying': r'数缺形时少直观，形少数时难入微；\\数形结合百般好，割裂分家万事休。',
        'saying_author': '——华罗庚',
        'statement': r'\scriptsize 本视频内容主要根据《线性代数的几何意义》制作'
    }

class Epilogue(Scene):
    CONFIG = {
        'producer': r'\large ${\sf{7}}^{\sf th}$ \sf Dimension',
        'anim_engine':
        r'{\scriptsize by}\\{\sf Grant Sanderson}\\「3Blue1Brown」',
        'bgm': [
            r'Arryo Seco~-~Curtis Schweitzer\\',
        ],
        'cfonts': [
            r'\bf 思源黑体',
            r'思源宋体',
        ],
        'efonts': [
            r'Palatino',
            r'\sf Zapfino',
        ],
        'refs': [
            r'',
        ],
        'acknowledgement': True,
    }