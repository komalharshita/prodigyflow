def estimate_time(total_hours, num_topics):
    if num_topics == 0:
        return total_hours
    return total_hours / num_topics
