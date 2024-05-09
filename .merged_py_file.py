# Content from: ./.merged_py_file.py


# Content from: ./Docify-Combiner.py
import os
FINAL = "."
def copy_py_files(directory, output_file):
    with open(output_file, 'w') as output:
        for root, _, files in os.walk(directory):
            for filename in sorted(files):
                if filename.endswith(".py") and filename != "Dockify-Combiner.py":
                    file_path = os.path.join(root, filename)
                    print(file_path)
                    with open(file_path, 'r') as file:
                        output.write("# Content from: {}\n".format(file_path))
                        output.write(file.read())
                        output.write("\n\n")
                        

                        
def list_folders_and_files():
    """
    Lists all folders and files in the current directory.
    """
    items = os.listdir()
    folders = [item for item in items if os.path.isdir(item)]
    files = [item for item in items if os.path.isfile(item)]
    return folders, files

def navigate():
    """
    Allows the user to navigate through folders and files.
    """
    global FINAL
    while True:
        print("\nCurrent Directory Contents:")
        folders, files = list_folders_and_files()
        print("Folders:")
        for folder in folders:
            print(folder + "/")
        print("\nFiles:")
        for file in files:
            print(file)
        
        choice = input("\nEnter folder or file name to navigate (or press Enter to exit): ")
        if choice == "":
            # return os.path.abspath(choice)
            break
        elif os.path.isdir(choice):
            os.chdir(choice)
        elif os.path.isfile(choice):
            return os.path.abspath(choice)
        else:
            print("Invalid choice. Please enter a valid folder or file name.")


def main():
    # source_directory = input("Enter directory name (. for current directory): \n") 
    output_file = ".merged_py_file.py"
    # source_directory = navigate()
    source_directory = "."

    copy_py_files(source_directory, output_file)
    print("All .py files copied to {}".format(output_file))

if __name__ == "__main__":
    main()


# Content from: ./setup.py
#!/usr/bin/env python
import sys
from io import open

import setuptools

requires = ['textblob', 'wordfilter', 'internetarchive', 'requests']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='olipy',
    version='1.0.4',
    author='Leonard Richardson',
    author_email='leonardr@segfault.org',
    url="https://github.com/leonardr/olipy/",
    description="Python library for artistic text generation",
    license='GPLv3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'olipy.apollo = olipy.example:apollo',
            'olipy.board_games = olipy.example:board_games',
            'olipy.corrupt = olipy.example:corrupt',
            'olipy.dinosaurs = olipy.example:dinosaurs',
            'olipy.ebooks = olipy.example:ebooks',
            'olipy.gibberish = olipy.example:gibberish',
            'olipy.mashteroids = olipy.example:mashteroids',
            'olipy.sonnet = olipy.example:sonnet',
            'olipy.typewriter = olipy.example:typewriter',
            'olipy.words = olipy.example:words',
        ]
    },
    package_data = {
        "olipy": [
            "data/%s/*.json" % ("*/" * x)
            for x in range(10)
        ]
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Text Processing',
        'Topic :: Artistic Software',
    ],
)


# Content from: ./olipy/__init__.py
__version__ = "1.0.3"


# Content from: ./olipy/alphabet.py
# encoding: utf-8
"""Thematic collections of Unicode glyphs.

This is used by gibberish.py.
"""

import unicodedata
import random
from olipy import corpora

CUSTOM_ALPHABETS = {
    "Dice": u"\N{Die Face-1}\N{Die Face-2}\N{Die Face-3}\N{Die Face-4}\N{Die Face-5}\N{Die Face-6}",
    "Completely Circled Alphabetics": u"ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
    "Circled Alphabetics": u"⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
    "Fullwidth Alphabetics" : u"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
    "Bold Alphabetics" : u"𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
    "Italic Alphabetics" : u"𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧",
    "Bold Italic Alphabetics" : u"𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛",
    "Script Alphabetics" : u"𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏",
    "Script Bold Alphabetics" : u"𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
    "Fraktur Alphabetics" : u"𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
    "Doublestruck Alphabetics" : u"𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
    "Fraktur Bold Alphabetics" : u"𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",
    "Sans Alphabetics" : u"𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓",
    "Sans Bold Alphabetics" : u"𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",
    "Sans Italic Alphabetics" : u"𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",
    "Sans Bold Italic Alphabetics" : u"𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",
    "Monospace Alphabetics" : u"𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
    "Alphabetics with Umlaut" : u"ÄB̈C̈D̈ËF̈G̈ḦÏJ̈K̈L̈M̈N̈ÖP̈Q̈R̈S̈T̈ÜV̈ẄẌŸZ̈äb̈c̈d̈ëf̈g̈ḧïj̈k̈l̈m̈n̈öp̈q̈r̈s̈ẗüv̈ẅẍÿz̈",
    "Modifier Alphabetics" : u"ᴬᴮʿᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴻᴼᴾᴿᵀᵁⱽᵂₐᵇᵈᵉᶠᵍʰᶤʲᵏˡᵐᵑᵒᵖʳˢᵗᵤᵛʷˣʸᶻ",
    "Turned Alphabetics": u"ɐqɔpǝɟƃɥıɾʞʃɯuodbɹsʇnʌʍxʎz",
    "Subscript Alphabetics": u"ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘʀꜱᴛᴜᴠᴡʏᴢₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ",
    "Superscript Alphabetics": u"ᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ",
    "Superscript and Subscript Math" : u"₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾",
    "Filled Circled Numerics": u"➊➋➌➍➎➏➐➑➒",
    "Double Circled Numerics": u"⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾",
    "Empty Circled Numerics": u"①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳",
    "Circled Alphanumerics": u"①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾❶❷❸❹❺❻❼❽❾❿➀➁➂➃➄➅➆➇➈➉➊➋➌➍➎➏➐➑➒➓㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿♳♴♵♶♷♸♹⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾",
    "Stars": u"✢✣✤✥✦✧✨✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋*͙⁎⁑⃰∗⊛⧆﹡＊٭≛⋆⍟⍣★☆☪⚝✡✦✧⭐⭑⭒",
    "Symbology": u"☀☁☂☃☄★☆☎☏☔☕☚☛☠☢☤☭☮☯☹☺☻☼♫⚐⚑⚒⚓⚔⚕⚖♻✄✌✍✏♀♂⌚",
    "Crossouts": u"Xxˣ͓̽ͯᶍẊẋẌẍₓ⒳Ⓧⓧ☒✕✖✗✘Ｘｘ𝁪𝅃𝅅𝐗𝐱𝑋𝑥𝑿𝒙𝒳𝓍𝓧𝔁𝔛𝔵𝕏𝕩𝖃𝖝𝖷𝗑𝗫𝘅𝘟𝘹𝙓𝙭𝚇𝚡×⨯ⵝ᙭Ҳ⚔⤧ҳ⤩᙮ⅹⅩ⤨⤪⨉⤫⤬",
    "Box Drawing All": u"─━│┃┄┅┆┇┈┉┊┋┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╌╍╎╏═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╵╶╷╸╹╺╻╼╽╾╿",
    "Box Drawing Double": u"═║╔╗╚╝╠╣╦╩╬",
    "Box Drawing Dots": u"┄┅┆┇┈┉┊┋╍╌╎╏",
    "Box Drawing Thick and Thin": u"┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╸╹╺╻╼╽╾╿",

    "Box Drawing Single and Double": u"┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╴╵╶╷",
    "Block Drawing by Height": u"▀▁▂▃▄▅▆▇█▔",
    "Block Drawing by Width": u"█▉▊▋▌▍▎▏▐▕",
    "Skin Tones" : u"🏻🏼🏽🏾🏿",
 }

