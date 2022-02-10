# 9번 테스트 케이스 실패 (나머지는 통과)

import re
from collections import defaultdict

def solution(word, pages):
    best_idx, best_score = 0, 0
    pages_dict = {}
    graph = defaultdict(list)
    
    for idx, page in enumerate(pages):
        url = re.search(r"content=\"([\S]+)\"", page).group(1)
        
        basic_score = 0
        for target in re.findall(r"[a-zA-Z]+", page):
            if word.lower() == target.lower():
                basic_score += 1
        
        ext_links = re.findall(r"<a href=\"([\S]+)\"", page)
        for ext_link in ext_links:
            graph[ext_link].append(url)
        
        pages_dict[url] = {
            "idx": idx,
            "basic_score": basic_score,
            'link_score': basic_score/len(ext_links) if ext_links else 0
        }
    
    for idx, url in enumerate(pages_dict):
        matching_score = pages_dict[url]['basic_score']
        for link in graph[url]:
            matching_score += pages_dict[link]['link_score']
        if matching_score > best_score:
            best_score = matching_score
            best_idx = idx
    
    return best_idx