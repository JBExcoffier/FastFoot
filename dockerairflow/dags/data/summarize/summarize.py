from data.utils.prompt import get_response


def summarize_football(articles: list):
    instruction = """You will base yourself on several short documents in the form of - TITLE : BRIEF SUMMARY concerning articles about the same sport, football (soccer). 
    These articles come from a sports news website specialized in football and therefore concern the most important football (soccer) news of the moment.
    
    Your task is to understand these documents, as some articles may talk more or less about the same information, and to create a very short synthesis. 
    You must therefore blend the information from all the documents, some information being repeated, and synthesize it into two sentences maximum. Each sentence should also be short in itself.

    You must write your synthesis in a punchy and lively style that makes readers want to read the articles !
    You must only return the synthesis, without any additional introductory or concluding sentences."""

    documents = """Here are the documents on which you base your synthesis. They are in the form of - TITLE : BRIEF SUMMARY.
    """
    documents += "\n"
    for a in articles:
        documents += "- " + a["title"] + " : " + a["intro"] + "\n"

    prompt = (
        "[INSTRUCTION]"
        + "\n"
        + instruction
        + "\n"
        + "[/INSTRUCTION]"
        + "\n" * 3
        + documents
    )

    ai_summary = get_response(prompt=prompt, temperature=0.5)

    return ai_summary