class Alphabet:

    @classmethod
    def default(cls):
        """Load some interesting alphabets."""
        cls._fill_by_name(corpora.language.unicode_code_sheets['code_sheets'])
        return cls

    @classmethod
    def _fill_by_name(cls, data=None, add_custom=True):
        for c in data:
            name = c['name']
            if 'characters' in c and len(c['characters']) > 0:
                cls.by_name[name] = c
            if 'child' in c:
                cls._fill_by_name(c['child'], False)

        if not add_custom:
            return

        # Also add in custom alphabets
        for name, chars in CUSTOM_ALPHABETS.items():
            cls.by_name[name] = dict(characters=chars)

        # Add emoji.
        emoji = []
        for i in cls.EMOJI_S:
            emoji += cls.by_name[i]['characters']
        cls.by_name['Emoji'] = dict(characters=emoji)


    by_name = {}

    @classmethod
    def random_choice(cls, *alphabets):
        """A random choice among alphabets"""
        if not alphabets:
            alphabets = list(cls.by_name.keys())
        choice = random.choice(alphabets)
        return cls.characters([choice])

    @classmethod
    def random_choice_no_modifiers(cls, minimum_size=2):
        """A completely random choice among non-modifier alphabets."""
        choice = None
        while choice is None:
            choice = random.choice(list(cls.by_name.keys()))
            if choice in cls.MODIFIERS:
                choice = None
            # print "Choice: %s, len: %s" % (choice, len(cls.characters(choice)))
            if choice is not None:
                chars = cls.characters(choice)
                if len(chars) < minimum_size:
                    choice = None

        return chars

    @classmethod
    def subset(cls, alphabet, how_many_characters=None):
        """A limited subset of an alphabet."""
        full = Alphabet.random_choice_no_modifiers()
        limited = ''
        if not how_many_characters:
            how_many_characters = max(2, int(random.gauss(4, 2)))
        for i in range(how_many_characters):
            limited += random.choice(alphabet)
        return limited

    @classmethod
    def random_whitespace(cls):
        "A whitespace character selected at random."
        return random.choice(cls.WHITESPACE)

    @classmethod
    def random_modifier(cls):
        "A modifier selected at random."
        alphabet = Alphabet.characters(cls.MODIFIERS)
        return random.choice(alphabet)

    @classmethod
    def characters(cls, alphabets):
        char = []
        if not isinstance(alphabets, list):
            alphabets = [alphabets]
        # print "Character lookup for %r" % alphabets
        for alphabet in alphabets:
            # print "Looking up %s" % alphabet
            if isinstance(alphabet, list):
                char.extend(cls.characters(alphabet))
            else:
                try:
                    char.extend(cls.by_name[alphabet]['characters'])
                except Exception as e:
                    # Assume the string is the alphabet itself rather than the name of an alphabet.
                    char.extend(alphabet)
        return ''.join(char)

    # Some combination European alphabets
    ASCII = "Basic Latin (ASCII)"
    LATIN_1 = [ASCII, "Latin-1 Supplement"]
    LATIN_EXTRAS = [
        "Latin Extended-A", "Latin Extended-B",
        "Latin Extended-C", "Latin Extended-D",
        "Latin Extended Additional", "Latin Ligatures"]
    LATIN_FULL = LATIN_1 + LATIN_EXTRAS
    CYRILLIC = ["Cyrillic"]
    CYRILLIC_FULL = ["Cyrillic", "Cyrillic Supplement", "Cyrillic Extended-A", "Cyrillic Extended-B"]

    LATIN_S = [ASCII, LATIN_1, LATIN_FULL, 
               "Circled Alphabetics",
               "Circled Alphanumerics",
               "Bold Alphabetics",
               "Italic Alphabetics",
               "Script Alphabetics",
               "Bold Italic Alphabetics",
               "Script Bold Alphabetics",
               "Fraktur Alphabetics",
               "Doublestruck Alphabetics",
               "Fraktur Bold Alphabetics",
               "Sans Alphabetics",
               "Sans Bold Alphabetics",
               "Sans Italic Alphabetics",
               "Sans Bold Italic Alphabetics",
               "Monospace Alphabetics",
               "Alphabetics with Umlaut",
               "Turned Alphabetics",
               "Subscript Alphabetics",
               "Superscript Alphabetics",
               ]

    CYRILLIC_S = [CYRILLIC, CYRILLIC_FULL]

    # A set of European alphabets.
    EUROPEAN_S = [
        ASCII, LATIN_1, LATIN_FULL, CYRILLIC, CYRILLIC_FULL,
        ["Armenian", "Armenian Ligatures"],
        ["Coptic"],        
        ["Georgian"],
        ["Georgian", "Georgian Supplement"],
        ["Glagolitic"],
        ["Gothic"],
        ["Greek"],
        ["Greek", "Greek Extended"],
        ["Ogham"],
        ["Old Italic"],
        ["Runic"]
        ]

    # Some combination African alphabets.
    ETHIOPIC = ["Ethiopic"]
    ETHIOPIC_FULL = ["Ethiopic", "Ethiopic Supplement", "Ethiopic Extended", "Ethiopic Extended-A"]

    # A set of African alphabets.
    AFRICAN_S = [ETHIOPIC_FULL, "N'Ko", "Osmanya", "Tifinagh", "Vai"]

    # Some combination Middle Eastern alphabets.
    ARABIC = ["Arabic"]
    ARABIC_FULL = ARABIC + ["Arabic Supplement"]
    ARABIC_WITH_PRESENTATION_FORMS = ARABIC + ["Arabic Presentation Forms-B"]
    HEBREW = ["Hebrew"]
    HEBREW_WITH_PRESENTATION_FORMS = HEBREW + ["Hebrew Presentation Forms"]

    # A set of Middle Eastern alphabets.
    MIDDLE_EASTERN_S = [
        ARABIC, ARABIC_FULL, ARABIC_WITH_PRESENTATION_FORMS,
        HEBREW, HEBREW_WITH_PRESENTATION_FORMS,
        "Old Persian",
        "Ugaritic",
        "Phoenician",
        "Syriac"
        ]

    # A set of Central Asian alphabets.
    CENTRAL_ASIAN_S = [
        "Tibetan",
        ]

    # Some combination South Asian alphabets
    DEVANAGARI = ["Devanagari"]
    DEVANAGARI_EXTENDED = DEVANAGARI + ["Devanagari Extended"]

    # A set of South Asian alphabets
    SOUTH_ASIAN_S = [
        DEVANAGARI,
        DEVANAGARI_EXTENDED,
        "Bengali and Assamese",
        "Gujarati",
        "Gurmukhi",
        "Kannada",
        "Malayalam",
        "Oriya",
        "Sinhala",
        "Tamil",
        "Telugu",
        "Thaana"
        ]

    # Some combination Southeast Asian alphabets
    KHMER = ["Khmer"]
    KHMER_WITH_SYMBOLS = KHMER + ["Khmer Symbols"]
    MYANMAR = ["Myanmar"]
    MYANMAR_EXTENDED = MYANMAR + ["Myanmar Extended-A"]

    # A set of Southeast Asian alphabets
    SOUTHEAST_ASIAN_S = [
        KHMER,
        KHMER_WITH_SYMBOLS,
        MYANMAR,
        MYANMAR_EXTENDED,
        "Buginese",
        "Kayah Li",
        "Lao",
        "Tai Le",
        "Thai",
        ]

    # A set of Phillipine alphabets
    PHILLIPINE_S = [
        "Hanunoo",
        ]

    # Some combination East Asian alphabets.
    HANGUL_JAMO = ["Hangul Jamo"]
    HANGUL_JAMO_WITH_COMPATIBILITY = HANGUL_JAMO + ["Hangul Compatibility Jamo"]
    KATAKANA = ["Katakana"]
    KATAKANA_ALL = KATAKANA + ["Katakana Phonetic Extensions"]

    # A set of East Asian alphabets
    EAST_ASIAN_S = [
        "Bopomofo",
        "CJK Unified Ideographs (Han)",
        "CJK Compatibility Ideographs",
        # "CJK Radicals  KangXi Radicals", # Name is weird
        "Hangul Syllables",
        "Hiragana",
        HANGUL_JAMO,
        HANGUL_JAMO_WITH_COMPATIBILITY,
        KATAKANA,
        KATAKANA_ALL,
        ]

    # Some combination American alphabets
    UCAS = "Unified Canadian Aboriginal Syllabics"
    UCAS_ALL = ["Unified Canadian Aboriginal Syllabics", "UCAS Extended"]

    # A set of American alphabets
    AMERICAN_S = ["Cherokee",
                  "Deseret",
                  UCAS,
                  UCAS_ALL]

    # All available alphabets that are used to convey human language.
    ALL_LANGUAGE_ALPHABETS_S = (EUROPEAN_S + AFRICAN_S + MIDDLE_EASTERN_S
                                + CENTRAL_ASIAN_S + SOUTH_ASIAN_S
                                + SOUTHEAST_ASIAN_S + PHILLIPINE_S
                                + EAST_ASIAN_S + AMERICAN_S)

    # Ways to modify characters.
    DIACRITICAL = ["Combining Diacritical Marks"]
    DIACRITICAL_FULL = DIACRITICAL + [
        "Combining Diacritical Marks Supplement",
        "Combining Half Marks",
        "Combining Diacritical Marks for Symbols"]
    MODIFIERS = DIACRITICAL_FULL

    # "Weird Twitter" versions of Latin characters
    WEIRD_TWITTER_LATIN = [
        "Fullwidth ASCII Punctuation",
        "Superscripts and Subscripts",
        "Mathematical Alphanumeric Symbols",
        "Letterlike Symbols",
        "Enclosed Alphanumerics",
        "Enclosed Alphanumeric Supplement",
        "Additional Squared Symbols",
        "Control Pictures",
        "Braille Patterns",
        "IPA Extensions",
        "Phonetic Extensions",
        "Phonetic Extensions Supplement",
        "Old Italic",
        "Circled Alphabetics",
        "Circled Alphanumerics",
        "Double Circled Numerics",
        "Bold Alphabetics",
        "Italic Alphabetics",
        "Script Alphabetics",
        "Bold Italic Alphabetics",
        "Script Bold Alphabetics",
        "Fraktur Alphabetics",
        "Doublestruck Alphabetics",
        "Fraktur Bold Alphabetics",
        "Sans Alphabetics",
        "Sans Bold Alphabetics",
        "Sans Italic Alphabetics",
        "Sans Bold Italic Alphabetics",
        "Monospace Alphabetics",
        "Alphabetics with Umlaut",
        ]

    # "Weird Twitter" mixins for Latin characters.
    WEIRD_TWITTER_LATIN_MIXINS = [
        "Alphabetic Presentation Forms",
        "General Punctuation",
        "Latin-1 Punctuation",
        "Small Form Variants",
        "Currency Symbols",
        "Dollar Sign",
        "Yen, Pound and Cent",
        "Rial Sign",
        "Vertical Forms",
        "Number Forms",
        "Fullwidth ASCII Digits",
        "Modifier Tone Letters",
        "Spacing Modifier Letters",
        "CJK Compatibility",
        ]

    # "Weird Twitter" versions of Japanese characters
    WEIRD_TWITTER_JAPANESE = [
        "Halfwidth and Fullwidth Forms",
        "Fullwidth ASCII Digits",
        "Halfwidth Katakana",
        ]

    # "Weird Twitter" mixins for Japanese characters
    WEIRD_TWITTER_JAPANESE_MIXINS = [
        "CJK Compatibility Ideographs",
        "Fullwidth ASCII Punctuation",
        "Vertical Forms",
        "CJK Symbols and Punctuation",
        "CJK Compatibility Forms",
        "Enclosed CJK Letters and Months",
        ]

    # "Weird Twitter" for the Han unification plane
    WEIRD_TWITTER_CJK = [
        "Bopomofo",
        "CJK Compatibility Ideographs",
        "CJK Radicals / KangXi Radicals"
        ]

    # "Weird Twitter" mixins for the Han unification plane
    WEIRD_TWITTER_CJK_MIXINS = WEIRD_TWITTER_JAPANESE_MIXINS + [
        "CJK Compatibility"]

    # "Weird Twitter" math glyphs
    WEIRD_TWITTER_MATH = [
        "Number Forms",
        "Fullwidth ASCII Digits",
        "Superscripts and Subscripts",
        "Superscript and Subscript Math",
        ]

    WEIRD_TWITTER_MATH_MIXINS = [
        "Mathematical Operators",
        "Supplemental Mathematical Operators",
        "Miscellaneous Mathematical Symbols-A",
        "Floors and Ceilings",
        ]

    # Symbolic glyphs
    SYMBOLIC_ALPHABETS = [
        "APL symbols",
        "Miscellaneous Technical",
        "Miscellaneous Symbols And Pictographs",
        "Optical Character Recognition (OCR)",
        "Arrows",
        "Supplemental Arrows-A",
        "Supplemental Arrows-B",
        "Additional Arrows",
        "Dingbats",
        "Emoticons",
        "Musical Symbols",
        "Byzantine Musical Symbols",
        ]

    # Gaming glyphs
    GAMING_ALPHABETS = [
        "Chess, Checkers/Draughts",
        "Dice",
        "Domino Tiles",
        "Japanese Chess",
        "Mahjong Tiles",
        "Playing Cards",
        "Card suits",
        ]

    # Geometric glyphs, and glyphs designed for other purposes that
    # have geometric appeal
    GEOMETRIC_ALPHABETS = [
        "Geometric Shapes",
        # "CJK Compatibility Forms",
        "Additional Shapes",
        "Box Drawing",
        "Block Elements",
        "Braille Patterns",
        "Yijing Mono-, Di- and Trigrams",
        "Stars",
        ]

    # Yijing symbols
    YIJING = [
        "Yijing Mono-, Di- and Trigrams",
        "Yijing Hexagram Symbols",
        "Tai Xuan Jing Symbols",
        ]

    # Small glitchy alphabets that can be tossed in almost anywhere.
    GLITCHES = [
        "Optical Character Recognition (OCR)",
        "Floors and Ceilings",
        "Shading Mosaic", # Custom alphabet
        "One Dot", # Custom alphabet
        "Fill Mosaic", # Custom alphabet
        ]

    # Custom alphabets 
    CUSTOM_S = [
        "Geometric Shapes",
        ["Geometric Shapes", "Arrows"],
        ["Geometric Shapes", "Additional Shapes"],
        ["Geometric Shapes", "Additional Shapes", "Box Drawing", "Block Elements"],
        "Box Drawing",
        "Block Elements",
        ["Box Drawing", "Block Elements"],
        ["Box Drawing", "Block Elements", "Optical Character Recognition (OCR)"],
        "Optical Character Recognition (OCR)",
        "Braille Patterns",
        ["Braille Patterns", "Optical Character Recognition (OCR)"],
        ["Dingbats", "Miscellaneous Symbols"],
        ["Dingbats", "Emoticons", "Miscellaneous Symbols"],
        ["Dingbats", "Emoticons", "Miscellaneous Symbols", "Miscellaneous Symbols and Arrows"],
        ["Basic Latin (ASCII)", "Emoticons"],
        "Chess, Checkers/Draughts",
        "Domino Tiles",
        "Playing Cards",
        "Mahjong Tiles",
        "Dice",
        ["Dice", "Domino Tiles"],
        ["Playing Cards", "Card suits"],
        "Yijing Mono-, Di- and Trigrams",
        "Yijing Hexagram Symbols",
        "Tai Xuan Jing Symbols",
        ["Yijing Mono-, Di- and Trigrams", "Yijing Hexagram Symbols", "Tai Xuan Jing Symbols"],
        ["Yijing Mono-, Di- and Trigrams", "Yijing Hexagram Symbols", "Tai Xuan Jing Symbols", "Braille Patterns", "Optical Character Recognition (OCR)"],
        ["Hiragana", "Katakana"],
        ]

    def unicode_charset(name, *chrs):
        charset = "".join(map(unicodedata.lookup, chrs))
        CUSTOM_ALPHABETS[name] = charset
        return charset

    # Custom alphabets
    UP_POINTING_TRIANGLES = unicode_charset("Up-Pointing Triangles",
        "Apl functional symbol delta stile",
        "Black lower left triangle",
        "Black lower right triangle",
        "Black up-pointing small triangle",
        "Black up-pointing triangle",
        "Canadian syllabics glottal stop",
        "Canadian syllabics i",
        "Combining enclosing upward pointing triangle",
        "Coptic capital letter dalda",
        "Coptic small letter dalda",
        "Cyrillic capital letter closed little yus",
        "Cyrillic small letter little yus",
        "Greek capital letter delta",
        "Increment",
        "Mathematical bold capital delta",
        "Mathematical bold italic capital delta",
        "Minus sign in triangle",
        "Segment",
        "Tifinagh letter yav",
        "Triangle with dot above",
        "Triangle with serifs at bottom",
        "Triangle with underbar",
        "Up-pointing triangle with left half black",
        "Up-pointing triangle with right half black",
        "Lower left triangle",
        "Lower right triangle",
        "White trapezium",
        "White up-pointing small triangle",
        "White up-pointing small triangle",
        "White up-pointing triangle",
        #            "Alchemical symbol for fire",
        )

    DOWN_POINTING_TRIANGLES = unicode_charset("Down-Pointing Triangles",
        "Apl functional symbol del stile",
        "Black down-pointing small triangle",
        "Black down-pointing triangle",
        "Canadian syllabics carrier ru",
        "Canadian syllabics e",
        "Canadian syllabics pe",
        "Down-pointing triangle with left half black",
        "Down-pointing triangle with right half black",
        "For all",
        "Latin capital letter v",
        "Mathematical bold capital v",
        "Mathematical bold italic nabla",
        "Mathematical bold nabla",
        "Mathematical bold small v",
        "Mathematical italic nabla",
        "Mathematical monospace capital v",
        "Mathematical monospace small v",
        "Mathematical sans-serif bold nabla",
        "Mathematical sans-serif capital v",
        "Nabla",
        "Tifinagh letter yadh",
        "Vai symbol kung",
        "White down-pointing small triangle",
        "White down-pointing triangle",
        #            "Alchemical symbol for aquafortis"
        #            "Alchemical symbol for dissolve-2",
        #            "Alchemical symbol for water",
        #            "Greek vocal notation symbol-21",
        #            "Heavy white down-pointing triangle",
        )

    LEFT_POINTING_TRIANGLES = unicode_charset("Left-Pointing Triangles",
        "Apl functional symbol quad less-than",
        "Black left-pointing pointer",
        "Black left-pointing small triangle",
        "Black left-pointing triangle",
        "Canadian syllabics a",
        "Canadian syllabics carrier ra",
        "Canadian syllabics p",
        "Canadian syllabics pa",
        "Normal subgroup of",
        "Spherical angle",
        "Lower right triangle",
        "Upper right triangle",
        "Black upper right triangle",
        "Black lower right triangle",
        "Vai syllable gboo",
        "White left-pointing pointer",
        "White left-pointing small triangle",
        "White left-pointing triangle",
        # "Closed subset",
        # "Greek instrumental notation symbol-38",
        # "Large left triangle operator",
        # "Less-than closed by curve",
        #"Z notation domain antirestriction",
        )

    RIGHT_POINTING_TRIANGLES = unicode_charset("Right-Pointing Triangles",
        "Apl functional symbol quad greater-than",
        "Black lower right triangle",
        "Black right-pointing small triangle",
        "Black right-pointing triangle",
        "Black upper left triangle",
        "Canadian syllabics carrier hwee",
        "Canadian syllabics carrier i",
        "Canadian syllabics carrier re",
        "Canadian syllabics carrier we",
        "Canadian syllabics fo",
        "Canadian syllabics o",
        "Contains as normal subgroup",
        "Greater-than sign",
        "Lower right triangle",
        "Spherical angle opening left",
        "Succeeds",
        "Triangular bullet",
        "Upper left triangle",
        "White right-pointing pointer",
        "White right-pointing small triangle",
        "White right-pointing triangle",
        # "Closed superset",
        # "Conical taper",
        # "Greater-than closed by curve",
        # "Greek instrumental notation symbol-37",
        # "Z notation range antirestriction",
        )

    TRIANGLES = UP_POINTING_TRIANGLES + DOWN_POINTING_TRIANGLES + LEFT_POINTING_TRIANGLES + RIGHT_POINTING_TRIANGLES

    RECTANGLES = unicode_charset("Rectangles",
        "BLACK RECTANGLE", #▬
        "WHITE RECTANGLE", #▭
        "BLACK VERTICAL RECTANGLE", #▮
        "WHITE VERTICAL RECTANGLE", #▯
                            )

    QUADRILATERALS = unicode_charset("Quadrilaterals",
        "Apl functional symbol quad backslash",
        "Apl functional symbol quad slash",
        "Apl functional symbol quad",
        "Apl functional symbol quote quad",
        "Apl functional symbol squish quad",
        "Ballot box",
        "Black large square",
        "Black medium small square",
        "Black medium square",
        "Black parallelogram",
        "Black small square",
        "Black square",
        "Combining enclosing screen",
        "Combining enclosing square",
        "Flatness",
        "Hebrew letter wide final mem",
        "Katakana letter ro",
        "Lower right drop-shadowed white square",
        "Lower right shadowed white square",
        "Square lozenge",
        "Upper right drop-shadowed white square",
        "Upper right shadowed white square",
        "Viewdata square",
        "White large square",
        "White medium small square",
        "White medium square",
        "White parallelogram",
        "White small square",
        "White square with rounded corners",
        "White square",
        "White trapezium",
        "X in a rectangle box",
        #"Square with contoured outline",
        #"Ticket",
        "BALLOT BOX WITH CHECK", #☑
        "BALLOT BOX WITH X", #☒
        "MUSICAL SYMBOL SQUARE NOTEHEAD WHITE", #𝅆
        "MUSICAL SYMBOL SQUARE NOTEHEAD BLACK", #𝅇
        "SQUARE WITH TOP HALF BLACK", #⬒
        "SQUARE WITH BOTTOM HALF BLACK", #⬓
        "SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK", #⬔
        "SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK", #⬕
        "DOTTED SQUARE", #⬚
        "TWO JOINED SQUARES", #⧉
        "WHITE SQUARE WITH LEFTWARDS TICK", #⟤
        "WHITE SQUARE WITH RIGHTWARDS TICK", #⟥
        "SQUARE WITH LEFT HALF BLACK", #◧
        "SQUARE WITH RIGHT HALF BLACK", #◨
        "SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK", #◩
        "SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK", #◪
        "WHITE SQUARE CONTAINING BLACK SMALL SQUARE", #▣
        "SQUARE WITH HORIZONTAL FILL", #▤
        "SQUARE WITH VERTICAL FILL", #▥
        "SQUARE WITH ORTHOGONAL CROSSHATCH FILL", #▦
        "SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL", #▧
        "SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL", #▨
        "SQUARE WITH DIAGONAL CROSSHATCH FILL", #▩
        "WHITE SQUARE WITH CENTRE VERTICAL LINE", #⎅
        "SQUARE FOOT", #⏍
        ) + RECTANGLES

    PENTAGONS_AND_LARGER_POLYGONS = unicode_charset("Miscellaneous Polygons",
        "Benzene ring with circle",
        "Benzene ring",
        "Black horizontal ellipse",
        "Black shogi piece",
        "Canadian syllabics carrier tho",
        "House",
        "Software-function symbol",
        "White horizontal ellipse",
        "White shogi piece",
        "BLACK PENTAGON", #⬟
        "WHITE PENTAGON", #⬠
        "WHITE HEXAGON", #⬡
        "BLACK HEXAGON", #⬢
        "HORIZONTAL BLACK HEXAGON", #⬣
        "BLACK RIGHT-POINTING PENTAGON", #⭓
        "WHITE RIGHT-POINTING PENTAGON", #⭔
        # "Chestnut",
        )

    CIRCLES = unicode_charset("Circles",
        "UGARITIC LETTER THANNA", #𐎘
        "HEBREW MARK MASORA CIRCLE", #֯
        "ARABIC END OF AYAH", #۝
        "COMBINING ENCLOSING CIRCLE", #⃝
        "COMBINING ENCLOSING CIRCLE BACKSLASH", #⃠
        "APL FUNCTIONAL SYMBOL CIRCLE STILE", #⌽
        "APL FUNCTIONAL SYMBOL CIRCLE JOT", #⌾
        "APL FUNCTIONAL SYMBOL CIRCLE BACKSLASH", #⍉
        "APL FUNCTIONAL SYMBOL CIRCLE UNDERBAR", #⍜
        "APL FUNCTIONAL SYMBOL CIRCLE STAR", #⍟
        "APL FUNCTIONAL SYMBOL CIRCLE DIAERESIS", #⍥
        "BROKEN CIRCLE WITH NORTHWEST ARROW", #⎋
        "DENTISTRY SYMBOL LIGHT VERTICAL WITH CIRCLE", #⏀
        "DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH CIRCLE", #⏁
        "DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH CIRCLE", #⏂
        "BENZENE RING WITH CIRCLE", #⏣
        "BULLSEYE", # ◎
        "WHITE CIRCLE", #○
        "DOTTED CIRCLE", #◌
        "CIRCLE WITH VERTICAL FILL", #◍
        "BLACK CIRCLE", #●
        "CIRCLE WITH LEFT HALF BLACK", #◐
        "CIRCLE WITH RIGHT HALF BLACK", #◑
        "CIRCLE WITH LOWER HALF BLACK", #◒
        "CIRCLE WITH UPPER HALF BLACK", #◓
        "CIRCLE WITH UPPER RIGHT QUADRANT BLACK", #◔
        "CIRCLE WITH ALL BUT UPPER LEFT QUADRANT BLACK", #◕
        "INVERSE WHITE CIRCLE", #◙
        "LARGE CIRCLE", #◯
        "WHITE CIRCLE WITH UPPER LEFT QUADRANT", #◴
        "WHITE CIRCLE WITH LOWER LEFT QUADRANT", #◵
        "WHITE CIRCLE WITH LOWER RIGHT QUADRANT", #◶
        "WHITE CIRCLE WITH UPPER RIGHT QUADRANT", #◷
        "WHITE CIRCLE WITH DOT RIGHT", #⚆
        "WHITE CIRCLE WITH TWO DOTS", #⚇
        "BLACK CIRCLE WITH WHITE DOT RIGHT", #⚈
        "BLACK CIRCLE WITH TWO WHITE DOTS", #⚉
        "MEDIUM WHITE CIRCLE", #⚪
        "MEDIUM BLACK CIRCLE", #⚫
        "MEDIUM SMALL WHITE CIRCLE", #⚬
        "SHADOWED WHITE CIRCLE", #❍
        "ANTICLOCKWISE GAPPED CIRCLE ARROW", #⟲
        "CLOCKWISE GAPPED CIRCLE ARROW", #⟳
        "ANTICLOCKWISE CLOSED CIRCLE ARROW", #⥀
        "CLOCKWISE CLOSED CIRCLE ARROW", #⥁
        "EMPTY SET WITH SMALL CIRCLE ABOVE", #⦲
        "CIRCLE WITH HORIZONTAL BAR", #⦵
        "CIRCLE WITH SMALL CIRCLE TO THE RIGHT", #⧂
        "CIRCLE WITH TWO HORIZONTAL STROKES TO THE RIGHT", #⧃
        "BLACK LARGE CIRCLE", #⬤
        )

    SHAPE_CHARSET_S = [UP_POINTING_TRIANGLES, DOWN_POINTING_TRIANGLES, LEFT_POINTING_TRIANGLES, RIGHT_POINTING_TRIANGLES, PENTAGONS_AND_LARGER_POLYGONS, QUADRILATERALS, CIRCLES]

    ONE_DOT = unicode_charset("One Dot",
        "Braille pattern dots-3",
        "Braille pattern dots-7",
        "Bullet operator",
        "Bullet",
        "Canadian syllabics final middle dot",
        "Canadian syllabics y-cree w",
        "Combining dot above right",
        "Combining dot above",
        "Combining dot below",
        "Dot above",
        "Full stop",
        "Greek ano teleia",
        "Hebrew mark lower dot",
        "Hebrew point dagesh or mapiq",
        "Hebrew point holam haser for vav",
        "Hebrew point sin dot",
        "Hyphenation point",
        "Medium black circle",
        "Middle dot",
        "Nko combining nasalization mark",
        "Nko combining short rising tone",
        "One dot leader",
        "Syriac feminine dot",
        "Syriac hbasa-esasa dotted",
        "Syriac qushshaya",
        "Syriac rukkakha",
        #"Raised dot",
        )

    TWO_DOTS_HORIZONTAL = unicode_charset("Two Dots Horizontal",
        "Braille pattern dots-14",
        "Braille pattern dots-25",
        "Braille pattern dots-36",
        "Braille pattern dots-78",
        "Byzantine musical symbol dipli",
        "Byzantine musical symbol isakia telous ichimatos",
        "Combining diaeresis below",
        "Combining diaeresis",
        "Diaeresis",
        "Double prime",
        "Double low-9 quotation mark",
        "Hebrew point tsere",
        "Hebrew punctuation gershayim",
        "Left double quotation mark",
        "Nko combining double dot above",
        "Right double quotation mark",
        "Syriac dotted zlama angular",
        "Syriac dotted zlama horizontal",
        "Syriac horizontal colon",
        "Two dot leader",
        )

    TWO_DOTS_VERTICAL = unicode_charset("Two Dots Vertical",
        "Arabic semicolon",
        "Armenian full stop",
        "Braille pattern dots-13",
        "Braille pattern dots-17",
        "Braille pattern dots-27",
        "Braille pattern dots-46",
        "Braille pattern dots-48",
        "Braille pattern dots-58",
        "Colon",
        "Greek question mark",
        "Hebrew punctuation sof pasuq",
        "Modifier letter colon",
        "Modifier letter raised colon",
        "Modifier letter triangular colon",
        "Musical symbol repeat dots",
        "Ratio",
        "Reversed semicolon",
        "Semicolon",
        "Syriac pthaha dotted",
        "Syriac sublinear colon",
        "Syriac supralinear colon",
        "Two dot punctuation",
        )

    TWO_DOTS_DIAGONAL = unicode_charset("Two Dots Diagonal",
        "Braille pattern dots-15",
        "Braille pattern dots-15",
        "Braille pattern dots-15",
        "Braille pattern dots-15",
        "Braille pattern dots-16",
        "Braille pattern dots-18",
        "Braille pattern dots-24",
        "Braille pattern dots-26",
        "Braille pattern dots-28",
        "Braille pattern dots-34",
        "Braille pattern dots-35",
        "Braille pattern dots-38",
        "Braille pattern dots-47",
        "Braille pattern dots-57",
        "Braille pattern dots-67",
        "Syriac colon skewed left",
        "Syriac sublinear colon skewed right",
        # "Syriac supralinear colon skewed left ",
        )

    TWO_DOTS = TWO_DOTS_HORIZONTAL + TWO_DOTS_VERTICAL + TWO_DOTS_DIAGONAL

    MULTI_DOTS_VERTICAL = unicode_charset("Many Dots Vertical",
        "Vertical ellipsis",
        "Tifinagh letter tuareg yagh",
        "Braille pattern dots-458",
        # "Triple colon operator",
        "Braille pattern dots-137",
        "Braille pattern dots-127",
        "Braille pattern dots-468",
        "Tricolon",
        "Latin small letter i with dot below",
        "Braille pattern dots-237",
        "Ethiopic question mark",
        "Braille pattern dots-456",
        "Braille pattern dots-568",
        "Braille pattern dots-123",
        "Dotted fence",
        "Tifinagh letter tuareg yah",
        )

    MULTI_DOTS_HORIZONTAL = unicode_charset("Many Dots Horizontal",
        "Horizontal ellipsis",
        "Midline horizontal ellipsis",
        "Monogram for earth",
        "Box drawings light triple dash horizontal",
        "Combining three dots above",
        "Tifinagh letter tuareg yaq",
        "Byzantine musical symbol saximata",
        "Box drawings heavy triple dash horizontal",
        "Combining triple underdot",
        "Byzantine musical symbol tripli",
        "Box drawings light quadruple dash horizontal",
        "Combining four dots above",
        "Ocr customer account number",
        "Box drawings heavy quadruple dash horizontal",
        "Byzantine musical symbol tetrapli",
        "Triple prime",
        "Vai syllable di",
        )

    MULTI_DOTS_DIAGONAL = unicode_charset("Many Dots Diagonal",
        "Down right diagonal ellipsis",
        "Hebrew point qubuts",
        "Buginese pallawa",
        "Up right diagonal ellipsis",
        "Ocr amount of check",
        "Braille pattern dots-347",
        "Braille pattern dots-457",
        "Byzantine musical symbol dyo"
        )

    MULTI_DOTS_MISC = unicode_charset("Many Dots Miscellaneous",
        # "Drive slow sign",
        "Proportion",
        "Tifinagh letter tuareg yakh",
        "Braille pattern dots-1346",
        "Squared four dot punctuation",
        "Braille pattern dots-2578",
        "Braille pattern dots-1478",
        "Braille pattern dots-1467",
        "Braille pattern dots-1245",
        "Ethiopic full stop",
        "Tifinagh letter ayer yagh",
        "Braille pattern dots-1358",
        "Braille pattern dots-13456",
        "Braille pattern dots-23578",
        "Digram for earth",
        "Combining cyrillic ten millions sign",
        )

    MULTI_DOTS = MULTI_DOTS_HORIZONTAL + MULTI_DOTS_VERTICAL + MULTI_DOTS_DIAGONAL + MULTI_DOTS_MISC

    DOTS = ONE_DOT + TWO_DOTS + MULTI_DOTS

    DOT_CHARSET_S = [ONE_DOT, TWO_DOTS, DOTS]

    # Small custom charsets that make nice mosaics when combined.
    TRIANGLE_MOSAIC = unicode_charset("Triangle Mosaic",
            "Black lower left triangle",
            "Black lower right triangle",
            "Black upper left triangle",
            "Black upper right triangle",
            )

    BLOCK_MOSAIC = unicode_charset("Block Mosaic",
            "UPPER HALF BLOCK",
            "LOWER HALF BLOCK",
            "FULL BLOCK",
            "LEFT HALF BLOCK",
            "RIGHT HALF BLOCK",
            )

    VERTICAL_BLOCK_MOSAIC = unicode_charset("Vertical Block Mosaic",
            "UPPER HALF BLOCK",
            "LOWER HALF BLOCK",
            "FULL BLOCK",
            )

    HORIZONTAL_BLOCK_MOSAIC = unicode_charset("Horizontal Block Mosaic",
            "LEFT HALF BLOCK",
            "RIGHT HALF BLOCK",
            "FULL BLOCK",
            )

    TERMINAL_GRAPHIC_MOSAIC = unicode_charset("Terminal Graphic Mosaic",
            "QUADRANT LOWER LEFT",
            "QUADRANT LOWER RIGHT",
            "QUADRANT UPPER LEFT",
            "QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT",
            "QUADRANT UPPER LEFT AND LOWER RIGHT",
            "QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT",
            "QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT",
            "QUADRANT UPPER RIGHT",
            "QUADRANT UPPER RIGHT AND LOWER LEFT",
            "QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT",
            )

    SHADING_MOSAIC = unicode_charset("Shading Mosaic",
            "LIGHT SHADE",
            "MEDIUM SHADE",
            "DARK SHADE",
            "FULL BLOCK",
            )

    FILL_MOSAIC = unicode_charset("Fill Mosaic",
        "SQUARE WITH HORIZONTAL FILL", #▤
        "SQUARE WITH VERTICAL FILL", #▥
        "SQUARE WITH ORTHOGONAL CROSSHATCH FILL", #▦
        "SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL", #▧
        "SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL", #▨
        "SQUARE WITH DIAGONAL CROSSHATCH FILL", #▩
        )

    BOX_DRAWING_MOSAIC = unicode_charset("Box Drawing Light Mosaic",
            "BOX DRAWINGS LIGHT DOWN AND RIGHT",
            "BOX DRAWINGS LIGHT DOWN AND LEFT",
            "BOX DRAWINGS LIGHT UP AND LEFT",
            "BOX DRAWINGS LIGHT UP AND RIGHT",
            )

    BOX_DRAWING_HEAVY_MOSAIC = unicode_charset("Box Drawing Heavy Mosaic",
        "BOX DRAWINGS HEAVY HORIZONTAL", #━
        "BOX DRAWINGS HEAVY VERTICAL", #┃
        "BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL", #┅
        "BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL", #┇
        "BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL", #┉
        "BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL", #┋
        "BOX DRAWINGS HEAVY DOWN AND RIGHT", #┏
        "BOX DRAWINGS HEAVY DOWN AND LEFT", #┓
        "BOX DRAWINGS HEAVY UP AND RIGHT", #┗
        "BOX DRAWINGS HEAVY UP AND LEFT", #┛
        "BOX DRAWINGS HEAVY VERTICAL AND RIGHT", #┣
        "BOX DRAWINGS HEAVY VERTICAL AND LEFT", #┫
        "BOX DRAWINGS HEAVY DOWN AND HORIZONTAL", #┳
        "BOX DRAWINGS HEAVY UP AND HORIZONTAL", #┻
        "BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL", #╋
        "BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL", #╍
        "BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL", #╏
        "BOX DRAWINGS HEAVY LEFT", #╸
        "BOX DRAWINGS HEAVY UP", #╹
        "BOX DRAWINGS HEAVY RIGHT", #╺
        "BOX DRAWINGS HEAVY DOWN", #╻
        )

    BOX_DRAWING_ARC_MOSAIC = unicode_charset("Box Drawing Arc Mosaic",
            "BOX DRAWINGS LIGHT ARC DOWN AND RIGHT",
            "BOX DRAWINGS LIGHT ARC DOWN AND LEFT",
            "BOX DRAWINGS LIGHT ARC UP AND LEFT",
            "BOX DRAWINGS LIGHT ARC UP AND RIGHT",
            )

    CHARACTER_CELL_DIAGONAL_MOSAIC = unicode_charset("Character Cell Diagonal Mosaic",
            "BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT",
            "BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT",
            "BOX DRAWINGS LIGHT DIAGONAL CROSS",
            )

    PARTIALLY_FILLED_SQUARE_MOSAIC_DIAGONALS_ONLY = unicode_charset("Partially Filled Square Mosaic (Diagonals Only)",
        "SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK", #⬔
        "SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK", #⬕
        "SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK", #◪
        "SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK", #◩
        )

    PARTIALLY_FILLED_SQUARE_MOSAIC = unicode_charset(
        "Partially Filled Square Mosaic",
        "SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK", #⬔
        "SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK", #⬕
        "SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK", #◪
        "SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK", #◩
        "SQUARE WITH LEFT HALF BLACK", #◧
        "SQUARE WITH RIGHT HALF BLACK", #◨
        "SQUARE WITH TOP HALF BLACK", #⬒
        "SQUARE WITH BOTTOM HALF BLACK", #⬓
        )

    PARTIALLY_FILLED_CIRCLE_MOSAIC = unicode_charset("Partially Filled Circle Mosaic",
        "BLACK CIRCLE", #●
        "CIRCLE WITH LEFT HALF BLACK", #◐
        "CIRCLE WITH RIGHT HALF BLACK", #◑
        "CIRCLE WITH LOWER HALF BLACK", #◒
        "CIRCLE WITH UPPER HALF BLACK", #◓
        "CIRCLE WITH UPPER RIGHT QUADRANT BLACK", #◔
        "CIRCLE WITH ALL BUT UPPER LEFT QUADRANT BLACK", #◕
        )

    # These charsets can make a (potentially mirrorable) mosaic 
    # in conjunction with EM SPACE.
    TILABLE_CHARSET_S = [
        CUSTOM_ALPHABETS["Box Drawing Dots"],
        CUSTOM_ALPHABETS["Box Drawing Thick and Thin"],
        CUSTOM_ALPHABETS["Box Drawing Single and Double"],
        CUSTOM_ALPHABETS["Box Drawing Double"],
        CUSTOM_ALPHABETS["Block Drawing by Width"],
        CUSTOM_ALPHABETS["Block Drawing by Height"],
        "Yijing Hexagram Symbols",
        "Tai Xuan Jing Symbols",
        "Braille Patterns",
        "Emoji",
        BLOCK_MOSAIC,
        # CUSTOM_ALPHABETS["Box Drawing All"],
        # BOX_DRAWING_ARC_MOSAIC,
        PARTIALLY_FILLED_CIRCLE_MOSAIC,
        BOX_DRAWING_HEAVY_MOSAIC,
        BOX_DRAWING_MOSAIC,
        CHARACTER_CELL_DIAGONAL_MOSAIC,
        FILL_MOSAIC,
        HORIZONTAL_BLOCK_MOSAIC,
        PARTIALLY_FILLED_SQUARE_MOSAIC,
        SHADING_MOSAIC,
        TERMINAL_GRAPHIC_MOSAIC,
        VERTICAL_BLOCK_MOSAIC,
        RECTANGLES,
    ]

    MOSAIC_CHARSET_S = [
        CUSTOM_ALPHABETS["Completely Circled Alphabetics"],
        CUSTOM_ALPHABETS["Fullwidth Alphabetics"],
        CUSTOM_ALPHABETS["Double Circled Numerics"],
        CUSTOM_ALPHABETS["Filled Circled Numerics"],
        CUSTOM_ALPHABETS["Empty Circled Numerics"],
        CUSTOM_ALPHABETS["Dice"],
        CUSTOM_ALPHABETS["Box Drawing All"],
        CUSTOM_ALPHABETS["Box Drawing Dots"],
        CUSTOM_ALPHABETS["Box Drawing Thick and Thin"],
        CUSTOM_ALPHABETS["Box Drawing Single and Double"],
        CUSTOM_ALPHABETS["Box Drawing Double"],
        CUSTOM_ALPHABETS["Block Drawing by Width"],
        CUSTOM_ALPHABETS["Block Drawing by Height"],
        CUSTOM_ALPHABETS["Skin Tones"],
        RECTANGLES,
        BLOCK_MOSAIC,
        BOX_DRAWING_ARC_MOSAIC,
        BOX_DRAWING_HEAVY_MOSAIC,
        BOX_DRAWING_MOSAIC,
        CHARACTER_CELL_DIAGONAL_MOSAIC,
        FILL_MOSAIC,
        HORIZONTAL_BLOCK_MOSAIC,
        PARTIALLY_FILLED_CIRCLE_MOSAIC,
        PARTIALLY_FILLED_SQUARE_MOSAIC,
        SHADING_MOSAIC,
        TERMINAL_GRAPHIC_MOSAIC,
        VERTICAL_BLOCK_MOSAIC,
        TRIANGLES,
        ]

    EMOJI_S = [
        "Miscellaneous Symbols And Pictographs",
        "Transport and Map Symbols",
        "Emoticons",
        ]

    WHITESPACE = unicode_charset(
        "NO-BREAK SPACE",
        "EN QUAD",
        "EM QUAD",
        "EN SPACE",
        "EM SPACE",
        "THREE-PER-EM SPACE",
        "FOUR-PER-EM SPACE",
        "SIX-PER-EM SPACE",
        "FIGURE SPACE",
        "PUNCTUATION SPACE",
        "THIN SPACE",
        "HAIR SPACE",
        "NARROW NO-BREAK SPACE",
        "MEDIUM MATHEMATICAL SPACE",
        "IDEOGRAPHIC SPACE",
    )


