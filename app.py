import os
import json
import requests

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

from helper.news_parser_helper import NewsContentParser
from helper.google_cse_helper import GoogleCSEHelper

from util.support import SupportUtil

GoogleCSEHelper = GoogleCSEHelper()
SupportUtil = SupportUtil()

PARSE_FAILED_MSG = os.getenv('PARSE_FAILED_MSG')
RESULTS_JSON_PATH = os.getenv('RESULTS_JSON_PATH')

if __name__ == "__main__":
    keywords = SupportUtil.get_keywords()
    items = []
    for keyword in keywords:
        raw_results = GoogleCSEHelper.search_and_get_results(keyword)
        base_text = []
        for raw_result in raw_results:
            url = SupportUtil.resolve_url(raw_result['url'])
            raw_html = requests.get(url).content
            parser = NewsContentParser(raw_html, url)

            results = parser.parse_content()
            print(url)
            if (results is not None):
                base_text.append(SupportUtil.build_base_text(raw_result, results))
            else:
                print('\n', PARSE_FAILED_MSG, '\n')
        item = SupportUtil.build_item(keyword, base_text)
        items.append(item)

    dict_obj = { 'items': items }
    file_obj = open('example_results.json', 'w')
    json.dump(dict_obj, file_obj)