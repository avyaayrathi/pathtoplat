def analyze_submissions(submissions):
    topic_errors = {}

    for s in submissions:
        if s.result != "AC":
            topic_errors[s.topic] = topic_errors.get(s.topic, 0) + 1

    weak_topics = sorted(topic_errors, key=topic_errors.get, reverse=True)
    return weak_topics[:3]