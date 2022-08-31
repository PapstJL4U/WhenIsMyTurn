"""find the +onBlock moves in GG Strive and find the percentage for normals and specials
    to do so we need to scrap dustloop.com for each characters moves and do some math
"""
import website_fiddling as wf
import dustloop_links as dl


if __name__ == "__main__":
    wf.find_Moves(dl.I_No)