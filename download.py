"""
Download the 4000 most recent cs.CL papers and store them to a pickle file.
"""
import feedparser
import pickle
import time


QUERY_URL = 'http://export.arxiv.org/api/query?search_query=cat:cs.CL&sortBy=submittedDate&start={}&max_results={}'

if __name__ == '__main__':
    papers = []
    for i in range(0, 4000, 50):
        query = QUERY_URL.format(i, 50)
        res = feedparser.parse(query)
        for e in res.entries:
            papers.append({
              'title': e.title,
              'published': e.published_parsed,
              'authors': e.authors,
              'link': e.link
            })
        time.sleep(2)

    with open('data.pkl', 'wb') as f:
        pickle.dump(papers, f)
