from collections import OrderedDict

import pytest

from oarepo_nusl_rules.xoai.rules import xoai_abstract


@pytest.fixture
def source():
    return [
        OrderedDict(
            [
                ('@name', 'cs'),
                ('element', OrderedDict(
                    [
                        ('@name', 'cs_CZ'), ('field', OrderedDict(
                        [
                            ('@name', 'value'),
                            ('#text',
                             'Předkládaná disertační práce je věnována analýze frazeologických '
                             'jednotek používaných v současném politickém diskurzu v Rusku a '
                             'České republice. Popisuje funkce frazémů objevujících se v '
                             'politickém diskurzu, které slouží jako prostředek ke zvýšení '
                             'expresivity projevu, navázání kontaktu s publikem a jako '
                             'prostředek nepřímého ovlivňování komunikačního partnera. Rovněž '
                             'se zabývá analýzou kognitivních a pragmatických aspektů užití '
                             'frazémů a metajazykových komentářů vyskytujících se v projevech '
                             'politiků v porovnávacím pohledu. Práce popisuje specifika užití '
                             'frazeologických jednotek podílejících se na vytváření jazykového '
                             'obrazu politika. Klíčová slova: frazeologie, frazeologismus, '
                             'diskurz, politický diskurz, politická lingvistika, kognitivní '
                             'lingvistika, image politika, jazykový obraz politika.')
                        ]
                    )
                                             )
                    ]
                )
                 )
            ]
        ),
        OrderedDict(
            [
                ('@name', 'en'),
                ('element', OrderedDict(
                    [
                        ('@name', 'en_US'), ('field', OrderedDict(
                        [
                            ('@name', 'value'),
                            (
                                '#text',
                                'In the dissertation the author presents the analysis of the use '
                                'of phraseological units in modern political discourse in Russia '
                                'and the Czech Republic. The author shows that phraseology can be '
                                'a tool for increasing the expressiveness of a speech, '
                                'for contacting and influencing the audience in the political '
                                'discourse. The analysis of cognitive and pragmatic specifics of '
                                'idioms and metalanguage commentaries in the speech of '
                                'politicians in a comparative aspect is carried out. As a result '
                                'the author showes the specifics of the use of phraseological '
                                'units in describing the speech image of a politician. Key words: '
                                'phraseology, phraseologism, discourse, political discourse, '
                                'political linguistics, cognitive linguistics, image of a '
                                'politician, speech portrait of a politician.'
                            )
                        ]
                    )
                                             )
                    ]
                )
                 )
            ]
        )
    ]


def test_abstract_1(source):
    assert xoai_abstract(source) == {
        'abstract': [
            {
                'name': 'Předkládaná disertační práce je věnována analýze '
                        'frazeologických jednotek používaných v současném politickém '
                        'diskurzu v Rusku a České republice. Popisuje funkce frazémů '
                        'objevujících se v politickém diskurzu, které slouží jako '
                        'prostředek ke zvýšení expresivity projevu, navázání kontaktu s '
                        'publikem a jako prostředek nepřímého ovlivňování komunikačního '
                        'partnera. Rovněž se zabývá analýzou kognitivních a '
                        'pragmatických aspektů užití frazémů a metajazykových komentářů '
                        'vyskytujících se v projevech politiků v porovnávacím pohledu. '
                        'Práce popisuje specifika užití frazeologických jednotek '
                        'podílejících se na vytváření jazykového obrazu politika. '
                        'Klíčová slova: frazeologie, frazeologismus, diskurz, politický '
                        'diskurz, politická lingvistika, kognitivní lingvistika, '
                        'image politika, jazykový obraz politika.',
                'lang': 'cs'
            },
            {
                'name': 'In the dissertation the author presents the analysis of the use '
                        'of phraseological units in modern political discourse in Russia '
                        'and the Czech Republic. The author shows that phraseology can '
                        'be a tool for increasing the expressiveness of a speech, '
                        'for contacting and influencing the audience in the political '
                        'discourse. The analysis of cognitive and pragmatic specifics of '
                        'idioms and metalanguage commentaries in the speech of '
                        'politicians in a comparative aspect is carried out. As a result '
                        'the author showes the specifics of the use of phraseological '
                        'units in describing the speech image of a politician. Key '
                        'words: phraseology, phraseologism, discourse, political '
                        'discourse, political linguistics, cognitive linguistics'
                        ', image of a politician, speech portrait of a politician.',
                'lang': 'en'
            }
        ]
    }
