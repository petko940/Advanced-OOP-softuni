from collections import deque

suggested_links = deque([int(x) for x in input().split()])
featured_articles = deque([int(x) for x in input().split()])
target_engagement_value = int(input())

final_feed = []

while suggested_links and featured_articles:
    first_suggested_link = suggested_links.popleft()
    current_suggested_link = first_suggested_link
    last_featured_article = featured_articles.pop()
    current_feature_article = last_featured_article

    if first_suggested_link > last_featured_article:
        greater_element = first_suggested_link
        smaller_element = last_featured_article
    else:
        greater_element = last_featured_article
        smaller_element = first_suggested_link

    remainder = greater_element % smaller_element

    if greater_element == smaller_element:
        final_feed.append(0)
        continue

    if greater_element == current_feature_article:
        final_feed.append(abs(remainder))
        if remainder:
            featured_articles.append(remainder * 2)
    else:
        final_feed.append(-abs(remainder))
        if remainder:
            suggested_links.append(remainder * 2)

total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join([str(x) for x in final_feed])}")
if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")
