# -*- coding: utf-8 -*-
# vim:set noet ts=4:
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2009 Hideaki ABE <abe.sendai@gmail.com>
# Copyright (c) 2007-2011 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import gtk
import sys

from prefs import Prefs

N_ = lambda a : a

__all__ = ['AnthyPrefs']


class AnthyPrefs(Prefs):
    _prefix = 'engine/anthy'

    def __init__(self, bus=None, config=None):
        super(AnthyPrefs, self).__init__(bus, config)
        self.default = _config

        # The keys will be EOSL in the near future.
        self.__update_key ("common",
                           "behivior_on_focus_out",
                           "behavior_on_focus_out")
        self.__update_key ("common",
                           "behivior_on_period",
                           "behavior_on_period")
        self.fetch_all()

    def __update_key (self, section, old_key, new_key):
        file = __file__
        if __file__.find('/') >= 0:
            file = __file__[__file__.rindex('/') + 1:]
        warning_message = \
            "(" + file + ") ibus-anthy-WARNING **: "                        \
            "The key (" + old_key + ") will be removed in the future. "     \
            "Currently the key (" + new_key + ") is used instead. "         \
            "The ibus keys are defined in " +                               \
            "/".join(["/desktop/ibus", self._prefix, section]) + " ."

        if not self.fetch_item(section, old_key, True):
            return
        print >> sys.stderr, warning_message
        if self.fetch_item(section, new_key, True):
            return

        self.fetch_item(section, old_key)
        value = self.get_value(section, old_key)
        self.set_value(section, new_key, value)
        self.commit_item(section, new_key)
        self.undo_item(section, new_key)

    def keys(self, section):
        if section.startswith('shortcut/'):
            return _cmd_keys
        return self.default[section].keys()

    def get_japanese_ordered_list(self):
        return _japanese_ordered_list

    def get_version(self):
        return '1.2.6'

# Sad! dict.keys() doesn't return the saved order.
# locale.strcoll() also just returns the Unicode code point.
# Unicode order is wrong in Japanese large 'a' and small 'a'.
# The workaround is to save the order here...
_japanese_ordered_list = [
    "あ", "い", "う", "え", "お",
    "ぁ", "ぃ", "ぅ", "ぇ", "ぉ",
    "いぇ",
    "うぁ", "うぃ", "うぅ", "うぇ", "うぉ",
    "うゃ", "うゅ", "うょ",
    "か", "き", "く", "け", "こ",
    "ゕ", "ゖ", "ヵ", "ヶ",
    "が", "ぎ", "ぐ", "げ", "ご",
    "きゃ", "きぃ", "きゅ", "きぇ", "きょ",
    "くぁ", "くぃ", "くぅ", "くぇ", "くぉ",
    "ぎゃ", "ぎぃ", "ぎゅ", "ぎぇ", "ぎょ",
    "ぐぁ", "ぐぃ", "ぐぅ", "ぐぇ", "ぐぉ",
    "さ", "し", "す", "せ", "そ",
    "ざ", "じ", "ず", "ぜ", "ぞ",
    "しゃ", "しぃ", "しゅ", "しぇ", "しょ",
    "じゃ", "じぃ", "じゅ", "じぇ", "じょ",
    "すぅぃ", "すぇ",
    "ずぇ",
    "た", "ち", "つ", "て", "と",
    "だ", "ぢ", "づ", "で", "ど",
    "っ",
    "ちゃ", "ちぃ", "ちゅ", "ちぇ", "ちょ",
    "ぢぃ", "ぢぇ",
    "ぢゃ", "ぢゅ", "ぢょ",
    "つぁ", "つぃ", "つぇ", "つぉ",
    "つゃ", "つぃぇ", "つゅ", "つょ",
    "づぁ", "づぃ", "づぇ", "づぉ",
    "づゃ", "づぃぇ", "づゅ", "づょ",
    "てぃ", "てぇ",
    "てゃ", "てゅ", "てょ",
    "とぅ",
    "でぃ", "でぇ",
    "でゃ", "でゅ", "でょ",
    "どぅ",
    "な", "に", "ぬ", "ね", "の",
    "にぃ", "にぇ",
    "にゃ", "にゅ", "にょ",
    "は", "ひ", "ふ", "へ", "ほ",
    "ば", "び", "ぶ", "べ", "ぼ",
    "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",
    "ひぃ", "ひぇ",
    "ひゃ", "ひゅ", "ひょ",
    "びぃ", "びぇ",
    "びゃ", "びゅ", "びょ",
    "ぴぃ", "ぴぇ",
    "ぴゃ", "ぴゅ", "ぴょ",
    "ふぁ", "ふぃ", "ふぇ", "ふぉ",
    "ふゃ", "ふゅ", "ふょ",
    "ぶぁ", "ぶぇ", "ぶぉ",
    "ぷぁ", "ぷぇ", "ぷぉ",
    "ま", "み", "む", "め", "も",
    "みぃ", "みぇ",
    "みゃ", "みゅ", "みょ",
    "や", "ゆ", "よ",
    "ゃ", "ゅ", "ょ",
    "ら", "り", "る", "れ", "ろ",
    "りぃ", "りぇ",
    "りゃ", "りゅ", "りょ",
    "わ", "を", "ん",
    "ゎ",
    "ゐ", "ゑ",
    "ー",
    "ヴぁ", "ヴぃ", "ヴ", "ヴぇ", "ヴぉ",
    "ヴゃ", "ヴぃぇ", "ヴゅ", "ヴょ",
]