# Content from: ./olipy/corpora.py
"""A port of Allison Parrish's pycorpora module.

This was necessary to a) add extra stuff like word lists using the
same mechanism defined by pycorpora and b) include an actual copy of
the Corpora Project with a packaged Python module.
"""
import os
import sys
import json

cache = dict()
loaders = []

this_dir = os.path.split(__file__)[0]
data_path = os.path.join(this_dir, "data")
components = [
    (data_path, "corpora-original", "data"),
    (data_path, "corpora-olipy")
]
data_directories = [os.path.join(*x) for x in components]

def _read(path):
    if not path in cache:
        if not os.path.exists(path):
            return
        data = json.load(open(path))
        cache[path] = data
    return cache[path]

def fetch_resource(name, *directories):
    directories = directories or data_directories
    result = None
    for directory in reversed(directories):
        path = os.path.join(directory, name)
        result = _read(path)
        if not result:
            continue
    return result

def get_categories(name=None, *directories):
    categories = []
    directories = directories or data_directories
    for directory in directories:
        if name:
            directory = os.path.join(directory, name)
        if not os.path.isdir(directory):
            continue
        for x in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, x)):
                categories.append(x)
        return categories

def get_files(name=None, *directories):
    files = []
    directories = directories or data_directories
    for directory in directories:
        if name:
            directory = os.path.join(directory, name)
        if not os.path.isdir(directory):
            continue
        for x in os.listdir(directory):
            path = os.path.join(directory, x)
            if (not os.path.isdir(path) and path.endswith(".json")):
                files.append(x[:-5])
    return files

def get_file(*components):
    return fetch_resource(os.path.join(*components) + ".json")

def load(name):
    """Find the first corpus with the given name and load it from disk."""
    for loader in loaders:
        value = loader.search(name)
        if value:
            return value

def names():
    """Generate a list of all corpus names."""
    for loader in loaders:
        for name in loader.names:
            yield name

class CorpusLoader(object):
    def __init__(self, *directories):
        self.directories = list(directories)

    def __getitem__(self, key):
        return self.__getattr__(key)

    @property
    def children(self):
        by_filename = {}
        for directory in self.directories:
            for filename in sorted(os.listdir(directory)):
                path = os.path.join(directory, filename)
                if not os.path.isdir(path):
                    continue
                loader = by_filename.get(filename)
                if not loader:
                    loader = CorpusLoader()
                    by_filename[filename] = loader
                loader.directories.append(path)

        return by_filename.values()

    @property
    def names(self):
        for directory in self.directories:
            for filename in sorted(os.listdir(directory)):
                path = os.path.join(directory, filename)
                if os.path.isdir(path):
                    continue
                if not path.endswith(".json"):
                    continue
                yield filename[:-5]

    def search(self, name):
        for filename in self.names:
            if name == filename:
                return self.__getattr__(name)
        for loader in self.children:
            value = loader.search(name)
            if value:
                return value

    def __getattr__(self, attr):
        """If `attr` designates a file, load it as JSON and return it."""
        loader = None
        for directory in self.directories:
            file_loc =os.path.join(directory, attr + '.json')
            dir_loc = os.path.join(directory, attr)
            if os.path.exists(file_loc):
                return _read(file_loc)
            elif os.path.isdir(dir_loc):
                if not loader:
                    loader = CorpusLoader()
                loader.directories.append(dir_loc)
        if loader:
            return loader
        raise AttributeError("no resource named " + attr)

    def get_categories(self):
        return get_categories(None, *self.directories)

    def get_files(self):
        return get_files(None, *self.directories)

    def get_file(self, *components):
        path = os.path.join(*components)
        return _read(path)

# Load the standard corpora data from corpora-original/data and the
# olipy extensions from corpora-more.
module = sys.modules[__name__]
for subdir in data_directories:
    for resource_type in sorted(os.listdir(subdir)):
        directory = os.path.join(subdir, resource_type)
        if not os.path.isdir(directory):
            continue
        var = resource_type.replace("-", "_")
        loader = getattr(module, var, None)
        if not loader:
            loader = CorpusLoader()
            loaders.append(loader)
            setattr(module, var, loader)
        loader.directories.append(directory)


# Content from: ./olipy/ebooks.py
import random
import re
import textwrap
from textblob import TextBlob, Sentence
from olipy import corpora
stopwords = corpora.words.stopwords.en

from olipy.tokenizer import WordTokenizer

