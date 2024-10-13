import torch
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
from functools import lru_cache

# Dictionary to store questions and answers for each document
qa_history = {}

@lru_cache(maxsize=1)
def load_model():
    """
    Load the DistilBERT model and tokenizer. This will be cached.
    """
    model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased-distilled-squad')
    return model, tokenizer

def get_answers(text_chunks, question, document_id):
    """
    Retrieve answers for a given question based on the provided text chunks.
    
    :param text_chunks: List of text chunks extracted from the document.
    :param question: The question to answer.
    :param document_id: Unique identifier for the document (e.g., filename).
    :return: List of dictionaries containing possible answers and their confidence scores.
    """
    model, tokenizer = load_model()  # Ensure the model and tokenizer are loaded

    # Initialize the QA history for the document if it doesn't exist
    if document_id not in qa_history:
        qa_history[document_id] = []

    answers = []
    
    for chunk in text_chunks:
        # Tokenize the input
        inputs = tokenizer(question, chunk, return_tensors='pt')
        
        # Get the model's output
        with torch.no_grad():
            outputs = model(**inputs)
        
        # Get the start and end scores
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits
        
        # Get the most likely start and end of the answer
        start_index = torch.argmax(start_scores)
        end_index = torch.argmax(end_scores) + 1  # +1 to include the end token
        
        # Convert token indices back to words
        answer_tokens = inputs['input_ids'][0][start_index:end_index]
        answer = tokenizer.decode(answer_tokens)
        
        # Confidence score
        confidence = (torch.softmax(start_scores, dim=1)[0][start_index] + 
                      torch.softmax(end_scores, dim=1)[0][end_index - 1]).item()  # Combine start and end confidence
        
        answers.append({
            'answer': answer,
            'confidence': confidence
        })
    
    # Store the question and its answers in the history
    qa_history[document_id].append({
        'question': question,
        'answers': answers
    })

    return answers

def get_qa_history(document_id):
    """
    Retrieve the question-answer history for a given document ID.
    
    :param document_id: Unique identifier for the document (e.g., filename).
    :return: List of questions and their corresponding answers.
    """
    return qa_history.get(document_id, [])