_cmd_keys = [
    "on_off",
    "circle_input_mode",
    "circle_kana_mode",
    "latin_mode",
    "wide_latin_mode",
    "hiragana_mode",
    "katakana_mode",
    "half_katakana_mode",
#    "cancel_pseudo_ascii_mode_key",
    "circle_typing_method",
    "circle_dict_method",

    "insert_space",
    "insert_alternate_space",
    "insert_half_space",
    "insert_wide_space",
    "backspace",
    "delete",
    "commit",
    "convert",
    "predict",
    "cancel",
    "cancel_all",
    "reconvert",
#    "do_nothing",

    "select_first_candidate",
    "select_last_candidate",
    "select_next_candidate",
    "select_prev_candidate",
    "candidates_page_up",
    "candidates_page_down",

    "move_caret_first",
    "move_caret_last",
    "move_caret_forward",
    "move_caret_backward",

    "select_first_segment",
    "select_last_segment",
    "select_next_segment",
    "select_prev_segment",
    "shrink_segment",
    "expand_segment",
    "commit_first_segment",
    "commit_selected_segment",

    "select_candidates_1",
    "select_candidates_2",
    "select_candidates_3",
    "select_candidates_4",
    "select_candidates_5",
    "select_candidates_6",
    "select_candidates_7",
    "select_candidates_8",
    "select_candidates_9",
    "select_candidates_0",

    "convert_to_char_type_forward",
    "convert_to_char_type_backward",
    "convert_to_hiragana",
    "convert_to_katakana",
    "convert_to_half",
    "convert_to_half_katakana",
    "convert_to_wide_latin",
    "convert_to_latin",

    "dict_admin",
    "add_word",

    "start_setup",
]

