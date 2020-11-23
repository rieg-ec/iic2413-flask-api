

def build_text_search_pipeline(request_body):
    """ builds pipeline for aggregation query in /text-search endpoint """
    pipeline = [
        {
            '$project': {'_id': 0}
        }
    ]

    if request_body.get('userId'):
        match_id = {'$match': {'sender': {'$eq': request_body.get('userId')}}}
        pipeline.insert(0, match_id)

    if request_body.get('required') or request_body.get('desired'):
        required = ''
        forbidden = ''
        desired = ''
        if request_body.get('required'):
            required = ' '.join(f'\"{i}\"' for i in request_body.get('required'))

        if request_body.get('desired'):
            desired = ' '.join(f'{i}' for i in request_body.get('desired'))

        if request_body.get('forbidden'):
            forbidden = ' '.join(f'-{i}' for i in request_body.get('forbidden'))

        match_text = {
            '$match': {'$text': {'$search': f'{required} {desired} {forbidden}'}}
        }
        pipeline.insert(0, match_text)
        pipeline.append({'$sort': {'score': {'$meta': 'textScore'}}})

    return pipeline


def forbidden_pipeline(request_body):
    forbidden = ' '.join(f'{i}' for i in request_body.get('forbidden'))
    pipeline = [
        {
            '$match': {'$text': {'$search': forbidden}}
        },
        {
            '$project': {'_id': 0}
        }
    ]
    return pipeline


def filter_forbidden(cursor, forbidden):
    """ returns filtered list without documents containing
        forbidden words in message """
    result = []
    forbidden_documents = [document for document in forbidden]
    for document in cursor:
        if document not in forbidden_documents:
            result.append(document)
    return result
