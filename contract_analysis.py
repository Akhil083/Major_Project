# import numpy as np
# from typing import Dict, List, Tuple
# import fav_keywords  # Make sure this file contains the keywords and rules

# class ContractAnalyzer:
#     def __init__(self):
#         self.keywords = fav_keywords.KEYWORDS

#     def calculate_favorability(self, clause_type: str, text: str) -> Tuple[int, int, int]:
#         """
#         Calculate favorability based on keywords and rules.

#         :param clause_type: The type of clause being evaluated.
#         :param text: The text of the clause.
#         :return: A tuple containing favorability score and the start and end indices of the match.
#         """
#         favorability_score = 0
#         start_index = -1
#         end_index = -1

#         # Check for keywords
#         keywords_info = self.keywords.get(clause_type)
#         if keywords_info:
#             keywords = keywords_info['keywords']
#             rules = keywords_info['rules']

#             # Check for presence of keywords
#             for keyword in keywords:
#                 if keyword in text.lower():
#                     favorability_score += 50  # Base score for presence of keywords
#                     start_index = text.lower().index(keyword)  # Start index of the keyword
#                     end_index = start_index + len(keyword) - 1  # End index of the keyword

#                     # Check positive rules
#                     if any(rule in text.lower() for rule in rules['positive']):
#                         favorability_score += 30  # Score for favorable conditions

#                     # Check negative rules
#                     if any(rule in text.lower() for rule in rules['negative']):
#                         favorability_score -= 20  # Penalty for unfavorable conditions

#                     break  # Exit loop after first match

#         # Ensure the score is within the 1-100 range
#         favorability_score = min(max(favorability_score, 1), 100)
#         return favorability_score, start_index, end_index

#     def analyze_document(self, text_chunks: List[str]) -> Dict:
#         """
#         Analyze the document to identify clauses and provide favorability scores.

#         :param text_chunks: List of text chunks extracted from the document.
#         :return: Analysis results containing clause annotations and favorability scores.
#         """
#         clause_counts = {clause_type: 0 for clause_type in self.keywords.keys()}
#         clause_info = []
#         total_favorability = 0
#         num_clauses = 0

#         for chunk in text_chunks:
#             for clause_type in self.keywords.keys():
#                 favorability, start_index, end_index = self.calculate_favorability(clause_type, chunk)
#                 if favorability > 0:  # Only consider clauses with a positive favorability
#                     clause_info.append({
#                         "clause": chunk,
#                         "type": clause_type,
#                         "favorability": favorability,
#                         "start_index": start_index,
#                         "end_index": end_index
#                     })
#                     clause_counts[clause_type] += 1
#                     total_favorability += favorability
#                     num_clauses += 1

#         overall_favorability = total_favorability / num_clauses if num_clauses > 0 else 0

#         return {
#             "clause_info": clause_info,
#             "clause_counts": clause_counts,
#             "overall_favorability": overall_favorability
#         }




import numpy as np
from typing import Dict, List, Tuple
import fav_keywords  # Make sure this file contains the keywords and rules
import spacy
from functools import lru_cache

class ContractAnalyzer:
    def __init__(self):
        self.keywords = fav_keywords.contract_keywords
        self.nlp = spacy.load("en_core_web_md") # en_core_web_trf
        
    @lru_cache(maxsize=512)  # Load spaCy's English model
    def lemmatize_text(self, text: str) -> str:
        """
        Lemmatize the input text.

        :param text: The raw input text to lemmatize.
        :return: Lemmatized version of the input text.
        """
        doc = self.nlp(text)
        lemmatized_text = " ".join([token.lemma_ for token in doc])
        return lemmatized_text

    def calculate_favorability(self, clause_type: str, text: str) -> Tuple[int, int, int]:
        """
        Calculate favorability based on keywords and rules, using lemmatization.

        :param clause_type: The type of clause being evaluated.
        :param text: The text of the clause.
        :return: A tuple containing favorability score and the start and end indices of the match.
        """
        favorability_score = 0
        start_index = -1
        end_index = -1

        # Lemmatize the text for better matching
        lemmatized_text = self.lemmatize_text(text.lower())

        # Check for keywords
        keywords_info = self.keywords.get(clause_type)
        if keywords_info:
            keywords = keywords_info['keywords']
            rules = keywords_info['rules']

            # Check for presence of keywords
            for keyword in keywords:
                lemmatized_keyword = self.lemmatize_text(keyword.lower())  # Lemmatize the keyword
                if lemmatized_keyword in lemmatized_text:
                    favorability_score += 50  # Base score for presence of keywords
                    start_index = lemmatized_text.index(lemmatized_keyword)  # Start index of the keyword
                    end_index = start_index + len(lemmatized_keyword) - 1  # End index of the keyword

                    # Check positive rules
                    if any(self.lemmatize_text(rule.lower()) in lemmatized_text for rule in rules['positive']):
                        favorability_score += 30  # Score for favorable conditions

                    # Check negative rules
                    if any(self.lemmatize_text(rule.lower()) in lemmatized_text for rule in rules['negative']):
                        favorability_score -= 20  # Penalty for unfavorable conditions

                    break  # Exit loop after first match

        # Ensure the score is within the 1-100 range
        favorability_score = min(max(favorability_score, 1), 100)
        return favorability_score, start_index, end_index

    def analyze_document(self, text_chunks: List[str]) -> Dict:
        """
        Analyze the document to identify clauses and provide favorability scores.

        :param text_chunks: List of text chunks extracted from the document.
        :return: Analysis results containing clause annotations and favorability scores.
        """
        clause_counts = {clause_type: 0 for clause_type in self.keywords.keys()}
        clause_info = []
        total_favorability = 0
        num_clauses = 0

        for chunk in text_chunks:
            for clause_type in self.keywords.keys():
                favorability, start_index, end_index = self.calculate_favorability(clause_type, chunk)
                if favorability > 0:  # Only consider clauses with a positive favorability
                    clause_info.append({
                        "clause": chunk,
                        "type": clause_type,
                        "favorability": favorability,
                        "start_index": start_index,
                        "end_index": end_index
                    })
                    clause_counts[clause_type] += 1
                    total_favorability += favorability
                    num_clauses += 1

        overall_favorability = total_favorability / num_clauses if num_clauses > 0 else 0

        return {
            "clause_info": clause_info,
            "clause_counts": clause_counts,
            "overall_favorability": overall_favorability
        }
