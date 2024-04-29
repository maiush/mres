theirs_compare = """\
[INST] {INSTRUCTION}

Source text: {ARTICLE}

Compare the following summaries:

Summary A: {SUMMARY1}

Summary B: {SUMMARY2}

Question: Which summary is more {ASPECT}? \
If the summary A is more {ASPECT}, please return 'A'. \
If the summary B is more {ASPECT}, please return 'B' \
You must only return the choice. [/INST] Answer: """


theirs_score = """\
[INST] {INSTRUCTION}

Source text: {ARTICLE}

Summary: {SUMMARY}

Please rate on a scale from 1 to 5, where 1 represents very low {ASPECT}, \
and 5 indicates excellent {ASPECT}. You must only return an int score. \
[/INST] Score: """


mine_compare = """\
[INST] Consider the following article: {ARTICLE}
Below are two summaries of this article:
Choice 1: {SUMMARY1}
Choice 2: {SUMMARY2} 
Which summary is more {ASPECT}? [/INST] Between Choice 1 and Choice 2, the more {ASPECT} summary is Choice {CHOICE}"""


instructions = {
    "coherence": "Compare the coherence of the two following summaries.",
    "fluency": "Evaluate and compare the fluency of the two following summaries.",
    "relevance": """Evaluate and compare how two summaries consistently follow the source text.
A summary is relevant if it captures the main points from the article, without leaving out any crucial details or adding any unnecessary or inaccurate ones.
A summary is more relevant if it uses the same or similar terms and expressions as the article.
A summary is less relevant if it omits some of the key facts from the article, or if it introduces irrelevant information that is not supported by the article.""",
    "consistency": """Evaluate and compare how two summary consistently follow the source text.
A summary is consistent with the article if it faithfully reflects the main points, facts, and tone of the article.
A summary is inconsistent if it introduces any errors, contradictions, or distortions of the original article."""
}