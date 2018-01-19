TEXT_REPORT = """TEXT REPORT for "{TITLE}"

\t{TEXT}

\tTotal sentences:  {SENTENCES_COUNT}
\tEvaluation:       {POSITIVE} | {NEGATIVE}
\tSummary:          {SUMMARY}

SENTENCES DETAILS:
{SENTENCE_REPORTS}
"""

SENTENCE_REPORT = """
\t[{INDEX}] {SENTENCE}

\tTotal keywords:    {KEYWORDS_COUNT}
{KEYWORD_REPORT}"""

KEYWORD_REPORT = """
\t\tCategory:        {CATEGORY}
\t\tKeyword:         {KEYWORD}
\t\tIntensifier:     {INTENSIFIER}
\t\tInverted:        {INVERTED}
\t\tEvaluation:      {POSITIVE} | {NEGATIVE}"""