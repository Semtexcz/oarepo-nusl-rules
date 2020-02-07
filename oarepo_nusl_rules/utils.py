import re
from collections import OrderedDict
from functools import lru_cache

from flask_taxonomies.models import Taxonomy
from flask_taxonomies.utils import find_in_json, find_in_json_contains, link_self
from pycountry import languages

from oarepo_nusl_rules.exceptions import NotFoundError


def get_iso_lang_code(lang):
    """
    Convert two-digit iso code into three-digit iso code
    :param lang: Two digit iso code
    :return: Three digit iso code
    """
    iso_lang = languages.get(alpha_2=lang)
    if iso_lang is not None:
        if hasattr(iso_lang, "bibliographic"):
            return getattr(iso_lang, "bibliographic")
        else:
            return getattr(iso_lang, "alpha_3")


@lru_cache()
def doctype_dict(doctype_val):
    doctypes = {
        'bakalářská práce': 'bakalarske_prace',
        'diplomová práce': 'diplomove_prace',
        'dizertační práce': 'disertacni_prace',
        'rigorózní práce': 'rigorozni_prace',
        'habilitační práce': 'habilitacni_prace'
    }
    return doctypes.get(doctype_val, doctype_val)


def psh_term_filter(psh_list_terms, keyword):
    """
    Filter one subject from a list of keywords that matched the taxonomy.
    :param psh_list_terms: List of keywords.
    :param keyword:
    :return: taxonomy_term
    """
    psh_list_terms = [term for term in psh_list_terms if "PSH" in term.tree_path]
    if len(psh_list_terms) == 0:
        return None
    matched_terms = []
    for term in psh_list_terms:
        match = False
        for dictionary in term.extra_data["title"]:
            for v in dictionary.values():
                if v == keyword:
                    match = True
        if match:
            matched_terms.append(term)
    if len(matched_terms) > 0:
        return matched_terms[0]
    return None


# def studyfield_ref(study, tax, grantor, doc_type):
#     # https://docs.sqlalchemy.org/en/13/dialects/postgresql.html#sqlalchemy.dialects.postgresql
#     .JSON
#     # https://github.com/sqlalchemy/sqlalchemy/issues/3859  # issuecomment-441935478
#     fields = find_in_json(study, tax, tree_address=("title", 0, "value")).all()
#     if len(fields) == 0:
#         fields = aliases(tax, study)
#     if len(fields) == 0:
#         field = find_in_json_contains(study, tax, "source_data").first()
#         if field is None:
#             return ""
#         return {
#             "studyField": [{"$ref": link_self(tax.slug, field)}]
#         }
#     if len(fields) > 1:
#         fields = filter(fields, doc_type, grantor)
#
#     return {
#         "studyField": [{"$ref": link_self(tax.slug, field)} for field in fields],
#
#     }


def aliases(tax, study):
    fields = find_in_json(study, tax, tree_address="aliases").all()
    if len(fields) == 0:
        fields = find_in_json_contains(study, tax, tree_address="aliases").all()
    return fields


def filter(fields, doc_type, grantor):
    fields = doc_filter(fields, doc_type)
    fields = grantor_filter(fields, grantor)
    return fields


def doc_filter(fields, doc_type):
    if doc_type is not None:
        if doc_type == "rigorozni_prace":
            doc_type = "disertacni_prace"
        degree_dict = {
            "Bakalářský": "bakalarske_prace",
            "Magisterský": "diplomove_prace",
            "Navazující magisterský": "diplomove_prace",
            "Doktorský": "disertacni_prace"
        }
        return [field for field in fields if
                degree_dict.get(field.extra_data.get("degree_level")) == doc_type]
    return fields


def grantor_filter(fields, grantor):
    if grantor is not None:
        matched_fields = [field for field in fields if
                          field.extra_data.get("grantor") is not None and
                          field.extra_data["grantor"][0][
                              "university"].lower() == grantor]
        if len(matched_fields) == 0:
            return fields
        else:
            return matched_fields
    else:
        return fields


def extract_title(dictionary, titles):
    for k, v in dictionary.items():
        pattern = r"[a-zA-Z]{2}_[a-zA-Z]{2}"
        if re.match(pattern, k) is not None:
            code = k[:2]
        else:
            continue
        lang = get_iso_lang_code(code)
        if lang is not None:
            titles.append(
                {
                    "name": v[0],
                    "lang": lang
                }
            )


def xoai_get_langs(text: str) -> dict:
    """
    Function get data from field (XML source), extract lang abbreviation and return taxonomy link
    :param text: It is language string e.g.: cs_CZ or en_US
    :return: Taxonomy reference with $ref
    :rtype: Dict
    """
    lang_code = get_iso_lang_code(text[:2])
    taxonomy = Taxonomy.get("languages")
    term = taxonomy.get_term(lang_code)
    if term is None:
        raise NotFoundError(f"The language \"{lang_code}\" is not present in the Taxonomy")
    return {'$ref': link_self(taxonomy.code, term)}
