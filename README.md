# Crawling Indonesia Covid-19 Data from RAPIDAPI

[![Python Version](https://img.shields.io/badge/python-3.8.5-brightgreen.svg)](https://python.org)
[![Scrapy Version](https://img.shields.io/badge/scrapy-2.4.1-brightgreen.svg)](https://scrapy.org)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/rdmaulana/scrapy-covid-api.git
```

Create account on rapidapi.com to use this API.
```bash
https://rapidapi.com/api-sports/api/covid-193
```

In settings.py , edit "x-rapidapi-key" with your API KEY.
```bash
'x-rapidapi-key' : 'YOUR_RAPIDAPI_KEY'
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Finally, run scrapy:

```bash
scrapy crawl best_movies
```

If want to put some json output:

```bash
scrapy crawl covid19 -o result.json
```

## License

The source code is released under the [MIT License](https://github.com/rdmaulana/scrapy-covid-api/blob/main/LICENSE).



