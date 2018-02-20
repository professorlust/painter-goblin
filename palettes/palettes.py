#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from random import seed, shuffle
from collections import namedtuple

class Palettes:

	def get_palette(self):

		Painter_goblin_palette = namedtuple('Painter_goblin_palette', 'label colors')
		p = [

		# purple rain
		Painter_goblin_palette("#PurpleRain", [(0x02, 0x01, 0x22),
			(0x02, 0x06, 0x5D), (0x1B, 0x07, 0x4D), (0x2B, 0x0E, 0x76),
			(0xFF, 0xD3, 0xCA)]),

		# france1/seatoun
		Painter_goblin_palette("#Seatoun", [(0x00, 0x00, 0x00),
			(0xff, 0x00, 0x00), (0xbd, 0xbd, 0xbd), (0x69, 0x78, 0xad)]),

		# four variants, yellows, reds, blues, greens
		Painter_goblin_palette("#Yellows", [(0xEF, 0xEF, 0x3F),
			(0xC8, 0xC3, 0xC3), (0x3D, 0x3D, 0x3D), (0x53, 0x53, 0x53),
			(0x00, 0x00, 0x00)]),

		#Reds
		Painter_goblin_palette("#Reds", [(0xEF, 0x00, 0x00),
			(0xC8, 0xC3, 0xC3), (0x3D, 0x3D, 0x3D), (0x53, 0x53, 0x53),
			(0x00, 0x00, 0x00)]),

		#Greens
		Painter_goblin_palette("#Greens", [(0x00, 0xEF, 0x00),
			(0xC8, 0xC3, 0xC3), (0x3D, 0x3D, 0x3D), (0x53, 0x53, 0x53),
			(0x00, 0x00, 0x00)]),

		#Blues
		Painter_goblin_palette("#Blues", [(0x00, 0x00, 0xEF),
			(0xC8, 0xC3, 0xC3), (0x1D, 0x1D, 0x1D), (0x53, 0x53, 0x53),
			(0x00, 0x00, 0xCC)]),

		# madmax
		Painter_goblin_palette("#MadMaxFuryRoad", [(0xfb, 0xfd, 0xfa),
			(0xe3, 0x77, 0x12), (0x1a, 0x37, 0x39), (0x00, 0x64, 0x6c),
			(0xbb, 0xbb, 0xbb)]),

		# oranges/browns
		Painter_goblin_palette("#OrangeBrowns", [(0xc2, 0x8e, 0x27),
			(0x03, 0x55, 0x52), (0x4d, 0x9c, 0x6d), (0x85, 0x2c, 0x1a),
			(0x00, 0x00, 0x00)]),

		# magenta, electric green, and others...
		Painter_goblin_palette("#MagentaConverse", [(0x00, 0x00, 0x00),
			(0xFF, 0x53, 0x53), (0xd1, 0xb6, 0xf3), (0xFF, 0x00, 0x69),
			(0xaa, 0xFF, 0x57)]),

		# rainbow palette
		Painter_goblin_palette("#🌈", [(0x03, 0x03, 0xc1), (0x00, 0xFF, 0x00),
			(0xFF, 0xFF, 0x00), (0xFF, 0x7F, 0x00), (0xFF, 0x00, 0x00)]),

		# browns and greys
		Painter_goblin_palette("#BrownGrey", [(0xc5, 0x7e, 0x42),
			(0x91, 0x87, 0x8d), (0x7d, 0x70, 0x7c), (0x2a, 0x12, 0x1c),
			(0x53, 0x6d, 0x81)]),

		# purples and soft greys
		Painter_goblin_palette("#PurpleGrey", [(0x81, 0x40, 0x59),
			(0x55, 0x57, 0x53), (0xd0, 0xcc, 0xcc), (0x2d, 0x31, 0x3d),
			(0xfe, 0xc4, 0xd0)]),

		# sonic
		Painter_goblin_palette("#SonicTheHedgehog", [(0x34, 0x53, 0xca),
			(0xfd, 0x92, 0x19), (0x77, 0x98, 0xee), (0xdf, 0x98, 0x21),
			(0x68, 0x32, 0x09)]),

		# mario
		Painter_goblin_palette("#SuperMario", [(0xec, 0x4b, 0x09),
			(0xff, 0x0a, 0x1a), (0x5d, 0x94, 0xfb), (0x12, 0x7c, 0x22),
			(0xdb, 0xfc, 0xff)]),

		# lightblue
		Painter_goblin_palette("#LightBlue", [(0x0c, 0x2c, 0x52),
			(0x5f, 0x6b, 0x61), (0x5e, 0x9d, 0xc8), (0xdc, 0xf0, 0xf7),
			(0x00, 0x00, 0x00)]),

		# France
		Painter_goblin_palette(unicode("#LeTriTricolore 🇫🇷",'utf-8'), [(0xff, 0x00, 0x00),
			(0xFF, 0xFF, 0xFF), (0x00, 0x00, 0xFF)]),

		# stark
		Painter_goblin_palette("#stark", [(0xC0, 0x00, 0x00),
			(0xFF, 0xFF, 0xFF), (0x00, 0x00, 0x00)]),

		# teletext1 (blue, magenta)
		Painter_goblin_palette("#TeletextBlueMagenta", [(0x00, 0xff, 0xff),
			(0x00, 0x00, 0x00), (0xff, 0x00, 0x00), (0xff, 0x00, 0xff)]),

		# teletext2 (yellow, green, blue)
		Painter_goblin_palette("#TeletextYellowGreenBlue", [(0xfe, 0xfe, 0x00),
			(0x00, 0xfe, 0xfe), (0x00, 0xfe, 0x00), (0xff, 0xff, 0xff)]),

		# teletext3 (red, yellow blue)
		Painter_goblin_palette("#TeletextRedYellowBlue", [(0xfe, 0xfe, 0x00),
			(0x00, 0xfe, 0xfe), (0xff, 0x00, 0x00), (0x00, 0x00, 0x00)]),

		# mario sprite
		Painter_goblin_palette("#MarioSprite", [(0x3f, 0x47, 0xcc),
			(0xf9, 0x38, 0x01), (0xfe, 0xa3, 0x46), (0xFF, 0xFF, 0xFF),
			(0x00, 0x00, 0x00)]),

		# redwhiteblack
		Painter_goblin_palette("#RussianRevolution", [(0xdd, 0x00, 0x00),
			(0xFF, 0xFF, 0xFF), (0x00, 0x00, 0x00), (0xFF, 0xFF, 0xFF),
			(0xFF, 0xFF, 0xFF)]),

		# bluewhiteblack
		Painter_goblin_palette("#BlueWhiteBlack", [(0x0c, 0x2c, 0x52),
			(0xFF, 0xFF, 0xFF), (0x00, 0x00, 0x00), (0xFF, 0xFF, 0xFF),
			(0xFF, 0xFF, 0xFF)]),

		# cyan, black, purple, greys...
		Painter_goblin_palette("#CyanBlackPurpleGrey", [(0x00, 0x00, 0x00),
			(0x9c, 0x29, 0xc6), (0xcb, 0xcb, 0xcb), (0x00, 0xd7, 0xcc),
			(0x61, 0x5e, 0x6a)]),

		# print-test, The Crack, William Kokoni
		Painter_goblin_palette("#WilliamKokoni", [(0x00, 0x9d, 0xc4),
			(0xa0, 0xc3, 0xbd), (0xfa, 0x18, 0x3b), (0x3a, 0x45, 0x42),
			(0xd6, 0x7b, 0x7e)]),

		# moma, Emigre 29, The Designers Republic, Emigre Inc., Rudy
		# VanderLans, Zuzana Licko, 1994
		Painter_goblin_palette("#Emigre29", [(0x50, 0x4d, 0x6b),
			(0x84, 0x64, 0x5a), (0xa6, 0x9e, 0x9e), (0xfc, 0xc1, 0x78),
			(0xf6, 0xed, 0xdb)]),

		# toronto queen
		Painter_goblin_palette("#TorontoQueen", [(0xfc, 0x2f, 0xac),
			(0x00, 0x48, 0xff), (0x07, 0x1e, 0x45), (0xf0, 0xb3, 0x00),
			(0xc1, 0xe3, 0xff)]),

		# warhol cow...
		Painter_goblin_palette("#WarholCow", [(0x27, 0x0b, 0x17),
			(0x7f, 0x0d, 0x34), (0xc8, 0x0f, 0x4e), (0xfe, 0x1d, 0x69),
			(0xff, 0xe1, 0x3b)]),

		# palette from wiki image http://www.wikidata.org/entity/Q28771811
		Painter_goblin_palette("#Phoenix", [(0xf1, 0xa0, 0x30),
			(0xf6, 0x59, 0x01), (0xb5, 0x42, 0x19), (0x62, 0x3a, 0x29),
			(0x2d, 0x28, 0x30)]),

		# alien
		Painter_goblin_palette("#Alien1979", [(0x00, 0x02, 0x00),
			(0x30, 0x5e, 0x1a), (0x77, 0xac, 0x1a), (0xce, 0xc3, 0x66),
			(0xff, 0xed, 0x21)]),

		# bowie - ziggy stardust
		Painter_goblin_palette("#ZiggyStardust", [(0xdf, 0x1c, 0x06),
			(0x4b, 0x4d, 0x4b), (0x59, 0x55, 0xcc), (0xff, 0x95, 0x71),
			(0xff, 0xeb, 0xdf)]),

		# white, pink
		Painter_goblin_palette("#WhitePink", [(0x22, 0x22, 0x22),
			(0x99, 0x99, 0x99), (0xf8, 0xf8, 0xff), (0xfe, 0xfe, 0xfa),
			(0xff, 0x1f, 0xfa)]),

		# Anna Atkins's cyanotypes:
		# https://digitalcollections.nypl.org/collections/ocean-flowers-anna-atkinss-cyanotypes-of-british-algae#/?tab=navigation
		Painter_goblin_palette("#CyanoTypes", [(0x22, 0x67, 0x88),
			(0x30, 0x6e, 0x8e), (0x59, 0x8c, 0xa6), (0x88, 0xb0, 0xc0),
			(0xc6, 0xd6, 0xd7)]),

		# velvet underground
		Painter_goblin_palette("#VelvetUnderground", [(0xec, 0xef, 0xeb),
			(0xec, 0xef, 0xeb), (0xec, 0xef, 0xeb), (0xf5, 0xd3, 0x17), (0x00, 0x00, 0x00)]),

		# The Icknield Way, Spencer Gore, 1912
		Painter_goblin_palette("#SpencerGore", [(0x95, 0x2b, 0x58),
			(0x05, 0x6a, 0x47), (0x00, 0x46, 0x76), (0xf7, 0x76, 0x20),
			(0xff, 0x9f, 0x22)]),

		# Original Batman
		Painter_goblin_palette("#Batman", [(0x39, 0x3a, 0x38),
			(0xfd, 0xf7, 0x00), (0x00, 0x02, 0x00)]),

		# Picasso: Blue Period: Mother and Child
		Painter_goblin_palette("#PicassoBlue", [(0xf4, 0xf4, 0xf4),
			(0x9b, 0x74, 0x57), (0x3d, 0x64, 0x45), (0x0d, 0x24, 0x46),
			(0x2b, 0x7a, 0xbc)]),

		# Cybercats
		Painter_goblin_palette("#Cybercats", [(0x18, 0x15, 0x13),
			(0xe1, 0x24, 0x05), (0x57, 0x55, 0x4e), (0x34, 0x91, 0xc6),
			(0xe7, 0xff, 0x1e)]),

		# Solaris : Concept Art
		Painter_goblin_palette("#SolarisConcept", [(0x10, 0x0e, 0x29),
			(0xcb, 0xe1, 0x33), (0x30, 0x41, 0x33), (0x30, 0x2e, 0x46),
			(0xbf, 0x21, 0x3b)]),

		# Leroy W. Flint Apocalypse, A Triptych , c. 1953
		Painter_goblin_palette("#Apocalypse", [(0xff,0xbb,0x08),
			(0xff,0x3d,0x00), (0xb9,0x00,0x00), (0x53,0x00,0x00),
			(0x21,0x02,0x00)]),

        # kazimir malevich supremus 58
		Painter_goblin_palette("#MalevichSupremus", [(0xd2,0xe2,0xe0),
			(0x0c,0x0c,0x0c), (0xff,0xc3,0x0d), (0xff,0xff,0xf1),
			(0x2a,0x49,0x98)]),

		Painter_goblin_palette("#LollyRocket", [(0x0e,0x00,0x02),
			(0x31,0x02,0x29), (0x5e,0x00,0x52), (0xff,0x46,0x42),
			(0xeb,0xf6,0xf9)]),

		Painter_goblin_palette("#KeithHaring", [(0x1c,0x15,0x09),
			(0xeb,0x28,0x96), (0xff,0x74,0x2b), (0x80,0xd9,0x8e),
			(0xfd,0xf8,0x36)]),

		Painter_goblin_palette("#HugoGellert #One", [(0x15,0x0f,0x12),
			(0x1e,0x30,0x5f), (0xfb,0x00,0x00), (0x8f,0x25,0x06),
			(0xfb,0xca,0x09)]),

		Painter_goblin_palette("#HugoGellert #Two", [(0x2a,0x0b,0x02),
			(0x15,0x21,0x6f), (0xae,0x10,0x03), (0xff,0x0c,0x00),
			(0xfd,0xf5,0xea)]),

		]

		# seed the random number generator
		seed(time.time())

		# get the palette we want
		shuffle(p)

		# get first entry following shuffle
		label = p[0].label
		palette = p[0].colors

		# and shuffle that palette
		shuffle(palette)

		return label, palette
