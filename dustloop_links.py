"""Just the list of frame data websites"""
from re import I
from sre_constants import CH_LOCALE

Anji: str = "https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data"
Bridget: str = "https://www.dustloop.com/w/GGST/Bridget/Frame_Data"
Giovanna: str = "https://www.dustloop.com/w/GGST/Giovanna/Frame_Data"
I_No: str = "https://www.dustloop.com/w/GGST/I-No/Frame_Data"
Leo: str = "https://www.dustloop.com/w/GGST/Leo_Whitefang/Frame_Data"
Nagoriyuki: str = "https://www.dustloop.com/w/GGST/Nagoriyuki/Frame_Data"
Sol: str = "https://www.dustloop.com/w/GGST/Sol_Badguy/Frame_Data"
Axl: str = "https://www.dustloop.com/w/GGST/Axl_Low/Frame_Data"
Chipp: str = "https://www.dustloop.com/w/GGST/Chipp_Zanuff/Frame_Data"
Goldlewis: str = "https://www.dustloop.com/w/GGST/Goldlewis_Dickinson/Frame_Data"
Jack_O: str = "https://www.dustloop.com/w/GGST/Jack-O/Frame_Data"
May: str = "https://www.dustloop.com/w/GGST/May/Frame_Data"
Potemkin: str = "https://www.dustloop.com/w/GGST/Potemkin/Frame_Data"
Testament: str = "https://www.dustloop.com/w/GGST/Testament/Frame_Data"
Faust: str = "https://www.dustloop.com/w/GGST/Faust/Frame_Data"
Baiken: str = "https://www.dustloop.com/w/GGST/Baiken/Frame_Data"
Happy_Chaos: str = "https://www.dustloop.com/w/GGST/Happy_Chaos/Frame_Data"
Ky_Kiske: str = "https://www.dustloop.com/w/GGST/Ky_Kiske/Frame_Data"
Millia: str = "https://www.dustloop.com/w/GGST/Millia_Rage/Frame_Data"
Ramlethal: str = "https://www.dustloop.com/w/GGST/Ramlethal_Valentine/Frame_Data"
Zato_1: str = "https://www.dustloop.com/w/GGST/Zato-1/Frame_Data"

characters = (Anji, Bridget, Giovanna, I_No, Leo, Nagoriyuki, Sol, Axl, Chipp, Goldlewis, Jack_O, May,
                Potemkin, Testament, Faust, Baiken, Happy_Chaos, Ky_Kiske, Millia, Ramlethal, Zato_1)

def name_by_index(index:int=0)->str:
    return characters[index].split("/")[-2]

def name_by_index(index:float=0.0)->str:
    return characters[int(index)].split("/")[-2]