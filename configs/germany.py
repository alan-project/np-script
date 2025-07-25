import os

summarization_prompt = """
You're a news editor and categorization assistant. Summarize and categorize the following article.
- Create a short, engaging German title (1 line max)
- Write a brief summary in 2~3 lines in plain German
- Determine the category of the article. Choose ONLY ONE from: crime, politics, economy, culture, technology, sports, health, other
- Use a neutral, formal tone suitable for news articles
- Avoid casual or conversational phrases
- Do not use the original title
- Respond in the exact format below:
Category: <one of above>
Title: <your new title>
Content: <your summary>

If the content is not suitable for summarization (e.g., too short, incomplete, or lacks meaning), just return: SKIP

Article:
{content}
"""

def translation_prompt(lang):
    return f"""
You are a professional news translator. Translate the following German news title and summary into {lang}.
- Keep proper nouns (like names, locations, or organizations) in German within parentheses in the summary.
- For the title, translate naturally in {lang} but keep it short and concise. Avoid using parentheses in the title.
- Maintain a neutral, objective tone suitable for news articles.
- Use formal language and avoid conversational tone.
- Do not add any extra comments or labels.

Return your response in this format:
Title: <translated title>
Content: <translated summary>
"""

def top_prompt(top_n):
    return f"""
You are an expert news editor working for a German news app targeted at newcomers to Germany.
Select the top {top_n} most important and engaging news articles from the list below.

Selection criteria:
- Prioritize articles that are directly related to Germany or Europe
- Overall importance and public impact
- Reader engagement potential
- Avoid selecting multiple articles with very similar or identical titles

Return ONLY the article IDs of the selected articles, one per line.
"""

config = {
    "country": "Germany",
    "api_url": os.getenv("NEWS_API_URL"),
    "firestore_collection": "germany_articles",
    "info_doc": "germany_info",
    "base_lang": "de",
    "lang_list": ["en", "ar", "ro","tr", "ru"],
    "select_all": False,
    "top_article_ratio": 0.15,
    "timezone": "Europe/Berlin",
    "daily_popular_days": 2,
    "daily_popular_limit": 10,
    "summarization_prompt": summarization_prompt,
    "translation_prompt": translation_prompt,
    "top_prompt": top_prompt
}