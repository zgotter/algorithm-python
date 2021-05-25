# 성공

import re

def solution(new_id):
    # step 1
    new_id = new_id.lower()
    
    # step 2
    new_id = re.sub('[^a-z0-9-_.]*','',new_id)
    
    # step 3
    dot = re.compile('[.]{2}')
    while dot.findall(new_id):
        new_id = re.sub('[.]{2}', '.', new_id)
        
    # step 4
    if len(new_id) > 0 and new_id[0] == '.': new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.': new_id = new_id[:-1]
    
    # step 5
    if len(new_id) == 0: new_id = 'a'
    print(f'id:{new_id}')
    
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:-1]
            
    # step 7
    if len(new_id) <= 2:
        w = new_id[-1]
        for i in range(3-len(new_id)):
            new_id += w
    
    return new_id