_config = {
    'common': {
        'input_mode': 0,
        'typing_method': 0,
        'conversion_segment_mode': 0,

        'period_style': 0,
        'symbol_style': 1,
        'ten_key_mode': 1,
        'behavior_on_focus_out': 0,
        'behavior_on_period': 0,

        'page_size': 10,
        'half_width_symbol': False,
        'half_width_number': False,
        'half_width_space': False,

        'shortcut_type': 'default',

        'dict_admin_command': ['/usr/local/bin/kasumi', 'kasumi'],
        'add_word_command': ['/usr/local/bin/kasumi', 'kasumi', '-a'],
        'dict_config_icon': '/usr/local/share/pixmaps/kasumi.png',
    },

    'romaji_typing_rule': {
        'method': 'default',
        # The newkeys list is saved for every romaji_typing_rule/$method
        # so that prefs.get_value_direct() is not used.
        # prefs.fetch_section() doesn't get the keys if they exist
        # in gconf only.
        'newkeys': [],
    },

    ##0 MS-IME
    # http://www.filibeto.org/sun/lib/solaris10-docs/E19253-01/819-7844/appe-1-4/index.html
    ##1 ATOK
    # http://www.filibeto.org/sun/lib/solaris10-docs/E19253-01/819-7844/appe-1-3/index.html
    ##2 Gairaigo http://ja.wikipedia.org/wiki/%E5%A4%96%E6%9D%A5%E8%AA%9E
    ##3 ANSI/BSI Suggestions http://en.wikipedia.org/wiki/Katakana
    # Maybe we need a compatibility between MS-IME and ibus-anthy.
    'romaji_typing_rule/default': {
        "-": "ー",
        "a" : "あ",
        "i" : "い",
        "u" : "う",
        "e" : "え",
        "o" : "お",
        "xa" : "ぁ",
        "xi" : "ぃ",
        "xu" : "ぅ",
        "xe" : "ぇ",
        "xo" : "ぉ",
        "la" : "ぁ",
        "li" : "ぃ",
        "lu" : "ぅ",
        "le" : "ぇ",
        "lo" : "ぉ",
        "wha" : "うぁ",
        "whi" : "うぃ",
        "whe" : "うぇ",
        "who" : "うぉ",
        "wya" : "うゃ", ##2
        "wyu" : "うゅ", ##2
        "wyo" : "うょ", ##2
        "va" : "ヴぁ",
        "vi" : "ヴぃ",
        "vu" : "ヴ",
        "ve" : "ヴぇ",
        "vo" : "ヴぉ",
        "vya" : "ヴゃ",   ##2
        "vyu" : "ヴゅ",   ##2
        "vye" : "ヴぃぇ", ##2
        "vyo" : "ヴょ",   ##2
        "ka" : "か",
        "ki" : "き",
        "ku" : "く",
        "ke" : "け",
        "ko" : "こ",
        "lka" : "ヵ",
        "lke" : "ヶ",
#        "xka" : "ゕ",
        "xka" : "ヵ",
#        "xke" : "ゖ",
        "xke" : "ヶ",
        "ga" : "が",
        "gi" : "ぎ",
        "gu" : "ぐ",
        "ge" : "げ",
        "go" : "ご",
        "kya" : "きゃ",
        "kyi" : "きぃ",
        "kyu" : "きゅ",
        "kye" : "きぇ",
        "kyo" : "きょ",
        "kwa" : "くぁ",
        "kwi" : "くぃ", ##2
        "kwu" : "くぅ", ##2
        "kwe" : "くぇ", ##2
        "kwo" : "くぉ", ##2
        "gya" : "ぎゃ",
        "gyi" : "ぎぃ",
        "gyu" : "ぎゅ",
        "gye" : "ぎぇ",
        "gyo" : "ぎょ",
        "gwa" : "ぐぁ",
        "gwi" : "ぐぃ", ##2
        "gwu" : "ぐぅ", ##2
        "gwe" : "ぐぇ", ##2
        "gwo" : "ぐぉ", ##2
        "sa" : "さ",
        "si" : "し",
        "su" : "す",
        "se" : "せ",
        "so" : "そ",
        "za" : "ざ",
        "zi" : "じ",
        "zu" : "ず",
        "ze" : "ぜ",
        "zo" : "ぞ",
        "sya" : "しゃ",
        "syi" : "しぃ",
        "syu" : "しゅ",
        "sye" : "しぇ",
        "syo" : "しょ",
        "sha" : "しゃ",
        "shi" : "し",
        "shu" : "しゅ",
        "she" : "しぇ",
        "sho" : "しょ",
        "zya" : "じゃ",
        "zyi" : "じぃ",
        "zyu" : "じゅ",
        "zye" : "じぇ",
        "zyo" : "じょ",
        "ja" : "じゃ",
        "jya" : "じゃ",
        "ji" : "じ",
        "jyi" : "じぃ",
        "ju" : "じゅ",
        "jyu" : "じゅ",
        "je" : "じぇ",
        "jye" : "じぇ",
        "jo" : "じょ",
        "jyo" : "じょ",
        "swi" : "すぅぃ", ##2
        "swe" : "すぇ",   ##2
        "zwe" : "ずぇ",   ##2
        "ta" : "た",
        "ti" : "ち",
        "tu" : "つ",
        "tsu" : "つ",
        "te" : "て",
        "to" : "と",
        "da" : "だ",
        "di" : "ぢ",
        "du" : "づ",
        "de" : "で",
        "do" : "ど",
        "xtu" : "っ",
        "xtsu" : "っ",
        "ltu" : "っ",
        "ltsu" : "っ",
        "tya" : "ちゃ",
        "tyi" : "ちぃ",
        "tyu" : "ちゅ",
        "tye" : "ちぇ",
        "tyo" : "ちょ",
        "cya" : "ちゃ",
        "cyi" : "ちぃ",
        "cyu" : "ちゅ",
        "cye" : "ちぇ",
        "cyo" : "ちょ",
        "cha" : "ちゃ",
        "chi" : "ち",
        "chu" : "ちゅ",
        "che" : "ちぇ",
        "cho" : "ちょ",
        "dya" : "ぢゃ",
        "dyi" : "ぢぃ",
        "dyu" : "ぢゅ",
        "dye" : "ぢぇ",
        "dyo" : "ぢょ",
        "tsa" : "つぁ",
        "tsi" : "つぃ",
        "tse" : "つぇ",
        "tso" : "つぉ",
        "tsya" : "つゃ",   ##3
        "tsyu" : "つゅ",   ##3
        "tsye" : "つぃぇ", ##3
        "tsyo" : "つょ",   ##3
        "dza" : "づぁ",    ##3
        "dzi" : "づぃ",    ##3
        "dze" : "づぇ",    ##3
        "dzo" : "づぉ",    ##3
        "dzya" : "づゃ",   ##3
        "dzyu" : "づゅ",   ##3
        "dzye" : "づぃぇ", ##3
        "dzyo" : "づょ",   ##3
        "tha" : "てゃ",
        "thi" : "てぃ",
        "thu" : "てゅ",
        "the" : "てぇ",
        "tho" : "てょ",
        "twu" : "とぅ",
        "dha" : "でゃ",
        "dhi" : "でぃ",
        "dhu" : "でゅ",
        "dhe" : "でぇ",
        "dho" : "でょ",
        "dwu" : "どぅ",
        "na" : "な",
        "ni" : "に",
        "nu" : "ぬ",
        "ne" : "ね",
        "no" : "の",
        "nya" : "にゃ",
        "nyi" : "にぃ",
        "nyu" : "にゅ",
        "nye" : "にぇ",
        "nyo" : "にょ",
        "ha" : "は",
        "hi" : "ひ",
        "hu" : "ふ",
        "he" : "へ",
        "ho" : "ほ",
        "ba" : "ば",
        "bi" : "び",
        "bu" : "ぶ",
        "be" : "べ",
        "bo" : "ぼ",
        "pa" : "ぱ",
        "pi" : "ぴ",
        "pu" : "ぷ",
        "pe" : "ぺ",
        "po" : "ぽ",
        "hya" : "ひゃ",
        "hyi" : "ひぃ",
        "hyu" : "ひゅ",
        "hye" : "ひぇ",
        "hyo" : "ひょ",
        "bya" : "びゃ",
        "byi" : "びぃ",
        "byu" : "びゅ",
        "bye" : "びぇ",
        "byo" : "びょ",
        "pya" : "ぴゃ",
        "pyi" : "ぴぃ",
        "pyu" : "ぴゅ",
        "pye" : "ぴぇ",
        "pyo" : "ぴょ",
        "fa" : "ふぁ",
        "fi" : "ふぃ",
        "fu" : "ふ",
        "fe" : "ふぇ",
        "fo" : "ふぉ",
        "fya" : "ふゃ",
        "fyi" : "ふぃ",
        "fyu" : "ふゅ",
        "fye" : "ふぇ",
        "fyo" : "ふょ",
        "bwa" : "ぶぁ", ##2
        "bwe" : "ぶぇ", ##2
        "bwo" : "ぶぉ", ##2
        "pwa" : "ぷぁ", ##2
        "pwe" : "ぷぇ", ##2
        "pwo" : "ぷぉ", ##2
        "ma" : "ま",
        "mi" : "み",
        "mu" : "む",
        "me" : "め",
        "mo" : "も",
        "mya" : "みゃ",
        "myi" : "みぃ",
        "myu" : "みゅ",
        "mye" : "みぇ",
        "myo" : "みょ",
        "ya" : "や",
        "yi" : "い",
        "yu" : "ゆ",
        "ye" : "いぇ",
        "yo" : "よ",
        "lya" : "ゃ",
        "lyi" : "ぃ",
        "lyu" : "ゅ",
        "lye" : "ぇ",
        "lyo" : "ょ",
        "xya" : "ゃ",
        "xyi" : "ぃ",
        "xyu" : "ゅ",
        "xye" : "ぇ",
        "xyo" : "ょ",
        "ra" : "ら",
        "ri" : "り",
        "ru" : "る",
        "re" : "れ",
        "ro" : "ろ",
        "rya" : "りゃ",
        "ryi" : "りぃ",
        "ryu" : "りゅ",
        "rye" : "りぇ",
        "ryo" : "りょ",
        "wa" : "わ",
        "wi" : "うぃ",
        "wu" : "う",
        "we" : "うぇ",
        "wo" : "を",
        "lwa" : "ゎ",
        "xwa" : "ゎ",
        "n'" : "ん",
        "nn" : "ん",
        "wyi" : "ゐ",
        "wye" : "ゑ",
    },

    'kana_typing_rule': {
        'method': 'default',
        'newkeys': [],
    },

    'kana_typing_rule/default': {
        # no modifiers keys
        "1" : "ぬ",
        "2" : "ふ",
        "3" : "あ",
        "4" : "う",
        "5" : "え",
        "6" : "お",
        "7" : "や",
        "8" : "ゆ",
        "9" : "よ",
        "0" : "わ",
        "-" : "ほ",
        "^" : "へ",

        "q" : "た",
        "w" : "て",
        "e" : "い",
        "r" : "す",
        "t" : "か",
        "y" : "ん",
        "u" : "な",
        "i" : "に",
        "o" : "ら",
        "p" : "せ",
        "@" : "゛",
        "[" : "゜",

        "a" : "ち",
        "s" : "と",
        "d" : "し",
        "f" : "は",
        "g" : "き",
        "h" : "く",
        "j" : "ま",
        "k" : "の",
        "l" : "り",
        ";" : "れ",
        ":" : "け",
        "]" : "む",

        "z" : "つ",
        "x" : "さ",
        "c" : "そ",
        "v" : "ひ",
        "b" : "こ",
        "n" : "み",
        "m" : "も",
        "," : "ね",
        "." : "る",
        "/" : "め",
        # "\\" : "ー",
        "\\" : "ろ",

        # shift modifiered keys
        "!" : "ぬ",
        "\"" : "ふ",
        "#" : "ぁ",
        "$" : "ぅ",
        "%" : "ぇ",
        "&" : "ぉ",
        "'" : "ゃ",
        "(" : "ゅ",
        ")" : "ょ",
        "~" : "を",
        "=" : "ほ",
        "|" : "ー",

        "Q" : "た",
        "W" : "て",
        "E" : "ぃ",
        "R" : "す",
        "T" : "ヵ",
        "Y" : "ん",
        "U" : "な",
        "I" : "に",
        "O" : "ら",
        "P" : "せ",
        "`" : "゛",

        "{" : "「",

        "A" : "ち",
        "S" : "と",
        "D" : "し",
        "F" : "ゎ",
        "G" : "き",
        "H" : "く",
        "J" : "ま",
        "K" : "の",
        "L" : "り",
        "+" : "れ",
        "*" : "ヶ",

        "}" : "」",

        "Z" : "っ",
        "X" : "さ",
        "C" : "そ",
        "V" : "ゐ",
        "B" : "こ",
        "M" : "も",
        "N" : "み",
        "<" : "、",
        ">" : "。",

        "?" : "・",
        "_" : "ろ",

        "¥" : "ー",
    },

    'thumb': {
        'keyboard_layout_mode': True,
        'keyboard_layout': 0,
        'fmv_extension': 2,
        'handakuten': False,
        'rs': 'Henkan',
        'ls': 'Muhenkan',
        't1': 100,
        't2': 75,
    },

    'thumb_typing_rule': {
        'method': 'base',
        'newkeys': [],
        'nicola_j_table_newkeys': [],
        'nicola_a_table_newkeys': [],
        'nicola_f_table_newkeys': [],
        'kb231_j_fmv_table_newkeys': [],
        'kb231_a_fmv_table_newkeys': [],
        'kb231_f_fmv_table_newkeys': [],
        'kb611_j_fmv_table_newkeys': [],
        'kb611_a_fmv_table_newkeys': [],
        'kb611_f_fmv_table_newkeys': [],
    },

    'thumb_typing_rule/base': {
        'q': [u'。', u'',   u'ぁ'],
        'w': [u'か', u'が', u'え'],
        'e': [u'た', u'だ', u'り'],
        'r': [u'こ', u'ご', u'ゃ'],
        't': [u'さ', u'ざ', u'れ'],

        'y': [u'ら', u'よ', u'ぱ'],
        'u': [u'ち', u'に', u'ぢ'],
        'i': [u'く', u'る', u'ぐ'],
        'o': [u'つ', u'ま', u'づ'],
        'p': [u'，',  u'ぇ', u'ぴ'],
        '@': [u'、', u'',   u''],
        '[': [u'゛', u'゜', u''],

        'a': [u'う', u'',   u'を'],
        's': [u'し', u'じ', u'あ'],
        'd': [u'て', u'で', u'な'],
        'f': [u'け', u'げ', u'ゅ'],
        'g': [u'せ', u'ぜ', u'も'],

        'h': [u'は', u'み', u'ば'],
        'j': [u'と', u'お', u'ど'],
        'k': [u'き', u'の', u'ぎ'],
        'l': [u'い', u'ょ', u'ぽ'],
        ';': [u'ん', u'っ', u''],

        'z': [u'．',  u'',   u'ぅ'],
        'x': [u'ひ', u'び', u'ー'],
        'c': [u'す', u'ず', u'ろ'],
        'v': [u'ふ', u'ぶ', u'や'],
        'b': [u'へ', u'べ', u'ぃ'],

        'n': [u'め', u'ぬ', u'ぷ'],
        'm': [u'そ', u'ゆ', u'ぞ'],
        ',': [u'ね', u'む', u'ぺ'],
        '.': [u'ほ', u'わ', u'ぼ'],
        '/': [u'・', u'ぉ', u''],

        '1': [u'1',  u'',   u'？'],
        '2': [u'2',  u'',   u'／'],
        '4': [u'4',  u'',   u'「'],
        '5': [u'5',  u'',   u'」'],

        '6': [u'6',  u'［',  u''],
        '7': [u'7',  u'］',  u''],
        '8': [u'8',  u'（',  u''],
        '9': [u'9',  u'）',  u''],
        '\\': [u'￥', u'',  u''],
    },

    'thumb_typing_rule/nicola_j_table': {
        ':': [u'：', u'',   u''],
        '@': [u'、', u'',   u''],
        '[': [u'゛', u'゜', u''],
        ']': [u'」', u'',   u''],
        '8': [u'8',  u'（', u''],
        '9': [u'9',  u'）', u''],
        '0': [u'0',  u'',   u''],
    },

    'thumb_typing_rule/nicola_a_table': {
        ':': [u'：', u'',   u''],
        '@': [u'＠', u'',   u''],
        '[': [u'、', u'',   u''],
        ']': [u'゛', u'゜', u''],
        '8': [u'8',  u'',   u''],
        '9': [u'9',  u'（', u''],
        '0': [u'0',  u'）', u''],
    },

    'thumb_typing_rule/nicola_f_table': {
        ':': [u'、', u'',   u''],
        '@': [u'＠', u'',   u''],
        '[': [u'゛', u'゜', u''],
        ']': [u'」', u'',   u''],
        '8': [u'8',  u'（', u''],
        '9': [u'9',  u'）', u''],
        '0': [u'0',  u'',   u''],
    },

    'thumb_typing_rule/kb231_j_fmv_table': {
        '3': [u'3',  u'',   u'～'],
        '0': [u'0',  u'『', u''],
        '-': [u'-',  u'』', u''],
        '=': [u'=',  u'',   u''],
    },

    'thumb_typing_rule/kb231_a_fmv_table': {
        '3': [u'3',  u'',   u'～'],
        '0': [u'0',  u'）', u''],
        '-': [u'-',  u'『', u''],
        '=': [u'=',  u'』', u''],
    },

    'thumb_typing_rule/kb231_f_fmv_table': {
        '3': [u'3',  u'',   u'～'],
        '0': [u'0',  u'『', u''],
        '-': [u'-',  u'』', u''],
        '=': [u'=',  u'',   u''],
    },

    'thumb_typing_rule/kb611_j_fmv_table': {
        '`':  [u'‘', u'',   u''],
        '^':  [u'々', u'£',  u''],
        ':':  [u'：', u'',   u''],
        '@':  [u'、', u'¢',  u''],
        '[':  [u'゛', u'゜', u''],
        # keysyms are same and keycodes depend on the platforms.
        #'￥': [u'￥', u'¬',  u''],
        '\\': [u'￥', u'¦',  u''],
    },

    'thumb_typing_rule/kb611_a_fmv_table': {
        '`':  [u'々', u'',   u'£'],
        ':':  [u'：', u'',   u''],
        '@':  [u'＠', u'',   u''],
        '[':  [u'、', u'¢',  u''],
        #'￥': [u'￥', u'¬',  u''],
        '\\': [u'￥', u'¦',  u''],
    },

    'thumb_typing_rule/kb611_f_fmv_table': {
        '`':  [u'‘', u'',   u''],
        '^':  [u'々', u'£',  u''],
        ':':  [u'、', u'¢',  u''],
        '@':  [u'＠', u'',   u''],
        '[':  [u'゛', u'゜', u''],
        #'￥': [u'￥', u'¬',  u''],
        '\\': [u'￥', u'¦',  u''],
    },

    'dict': {
        'anthy_zipcode': ['/usr/local/share/anthy/zipcode.t'],
        'ibus_symbol': ['/usr/local/share/ibus-anthy/dicts/symbol.t'],
        'ibus_oldchar': ['/usr/local/share/ibus-anthy/dicts/oldchar.t'],
        'files': [
            '/usr/local/share/anthy/zipcode.t',
            '/usr/local/share/ibus-anthy/dicts/symbol.t',
            '/usr/local/share/ibus-anthy/dicts/oldchar.t',
        ],
    },

    'dict/file/default': {
        'embed': False,
        'single': True,
        'icon': None,
        'short_label': None,
        'long_label': None,
        'preview_lines': 30,
        'reverse': False,
        'is_system': False,
        'encoding': 'utf-8',
    },

    'dict/file/embedded': {
        'embed': True,
        'single': True,
        'icon': None,
        'short_label': '般',
        'long_label': N_("General"),
        'preview_lines': 0,
        'reverse': False,
        'is_system': True,
    },

    'dict/file/anthy_zipcode': {
        'embed': False,
        'single': True,
        'icon': None,
        'short_label': '〒',
        'long_label': N_("Zip Code Conversion"),
        'preview_lines': 30,
        'reverse': True,
        'is_system': True,
        'encoding': 'euc_jp',
    },

    'dict/file/ibus_symbol': {
        'embed': True,
        'single': False,
        'icon': None,
        'short_label': '記',
        'long_label': N_("Symbol"),
        'preview_lines': -1,
        'reverse': False,
        'is_system': True,
    },

    'dict/file/ibus_oldchar': {
        'embed': False,
        'single': True,
        'icon': None,
        'short_label': '旧',
        'long_label': N_("Old Character Style"),
        'preview_lines': -1,
        'reverse': False,
        'is_system': True,
    },
}