class EbooksQuotes(object):

    def __init__(
        self, keywords=None, probability=0.001,
        minimum_quote_size=8, maximum_quote_size=140,
        wrap_at=30, truncate_chance=1.0/4):
        keywords = keywords or []
        self.keywords = [x.lower() for x in keywords]
        self.probability = probability
        self.minimum_quote_size = minimum_quote_size
        self.maximum_quote_size = maximum_quote_size
        self.wrap_at = wrap_at
        self.truncate_chance = truncate_chance
        self._blobs = {}

    COMMON_STARTING_WORDS= [
        "I","How","The","You","What","A","Why",
        "And","This","It","Do","In","We","Learn","If",
        "But","Don't","Your","When","Discover",
        "Are","Get","There","My","Have","To","That",
        "As","Make","Let","One"]

    # Quotes that end in certain parts of speech get higher ratings.
    PART_OF_SPEECH_SCORE_MULTIPLIERS = {
        "NNP": 3.2,
        "NNS": 2.7,
        "NN": 2.5,
        "VGD": 1.9,
        "VBG": 1.9,
        "PRP": 1.8,
        "VB": 1.6,
        "JJR": 1.3,
        "CD": 1.2,
        "RB": 1.2,
        "VBP": 1}

    PUNCTUATION_AND_COMMON_STARTING_WORD = re.compile('[.!?"] (%s) ' % (
            "|".join(COMMON_STARTING_WORDS)))

    SEVERAL_CAPITALIZED_WORDS = re.compile("(([A-Z][a-zA-Z]+,? ){2,}[A-Z][a-zA-Z]+[!?.]?)")

    ONE_LETTER = re.compile("[A-Za-z]")
    ONE_WORD = re.compile("\W+")

    data = ['" ', "' ", "--", '\)', ']', ',', '\.', '-']
    BEGINNING_CRUFT = re.compile("^(%s)" % "|".join(data))

    TOKENIZER = WordTokenizer()

    @classmethod
    def rate(cls, s, base_score=1.0, frequencies=None, obscurity_cutoff=None):
        "Rate a string's suitability as an _ebook quote."
        s = s.strip()
        score = float(base_score)
        # print s
        # print " Starting rating: %.2f" % score

        # People like very short or very long quotes.
        # if len(s) < 40:
        #    score *= 2
        if len(s) > 128:
            score *= 2
            # print " Length bonus: %.2f" % score

        blob = TextBlob(s.decode("utf8"))
        try:
            words = blob.words
        except Exception as e:
            # TODO: I'm sick of trying to get TextBlob to parse
            # strings that include things like ". . . ". Just return
            # the current score.
            return score

        if frequencies:
            contains_known_word = False
            contains_obscure_word = False
            for word in words:
                l = word.lower()
                if l in frequencies:
                    contains_known_word = True
                    if frequencies[l] < obscurity_cutoff:
                        contains_obscure_word = True
                if contains_known_word and contains_obscure_word:
                    break

            # A string that contains no words that appear in the
            # frequency list is heavily penalized. It's probably
            # gibberish.
            if not contains_known_word:
                score *= 0.1
                # print " No known word: %.2f" % score

            # A string that contains no obscure words is even more
            # heavily penalized. It's almost certainly boring.
            if not contains_obscure_word:
                score *= 0.01
                # print " No obscure word: %.2f" % score

        if s[0].upper() == s[0]:
            # We like quotes that start with uppercase letters.
            score *= 2.5
            # print " Starts with uppercase letter: %.2f" % score

        # Let's take a look at the first and last words.
        first_word, ignore = blob.tags[0]
        if first_word.capitalize() in cls.COMMON_STARTING_WORDS:
            score *= 2.5
            # print " Starts with common starting word: %.2f" % score

        last_word, last_tag = blob.tags[-1]
        if last_tag in cls.PART_OF_SPEECH_SCORE_MULTIPLIERS:
            score *= cls.PART_OF_SPEECH_SCORE_MULTIPLIERS[last_tag]
            # print " Bonus for part of speech %s: %.2f" % (last_tag, score)

        if last_tag != 'NNP' and last_word[0].upper() == last_word[0]:
            score *= 1.25
            # print " Bonus for ending with a capitalized word: %.2f" % score
        # print "Final score: %.2f" % score
        return score

    # Ways of further tweaking a quote.
    def one_sentence_from(self, quote):
        """Reduce the given quote to a single sentence.

        The choice is biased against the first sentence, which is less likely
        to be the start of a real in-text sentence.
        """
        blob = TextBlob(quote)
        try:
            sentences = blob.sentences
        except Exception as e:
            # TextBlob can't parse this. Just return the whole string
            return quote
        if len(sentences) > 1 and len(sentences[-1]) < 10:
            # Don't choose a very short sentence if it's at the end of a chunk.
            sentences = sentences[:-1]
        s = random.choice(sentences)
        if s == sentences[0]:
            s = random.choice(sentences)
            if s == sentences[0]:
                s = random.choice(sentences)

        return s

    def remove_beginning_punctuation(self, string):
        old_string = None
        while string != old_string:
            old_string = string
            string = self.BEGINNING_CRUFT.sub("", string)
        return string

    def remove_ending_punctuation(self, string):
        # Notably absent: dash and colon, which make a quote
        # funnier.
        if isinstance(string, Sentence):
            string = string.string
        if string.count('"') == 1:
            string = string.replace('"', "")
        string = string.replace("_", "")
        while string and string[-1] in ',; ':
            string = string[:-1]
        return string

    def truncate_to_common_word(self, text):
        m = self.PUNCTUATION_AND_COMMON_STARTING_WORD.search(text)
        if m is None:
            return text
        new_text = text[m.span()[0]+2:]
        if len(new_text) < len(text) / 2:
            return text
        return new_text

    def truncate_at_stopword(self, string):
        # Truncate a string at the last stopword not preceded by
        # another stopword.
        # print "%s =>" % string

        if isinstance(string, Sentence):
            words = string.words
        else:
            try:
                words = TextBlob(string).sentences
            except Exception as e:
                # TextBlob can't parse this. Just return the whole string
                return string

        reversed_words = list(reversed(words[2:]))
        for i, w in enumerate(reversed_words):
            if (w in stopwords
                and i != len(reversed_words)-1 and
                not reversed_words[i+1] in stopwords):
                # print "Stopword %s (previous) %s" % (w, reversed_words[i+1])
                r = re.compile(r".*\b(%s)\b" % w)
                string = unicode(string)
                m = r.search(string)
                if m is not None:
                    string = string[:m.span(1)[0]]
                # print "=> %s" % string
                # print "---"
                break
        return string


    def quotes_in(self, paragraph):
        para = textwrap.wrap(paragraph, self.wrap_at)
        if len(para) == 0:
            return

        probability = self.probability
        if para[0][0].upper() == para[0][0]:
            # We greatly prefer lines that start with capital letters.
            probability *= 5
        else:
            probability /= 4

        gathering = False
        in_progress = None
        last_yield = None
        for i in range(len(para)):
            line = para[i]
            if gathering:
                # We are currently putting together a quote.
                done = False
                if (random.random() < self.truncate_chance
                    and len(in_progress) >= self.minimum_quote_size):
                    # Yield a truncated quote.
                    done = True
                else:
                    potential = in_progress + ' ' + line.strip()
                    if len(potential) >= self.maximum_quote_size:
                        # That would be too long. We're done.
                        done = True
                    else:
                        in_progress = potential

                if done:
                    quote = in_progress
                    in_progress = None
                    gathering = done = False

                    # Miscellaneous tweaks to increase the chance that
                    # the quote will be funny.
                    if random.random() < 0.6:
                        quote = self.one_sentence_from(quote)

                    if random.random() < 0.4:
                        quote = self.truncate_at_stopword(quote)

                    # Quotes that end with two consecutive stopwords
                    # are not funny. It would be best to parse every
                    # single quote and make sure it doesn't end with
                    # two consecutive stopwords. But in practice it's
                    # much faster to just check for the biggest
                    # offenders, which all end in 'the', and then trim
                    # the 'the'.
                    low = quote.lower()
                    for stopwords in ('of the', 'in the', 'and the',
                                      'in the', 'on the', 'for the'):
                        if low.endswith(stopwords):
                            quote = quote[:len(" the")-1]
                            break

                    if isinstance(quote, bytes):
                        quote = quote.decode("utf8")
                    quote = self.remove_ending_punctuation(quote)
                    quote = self.remove_beginning_punctuation(quote)

                    if random.random() > 0.75:
                        quote = self.truncate_to_common_word(quote)

                    if (len(quote) >= self.minimum_quote_size
                        and len(quote) <= self.maximum_quote_size
                        and self.ONE_LETTER.search(quote)):
                        yield quote
                        last_yield = quote
                        continue
            else:
                # We are not currently gathering a quote. Should we
                # be?
                r = random.random()
                if random.random() < probability:
                    # Run the regular expression and see if it matches.
                    m = self.SEVERAL_CAPITALIZED_WORDS.search(line)
                    if m is not None:
                        phrase = m.groups()[0]
                        if "Gutenberg" in phrase or "Proofreader" in phrase:
                            # Part of the meta, not part of text.
                            continue
                        # Tag the text to see if it's a proper noun.
                        blob = TextBlob(phrase)
                        tags = blob.tags
                        proper_nouns = [x for x, tag in tags if tag.startswith('NNP')]
                        if len(proper_nouns) < len(tags) / 3.0:
                            # We're good.
                            yield phrase
                            continue

                matches = self._line_matches(line)
                if matches or random.random() < probability:
                    gathering = True
                    if matches:
                        # A keyword match! Start gathering a quote either
                        # at this line or some earlier line.
                        maximum_backtrack = int(
                            self.maximum_quote_size / self.wrap_at) - 1
                        backtrack = random.randint(0, maximum_backtrack)
                        start_at = max(0, i - backtrack)
                        in_progress = " ".join(
                            [x.strip() for x in para[start_at:i+1]])
                    else:
                        in_progress = line.strip()

    def _line_matches(self, line):
        l = line.lower()
        for keyword in self.keywords:
            if keyword in l:
                return True
        return False



# Content from: ./olipy/example.py
import argparse
import json
import logging
import re
import sys
import textwrap
from olipy import corpora
from olipy.ebooks import EbooksQuotes
from olipy.gibberish import (
    Corruptor,
    Gibberish,
)
from olipy.gutenberg import ProjectGutenbergText
from olipy.queneau import (
    Assembler,
    CompositeAssembler,
    DialogueAssembler,
    WordAssembler,
)
from olipy.typewriter import Typewriter

def apollo():
    transcript = corpora.words.literature.nonfiction.apollo_11['transcript']
    d = DialogueAssembler.loadlist(transcript)
    last_speaker = None
    for i in range(1, 100):
        speaker, tokens = d.assemble(last_speaker)
        last_speaker = speaker
        print("%s: %s" % (speaker, " ".join(x for x, y in tokens)))

def board_games(how_many=10):
    corpus = Assembler.loadlist(
        corpora.games.bgg_board_games['board_games'], tokens_in='description'
    )

    no_punctuation_at_end = re.compile("[a-zA-Z0-9]$")
    whitespace = re.compile("\s+")

    for i in range(how_many):

        sentences = []
        names = []
        genres = []
        mechanics = []
        for line, source in corpus.assemble("0.l"):
            if no_punctuation_at_end.search(line):
                line += "."
            sentences.append(line)
            names.append(source['name'])
            genres.append([genre for id, genre in source.get('boardgamecategory', [])])
            mechanics.append([mechanic for id, mechanic in source.get('boardgamemechanic', [])])

        # Make assemblers for single- and multi-word names.
        single_word_assembler = WordAssembler()
        multi_word_assembler = Assembler()

        # Create a composite assembler that will choose single- and
        # multi-word names in appropriate proportion.
        name_assembler = CompositeAssembler([single_word_assembler, multi_word_assembler])
        for name in names:
            words = whitespace.split(name)
            if len(words) == 1:
                single_word_assembler.add(name)
            else:
                multi_word_assembler.add(words)
        assembler, choice = name_assembler.assemble()
        if assembler == single_word_assembler:
            separator = ''
        else:
            separator = ' '
        print(separator.join([x for x, source in choice]))

        # Make assemblers for the game's genres and mechanics
        for name, l in (('Genres', genres), ('Mechanics', mechanics)):
            assembler = Assembler()
            for list in l:
                assembler.add(list)
            choices = [choice for choice, source in assembler.assemble()]
            print("%s: %s" % (name, ", ".join(choices)))
        print("")

        for s in textwrap.wrap(" ".join(sentences)):
            print(s)
        if i < how_many-1:
            print("-" * 80)

def corrupt():
    """Corrupts whatever you type by adding diacritical marks."""
    if sys.version_info.major == 3:
        i = input
    else:
        i = raw_input

    go = True
    while go:
        data = i("> ")
        if data.strip() == '':
            break
        for corruption in range(10):
            print(Corruptor(corruption).corrupt(data) + "\n")
    
def dinosaurs():
    dinosaurs = corpora.animals.dinosaurs['dinosaurs']
    assembler = WordAssembler(dinosaurs)
    dinos = []
    for i in range(2):
        dino = assembler.assemble_word()
        if dino[0] in 'AEIO':
            dino = "an " + dino
        else:
            dino = "a " + dino
        dinos.append(dino)
    print("Look! Behind that ridge! It's %s fighting %s!" % tuple(dinos))

def ebooks():    
    parser = argparse.ArgumentParser(
        description="Generate pithy _ebooks quotes from Project Gutenberg texts.")
    parser.add_argument(
        '--path', help="The path to a mounted Project Gutenberg CD or DVD.",
        default=None)
    parser.add_argument(
        "keyword", nargs="*", help="Keywords to focus on when making selections.",
        default=["horse"])
    
    args = parser.parse_args()
    ebooks = EbooksQuotes(args.keyword)
    
    if args.path is None:
        default = corpora.words.literature.nonfiction.literary_shrines
        texts = [ProjectGutenbergText(default['text'])]
    else:
        texts = ProjectGutenbergText.texts_on_media(args.path)
    for text in texts:
        total = 0
        for para in text.paragraphs:
            for quote in ebooks.quotes_in(para):
                print(quote.encode("utf8"))
                total += 1
        logging.info("%d quotes found in text" % total)

def gibberish():
    print(Gibberish.random().tweet())
    
def mashteroids(how_many=10):
    import textwrap
    asteroids = corpora.science.minor_planet_details["minor_planets"]

    # Make an assembler to generate asteroid citations.
    corpus = Assembler.loadlist(asteroids, tokens_in='citation')

    for i in range(how_many):
        sentences = []
        names = []
        for sentence, source in corpus.assemble("f.l", min_length=3):
            sentences.append(sentence)
            names.append(source['name'])

        # Make a new assembler from the names of the asteroids that
        # were chosen, and use that to generate a new name
        name_assembler = WordAssembler(names)
        name = name_assembler.assemble_word()
        print(name)
        for s in textwrap.wrap(" ".join(sentences)):
            print(s)
        print("")

def sonnet():
    sonnets = corpora.words.literature.shakespeare_sonnets['sonnets']
    corpus = Assembler.loadlist(sonnets, tokens_in='lines')
    print("\n".join(line for line, source in corpus.assemble('0.l')))
        
def typewriter():
    print(Typewriter(3, 0.5).type(sys.stdin.read()))
    
def words():
    common = corpora.words.english_words['words']
    less_common = corpora.words.english_words['words']
    common_corpus = WordAssembler(common)
    full_corpus = WordAssembler(less_common)

    print('You know "%s", "%s", and "%s".' % tuple(common_corpus.assemble_word() for i in range(3)))
    print('But have you heard of "%s", "%s", or "%s"?' % tuple(full_corpus.assemble_word() for i in range(3)))


if __name__ == '__main__':
    func = sys
    module = sys.modules[__name__]
    getattr(module, sys.argv[1])()


# Content from: ./olipy/gibberish.py
# coding=utf-8
"""Create gibberish from source alphabets."""

from pdb import set_trace
import os
import json
import random
import sys
import unicodedata
from olipy.randomness import Gradient, WanderingMonsterTable, COMMON, UNCOMMON, RARE, VERY_RARE

from olipy.alphabet import *
from olipy.letterforms import alternate_spelling

class WordLength:

    @classmethod
    def random(cls):
        c = random.choice([cls.natural_word_length, cls.completely_random,
                             cls.ten_characters, cls.twenty_characters,
                             cls.short_words, cls.long_words])
        return c

    @classmethod
    def natural_word_length(cls):
        return random.choice([1,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,8,8,9,9,10,10,11])

    @classmethod
    def completely_random(cls):
        return random.randint(1, 140)

    @classmethod
    def ten_characters(cls):
        return 10

    @classmethod
    def twenty_characters(cls):
        return 20

    @classmethod
    def short_words(cls):
        return int(random.gauss(5, 2))

    @classmethod
    def long_words(cls):
        return int(random.gauss(50,20))

class Corruptor(object):
    """Corrupt text by adding diacritical marks."""
    def __init__(self, factor=2):
        """`factor` is the mean number of diacritical marks to be
        added to each character."""
        if factor == 0:
            self.factor = 0
        else:
            self.factor = 1.0/factor
        self.diacritics = Alphabet.characters(
            [Alphabet.DIACRITICAL[0], Alphabet.DIACRITICAL[0],
            "Combining Diacritical Marks for Symbols"])

    def corrupt(self, text):
        if self.factor == 0:
            return text
        new_chars = []
        for i in text:
            new_chars.append(i)
            for j in range(int(random.expovariate(self.factor))):
                new_chars.append(random.choice(self.diacritics))
        return ''.join(new_chars)

