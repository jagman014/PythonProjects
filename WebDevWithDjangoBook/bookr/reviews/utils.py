def average_rating(rating_list: list) -> int:
    if not rating_list:
        return 0
    
    return round(sum(rating_list) / len(rating_list))