_shortcut_default = {
    'on_off': ['Ctrl+J'],
    'circle_input_mode': ['Ctrl+comma', 'Ctrl+less'],
    'circle_kana_mode': ['Ctrl+period', 'Ctrl+greater', 'Hiragana_Katakana'],
#    'cancel_pseudo_ascii_mode_key': ['Escape'],
    'circle_typing_method': ['Alt+Romaji', 'Ctrl+slash'],
    'circle_dict_method': ['Alt+Henkan'],

    'insert_space': ['space'],
    'insert_alternate_space': ['Shift+space'],
    'backspace': ['BackSpace', 'Ctrl+H'],
    'delete': ['Delete', 'Ctrl+D'],
    'commit': ['Return', 'KP_Enter', 'Ctrl+J', 'Ctrl+M'],
    'convert': ['space', 'KP_Space', 'Henkan'],
    'predict': ['Tab', 'ISO_Left_Tab'],
    'cancel': ['Escape', 'Ctrl+G'],
    'reconvert': ['Shift+Henkan'],

    'move_caret_first': ['Ctrl+A', 'Home'],
    'move_caret_last': ['Ctrl+E', 'End'],
    'move_caret_forward': ['Right', 'Ctrl+F'],
    'move_caret_backward': ['Left', 'Ctrl+B'],

    'select_first_segment': ['Ctrl+A', 'Home'],
    'select_last_segment': ['Ctrl+E', 'End'],
    'select_next_segment': ['Right', 'Ctrl+F'],
    'select_prev_segment': ['Left', 'Ctrl+B'],
    'shrink_segment': ['Shift+Left', 'Ctrl+I'],
    'expand_segment': ['Shift+Right', 'Ctrl+O'],
    'commit_first_segment': ['Shift+Down'],
    'commit_selected_segment': ['Ctrl+Down'],

    'select_first_candidate': ['Home'],
    'select_last_candidate': ['End'],
    'select_next_candidate': ['space', 'KP_Space', 'Tab', 'ISO_Left_Tab', 'Henkan', 'Down', 'KP_Add', 'Ctrl+N'],
    'select_prev_candidate': ['Shift+Tab', 'Shift+ISO_Left_Tab', 'Up', 'KP_Subtract', 'Ctrl+P'],
    'candidates_page_up': ['Page_Up'],
    'candidates_page_down': ['Page_Down', 'KP_Tab'],

    'select_candidates_1': ['1'],
    'select_candidates_2': ['2'],
    'select_candidates_3': ['3'],
    'select_candidates_4': ['4'],
    'select_candidates_5': ['5'],
    'select_candidates_6': ['6'],
    'select_candidates_7': ['7'],
    'select_candidates_8': ['8'],
    'select_candidates_9': ['9'],
    'select_candidates_0': ['0'],

    'convert_to_char_type_forward': ['Muhenkan'],
    'convert_to_hiragana': ['F6'],
    'convert_to_katakana': ['F7'],
    'convert_to_half': ['F8'],
    'convert_to_half_katakana': ['Shift+F8'],
    'convert_to_wide_latin': ['F9'],
    'convert_to_latin': ['F10'],

    'dict_admin': ['F11'],
    'add_word': ['F12'],
}

