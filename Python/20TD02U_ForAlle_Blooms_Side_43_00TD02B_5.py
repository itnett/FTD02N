python
# Bruke LanguageTool for engelsk grammatikkontroll
tool = language_tool_python.LanguageTool('en')
text = "This is a example text with some grammatical mistake."
mistakes = tool.check(text)

for mistake in mistakes:
    print(f"Mistake: {mistake.message} - {mistake.sentence}")