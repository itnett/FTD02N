python
    rank = 1 - (COMMITS_WEIGHT * exponential_cdf(commits/COMMITS_MEDIAN)
                + PRS_WEIGHT * exponential_cdf(prs/PRS_MEDIAN)
                + ISSUES_WEIGHT * exponential_cdf(issues/ISSUES_MEDIAN)
                + STARS_WEIGHT * log_normal_cdf(stars/STARS_MEDIAN)
                + FOLLOWERS_WEIGHT * log_normal_cdf(followers/FOLLOWERS_MEDIAN)) / TOTAL_WEIGHT