_config['shortcut/default'] = dict.fromkeys(_cmd_keys, [])
_config['shortcut/default'].update(_shortcut_default)

_shortcut_atok = {
    'on_off': ['Henkan', 'Eisu_toggle', 'Zenkaku_Hankaku'],
    'circle_input_mode': ['F10'],
    'hiragana_mode': ['Hiragana_Katakana'],
    'katakana_mode': ['Shift+Hiragana_Katakana'],
    'circle_typing_method': ['Romaji', 'Alt+Romaji'],
    'circle_dict_method': ['Alt+Henkan'],
    'convert': ['space', 'Henkan', 'Shift+space', 'Shift+Henkan'],
    'predict': ['Tab'],
    'cancel': ['Escape', 'BackSpace', 'Ctrl+H', 'Ctrl+bracketleft'],
    'commit': ['Return', 'Ctrl+M'],
    'reconvert': ['Shift+Henkan'],

    'insert_space': ['space'],
    'insert_alternate_space': ['Shift+space'],
    'backspace': ['BackSpace', 'Ctrl+H'],
    'delete': ['Delete', 'Ctrl+G'],

    'move_caret_backward': ['Left', 'Ctrl+K'],
    'move_caret_forward': ['Right', 'Ctrl+L'],
    'move_caret_first': ['Ctrl+Left'],
    'move_caret_last': ['Ctrl+Right'],

    'select_prev_segment': ['Shift+Left'],
    'select_next_segment': ['Shift+Right'],
    'select_first_segment': ['Ctrl+Left'],
    'select_last_segment': ['Ctrl+Right'],
    'expand_segment': ['Right', 'Ctrl+L'],
    'shrink_segment': ['Left', 'Ctrl+K'],
    'commit_selected_segment': ['Down', 'Ctrl+N'],

    'candidates_page_up': ['Shift+Henkan', 'Page_Up'],
    'candidates_page_down': ['Henkan', 'Page_Down'],
    'select_next_candidate': ['space', 'Tab', 'Henkan', 'Shift+space', 'Shift+Henkan'],
    'select_prev_candidate': ['Up'],

    'select_candidates_1': ['1'],
    'select_candidates_2': ['2'],
    'select_candidates_3': ['3'],
    'select_candidates_4': ['4'],
    'select_candidates_5': ['5'],
    'select_candidates_6': ['6'],
    'select_candidates_7': ['7'],
    'select_candidates_8': ['8'],
    'select_candidates_9': ['9'],
    'select_candidates_0': ['0'],

    'convert_to_hiragana': ['F6', 'Ctrl+U'],
    'convert_to_katakana': ['F7', 'Ctrl+I'],
    'convert_to_half': ['F8', 'Ctrl+O'],
    'convert_to_half_katakana': ['Shift+F8'],
    'convert_to_wide_latin': ['F9', 'Ctrl+P'],
    'convert_to_latin': ['F10', 'Ctrl+at'],

    'add_word': ['Ctrl+F7'],
}