class Gibberish(object):

    minimum_length = 3
    can_truncate = True
    end_with = None

    @classmethod
    def from_alphabets(cls, alphabets):
        return cls("".join(Alphabet.characters(alphabets)))

    @classmethod
    def random(self, freq=None):
        return GibberishTable().choice(freq)

    def __init__(self, charset, word_length=None, word_separator=' ', num_words=None):
        self.charset = charset
        self.word_length = word_length
        self.word_separator = word_separator
        self.num_words = num_words

    @classmethod
    def characters_from_set(cls, choices, characters):
        chosen = ''
        for i in range(choices):
            chosen += random.choice(characters)
        return cls(chosen)

    def word(self, length=None):
        length = length or self.word_length()
        t = []
        for i in range(int(length)):
            t.append(random.choice(self.charset))
        return unicodedata.normalize("NFC", u''.join(t))

    def words(self, length):
        words = ''
        i = 0
        attempts = 0
        default_length = length
        while attempts < 1000:
            word_length = None
            if self.word_length is None:
                word_length = default_length
            word = self.word(word_length)
            if not word:
                default_length = int(default_length * 0.85)
            if not words:
                words = word
            else:
                new_words = words + self.word_separator + word
                if len(new_words) > length and not self.can_truncate:
                    break
                words = new_words
            i += 1
            if len(words) >= length or (self.num_words is not None and i > self.num_words):
                break
            attempts += 1
        return words[:int(length)]

    def tweet(self):
        if random.randint(0,4) == 0:
            length = 140
        else:
            if random.randint(0,4) == 0:
                # Short
                mean = 30
                dev = 10
                m = 5
            else:
                # Long
                mean = 90
                dev = 30
                m = 15
            length = int(max(m, min(random.gauss(mean, dev), 140)))
        if self.end_with:
            length -= len(self.end_with)
        length = max(self.minimum_length, length)
        tweet = None
        while not tweet:
            tweet = self.words(length)
            if not tweet:
                length = int(length * 1.15)
            if length > 140:
                break
        if self.end_with:
            tweet += self.end_with
        if not tweet:
            # Apparently it's just not possible.
            return None
        if not tweet[0].strip():
            # This tweet starts with whitespace. Use COMBINING
            # GRAPHEME JOINER to get Twitter to preserve the whitespace.
            tweet = u"\N{COMBINING GRAPHEME JOINER}" + tweet
        if len(tweet) > 140:
            tweet = tweet[:140]
        return tweet

    @classmethod
    def weird_twitter(cls, base_alphabets, alternate_alphabets,
                      mixin_alphabets, how_weird=1):
        """Give an alphabet the "Weird Twitter" treatment.

        A technique borrowed from the namesake Twitter community, in
        which an alphabet's glyphs are replaced by similar glyphs
        and/or junk glyphs.

        `base_alphabets` is a set of alphabets used in normal
        communcation. One of them will be chosen as the base alphabet.

        `alternate_alphabets` is a set of alphabets providing
        strange-looking versions of the glyphs in the base alphabets.

        `mixin alphabets` is a set of alphabets providing unusual
        glyphs that are thematically related to the base alphabet, but
        not normally used.

        `how_weird` is a way to weight the base alphabets against the
        "weird" alphabets. how_weird=0 is not weird at all. Higher
        numbers are weirder.

        Higher numbers for `how_weird` will also tend to introduce
        diacritical marks, symbolic characters, and completely random
        scripts into the alphabet.
        """
        if isinstance(base_alphabets, list):
            letters = Alphabet.random_choice(*base_alphabets)
        else:
            # The base alphabet is a literal string
            letters = base_alphabets

        if how_weird <= 0:
            return Gibberish(letters)

        # Choose a random number of mixins.
        mixins = ''
        for i in range(1, random.randint(1, how_weird+1)):
            mixins += Alphabet.random_choice(*mixin_alphabets)

        # Add either normal-looking letters or weird alternate
        # letters, until the size of the letters matches the size of
        # the mixins.
        while len(letters) < len(mixins):
            if random.randint(0, how_weird) == 0:
                choices = base_alphabets
            else:
                choices = alternate_alphabets

            if choices != base_alphabets or isinstance(base_alphabets, list):
                letters += Alphabet.random_choice(*choices)
            else:
                # Again, the base alphabet is a literal string
                letters += base_alphabets

        alphabet = letters + mixins

        # Possibly throw in some diacritical marks.
        marks = ''
        while random.random() * how_weird > 0.5:
            marks += Alphabet.random_choice(*Alphabet.MODIFIERS)
        alphabet += marks

        # There is a very small chance that a random symbolic or geometric
        # alphabet will be included.
        approximate_size_of_symbolic_alphabet = len(alphabet) / 10
        symbols = ''
        if random.random() * how_weird > 5:
            s = Alphabet.random_choice(*(Alphabet.SYMBOLIC_ALPHABETS + Alphabet.GEOMETRIC_ALPHABETS))
            while len(symbols) < approximate_size_of_symbolic_alphabet:
                symbols += s
        alphabet += symbols

        # And an even smaller chance that part of a random linguistic
        # alphabet will be included. If a large alphabet like "Hangul
        # Syllables" is chosen, this may dominate the rest of the
        # character set!
        approximate_size_of_foreign_alphabet = len(alphabet) / 5
        if random.random() * how_weird > 7:
            c = random.choice(Alphabet.ALL_LANGUAGE_ALPHABETS_S)
            if not isinstance(c, list):
                c = [c]
            foreign_alphabet = Alphabet.random_choice(*c)
            f = ''
            while len(f) < approximate_size_of_foreign_alphabet:
                f += foreign_alphabet
            alphabet += f

        return Gibberish(alphabet)

    @classmethod
    def limited_vocabulary(cls, how_many_characters=None, include_whitespace=None):
        full = Alphabet.random_choice_no_modifiers()
        limited = Alphabet.subset(full, how_many_characters)
        if include_whitespace is None:
            include_whitespace = random.random() < 0.33
        if include_whitespace:
            limited += random.choice(Alphabet.WHITESPACE)
        return cls(limited)

    @classmethod
    def a_little_weirder_than(self, base_charset):
        """Make the given charset a little more weird."""
        choices = (Alphabet.CUSTOM_S + [Alphabet.YIJING]
                   + [Alphabet.GEOMETRIC_ALPHABETS]
                   + [Alphabet.GAMING_ALPHABETS]
                   + [Alphabet.SYMBOLIC_ALPHABETS]
                   + [Alphabet.WEIRD_TWITTER_MATH_MIXINS]
                   + [Alphabet.DIACRITICAL]
                   + [Alphabet.DIACRITICAL_FULL])
        choice = random.choice(choices)
        extra = Alphabet.characters(choice)

        destination = len(extra) * 3
        multiplied_base_charset = base_charset
        while len(multiplied_base_charset) < destination:
            multiplied_base_charset += base_charset
        return Gibberish(multiplied_base_charset + extra)


class EmoticonGibberish(Gibberish):

    def __init__(self, charsets=None):
        if charsets is None:
            charsets = Alphabet.random_choice_no_modifiers()
        self.charsets = charsets
        self.mouths = u'____⁔𝁛ᨓ⏟‿⏝ω'
        super(EmoticonGibberish, self).__init__(None)

    def word(self, word_length=None):
        charset = random.choice(self.charsets)
        eye = random.choice(charset)

        return eye + random.choice(self.mouths) + eye

    def tweet(self):
        num_words = random.randint(1,3)
        return ' '.join(self.word() for word in range(num_words))

class SamplerGibberish(Gibberish):
    def __init__(self, alphabet=None):
        self.rows = random.randint(1,3)
        self.per_row = random.randint(3,4)
        if self.rows == 1:
            self.per_row += 3
        self.total_size = self.rows * self.per_row
        while not (alphabet and len(alphabet) > self.total_size):
            alphabet = Alphabet.random_choice()
        self.alphabet = alphabet

    def tweet(self):
        whitespace = Alphabet.random_whitespace()
        rows = []
        sample = random.sample(self.alphabet, self.total_size)
        for i in range(self.rows):
            row = ''
            for i in range(self.per_row):
                row += sample.pop()
            rows.append(whitespace.join(row))
        value = "\n".join(rows)
        return value

class GameBoardGibberish(Gibberish):
    def __init__(self, charset=None):
        choices = list(Alphabet.GAMING_ALPHABETS)
        choices.remove("Japanese Chess") # Not enough distinct characters.
        alphabet = random.choice(choices)
        charset = Alphabet.characters(alphabet)
        word_separator = "\n"
        l = random.randint(5, 9)
        num_words = l
        word_length = lambda: l
        super(GameBoardGibberish, self).__init__(
            charset, word_length, word_separator, num_words)

class AlternateSpellingGibberish(Gibberish):
    """The same string every time, but with a different variant of each
    character every time.
    """
    def __init__(self, base_string):
        self.base_string = base_string

    def tweet(self):
        return alternate_spelling(self.base_string)
        
class CheatCodeGibberish(Gibberish):
    "Video game input codes."

    def __init__(self):
        self.base_charset = u'←↑→↓'
        self.fighting_game_charset = self.base_charset + u'↖↗↘↙↺↻PK'
        self.nes_charset = self.base_charset + u'AB'

    def tweet(self):
        num_words = random.randint(5,10)
        if random.randint(0,2) == 0:
            charset = self.fighting_game_charset
        else:
            charset = self.nes_charset
        return ' '.join(random.choice(charset) for word in range(num_words))

class LimitedModifierGibberish(Gibberish):
    def __init__(self, table, num_modifiers=None):
        self.other_generator = table.choice(None)
        self.modifiers = ''
        if num_modifiers is None:
            num_modifiers = int(max(1, random.gauss(1,3)))
        for i in range(num_modifiers):
            modifier_charset = Alphabet.random_choice(*Alphabet.MODIFIERS)
            self.modifiers += random.choice(modifier_charset)

    def tweet(self):
        tweet = self.other_generator.tweet()
        new_tweet = []
        if not tweet:
            return None
        for i in tweet:
            new_tweet += i + random.choice(self.modifiers)
        new_tweet = unicodedata.normalize("NFC", "".join(new_tweet))
        return new_tweet[:140]

class MosaicGibberish(Gibberish):

    def __init__(self, alphabet=None, include_whitespace=None):
        if not alphabet:
            alphabet = random.choice(Alphabet.MOSAIC_CHARSET_S)
        l = int(random.gauss(8,3))
        if include_whitespace is None:
            include_whitespace = random.random() < 0.25
        if include_whitespace:
            choice = random.choice(Alphabet.WHITESPACE)
            size = random.randint(1, len(alphabet)*2)
            alphabet += (choice * size)
        word_length = lambda: l
        word_separator = '\n'
        num_words = None
        self.can_truncate = False
        super(MosaicGibberish, self).__init__(
            alphabet, word_length, word_separator, num_words)

Alphabet.default()

class GibberishGradient(Gibberish):

    minimum_length = 140
    gradient_method = Gradient.gradient

    def __init__(self):
        super(GibberishGradient, self).__init__(None)

    def words(self, length):
        alpha1 = Alphabet.random_choice_no_modifiers()
        alpha2 = Alphabet.random_choice_no_modifiers()
        a = "".join(x for x in self.gradient_method(alpha1, alpha2, length))
        return a

class ModifierGradientGibberish(Gibberish):
    """The alphabet stays the same throughout the tweet, but the modifier
    used slowly changes from one to another.
    """

    minimum_length = 140

    def __init__(self):
        super(ModifierGradientGibberish, self).__init__(None)
        mod1 = Alphabet.random_modifier()
        mod2 = None
        while mod2 is None or mod2 == mod1:
            mod2 = Alphabet.random_modifier()

        alphabet = Alphabet.random_choice_no_modifiers()
        self.a1 = [char + mod1 for char in alphabet]
        self.a2 = [char + mod2 for char in alphabet]

    def words(self, length):
        a = "".join(x for x in Gradient.gradient(self.a1, self.a2, length/2))
        return a

class GibberishRainbowGradient(GibberishGradient):

    minimum_length = 140
    gradient_method = Gradient.rainbow_gradient

class CompositeGibberish(Gibberish):

    def __init__(self, table):
        self.table = table
        super(CompositeGibberish, self).__init__(None)

    SEPARATORS = u"     /\-=#:.,|_⏟"

    def words(self, length):
        num_gibberish = random.randint(2,5)
        size_of_each = (length-num_gibberish) / num_gibberish
        gibberishes = []
        for i in range(int(min(2, size_of_each))):
            g = None
            while g is None or not hasattr(g, 'word_length') or g.word_separator == '\n':
                g = self.table.choice(None)

            gibberishes.append(g.words(size_of_each))
        return random.choice(self.SEPARATORS).join(gibberishes)

class RosettaStoneGibberish(CompositeGibberish):
    """A number of small gibberishes, one per line."""
    SEPARATORS = u"\n"

class GibberishTable(WanderingMonsterTable):

    def __init__(self):
        super(GibberishTable, self).__init__()

        # Populate the table. An entry may be:
        #  * The name of an alphabet, or a list of names.
        #  * A Gibberish object.
        #  * A function that returns a Gibberish object.

        # One of the Cyrillic alphabets.
        self.add(self.choice_among_alphabets(Alphabet.CYRILLIC_S), RARE)

        # One of the Latin alphabets.
        self.add(self.choice_among_alphabets(Alphabet.LATIN_S), UNCOMMON)

        # One of the linguistic alphabets.
        self.add(self.choice_among_alphabets(Alphabet.ALL_LANGUAGE_ALPHABETS_S), COMMON)

        all_but_large_cjk = list(Alphabet.ALL_LANGUAGE_ALPHABETS_S)
        for i in ("CJK Unified Ideographs (Han)", "Hangul Syllables",
                  "CJK Compatibility Ideographs",):
            all_but_large_cjk.remove(i)

        # ALL of the non-huge linguistic alphabets.
        self.add(self.charset_from_alphabets(all_but_large_cjk), VERY_RARE)

        # Some combination of the non-huge linguistic alphabets.
        self.add(self.combination_of_alphabets(all_but_large_cjk), UNCOMMON)

        # A gradient between two alphabets.
        self.add(GibberishGradient, COMMON)
        self.add(GibberishRainbowGradient, UNCOMMON)
        self.add(ModifierGradientGibberish, UNCOMMON)

        # A mirrored mosaic
        from olipy.mosaic import MirroredMosaicGibberish
        self.add(MirroredMosaicGibberish, COMMON)

        # A mirrored mosaic from an untilable alphabet
        def untilable_mirror():
            alphabet = None
            while not alphabet or alphabet in Alphabet.TILABLE_CHARSET_S:
                alphabet = Alphabet.random_choice_no_modifiers()
            limited = Alphabet.subset(alphabet)
            gibberish = MirroredMosaicGibberish(limited)
            return gibberish
        self.add(untilable_mirror, UNCOMMON)

        # One of the geometric alphabets.
        self.add(self.choice_among_alphabets(Alphabet.GEOMETRIC_ALPHABETS), UNCOMMON)

        # One of the custom scripts.
        self.add(self.choice_among_alphabets(Alphabet.CUSTOM_S), UNCOMMON)

        # The combination of all geometric alphabets.
        self.add(Alphabet.GEOMETRIC_ALPHABETS, VERY_RARE)

        # A limited subset of one script.
        self.add(Gibberish.limited_vocabulary, COMMON)

        # A less limited subset of one script.
        self.add(lambda: Gibberish.limited_vocabulary(how_many_characters=3+int(random.gauss(4,2))), UNCOMMON)

        # A limited subset of one script, including whitespace
        self.add(lambda: Gibberish.limited_vocabulary(include_whitespace=True),
                 UNCOMMON)

        # A mosaic charset.
        self.add(MosaicGibberish, UNCOMMON)

        # Some other kind of gibberish with a modifier (chosen from a
        # small subset) applied to every character.
        self.add(lambda: LimitedModifierGibberish(self), COMMON)

        # Composite gibberish
        self.add(lambda: CompositeGibberish(self), UNCOMMON)

        # Composite gibberish, newline-separated
        self.add(lambda: RosettaStoneGibberish(self), UNCOMMON)

        # A game board charset.
        self.add(GameBoardGibberish, VERY_RARE)
        
        # A sampler from a charset.
        self.add(SamplerGibberish, RARE)

        # A shape-based charset
        self.add(self.choice_among_charsets(Alphabet.SHAPE_CHARSET_S), VERY_RARE)

        # A dot-based charset
        self.add(self.choice_among_charsets(Alphabet.DOT_CHARSET_S), UNCOMMON)

        # Weird Latin Twitter
        def weird_latin_twitter():
            return self.weird_twitter(
                [Alphabet.ASCII, Alphabet.LATIN_1],
                Alphabet.WEIRD_TWITTER_LATIN,
                Alphabet.WEIRD_TWITTER_LATIN_MIXINS)
        self.add(weird_latin_twitter, COMMON)

        # Nothing but emoji!
        def nothing_but_emoji():
            self.add(self.choice_among_charsets(Alphabet.EMOJI_S), RARE)

        # Weird Japanese Twitter
        def weird_japanese_twitter():
            return self.weird_twitter(
                ["Hiragana", Alphabet.KATAKANA, Alphabet.KATAKANA_ALL],
                Alphabet.WEIRD_TWITTER_CJK,
                Alphabet.WEIRD_TWITTER_CJK_MIXINS)
        self.add(weird_japanese_twitter, UNCOMMON)

        # Weird CJK Twitter
        def weird_cjk_twitter():
            return self.weird_twitter(
                ["CJK Unified Ideographs (Han)"],
                Alphabet.WEIRD_TWITTER_CJK,
                Alphabet.WEIRD_TWITTER_CJK_MIXINS, None, 10)
        self.add(weird_japanese_twitter, RARE)

        # Weird Math Twitter
        def weird_math_twitter():
            def math_word_length():
                return random.choice([1,1,1,1,1,1,2,2,2,3,3,3,4,4,5])
            return self.weird_twitter(
                "1234567890", Alphabet.WEIRD_TWITTER_MATH,
                Alphabet.WEIRD_TWITTER_MATH_MIXINS, math_word_length)
        self.add(weird_math_twitter, RARE)

        # Emoticons
        self.add(EmoticonGibberish, VERY_RARE)

        # Video game cheat codes.
        self.add(CheatCodeGibberish, VERY_RARE)

    def weird_twitter(self, base, weird, mixins, word_length=None,
                      weird_multiplier=1):
        how_weird = int(random.expovariate(1.0/6)) * weird_multiplier
        gibberish = Gibberish.weird_twitter(
            base, weird, mixins, how_weird)
        gibberish.word_length = word_length
        return gibberish

    def charset_from_alphabets(self, alphabets):
        charset = ''
        for alphabet in alphabets:
            if not isinstance(alphabet, list):
                alphabet = [alphabet]
            charset += Alphabet.characters(alphabet)
        gibberish = Gibberish(charset)
        gibberish.original_alphabets = alphabets
        return gibberish

    def choice_among_alphabets(self, alphabets):
        """Returns a function that chooses an alphabet from a list.

        There is a 33% chance that the charset will be weirded a bit.
        """
        def c():
            alphabet = random.choice(alphabets)
            if not isinstance(alphabet, list):
                alphabet = [alphabet]
            charset = Alphabet.characters(alphabet)
            if random.randint(0,2) == 0:
                # 33% chance to make it a little weirder.
                gibberish = Gibberish.a_little_weirder_than(charset)
            else:
                gibberish = Gibberish(charset)
            gibberish.original_alphabets = alphabets
            return gibberish
        return c

    def combination_of_alphabets(self, alphabets, num=None):
        """Returns a function that chooses a number of alphabets from a list."""
        def combo():
            how_many = num or max(2, int(random.gauss(4,2)))
            if len(alphabets) <= how_many:
                choices = alphabets
            else:
                choices = random.sample(alphabets, how_many)
            gibberish = self.charset_from_alphabets(choices)
            if random.randint(1,10) == 1:
                # 10% chance to make it a little weirder.
                gibberish = Gibberish.a_little_weirder_than(gibberish.charset)
            gibberish.original_alphabets = alphabets
            return gibberish
        return combo

    def choice_among_charsets(self, charsets):
        """Returns a function that chooses a charset from a list.

        There is a 10% chance that the charset will be weirded a bit.
        """
        def c():
            charset = random.choice(charsets)
            if random.randint(1,10) == 1:
                gibberish = Gibberish.a_little_weirder_than(charset)
            else:
                gibberish = Gibberish(charset)
            return gibberish
        return c

    def choice(self, freq):
        gibberish = super(GibberishTable, self).choice(freq)
        if isinstance(gibberish, Gibberish):
            pass
        elif callable(gibberish):
            gibberish = gibberish()
        elif not isinstance(gibberish, list):
            gibberish = [gibberish]
        if isinstance(gibberish, list):
            gibberish = Gibberish.from_alphabets(gibberish)
        if not isinstance(gibberish, Gibberish):
            raise Exception("Cannot turn %r into Gibberish object!", gibberish)

        if gibberish.__class__ != Gibberish:
            # Custom logic. Leave it alone.
            return gibberish

        # 75% chance to add some kind of word boundary algorithm.
        if random.randint(0,100) < 75:
            gibberish.word_length = WordLength.random()

        # Chance to use newline instead of space as word separator
        if (gibberish.word_length is not None
            and gibberish.word_length() >= 15
            and random.randint(0,3) == 0):
            gibberish.word_separator = '\n'

        # Blanket 10% chance to add 10% glitches
        if random.randint(0, 10) == 1:
            glitches = ''
            glitch_charset = Alphabet.random_choice(Alphabet.GLITCHES)
            max_glitches = len(gibberish.charset) / 10
            glitch_characters = ''
            while len(glitch_characters) < max_glitches:
                glitch_characters += random.choice(glitch_charset)
            gibberish.charset += glitch_characters

        # Blanket 10% chance to add an emoji on the end.
        if random.randint(0, 10) == 1:
            gibberish.end_with = " " + random.choice(Alphabet.characters('Emoji'))
        return gibberish

