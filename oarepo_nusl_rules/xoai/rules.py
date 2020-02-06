import datetime

# from flask_taxonomies.utils import find_in_json, find_in_json_contains
from collections import OrderedDict

from langdetect import detect

from oarepo_nusl_rules.decorators import rule
from oarepo_nusl_rules.exceptions import NotFoundError
from oarepo_nusl_rules.utils import get_iso_lang_code, extract_title


@rule
def xoai_abstract(source, *args, **kwargs):
    """
    CZ:
    EN:
    """
    value = []
    for lang_vers in source:
        lang = lang_vers["@name"]
        field = lang_vers["element"]["field"]
        if isinstance(field, list):
            for abstract in field:
                value.append(
                    {
                        "name": abstract["#text"],
                        "lang": lang
                    }
                )
        else:
            value.append(
                {
                    "name": field["#text"],
                    "lang": lang
                }
            )
    return {"abstract": value}


@rule
def xoai_contributor(source, *args, **kwargs):
    """
    CZ:
    EN:
    """
    value = []
    for person_role in source:
        role = person_role["@name"]
        field = person_role["element"]["field"]
        if isinstance(field, list):
            for person in field:
                value.append(
                    {
                        "name": person["#text"],
                        "role": role
                    }
                )
        else:
            value.append(
                {
                    "name": field["#text"],
                    "role": role
                }
            )

    return {
        "contributor": value
    }


@rule
def xoai_creator(source, *args, **kwargs):
    """
    CZ:
    EN:
    """
    value = []
    field = source["field"]
    if isinstance(field, list):
        for person in field:
            value.append(
                {
                    "name": person["#text"],
                }
            )
    else:
        value.append(
            {
                "name": field["#text"],
            }
        )
    return {"creator": value}


@rule
def xoai_date_accepted(source, *args, **kwargs):
    """
    CZ:
    EN:
    """
    field = source["field"]
    if field.get("@name") == "value":
        date = datetime.datetime.strptime(field.get("#text"), "%Y-%m-%d")
        return {"dateAccepted": date.strftime('%Y-%m-%d')}


@rule
def xoai_defended(source, *args, **kwargs):
    """
    CZ:
    EN:
    """
    for item in source:
        lang = item["@name"]
        field = item["element"]["field"]
        if isinstance(field, OrderedDict):
            if lang == "cs":
                if field["#text"] == 'Prospěl/a':
                    return {"defended": True}
                else:
                    return {"defended": False}
            if lang == "en":
                if field["#text"] == 'Pass':
                    return {"defended": True}
                else:
                    return {"defended": False}
            if lang == "code":
                if field["#text"] == 'P':
                    return {"defended": True}
                else:
                    return {"defended": False}


# @rule
# def degree_grantor(source, *args, **kwargs):
#     source = source.get("cs_CZ")
#     tax = Taxonomy.get("universities")
#     uk = tax.get_term("00216208")
#     if source:
#         grantor = source[0]
#         grantor = grantor.split(",")
#         grantor = [unit.strip() for unit in grantor]
#         if len(grantor) > 1:
#             for part in reversed(grantor):
#                 unit = find_in_json(part, tax).first()
#                 if unit is not None:
#                     return {
#                         "degreeGrantor": [
#                             {
#                                 "$ref": link_self(tax.slug, unit)
#                             }
#                         ]
#                     }
#     return {
#         "degreeGrantor": [
#             {
#                 "$ref": link_self(tax.slug, uk)
#             }
#         ]
#     }


# @rule
# def doctype(source, *args, **kwargs):
#     value = source["cs_CZ"][0]
#     tax = Taxonomy.get("doctype")
#     term = tax.get_term(doctype_dict(value))
#     return {
#         "doctype": {
#             "$ref": link_self(tax.slug, term)
#         }
#     }


@rule
def xoai_identifier(source, *args, **kwargs):
    return {
        "identifier": [
            {
                "value": source,
                "type": "originalOAI"
            },
            {
                "value": kwargs["metadata"]["dc"]["identifier"]["uri"]["none"][0],
                "type": "originalRecord"
            },
        ]
    }


#
# @rule
# def keywords(source, *args, **kwargs):
#     keyw_values = []
#     subjects = []
#     tax = Taxonomy.get("subject")
#     for key, value in source.items():
#         for word in value:
#             psh_list_terms = find_in_json_contains(word, tax, "title").all()
#             if len(psh_list_terms) == 0:
#                 psh_list_terms = find_in_json_contains(word, tax, "altTitle").all()
#             term = psh_term_filter(psh_list_terms, word)
#             if len(psh_list_terms) == 0 or term is None:
#                 keyw_values.append(
#                     {
#                         "name": word,
#                         "lang": get_iso_lang_code(key[:2])
#                     }
#                 )
#             else:
#                 subjects.append(
#                     {
#                         "$ref": link_self("subject", term)
#                     }
#                 )
#     if subjects and keyw_values:
#         return {
#             "subject": subjects,
#             "keywords": keyw_values
#         }
#     elif keyw_values:
#         return {
#             "keywords": keyw_values
#         }
#     elif subjects:
#         return {
#             "subject": subjects
#         }


@rule
def xoai_language(source, *args, **kwargs):
    langs = []
    for lang in source["none"]:
        code = get_iso_lang_code(lang[:2])
        if code is None:
            raise NotFoundError(
                f"The {lang} was not found in supported languages database. See pycountry.")
        langs.append(code)
    return {"language": langs}


@rule
def xoai_modified(source, *args, **kwargs):
    date_time_list = source.split(" ")
    date = date_time_list[0]
    time = date_time_list[1][:8]
    return {"modified": f"{date}T{time}"}


# @rule
# def studyfield(source, *args, **kwargs):
#     field = source.get("program").get("cs_CZ")
#     doc_type = kwargs["metadata"]["dc"]["type"]["cs_CZ"][0]
#     doc_type = doctype_dict(doc_type)
#     tax = Taxonomy.get("studyfields")
#     if field is not None and field:
#         field = field[0]
#         return studyfield_ref(field, tax, "Univerzita Karlova", doc_type)


@rule
def xoai_title(source, *args, **kwargs):
    titles = []
    extract_title(source, titles)
    if "translated" in source:
        extract_title(source["translated"], titles)
    return {"title": titles}
