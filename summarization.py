import torch
from transformers import BartForConditionalGeneration, BartTokenizer
from functools import lru_cache

# Load the BART model and tokenizer
@lru_cache(maxsize=None)
def load_model_and_tokenizer():
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    return model, tokenizer

def generate_summary(text_chunk, contract_title=None, parties=None, contract_type=None):
    """
    Generate a summary for a given text chunk using the BART model.
    :param text_chunk: The text chunk to summarize.
    :param contract_title: The title of the contract.
    :param parties: List of parties involved in the contract.
    :param contract_type: The type of contract.
    :return: The generated summary as a string.
    """
    model, tokenizer = load_model_and_tokenizer()
    
    # Create bullet points for the contract information
    bullet_points = []
    if contract_title:
        bullet_points.append(f"**Contract Title:** {contract_title}")
    if parties:
        bullet_points.append(f"**Parties Involved:** {', '.join(parties)}")
    if contract_type:
        bullet_points.append(f"**Type of Contract:** {contract_type}")

    # Join bullet points with line breaks
    bullet_points_str = "\n".join(bullet_points)
    
    # Encode the text chunk and generate summary
    inputs = tokenizer.encode(text_chunk, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Combine bullet points and summary
    final_summary = f"{bullet_points_str}\n\nSummary:\n{summary}"
    
    return final_summary
