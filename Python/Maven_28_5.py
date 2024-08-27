python
    class WorkEnvironmentReview:
        def __init__(self, department, rating, comments):
            self.department = department
            self.rating = rating
            self.comments = comments

    reviews = []
    reviews.append(WorkEnvironmentReview("IT", 4, "Gode arbeidsforhold, men forbedringspotensial på kommunikasjon"))

    for review in reviews:
        print(f"Avdeling: {review.department}, Rating: {review.rating}, Kommentar: {review.comments}")