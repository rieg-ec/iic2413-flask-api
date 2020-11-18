from bson.code import Code


filter_function = Code("""
    function(desired, message) {
        return desired
            .filter(str => message.toLowerCase()
                    .includes(str.toLowerCase()))
    }
""")


def build_text_search_pipeline(request_body):
    """ builds pipeline for aggregation query in /text-search endpoint """
    pipeline = [
        {
            '$project': {'_id': 0}
        }
    ]

    if 'desired' in request_body.keys():
        score_field = {
            '$addFields': {
                'score': {
                    '$size': {
                        '$function': {
                            'body': filter_function,
                            'args': [request_body['desired'], '$message'],
                            'lang': 'js'
                        }
                    }
                }
            }
        }
        sort_operator = {
            '$sort': {'score': -1}
        }
        pipeline.insert(0, score_field)
        pipeline.append(sort_operator)

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
    """ returns filtered cursor object without documents with forbidden words """
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
