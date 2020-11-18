
def build_score(collection, desired):
    """ adds a score key:value based on number of desired items in message """
    for document in collection:
        score = 0
        for item in desired:
            if item in document['message']:
                score += 1
        document['score'] = score

def build_text_search_pipeline(request_body):
    """ builds pipeline for aggregation query in /text-search endpoint """
    pipeline = [
        {
            '$project': {'_id': 0}
        }
    ]

    if 'userId' in request_body.keys():
        match_id = {'$match': {'sender': {'$eq': request_body['userId']}}}
        pipeline.insert(0, match_id)

    if 'required' in request_body.keys():
        required_join = ' '.join(f'\"{i}\"' for i in request_body['required'])
        if 'forbidden' in request_body.keys():
            forbidden_join = ' '.join(f'-\"{i}\"' for i in request_body['forbidden'])
        else:
            forbidden_join = ''

        match_text = {
            '$match': {'$text': {'$search': f'{required_join} {forbidden_join}'}}
        }
        pipeline.insert(0, match_text)

    return pipeline

def filter_forbidden(cursor, forbidden):
    """ returns filtered list without documents containing
        forbidden words in message """
    result = []
    for document in cursor:
        has_forbidden = False
        for word in forbidden:
            if word in document['message']:
                has_forbidden = True
                break
        if not has_forbidden:
            result.append(document)
    return result
