import_error = []

try:
   import requests
except ImportError or ModuleNotFoundError:
    import_error.append("requests")

try:
    from tqdm import tqdm
except ImportError or ModuleNotFoundError:
    import_error.append("tqdm")

try:
    from bs4 import BeautifulSoup
except ImportError or ModuleNotFoundError:
    import_error.append("beautifulsoup4")


try: 
    import argparse
except ImportError or ModuleNotFoundError:
    import_error.append("argparse")
  
try:    
   import random
except ImportError or ModuleNotFoundError:
    import_error.append("random")

if len(import_error) > 0:
    print("You have issues installing these libraries: ", import_error)
    print("Install them by typing 'pip install library_name")
    exit()

class Search:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }

        self.search_engines = [
            {'name': 'DuckDuckGo', 'url': 'https://duckduckgo.com/html/?q={}'},
            {'name': 'Google', 'url': 'https://www.google.com/search?q={}&num=20'},
            {'name': 'Bing', 'url': 'https://www.bing.com/search?q={}&count=20'},
            {'name': 'Yahoo', 'url': 'https://search.yahoo.com/search?p={}&n=20'},
            {'name': 'Ask', 'url': 'https://www.ask.com/web?q={}&qsrc=0&o=0&l=dir&qo=homepageSearchBox'},
            {'name': 'AOL', 'url': 'https://search.aol.com/aol/search?q={}&count=20'},
            {'name': 'Dogpile', 'url': 'https://www.dogpile.com/serp?q={}&num=20'},
            {'name': 'StartPage', 'url': 'https://www.startpage.com/do/dsearch?query={}&cat=web&pl=ext-ff&language=english&lui=english'},
            {'name': 'Yandex', 'url': 'https://yandex.com/search/?text={}&lr=213'},
            {'name': 'Wolfram Alpha', 'url': 'https://www.wolframalpha.com/input/?i={}'}
        ]

    def search(self, query, keywords=None):
        random.shuffle(self.search_engines)

        results = []
        total_links = 50 * len(self.search_engines)
        progress = tqdm(total=int(total_links), desc="Searching....", unit="link")
        for engine in self.search_engines:
            query_X = f"{query} {keywords}" if keywords else query
            url = engine['url'].format(query_X)
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.select('.result__url')
            titles = soup.select('.result__title')
            for index, link in enumerate(links[:50]):
                result = {'title': titles[index].text, 'url': link.get('href'), 'engine': engine['name']}
                results.append(result)
                progress.update(1)

        progress.close()

        if not results:
            print('[X] - No results found!!')
        else:
            results = sorted(results, key=lambda x: random.random())
            random_results = random.sample(results, min(len(results), 50))
            for index, result in enumerate(random_results, start=1):
                print(f"[****] - Result {index} ({result['engine']}): {result['title']}\n{result['url']}\n")

    def search_firmware(self, model_name):
        query = f"site:androidhost.ru {model_name}"
        query_two = f"site:gsm-firmware.com {model_name}"
        query_three = f"site:forum.xda-developers.com/search/thread {model_name}"
        query_four = f"site:romprovider.com {model_name}"
        return (
            self.search(query),
            self.search(query_two),
            self.search(query_three),
            self.search(query_four)
        )
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Research")
    #parser.add_argument("--limit", help="Specify the result limit")
    parser.add_argument("-keywords", help="Define keywords that will be used to search")
    parser.add_argument("---search", help="Search the stuff on the web", required=False)
    parser.add_argument("--firmware", help="Search for the specific firmware")

    args = parser.parse_args()
    print("""
    

______ _                                      
|  ___(_)                                     
| |_   _ _ __ _ __ _____      ____ _ _ __ ___ 
|  _| | | '__| '_ ` _ \ \ /\ / / _` | '__/ _ \
| |   | | |  | | | | | \ V  V / (_| | | |  __/
\_|   |_|_|  |_| |_| |_|\_/\_/ \__,_|_|  \___|
                                              
                                              
______                              _         
| ___ \                            | |        
| |_/ /___  ___  ___  __ _ _ __ ___| |__      
|    // _ \/ __|/ _ \/ _` | '__/ __| '_ \     
| |\ \  __/\__ \  __/ (_| | | | (__| | | |    
\_| \_\___||___/\___|\__,_|_|  \___|_| |_|    
                                              
                                              


    """)
    search = Search()
    if args.search:
      search.search(args.search)
    if args.search and args.keywords:
        search.search(args.search, args.keywords)
    if args.firmware:
        search.search_firmware(args.firmware)