_config['shortcut/atok'] = dict.fromkeys(_cmd_keys, [])
_config['shortcut/atok'].update(_shortcut_atok)

_shortcut_wnn = {
    'on_off': ['Shift+space'],
    'convert': ['space'],
    'predict': ['Ctrl+Q'],
    'cancel': ['Escape', 'Ctrl+G', 'Alt+Down', 'Muhenkan'],
    'commit': ['Ctrl+L', 'Ctrl+M', 'Ctrl+J', 'Return'],
    'insert_space': ['space'],
    'backspace': ['Ctrl+H', 'BackSpace'],
    'delete': ['Ctrl+D', 'Delete'],
    'circle_dict_method': ['Alt+Henkan'],

    'move_caret_backward': ['Ctrl+B', 'Left'],
    'move_caret_forward': ['Ctrl+F', 'Right'],
    'move_caret_first': ['Ctrl+A', 'Alt+Left'],
    'move_caret_last': ['Ctrl+E', 'Alt+Right'],

    'select_prev_segment': ['Ctrl+B', 'Left'],
    'select_next_segment': ['Ctrl+F', 'Right'],
    'select_first_segment': ['Ctrl+A', 'Alt+Left'],
    'select_last_segment': ['Ctrl+E', 'Alt+Right'],
    'expand_segment': ['Ctrl+O', 'F14'],
    'shrink_segment': ['Ctrl+I', 'F13'],

    'candidates_page_up': ['Tab'],
    'candidates_page_down': ['Shift+Tab'],
    'select_next_candidate': ['space', 'Ctrl+Q', 'Ctrl+P', 'Down'],
    'select_prev_candidate': ['Ctrl+N', 'Up'],

    'select_candidates_1': ['1'],
    'select_candidates_2': ['2'],
    'select_candidates_3': ['3'],
    'select_candidates_4': ['4'],
    'select_candidates_5': ['5'],
    'select_candidates_6': ['6'],
    'select_candidates_7': ['7'],
    'select_candidates_8': ['8'],
    'select_candidates_9': ['9'],
    'select_candidates_0': ['0'],

    'convert_to_hiragana': ['F6'],
    'convert_to_katakana': ['F7'],
    'convert_to_half': ['F8'],
    'convert_to_wide_latin': ['F9'],
    'convert_to_latin': ['F10'],
}

_config['shortcut/wnn'] = dict.fromkeys(_cmd_keys, [])
_config['shortcut/wnn'].update(_shortcut_wnn)