class GlyphNames(object):
    """I know the names of glyphs."""

    def __init__(self):
        self.inverse = dict()
        # self.missing = []
        # self.max_present = None
        for i in range(1, 1000000):
            c = unichr(i)
            try:
                glyph_name = unicodedata.name(c)
                self.inverse[glyph_name] = c
                # self.max_present = i
            except ValueError as e:
                # self.missing.append(i)
                continue

    @classmethod
    def names(self, s):
        """Yield the name of every glyph in the given string."""
        for glyph in s:
            try:
                yield glyph, unicodedata.name(glyph)
            except ValueError as e:
                yield glyph, None

    def matching(self, exp):
        """Yield all name-glyph pairs where the name matches a regexp."""
        for name, value in self.inverse.keys():
            if exp.search(name):
                yield name, value

if __name__ == '__main__':
    freq = None
    alphabets = None

    if len(sys.argv) == 2 and sys.argv[1] in (COMMON, UNCOMMON, RARE, VERY_RARE, None):
        freq = sys.argv[1]
    else:
        alphabets = sys.argv[1:]

    gibberish = None
    if alphabets:
        gibberish = Gibberish.from_alphabets(alphabets)
    table = GibberishTable()
    for i in range(1000):
        if not alphabets:
            gibberish = Gibberish.random(freq)
        print(gibberish.tweet().encode("utf8"))
        print('---')


