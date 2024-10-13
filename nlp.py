import numpy as np
import torch
from scipy.spatial.distance import cosine
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from functools import lru_cache
from clause_keywords import get_keyword_embeddings, load_embedding_model

@lru_cache(maxsize=1)
def load_ner_model():
    """
    Load the LegalBERT model and tokenizer using caching to reduce loading times.
    :return: The NER pipeline using LegalBERT.
    """
    tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
    model = AutoModelForTokenClassification.from_pretrained("nlpaueb/legal-bert-base-uncased")
    return pipeline("ner", model=model, tokenizer=tokenizer)

def get_text_embedding(text):
    """
    Calculate the average word embedding for a given text using the LegalBERT model.
    :param text: The input text.
    :return: A vector representing the average embedding of the words in the text.
    """
    model, tokenizer = load_embedding_model()
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Use the average of embeddings from the [CLS] token
    embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
    return embeddings

def extract_named_entities(text):
    """
    Perform Named Entity Recognition (NER) on the given text using LegalBERT.
    :param text: The input text.
    :return: A list of entities with their labels and positions.
    """
    ner_pipeline = load_ner_model()
    ner_results = ner_pipeline(text)
    entities = []
    for entity in ner_results:
        entities.append({
            'entity': entity['word'],
            'label': entity['entity'],
            'start_position': entity['start'],
            'end_position': entity['end']
        })
    return entities

def identify_clauses(text_chunks):
    """
    Identify and classify clauses in the text using word embeddings and similarity analysis.
    :param text_chunks: A list of text chunks extracted from the file.
    :return: A list of clauses with their start and end positions, and clause type classification.
    """
    keyword_embeddings = get_keyword_embeddings()
    identified_clauses = []

    for chunk in text_chunks:
        chunk_embedding = get_text_embedding(chunk)
        chunk_clauses = []
        
        if chunk_embedding is not None:
            for clause_type, embeddings in keyword_embeddings.items():
                for keyword_embedding in embeddings:
                    similarity = 1 - cosine(chunk_embedding, keyword_embedding)
                    if similarity > 0.7:  # Threshold for similarity
                        start_idx = chunk.lower().find(clause_type)
                        end_idx = start_idx + len(clause_type) if start_idx != -1 else None
                        chunk_clauses.append({
                            'clause_type': clause_type,
                            'similarity_score': similarity,
                            'start_position': start_idx,
                            'end_position': end_idx
                        })
        identified_clauses.append(chunk_clauses)

    return identified_clauses

def analyze_text(text_chunks):
    """
    Perform both Named Entity Recognition and Clause Identification on the text.
    :param text_chunks: A list of text chunks extracted from the file.
    :return: A dictionary containing both the extracted entities and identified clauses.
    """
    analysis_results = {
        'entities': [],
        'clauses': []
    }

    for chunk in text_chunks:
        entities = extract_named_entities(chunk)
        clauses = identify_clauses([chunk])

        analysis_results['entities'].extend(entities)
        analysis_results['clauses'].extend(clauses)

    return analysis_results
