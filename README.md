# Indonesian Google CSE and Content Parser

These are few simple python libraries to use Google Custom Search Engine (CSE) with content parser included.

## Google Custom Search Engine (CSE) Helper

This is a class to retrieve Google search's results based on input keyword. Just input all keywords into `keywords.txt` file. You can use the `search_and_get_results()` function with search query as an argument for direct use.

Just read the class file for more details.

## News Content Parser Helper

This is a class to parse text content from a source. The available source that able to be parsed is listed at `news_dict.json` file. If you want to add a new source, just go directly to the json file and add a new item with the same attributes.

Using the `parse_content()` function, a raw HTML file can be parsed into a clean text containing the main content of the source (including with list of its sentences).

For some cases, the parser still built on specific cases to parse the content retrieved from Google search results. For broad implementation, you can customize this class based on specific task required.

## Others
  - There are some additional cases in `util` directory for some supports, such as **resolving URL's** or **build a custom json file**, you can add custom utility files if needed or customize the existing support class
  - If you want to use the app, don't forget to create a new `.env` file based on example that already provided
  - The parser still use an Indonesian normalization API from **Prosa.ai** 
 
## Run

To run the app, simply use this command :

```sh
$ python app.py
```