# Content from: ./olipy/gutenberg.py
import json
import re
import logging
import os
import zipfile
import random
NS = dict()
try:
    import rdflib
    from rdflib.namespace import Namespace
    NS['dcterms'] = Namespace("http://purl.org/dc/terms/")
    NS['dcam'] = Namespace("http://purl.org/dc/dcam/")
    NS['rdf'] = Namespace(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    NS['gutenberg'] = Namespace("http://www.gutenberg.org/2009/pgterms/")
except ImportError as e:
    rdflib = None

class ProjectGutenbergText(object):
    """Class for dealing with Project Gutenberg texts."""

    ids_for_old_filenames = None

    ETEXT_ID = re.compile("^([0-9]+)")
    START = [re.compile("Start[^\n]*Project Gutenberg.*", re.I),
             re.compile("END.THE SMALL PRINT!.*", re.I),
             re.compile("SMALL PRINT!.*\*END\*", re.I),
             re.compile('\["Small Print" V.*', re.I),
             ]

    END = [re.compile("End[^\n]*Project Gutenberg.*", re.I),
           re.compile("of the Project Gutenberg", re.I),
           re.compile("End of this Etext", re.I),
           re.compile("End of\W+Project Gutenberg", re.M),
           re.compile("Ende dieses Projekt Gutenberg Etextes", re.I),
           re.compile("^The Project Gutenberg Etext", re.I),
           re.compile("The Project Gutenberg Etext", re.I),
           ]
    LANGUAGE = re.compile("Language: ([\w -()]+)", re.I)
    ENCODING = re.compile("C.*set encoding: ([\w -]+)", re.I)

    def __init__(self, text, name=None, rdf_catalog_path=None):
        header, text, footer = self.extract_header_and_footer(text)
        self.rdf_catalog_path= rdf_catalog_path
        self._graph = None
        if name is None:
            name = text[:20]   
            self.etext_id = None
        else:
            self.etext_id = self.etext_id_from_filename(name)
        self.name = name

        m = self.ENCODING.search(header)
        if m is None:
            if name.endswith(".utf-8"):
                self.original_encoding = 'utf-8'
            else:
                # Who knows?
                logging.warn("%s specifies no encoding, assuming ASCII." % name)
                self.original_encoding = None
        else:
            enc = m.groups()[0].strip()
            if enc == 'ISO Latin-1':
                enc = 'iso-8859-1'
            elif enc == 'ISO-646-US':
                enc = 'ascii'
            elif enc in 'Unicode UTF-8':
                enc = 'UTF-8'
            elif enc == 'CP-1251':
                enc = 'windows-1251'
            elif enc == 'CP-1252':
                enc = 'windows-1252'

            self.original_encoding = enc

        # Figure out which language(s) the text is in.
        if self.graph is not None:
            # The most reliable source is an RDF graph. If we have one, use it.
            self.languages = set(
                [unicode(x[2]) for x in self.graph.triples((None, NS['dcterms'].language, None))])
        else:
            # Look for a "Language: Foo" bit of text in the header.
            m = self.LANGUAGE.search(header)
            if m is None:
                logging.warn("%s specifies no language." % name)
                self.languages = set([])
            else:
                self.languages = set([m.groups()[0]])

        check_encoding = self.original_encoding or 'ascii'
        self.text = None
        try:
            self.text = unicode(text, check_encoding)
        except Exception as e:
            specified_encoding_is_wrong = ( self.original_encoding is not None)
            for try_encoding in ('utf-8', 'iso-8859-1', 'latin-1'):
                try:
                    if isinstance(text, bytes):
                        self.text = unicode(text, try_encoding)
                    else:
                        self.text = text
                    if specified_encoding_is_wrong:
                        logging.warn("%s claims encoding is %s, but it's actually %s. Original error: %s" % (
                                name, self.original_encoding, try_encoding, e))
                    break
                except UnicodeDecodeError as f:
                    pass
        if self.text is None:
            log.error("Can't determine encoding for %s (specified encoding is %s)" % (
                    name, self.original_encoding))

    def etext_uri(self):
        return "http://www.gutenberg.org/ebooks/%s" % self.etext_id

    @property
    def graph(self):
        if rdflib is None or self.rdf_catalog_path is None:
            return None
        if self._graph is None:
            self._graph = rdflib.Graph()
            self._graph.load(open(self.rdf_path))
        return self._graph

    @property
    def rdf_path(self):
        return os.path.join(
            self.rdf_catalog_path, "cache", "epub",
            str(self.etext_id), "pg%s.rdf" % self.etext_id)

    def etext_id_from_filename(self, path):
        if self.ids_for_old_filenames is None:
            # Load the mapping from JSON.
            this_dir = os.path.split(__file__)[0]
            mapping_file = os.path.join(
                this_dir, 'data', 'ids_for_old_project_gutenberg_filenames.json')
            self.ids_for_old_filenames = json.load(open(mapping_file))

        path_part, filename = os.path.split(path)
        ignore, directory_part = os.path.split(path_part)
        if "etext" in directory_part:
            unique_filename = os.path.join(directory_part, filename)
            return self.ids_for_old_filenames[unique_filename]
        else:
            return int(self.ETEXT_ID.search(filename).groups()[0])

    @classmethod
    def extract_header_and_footer(cls, text):
        """Split a PG document into (header, text, footer) tuple."""
        for s in cls.START:
            m = s.search(text)
            if m is not None:
                break
        if m is None:
            # Make a wild guess.
            start, start2 = 0, 1000
            # import pdb; pdb.set_trace()
        else:
            start, start2 = m.span()
        for s in cls.END:
            m = s.search(text, start2+100)
            if m is not None:
                break
        if m is None:
            # import pdb; pdb.set_trace()
            end =len(text)
            end2 = end
        else:
            end, end2 = m.span()
        return text[:start2], text[start2:end], text[end:]

    FORMAT = re.compile("_([^_]+).zip")

    @classmethod
    def files_on_media(
        cls, mount_path,
        allow_formats=["0", "8", None,], 
        deny_formats=["h", "t", "x", "m", "r", "pdf", "lit", "doc", "pub"],
        start_at=None):
        """Yields paths to zip files on a mounted Gutenberg CD or DVD.

        Yields a given text in at most one format. By default, UTF-8
        is prioritized over ISO-8859-1, which is prioritized over
        ASCII, and no other format is allowed.

        The best way to get Project Gutenberg ISOs is via BitTorrent:
        http://www.gutenberg.org/wiki/Gutenberg:The_CD_and_DVD_Project#Downloading_Via_BitTorrent
        """

        year_directories = ['etext' + x for x in (
                '90',' 91', '92', '93', '94', '95', '96', '97', '98', '99',
                '00', '01', '02', '03', '04', '05', '06')]
        numbered_directories = list(str(x) for x in range(1,10))

        started = (start_at is None)
        # if None in allow_formats:
        #     for directory in year_directories:
        #         # Early PG texts. One directory per year, one format per text.
        #         books_path =  os.path.join(mount_path, str(directory))
        #         for dirpath, dirnames, filenames in os.walk(books_path):
        #             for name in filenames:
        #                 if name.endswith('.zip'):
        #                     if not started and name.startswith(start_at):
        #                         started = True
        #                     if (started and not name.endswith('h.zip')
        #                         and not name.endswith('l.zip')):
        #                         yield os.path.join(dirpath, name)

        for directory in numbered_directories:
            # Later PG texts. One directory per text, each text
            # potentially in several formats.
            books_path =  os.path.join(mount_path, str(directory))
            for dirpath, dirnames, filenames in os.walk(books_path):
                # Does this directory contain a text?
                contains_text = False
                for name in filenames:
                    if name.endswith('.zip'):
                        contains_text = True

                if not contains_text:
                    continue

                formats = {}
                for name in filenames:
                    if not name.endswith('.zip'):
                        continue
                    m = cls.FORMAT.search(name)
                    if m is None:
                        format = None # ASCII text.
                    else:
                        format = m.groups()[0]
                    if format not in deny_formats:
                        formats[format] = name
                # We now have this text in a variety of formats. Yield
                # the highest-priority one.
                for format in allow_formats:
                    if format in formats:
                        if not started and name.startswith(start_at):
                            started = True
                        if started:
                            yield os.path.join(dirpath, formats[format])
                        break

    @classmethod
    def texts_on_media(
        cls, mount_path,
        rdf_catalog_path=None,
        allow_languages=["en", "English"],
        allow_formats=["0", "8", None,], 
        deny_formats=None,
        start_at=None):
        """Yield ProjectGutenbergText objects from a mounted Gutenberg CD or DVD.

        Yields a given text in at most one format. By default, only
        English texts are included. UTF-8 is prioritized over
        ISO-8859-1, which is prioritized over ASCII, and no other
        format is allowed.

        The best way to get Project Gutenberg ISOs is via BitTorrent:
        http://www.gutenberg.org/wiki/Gutenberg:The_CD_and_DVD_Project#Downloading_Via_BitTorrent
        """
        allow_languages = set(allow_languages)
        deny_formats = list(deny_formats or [])
        # We're not set up to handle any of these formats.
        deny_formats.extend(["h", "t", "x", "m", "r", "pdf", "lit", "doc", "pub"])
        for path in cls.files_on_media(mount_path, allow_formats, deny_formats, start_at):
            try:
                text = cls.text_from_zip(path, rdf_catalog_path)
                if not allow_languages or len(text.languages.intersection(allow_languages)) > 0:
                    yield text
            except Exception as e:
                logging.error("%s: %s" % (path, e))
                # raise e

    @classmethod
    def text_from_zip(cls, path, rdf_catalog_path=None):
        """Return a ProjectGutenbergText object from a zip file."""
        archive = zipfile.ZipFile(path)
        inside = archive.filelist
        filenames = [x.filename for x in inside]
        if len(inside) != 1:
            logging.warn("Supposedly plain-text %s has %d files in zip: %s" % (
                    path, len(inside), ", ".join(filenames)))
        possibilities = [x for x in filenames if x.lower().endswith(".txt")]
        data = archive.read(possibilities[0])
        return ProjectGutenbergText(data, path, rdf_catalog_path)

    @property
    def paragraphs(self):
        return self.text.split("\r\n\r\n")



# Content from: ./olipy/ia.py
"""Code for dealing with the Internet Archive."""
import datetime
import internetarchive as ia
import requests
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

class Item(object):
    "Wraps the ia.item class with extra utilities."""

    MEDIA_TYPE = None
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

    _session = None

    def __init__(self, identifier):
        item = metadata = None
        if isinstance(identifier, ia.item.Item):
            # This is an actual Item object from the underlying
            # API wrapper.
            item = identifier
            identifier = item.identifier
            metadata = item.metadata
        elif isinstance(identifier, dict):
            # This is raw metadata from the underlying API wrapper
            item = None
            metadata = identifier
            identifier = identifier['identifier']
        self.identifier = identifier
        self._item = item
        self._metadata = metadata
        self._files = None

    @classmethod
    def session(cls, set_to=None):
        """Keep one ArchiveSession object for the whole program.

        The session doesn't seem to keep any state so this should be
        fine.
        """
        if set_to:
            cls._session = set_to
        if not cls._session:
            cls._session = ia.session.ArchiveSession()
        return cls._session

    @classmethod
    def recent(cls, query="", cutoff=None, fields=None, sorts=None, page=100, *args, **kwargs):
        """Find all the items that match `query` that were added since
        `date`.
        """
        if isinstance(cutoff, basestring):
            cutoff = datetime.datetime.strptime(cutoff, cls.DATE_FORMAT)
        sorts = sorts or []
        sorts.insert(0, 'publicdate desc')

        fields = fields or []
        for item in cls.search(query, *args, fields=fields, sorts=sorts, **kwargs):
            if cutoff and item.date('publicdate') < cutoff:
                break
            yield item


    @classmethod
    def search(cls, query, collection=None, fields=None, sorts=None, *args, **kwargs):
        """Search Internet Archive items.
        :param fields: Retrieve these metadata fields for each item. List of
            fields: https://archive.org/services/search/v1/fields
            By default, 'title', 'publidate', and 'identifier' are retrieved.
        :param sorts: A list of fields to use as sort order. Add
            " asc" or " desc" to the name of the field to specify
            ascending or descending order.
        """
        fields = fields or []
        for mandatory in ['title', 'publicdate']:
            if not mandatory in fields:
                fields.append(mandatory)
        query = cls.modified_query(query, collection)
        search = ia.search.Search(
            cls.session(), query, *args, fields=fields, sorts=sorts,
            **kwargs
        )
        for i in search.iter_as_results():
            yield cls(i)

    @classmethod
    def modified_query(cls, query, collection):
        addenda = []
        if collection:
            addenda.append("collection:%s" % collection)
        if cls.MEDIA_TYPE:
            addenda.append("mediatype:%s" % cls.MEDIA_TYPE)
        if not addenda:
            return query
        if query:
            query += ' and '
        extra = " and ".join(addenda)
        return query + extra

    def date(self, field="date"):
        """Parse a date field associated with this item."""
        if not field.endswith('date'):
            field += 'date'
        data = self.metadata.get(field)
        if not data:
            return None
        parsed = datetime.datetime.strptime(data, self.DATE_FORMAT)
        return parsed

    @property
    def item(self):
        if not self._item:
            self._item = ia.get_item(self.identifier)
        return self._item

    @property
    def files(self):
        if not self._files:
            self._files = list(self.item.get_files())
        return self._files

    @property
    def metadata(self):
        if not self._metadata:
            self._metadata = self.item.metadata
        return self._metadata


class Text(Item):
    """This class knows about the IA book reader."""

    MEDIA_TYPE = "texts"

    # The URL to a specific page in the IA book reader.
    reader_template = "https://archive.org/details/%(identifier)s/page/n%(page)d"

    # The URL to the actual image of a specific page used in the IA book reader.
    reader_image_template = "https://%(server)s/BookReader/BookReaderImages.php?zip=%(zip_path)s&file=%(image_path)s"

    # The path to a ZIP file on an IA server, used to fill in %(zip_path)s in
    # reader_image_template
    zip_path_template = "/%(directory_number)s/items/%(identifier)s/%(archive_filename)s"

    @property
    def pages(self):
        """How many pages are in this book?

        i.e. how many images are in this text?
        """
        return int(self.metadata.get('imagecount', 0))

    @property
    def jp2_url(self):
        """Find the URL to the JP2 version of this text.

        This is essential to finding working image URLs.
        """
        jp2 = [
            x for x in self.files
            if x.format == u'Single Page Processed JP2 ZIP'
            and x.exists
        ]
        if not jp2:
            return None
        return jp2[0].url

    def reader_url(self, page):
        """Generate the URL to the Internet Archive reader for page X."""
        return self.reader_template % dict(
            identifier=self.identifier,
            page=page
        )

    def image_url(self, page, **kwargs):
        """Generate the URL to an image for page X.

        Before using the image you might want to make a HEAD request
        to make sure the image is actually there. The URL generation
        works pretty reliably, but I've seen cases where the book is
        shorter than reported.

        :param kwargs: Will be appended to the URL as extra arguments.
        Useful arguments include 'scale' and 'rotate'.
        """

        # Get the URL to the JP2 version of the text. This is the
        # version used by the web reader, so it's important to know
        # what it's called.
        jp2_url = self.jp2_url

        # Make a HEAD request to the jp2 URL to see which server the
        # file is on and which directory it's in.
        response = requests.head(jp2_url)
        if response.status_code != 302 or not 'location' in response.headers:
            return None
        location = response.headers['location']
        parsed = urlparse.urlparse(location)

        # ZIP files are hosted at servers whose URLs look like this:
        # https://ia600106.us.archive.org/
        server = parsed.netloc

        path = parsed.path.split("/")
        directory_number = path[1]
        jp2_filename = path[-1]

        # The ZIP lives on the server at a path that looks like:
        # /30/items/identifier/A_Great_Book/A_Great_Book_jp2.zip
        zip_path = self.zip_path_template % dict(
            directory_number=directory_number,
            identifier=self.identifier,
            archive_filename=jp2_filename,
        )

        # ZIP files for texts contain one JP2 file per page, in a
        # directory named after the ZIP file:
        # A_Great_Book_jp2/A_Great_Book_0000.jp2
        with_format_identifier = jp2_filename[:-len('.zip')]
        filename_base = jp2_filename[:-len("_jp2.zip")]
        image_filename = filename_base + "_%.4d.jp2" % page
        path_within_file = "/".join([with_format_identifier, image_filename])

        image_url = self.reader_image_template % dict(
            server=server,
            zip_path=zip_path,
            image_path=path_within_file,
        )
        extra = "&".join("%s=%s" % (k, v) for k, v in kwargs.items())
        if extra:
            image_url += "&" + extra
        return image_url


class Audio(Item):
    """This class knows about audio items."""
    MEDIA_TYPE = "audio"


# Content from: ./olipy/letterforms.py
# coding=utf-8
"""Unicode glyphs that resemble other glyphs."""
import random
import string

alternates = {
    "a" : u"",
    "b" : u"",
    "c" : u"ϲᒼᑦсϚⅽ꜀꜂ℂ℃⊏",
    "d" : u"",
    "e" : u"💶ᥱ",    
    "f" : u"ſʄ",
    "g" : u"",    
    "h" : u"ℌᑋ",
    "i" : u"",    
    "j" : u"",
    "k" : u"ⱪ",    
    "l" : u"",
    "m" : u"ϻ⩋ᨓოጦጠᶬ₥ෆ",
    "n" : u"⩏സﬨヘ",
    "o" : u"",    
    "p" : u"ᕵᑭᑭⲢ",
    "q" : u"",    
    "r" : u"╭┌ɼᒋᒥ꜒Γᖋ┍ᒋℾᒋɼґᣘ𝝘ⲅ𝈬꜓⦧",
    "s" : u"",    
    "t" : u"†Ϯϯ┼┽┿╀⍭┾╇+ⵜ╁╪╈╅╅╆╄⨨╂╃╉╊╋╉ߙ⁺ᚐႵ⍖Էէヒナヒモ",
    "u" : u"Цυսᥙɥᐡ",
    "v" : u"",
    "w" : u"ᐜ",    
    "x" : u"☒",
    "y" : u"ʮկ",    
    "z" : u"",

    "A" : u"⍍ᐃ",
    "B" : u"β3",
    "C" : u"ᑕϹСʗⅭⵎᥴⲤƇᑕ",    
    "D" : u"ᐅᑓᑔ",
    "E" : u"⪡ΕꗋΕƐЄᎬⴹЕĘɛℇᙓミ",
    "F" : u"ҒϜғƑߓ𝟋₣ᖴ╒𐌅℉",
    "G" : u"",    
    "H" : u"╫⩆",
    "I" : u"エェヱ",
    "J" : u"",
    "K" : u"ΚƘKК𐌊ҚкⱩⲔκᏦϏҜ𝝟₭ꗪ",    
    "L" : u"レ",
    "M" : u"ΜМϺ𐌑ⅯмⱮӍ𝝡ӎ",
    "N" : u"₪Иⵍи",
    "O" : u"🝕▣⌻⏣⧈0ロ",
    "P" : u"ꝒР♇ҏРΡᏢ⛿ᕈ𐌛Ᵽ𐌓ǷⲢ℗アァ",
    "Q" : u"",    
    "R" : u"𝈖ᎡƦɌⴽᖇ",
    "S" : u"⑀",    
    "T" : u"⊤┬ΤТ⟙ꔋ𝖳┰┯т𝍮⫪┮Ƭ🝨⥡┭Ţ⏉ᚁᎢ┳╥𝝩Ꞇィイフヮワᐪ",
    "U" : u"⋃⨆ᑌ∪ՍⵡŲ∐⌴ᓑԱ⊔𝈈பVリᑌ",
    "V" : u"ᐺ",
    "W" : u"",    
    "X" : u"⪥",
    "Y" : u"߂ЏЦ💴",
    "Z" : u"",
    "-" : u"ー",
}

multi_character_alternates = {
    "B" : ["]3", "|3"],
    "H" : ["|-|", "|=|"],
    "K" : ["]<", ")<", "|<"],
    "O" : ["()", "[]", "{}"],
    "U" : ["|_|"],
    "V" : ["\/"],
}

from olipy.alphabet import CUSTOM_ALPHABETS

alternate_letterforms = {}
for k, v in alternates.items():
    alternate_letterforms[k] = set(v)
for k, v in multi_character_alternates.items():
    alternate_letterforms[k].update(v)

full_alphabet_mapping = string.ascii_uppercase + string.ascii_lowercase
lowercase_alphabet_mapping = string.ascii_lowercase
def map_alphabet(alphabet, mapping=full_alphabet_mapping):
    for i, char in enumerate(alphabet):
        if not char.strip():
            continue
        map_to = mapping[i]
        alternate_letterforms[map_to].add(char)
    
# Incorporate some strings that map the alphabet onto alternate 'fonts'.
for alphabet_name in [
        "Completely Circled Alphabetics",
        "Fullwidth Alphabetics" ,
        "Bold Alphabetics" ,
        "Italic Alphabetics" ,
        "Bold Italic Alphabetics" ,
        "Script Alphabetics" ,
        "Script Bold Alphabetics" ,
        "Fraktur Alphabetics" ,
        "Doublestruck Alphabetics" ,
        "Fraktur Bold Alphabetics" ,
        "Sans Alphabetics" ,
        "Sans Bold Alphabetics" ,
        "Sans Italic Alphabetics" ,
        "Sans Bold Italic Alphabetics" ,
        "Monospace Alphabetics" ,
#        "Alphabetics with Umlaut" ,
]:
    alphabet = CUSTOM_ALPHABETS[alphabet_name]
    map_alphabet(alphabet)

full_alphabets = [
    u"ᴬᴮʿᴰᴱ ᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾ ᴿ ᵀᵁⱽᵂ   ₐᵇ ᵈᵉᶠᵍʰᶤʲᵏˡᵐᵑᵒᵖ ʳˢᵗᵤᵛʷˣʸᶻ",
    u"ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘ ʀꜱᴛᴜᴠᴡ ʏᴢₐ   ₑ  ₕᵢⱼₖₗₘₙₒₚ ᵣₛₜᵤᵥ ₓ  ",
]
for alphabet in full_alphabets:
    map_alphabet(alphabet)
    
lowercase_alphabets = [u"⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵"]
for alphabet in lowercase_alphabets:
    map_alphabet(alphabet, lowercase_alphabet_mapping)
    
# Finally, construct a case-insensitive version of alternate_letterforms.
alternate_letterforms_case_insensitive = dict()
for lower in string.ascii_lowercase:
    upper = lower.upper()
    combined = alternate_letterforms[lower].union(alternate_letterforms[upper])
    for destination in (lower, upper):
        alternate_letterforms_case_insensitive[destination] = combined

def alternate_spelling(string, case_sensitive=False):
    new_string = u""
    if case_sensitive:
        source = alternate_letterforms
    else:
        source = alternate_letterforms_case_insensitive
    for char in string:
        if char in source and source[char]:
            char = random.choice(list(source[char]))
        new_string += char
    return new_string


# Content from: ./olipy/markov.py
from random import choice

class MarkovGenerator(object):

    """A token generator using a Markov chain with configurable order.
    
    Queneau assembly is usually better than a Markov chain above the
    word level (constructing paragraphs from sentences) and below the word
    level (constructing words from phonemes), but Markov chains are
    usually better when assembling sequences of words.
    """

    def __init__(self, order=1, max=500):
        self.order = order # order (length) of ngrams
        self.max = max # maximum number of elements to generate
        self.ngrams = dict() # ngrams as keys; next elements as values
        self.beginnings = list() # beginning ngram of every line

    @classmethod
    def load(cls, f, order=1, max=500):
        """Load from a filehandle that defines a single chunk of text."""
        corpus = MarkovGenerator(order, max)
        corpus.add(f.read())
        return corpus

    @classmethod
    def loadlines(cls, f, order=1, max=500):
        """Load from a filehandle that defines one text per line."""
        corpus = MarkovGenerator(order, max)
        if not hasattr(f, 'read'):
            # Not a file-type object. Treat it as a multi-line string.
            f = f.split("\n")
        for l in f:
            corpus.add(l.strip())
        return corpus

    def tokenize(self, text):
        return text.split(" ")

    def add(self, text):
        tokens = self.tokenize(text)
        # discard this line if it's too short
        if len(tokens) < self.order:
            return

        # store the first ngram of this line
        beginning = tuple(tokens[:self.order])
        self.beginnings.append(beginning)

        i = 0
        for i in range(len(tokens) - self.order):

            gram = tuple(tokens[i:i+self.order])
            next = tokens[i+self.order] # get the element after the gram

            # if we've already seen this ngram, append; otherwise, set the
            # value for this key as a new list
            self.ngrams.setdefault(gram, []).append(next)

        if i > 0:
            # Store the fact that a given token was the last one on the line.
            final_gram = tuple(tokens[i+1:i+self.order+1])
            self.ngrams.setdefault(final_gram, []).append(None)

    # called from generate() to join together generated elements
    def concatenate(self, source):
        return " ".join(source)

    def assemble(self):
        "Yield a new text similar to existing texts."

        # get a random line beginning; convert to a list. 
        current = choice(self.beginnings)
        output = list(current)
        for token in current:
            yield token

        done = False
        for i in range(self.max):
            if current in self.ngrams:
                possible_next = self.ngrams[current]
                next = choice(possible_next)
                if next is None:
                    # This is the final item!
                    done = True
                    break
                yield self.modify(next)
                output.append(next)
                # get the last N entries of the output; we'll use this to look up
                # an ngram in the next iteration of the loop
                current = tuple(output[-self.order:])
            else:
                break

    generate = assemble
    chain = assemble

    def modify(self, token):
        """Modify a token before yielding it."""
        return token

class BracketMatchingMarkovGenerator(MarkovGenerator):

    """A generator that tries to ensure balanced brackets and double quotes.

    It's not perfect, but it's a lot better than nothing.
    """

    def __init__(self, *args, **kwargs):
        super(BracketMatchingMarkovGenerator, self).__init__(*args, **kwargs)
        self.useful_tokens = set([])

    def tokenize(self, text):
        tokens = super(BracketMatchingMarkovGenerator, self).tokenize(text)
        for token in tokens:
            for closing in ['"', ")", "]", "}"]:
                if token.endswith(closing):
                    self.useful_tokens.add(token)
        return tokens

    def assemble(self):
        self.stack = []
        for x in super(BracketMatchingMarkovGenerator, self).assemble():
            yield x

    def modify(self, token_to_yield):
        # Is there an opening bracket in this token?
        for opening, closing in ['""', "()", "[]", "{}"]:
            if opening in token_to_yield:
                index = token_to_yield.find(opening)
                if token_to_yield.find(closing, index+1) == -1:
                    self.stack.append(closing)
            elif closing in token_to_yield:
                # We are closing a bracket. Is there an open bracket?
                if len(self.stack) == 0:
                    #Nope.
                    token_to_yield = token_to_yield.replace(closing, "")
                elif closing != self.stack[-1]:
                    # Force it to be the right kind of bracket.
                    token_to_yield = token_to_yield.replace(
                        closing, self.stack[-1], 1)
                    self.stack.pop()
                else:
                    # It's already the right kind of bracket.
                    self.stack.pop()

        if len(self.stack) > 0:
            # If we modify this token by appending the closing bracket
            # on top of the stack, would we get a token that exists in
            # the corpus?
            check_for = token_to_yield + self.stack[-1]
            if check_for in self.useful_tokens:
                self.stack.pop()
                return check_for
        # No luck. Return the original token.
        return token_to_yield
  
if __name__ == '__main__':
    import sys
    generator = MarkovGenerator.loadlines(sys.stdin, order=1, max=500)
    for i in range(14):
        print(" ".join(list(generator.assemble())))


# Content from: ./olipy/mosaic.py
# encoding: utf-8
from pdb import set_trace
import re
import random
from olipy.randomness import WanderingMonsterTable
from olipy.gibberish import Alphabet, MosaicGibberish

class Mosaic(object):

    @classmethod
    def from_template(self, template, mapping):
        pass

    def __init__(self):
        self.cells = []

    @property
    def width(self):
        return len(self.cells[0])

    @property
    def height(self):
        return len(self.cells)

    def __unicode__(self):
        return "\n".join(self.cells)

class SymmetryList(object):

    def __init__(self, alphabet):
        self.horizontal = [x for x in alphabet if not x in Mirror.horizontal]
        self.vertical = [x for x in alphabet if not x in Mirror.horizontal]
        self.full = [x for x in self.horizontal if x in self.vertical]

    def choice(self, fallback, horizontal=True, vertical=True):
        x = None
        if horizontal and vertical:
            x = self.full
        elif horizontal:
            x = self.horizontal
        elif vertical:
            x = self.vertical
        if x:
            return random.choice(x)
        else:
            return fallback.choice()
        

class SymmetricalMosaic(Mosaic):

    def __init__(self, wmt=None, symmetry_list=None):
        self.wmt = wmt
        self.symmetry_list = symmetry_list
        super(SymmetricalMosaic, self).__init__()

    @classmethod
    def from_alphabet(cls, alphabet, common_spaces=False):
        wmt, symmetry_list = cls.make_wmt(alphabet, common_spaces)        
        return SymmetricalMosaic(wmt, symmetry_list)

    @classmethod
    def make_wmt(cls, alphabet, num_spaces=0):
        if isinstance(alphabet, list) or isinstance(alphabet, tuple):
            alphabet = "".join(alphabet)
        try:
            alphabet = Alphabet.characters(alphabet)
        except KeyError as e:
            pass
        common = uncommon = rare = None

        if len(alphabet) == 1:
            if not num_spaces:
                raise ValueError("Can't make a mosaic from a single character")
            common = alphabet
        elif len(alphabet) == 2:
            common = alphabet
        else:
            common, uncommon, rare = random.sample(alphabet, 3)
        common += u"\N{EM SPACE}" * num_spaces
        return (WanderingMonsterTable(common, uncommon, rare),
                SymmetryList(alphabet))

    @classmethod
    def random_size(cls, max_size=140, horizontal_symmetry=False,
                    vertical_symmetry=False):
        max_width = 14
        if horizontal_symmetry:
            max_width /= 2
        width = random.randint(3, int(max_width))

        max_height = min(10, max_size/(width+1))
        if vertical_symmetry:
            max_height /= 2
        height = random.randint(3, int(max_height))
        return height, width

    def populate(self, height, width, horizontal_symmetry=False,
                 vertical_symmetry=False):
        self.cells = []
        for i in range(height):
            self.cells.append("")
            for j in range(width):
                need_vertical_symmetry = (
                    j == width-1 and vertical_symmetry)
                need_horizontal_symmetry = (
                    i == height-1 and horizontal_symmetry)
                self.cells[-1] += self.choice(
                    need_horizontal_symmetry, need_vertical_symmetry)
        m = self
        if horizontal_symmetry:
            m = m.mirror_horizontal()
        if vertical_symmetry:
            m = m.mirror_vertical()
        return m

    def choice(self, need_horizontal_symmetry, need_vertical_symmetry):
        return self.symmetry_list.choice(
            self.wmt, need_horizontal_symmetry, need_vertical_symmetry)

    def mirror_horizontal(self, mirror_characters=True):
        """Return a new Mosaic that has this mosaic on the left and its mirror
        image to the right.
        """
        
        if self.width % 2 == 1:
            mirrored_width = self.width - 1
        else:
            mirrored_width = self.width

        mirror = SymmetricalMosaic()
        for row in self.cells:
            new_part = row[:mirrored_width][::-1]
            if mirror_characters:
                new_part = self.mirror_string_horizontal(new_part)
            mirror.cells.append(row + new_part)
        return mirror

    def mirror_vertical(self, mirror_characters=True):
        """Return a new Mosaic that has this mosaic on the top and its mirror
        image beneath.
        """
        mirror = SymmetricalMosaic()
        for row in self.cells:
            mirror.cells.append(row)
        for row in self.cells[:-1][::-1]:
            new_row = row
            if mirror_characters:
                new_row = self.mirror_string_vertical(new_row)
            mirror.cells.append(new_row)
        return mirror

    def mirror_string_horizontal(self, s):
        new_string = ''
        for i in s:
            if i in Mirror.horizontal:
                new_string += Mirror.horizontal[i]
            else:
                new_string += i
        return new_string

    def mirror_string_vertical(self, s):
        new_string = ''
        for i in s:
            if i in Mirror.vertical:
                new_string += Mirror.vertical[i]
            else:
                new_string += i
        return new_string

class MirroredMosaicGibberish(MosaicGibberish):

    def __init__(self, alphabet=None):
        if not alphabet:
            if random.randint(0, 5) == 2:
                # Give emoji a boost
                alphabet = "Emoji"
            else:
                alphabet = random.choice(Alphabet.TILABLE_CHARSET_S)
        self.alphabet = alphabet

    def tweet(self):
        a = random.random()
        hor_sym = False
        ver_sym = False
        if a < 0.25:
            hor_sym = True
        elif a < 0.4:
            ver_sym = True
        elif a < 0.95:
            hor_sym = ver_sym = True

        mostly_space = False
        if random.random() < 0.6:
            # Primarily characters.
            num_spaces = int(random.gauss(1.3,1))
        else:
            # Primarily whitespace
            num_spaces = random.randint(len(self.alphabet), len(self.alphabet)*2)
            mostly_space = True
        height, width = SymmetricalMosaic.random_size(140, hor_sym, ver_sym)

        mosaic = SymmetricalMosaic.from_alphabet(self.alphabet, num_spaces)
        m = mosaic.populate(height, width, hor_sym, ver_sym)
        m = m.__unicode__()
        if not m[0].strip():
            # This tweet starts with whitespace. Use COMBINING
            # GRAPHEME JOINER to get Twitter to preserve the whitespace.
            #
            # TODO: It's not clear whether this works.
            m = u"\N{COMBINING GRAPHEME JOINER}" + m
        return m

class Mirror(object):
    """Information about which characters mirror to which other characters."""

    left_right = u"""
◐◑
▌▐
╭╮
╰╯
└┘
┗┙
┖┚
┗┛
┌┐
┍┑
┎┒
┏┓
├┤
┝┥
┞┦
┟┧
┠┨
┡┩
┢┪
┽┾
╃╄
╅╆
╉╊
╸╺
╼╾
╱╲
▖▗
▜▛
▙▟
▘▝
▚▞
⬔◩
⬕◪
◧◨
▧▨
╒╕
╓╖
╔╗
╘╛
╙╜
╚╝
╞╡
╟╢
╠╣
╶╴
┣┫
┹┺
┵┶
┱┲
┭┮
╒╕
╓╖
╔╗
╘╛
╙╜
╚╝
"""

    top_bottom = u"""
    ╰╭
    ╯╮
    ╱╲
    ╀╁
    ╇╈
    ╹╻
    ╽╿
    ▀▄
    ◒◓
    ▚▞
    ▜▟
    ▙▛
    ⬔◪
    ⬕◩
    ⬒⬓
    ▧▨
┴┬
╘╒
╚╔
╝╗
╧╤
╙╖
╨╥
╛╕
╜╓
╩╦
╵╷
┳┻
╹╻
╽╿
╦╩
╥╨
╧╤
╩╦
╘╒
╙╓
╚╔
╛╕
╜╖
╝╗
    """



    def _make_mirror(s):
        m = {}
        parts = re.compile("\s+").split(s)
        for p in parts:
            p = p.strip()
            if not p:
                continue
            a, b = p
            m[a] = b
            m[b] = a
        return m

    horizontal = _make_mirror(left_right)
    vertical = _make_mirror(top_bottom)

    @classmethod
    def potentials(classmethod):
        """Report on characters that might need to be added to this class."""
        for alphabet in Alphabet.TILABLE_CHARSET_S:
            if isinstance(alphabet, basestring):
                try:
                    alphabet = Alphabet.characters(alphabet)
                except KeyError as e:
                    pass
                if len(alphabet) > 50:
                    continue
                for i in alphabet:
                    if i not in cls.left_right and i not in cls.top_bottom:
                        print(i)
                    print("\n")

if __name__ == '__main__':
    for i in range(4):
        print(MirroredMosaicGibberish().tweet())
        print("\n")


# Content from: ./olipy/pycorpora.py
# Import everything from corpora into a different file for exact
# compatibility with pycorpora.
from corpora import *


# Content from: ./olipy/queneau.py
"""Create Queneau assemblies of source texts."""
from io import StringIO
import json
import random
import re

class Assembler(object):

    def __init__(self, initial=[]):
        self.items = []
        self.tokens_by_position = {}
        self.lengths = []
        for i in initial:
            self.add(i)

    def token_bucket(self, token):
        return self.tokens_by_position

    def bucket_for_position(self, position, code, so_far):
        return self.tokens_by_position

    def add(self, item, tokens_in='tokens'):
        if isinstance(item, dict):
            if not tokens_in in item:
                raise ValueError(
                    "Dictionary added to corpus must put tokens in '%s'." % tokens_in)
            tokens = item[tokens_in]
        elif not (isinstance(item, tuple) or isinstance(item, list)):
            raise ValueError(
                "Only lists, tuples, and dicts may be added to the corpus.")
        else:
            tokens = item
        self.items.append(item)
        l = len(tokens)
        if l > 0:
            self.lengths.append(l)
            for i, token in enumerate(tokens):
                tup = (token, item)
                bucket = self.token_bucket(token)
                bucket.setdefault(i, []).append(tup)
                if bucket != self.tokens_by_position:
                    self.tokens_by_position.setdefault(i, []).append(tup)
                # Also add tokens to more general positions like "middle"
                # and "end".
                if i > 0 and i < l-1:
                    bucket.setdefault("m", []).append(tup)
                if i == l-1:
                    bucket.setdefault("l", []).append(tup)

    def _assert_possible_position(self, position, pattern, length):
        if len(self.tokens_by_position[position]) == 0:
            raise ValueError(
                'Pattern "%s" cannot generate an assembly of length %d with this corpus, because there are no possible values at position %d.' % (pattern, length, position))


    def empty_bucket(self):
        """Generate an empty token bucket."""
        return dict(f=[], m=[], l=[])

    def expand_pattern(self, pattern, length):
        """Decode a short string representing a family of Queneau assembly.

        Some common families, expanded to length 5:

        "0." -> 0, 1, 2, 3, 4
        "0.l" -> 0, 1, 2, 3, last
        "f.l" -> first, middle, middle, middle, last
        "f." -> first, middle, middle, middle, last
        "." -> first, middle, middle, middle, last

        Some less common families:

        "011." -> 0, 1, 1, 2, 3
        "011.l" -> 0, 1, 1, 2, last
        "0f1fl" -> 0, 0, 1, 0, last
        "f.f" -> first, middle, middle, middle, first
        "l.f" -> last, middle, middle, middle, first
        "m.l" -> middle, middle, middle, middle, last
        """
        if length < len(pattern):
            pattern = pattern[:length]
        expanded = []
        previous = None
        if pattern.count(".") > 1:
            raise ValueError(
                'Pattern may not contain more than one expansion characters.')
        if pattern.startswith('.'):
            pattern = "f." + pattern[1:]
        for i, code in enumerate(pattern):

            if code == 'f':
                # First item
                expanded.append(0)

            elif code == 'l':
                # Last item
                expanded.append("l")

            elif code == 'm':
                # An item that's neither first nor last.
                expanded.append("m")

            elif code in "0123456789":
                # An item from a specific place in the sequence.
                code = int(code)
                self._assert_possible_position(code, pattern, length)
                expanded.append(code)

            elif code == '.':
                # Expand the next few entries to fit a pattern
                # established by the previous code.

                # First, see how many things we have to fill in.
                to_be_generated = length-i # Number of items to be generated.
                generated_by_pattern = len(pattern)-i-i # Number of those items to be generated by remaining items in the pattern.
                expanded_size = to_be_generated-generated_by_pattern
                if isinstance(previous, int):
                    # A numeric position is expanded by incrementing
                    # the number.
                    for j in range(previous+1, previous+expanded_size+1):
                        self._assert_possible_position(j, pattern, length)
                        expanded.append(j)
                elif previous in 'flm':
                    for j in range(0, expanded_size):
                        if j == to_be_generated-1:
                            # The last item in the expansion will be
                            # taken from the set of last items.
                            expanded.append('l')
                        else:
                            # Any other item will be taken from the
                            # middle.
                            expanded.append('m')
            else:
                # Invalid code
                raise ValueError(
                    'Invalid character "%s" in pattern "%s".' % (code, pattern))
            previous = code
        return expanded

    def assemble(self, pattern="f.l", length=None, min_length=None):
        while length is None:
            length = random.choice(self.lengths)

        if min_length and length < min_length:
            length = min_length

        pattern = self.expand_pattern(pattern, length)

        so_far = []

        for position, code in enumerate(pattern):
            bucket = self.bucket_for_position(position, code, so_far)
            if bucket[code]:
                choice = random.choice(bucket[code])
                so_far.append(choice)
                yield choice

    @classmethod
    def load(cls, f, tokens_in='tokens'):
        """Load from a filehandle that defines a JSON list of objects."""
        corpus = Assembler()
        for i in json.load(f):
            if tokens_in in i:
                corpus.add(i, tokens_in)
        return corpus

    @classmethod
    def loadlines(cls, f, tokens_in='tokens'):
        """Load from a filehandle that defines a JSON object on every line."""
        corpus = cls()
        for i in f.readlines():
            o = json.loads(i)
            if tokens_in in o:
                corpus.add(o, tokens_in)
        return corpus

    @classmethod
    def loadlist(cls, l, tokens_in='tokens'):
        """Load from a list of objects.""" 
        corpus = cls()
        for o in l:
            if tokens_in in o:
                corpus.add(o, tokens_in)
        return corpus
    
    @classmethod
    def loads(cls, s):
        return cls.load(StringIO(s))

    def dumps(self, compress=False):
        return str(dump(StringIO(), compress))

    def dump(self, f, compress=False):
        for item in self.items:
            if compress:
                if isinstance(item, dict):
                    tokens = item['tokens']
                else:
                    tokens = item
                if len(tokens) == 0:
                    # Skip this one--it can't be used in assemblies.
                    continue
            f.write(json.dumps(item) + "\n")

class SentenceAssembler(Assembler):
    """Assemble sentences from words.

    Markov chains are usually better for this."""

    WHITESPACE = re.compile("\s+")

    def add(self, item):
        words = self.WHITESPACE.split(item)
        super(SentenceAssembler, self).add(words)

class WordAssembler(Assembler):

    """Assemble words from runs of vowels and consonants."""

    def __init__(self, initial=[]):
        self.vowel_runs_by_position = self.empty_bucket()
        self.consonant_runs_by_position = self.empty_bucket()
        super(WordAssembler, self).__init__(initial)

    sequence_of_vowels = re.compile("([aeiou]+)", re.I)
    vowels="aeiouAEIOU"

    def token_bucket(self, token):
        if token[0] in self.vowels:
            return self.vowel_runs_by_position
        else:
            return self.consonant_runs_by_position

    def bucket_for_position(self, position, code, so_far):
        if position == 0:
            # Choose the first token from the list of all first tokens.
            return self.tokens_by_position

        # Subsequent tokens must alternate between the vowel and
        # consonant buckets.
        if so_far[0][0] in self.vowels:
            vowels_at_mod = 0
        else:
            vowels_at_mod = 1
        if (position % 2) == vowels_at_mod:
            return self.vowel_runs_by_position
        else:
            return self.consonant_runs_by_position

    def add(self, word):
        chunks = [x.strip() for x in self.sequence_of_vowels.split(word) if x.strip()]
        super(WordAssembler, self).add(dict(tokens=chunks))

    def assemble_word(self, *args, **kwargs):
        word = None
        while not word:
            word = "".join(x[0] for x in self.assemble(*args, **kwargs))
        return word


class CompositeAssembler(Assembler):
    """Choose from a number of assemblers based on their relative sizes."""

    def __init__(self, initial):
        self.assemblers = []
        for i in initial:
            self.add(i)

    def add(self, assembler):
        self.assemblers.append(assembler)

    def assemble(self, *args):
        total = 0
        sizes = []
        for i in self.assemblers:
            size = len(i.items)
            total += size
            sizes.append(size)

        choice = random.randint(0, total)
        for i, assembler in enumerate(self.assemblers):
            choice -= sizes[i]
            if choice <= 0:
                return assembler, assembler.assemble(*args)


class DialogueAssembler(Assembler):
    """A separate corpus is established for each speaker.
    """

    def __init__(self, initial=[]):
        self.assembler_by_speaker = {} # Lines for each speaker
        self.transitions_by_speaker = {} # Which speaker tends to follow a given speaker?
        self.last_speaker = None
        self.last_section = None
        super(DialogueAssembler, self).__init__(initial)

    def add(self, o, tokens_in="tokens", speaker_in="speaker"):
        speaker = o[speaker_in]
        if speaker not in self.assembler_by_speaker:
            self.assembler_by_speaker[speaker] = Assembler()
        assembler = self.assembler_by_speaker[speaker]
        if self.last_speaker is not None:
            self.transitions_by_speaker.setdefault(self.last_speaker, []).append(speaker)
            self.transitions_by_speaker.setdefault(None, []).append(speaker)
        self.last_speaker = speaker
        assembler.add(o, tokens_in)

    def assemble(self, last_speaker=None, pattern="f.l"):
        speaker = random.choice(self.transitions_by_speaker[last_speaker])
        subassembler = self.assembler_by_speaker[speaker]
        return speaker, list(subassembler.assemble(pattern))


# Content from: ./olipy/randomness.py
"""Sophisticated tools for random choices."""
import random

COMMON = "common"                 # 65%
UNCOMMON = "uncommon"             # 20%
RARE = "rare"                     # 11%
VERY_RARE = "very rare"           # 4%

class WanderingMonsterTable(object):
    """Uses 1st edition AD&D rules to weight a random choice.

    Any given choice may be COMMON, UNCOMMON, RARE, or VERY RARE.
    """

    def __init__(self, common=None, uncommon=None, rare=None,
                 very_rare=None):
        self.common = common or []
        self.uncommon = uncommon or []
        self.rare = rare or []
        self.very_rare = very_rare or []

    def _bucket_for(self, freq):
        if freq == COMMON:
            l = self.common
        elif freq == UNCOMMON:
            l = self.uncommon
        elif freq == RARE:
            l = self.rare
        elif freq == VERY_RARE:
            l = self.very_rare
        else:
            raise ValueError("Invalid value for _freq: %s" % freq)
        return l

    def add(self, o, freq):
        self._bucket_for(freq).append(o)

    def choice(self, freq=None):
        if freq is not None:
            l = self._bucket_for(freq)
        else:
            c = random.randint(0, 99)
            if c < 65:
                l = self.common
            elif c < 85:
                l = self.uncommon
            elif c < 96:
                l = self.rare
            else:
                l = self.very_rare
            if not l:
                l = self.common
        return random.choice(l)

class Gradient(object):

    @classmethod
    def gradient(cls, go_from, go_to, length):
        """Yields a gradient from set1 to set2 of a given length."""
        for i in range(int(length)):
            chance = float(i)/length
            if random.random() > chance:
                c = go_from
            else:
                c = go_to
            yield random.choice(c)

    @classmethod
    def rainbow_gradient(cls, go_from, go_to, length):
        "Goes from go_from to go_to and back again."
        l1 = length / 2
        l2 = length - l1
        for x in cls.gradient(go_from, go_to, l1):
            yield x
        for x in cls.gradient(go_to, go_from, l2):
            yield x


# Content from: ./olipy/tokenizer.py
from __future__ import absolute_import
import re
from textblob.base import BaseTokenizer

class WordTokenizer(BaseTokenizer):
    """
This tokenizer is copy-pasted version of TreebankWordTokenizer
that doesn't split on @ and ':' symbols and doesn't split contractions::

>>> from nltk.tokenize.treebank import TreebankWordTokenizer
>>> s = '''Good muffins cost $3.88\\nin New York. Email: muffins@gmail.com'''
>>> TreebankWordTokenizer().tokenize(s)
['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York.', 'Email', ':', 'muffins', '@', 'gmail.com']
>>> WordTokenizer().tokenize(s)
['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York.', 'Email:', 'muffins@gmail.com']

>>> s = '''Shelbourne Road,'''
>>> WordTokenizer().tokenize(s)
['Shelbourne', 'Road', ',']

>>> s = '''population of 100,000'''
>>> WordTokenizer().tokenize(s)
['population', 'of', '100,000']
"""
    def tokenize(self, text):
        # starting quotes
        text = re.sub(r'^\"', r'``', text)
        text = re.sub(r'(``)', r' \1 ', text)
        text = re.sub(r'([ (\[{<])"', r'\1 `` ', text)

        # punctuation
        text = re.sub(r'(,)(\D|\Z)', r' \1 \2', text)
        text = re.sub(r'\.\.\.', r' ... ', text)
        text = re.sub(r'[;#$%&]', r' \g<0> ', text) # CHANGED @


        text = re.sub(r'([^\.])(\.)([\]\)}>"\']*)\s*$', r'\1 \2\3 ', text)
        text = re.sub(r'[?!]', r' \g<0> ', text)

        text = re.sub(r"([^'])' ", r"\1 ' ", text)

        # parens, brackets, etc.
        text = re.sub(r'[\]\[\(\)\{\}\<\>]', r' \g<0> ', text)
        text = re.sub(r'--', r' -- ', text)

        # add extra space to make things easier
        text = " " + text + " "

        #ending quotes
        text = re.sub(r'"', " '' ", text)
        text = re.sub(r'(\S)(\'\')', r'\1 \2 ', text)

        # CHANGED:

        # text = re.sub(r"([^' ])('[sS]|'[mM]|'[dD]|') ", r"\1 \2 ", text)
        # text = re.sub(r"([^' ])('ll|'LL|'re|'RE|'ve|'VE|n't|N'T) ", r"\1 \2 ",
        # text)
        #
        # for regexp in self.CONTRACTIONS2:
        # text = regexp.sub(r' \1 \2 ', text)
        # for regexp in self.CONTRACTIONS3:
        # text = regexp.sub(r' \1 \2 ', text)

        # We are not using CONTRACTIONS4 since
        # they are also commented out in the SED scripts
        # for regexp in self.CONTRACTIONS4:
        # text = regexp.sub(r' \1 \2 \3 ', text)

        return text.split()

    def itokenize(self, text, *args, **kwargs):
        return iterator(self.tokenize(text))

word_tokenizer = WordTokenizer()

def default_tokenizer(text):
    for tok in word_tokenizer.tokenize(text):
        if tok in ',;':
            continue
        yield tok



# Content from: ./olipy/typewriter.py
# encoding: utf-8
from olipy.randomness import WanderingMonsterTable
import random

class Typewriter(object):
    """Simulates the Adler Universal 39 typewriter used in "The Shining"
    and the sorts of typos that are commonly made on that typewriter.

    Originally written for @a_dull_bot.
    """
    neighbors = dict(
        A = "SQZW",
        l = "kop:,.",
        w = "q23esa",
        o = "90ipkl:",
        r = "45etdfg",
        k = "iojlm,",
        a = "sqzw",
        n = "bjkm ",
        d = "ersfxc",
        p = u"0-=o½l:",
        y = "67tughj",
        m = "jkln, ",
        e = "34wrsdf",
        s = "weadzx",
        J = "YUIHKNM",
        c = "dfxv ",
        u = "78yihj",
        b = "ghvn ",
    )
    neighbors[" "] = "    zxcvbnm,./"
    neighbors["."] = "l;,/"

    def __init__(b, mean_transforms=1.4, stdev_transforms=0.5):
        """Simulate someone hacking away at a typewriter

        :param mean_transforms: The mean number of mistakes per 100
        characters.

        :param stdev_stransforms: The acceptable standard
        deviation from the mean.
        """
        b.mean_transforms = mean_transforms
        b.stdev_transforms = stdev_transforms
        b.wmt = WanderingMonsterTable(
            common=[
                b.typo, b.typo, b.duplicate, b.transpose
            ],
            uncommon=[b.omit_period, b.delete_space, b.typo_add, b.delete],
            rare=[b.delete, b.lowercase_uppercase_letter,
                  b.extra_space_at_beginning, b.uppercase_letter],
            very_rare=[b.uppercase_word, b.uppercase_entire_string,
                       b.lowercase_entire_string, b.remove_word,
                       b.delete],
        )


    def find_typo(self, correct):
        if correct not in self.neighbors:
            # This is already a typo.
            return correct
        return random.choice(self.neighbors[correct])

    def typo(self, string):
        # Replace one character with a typo.
        if not string:
            return string
        i = random.randint(0, len(string)-1)
        incorrect = self.find_typo(string[i])
        return string[:i] + incorrect + string[i+1:]

    def typo_add(self, string):
        # Add a typo character hit before or after the correct character.
        if not string:
            return string
        i = random.randint(0, len(string)-1)
        correct = string[i]
        incorrect = self.find_typo(correct)
        if random.random() < 0.5:
            incorrect = correct + incorrect
        else:
            incorrect = incorrect + correct
        return string[:i] + incorrect + string[i+1:]

    def transpose(self, string):
        # Transpose two characters.
        if len(string) < 2:
            return string
        i = random.randint(0, len(string)-2)
        return string[:i] + string[i+1] + string[i] + string[i+2:]

    def duplicate(self, string):
        # Duplicate a character.
        if not string:
            return string
        i = random.randint(0, len(string)-1)
        return string[:i] + string[i] + string[i] + string[i+1:]

    def delete(self, string):
        # Delete a character.
        if not string:
            return string
        i = random.randint(0, len(string)-1)
        return string[:i] + string[i+1:]

    def delete_space(self, string):
        poses = [i for i, c in enumerate(string) if c == ' ']
        if not poses:
            return string
        i = random.choice(poses)
        return string[:i] + string[i+1:]

    def uppercase_word(self, string):
        words = string.split(" ")
        if not words:
            return string
        i = random.randint(0, len(words)-1)
        return " ".join(words[:i] + [words[i].upper()] + words[i+1:])

    def lowercase_uppercase_letter(self, string):
        poses = [(i,c) for i, c in enumerate(string) if c.upper() == c]
        i,c = random.choice(poses)
        return string[:i] + c.lower() + string[i+1:]

    def uppercase_letter(self, string):
        if not string:
            return string
        i = random.randint(0, len(string)-1)
        return string[:i] + string[i].upper() + string[i+1:]

    def uppercase_entire_string(self, string):
        return string.upper()

    def lowercase_entire_string(self, string):
        return string.upper()
    
    def remove_word(self, string):
        words = string.split(" ")
        if not words:
            return string
        i = random.randint(0, len(words)-1)
        return " ".join(words[:i] + words[i+1:])

    def omit_period(self, string):
        if not string:
            return string
        if string[-1] == '.':
            return string[:-1]
        return string

    def extra_space_at_beginning(self, string):
        return u"\N{EN SPACE}" + string

    def type(self, correct, so_far=""):
        length = len(correct)
        s = str(correct)
        transforms_per_100 = random.gauss(
            self.mean_transforms, self.stdev_transforms
        )
        chunks_100 = max(1, length/100)
        total_transforms = max(1, transforms_per_100 * chunks_100)

        for i in range(int(total_transforms)):
            s = self.wmt.choice()(s)
        s = so_far + s
        if random.random() < 0.1 and len(s) < 100:
            # If it's short, we may type the whole thing again.
            s = self.type(correct, s + " ")
        return s


# Content from: ./olipy/data/__init__.py
import json
import os

def load_json(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    return json.load(open(path))


