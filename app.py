# # from flask import Flask, render_template, request, redirect, url_for
# # from file_processing import display_pdf, extract_text_chunks
# # from nlp import identify_clauses, extract_entities  # Updated to match new function structure
# # from summarization import generate_summary  # Ensure this matches your new summarization function name
# # from question_answering import get_answers
# # from contract_analysis import analyze_clauses

# # # Initialize the Flask app
# # app = Flask(__name__)

# # # Home Route
# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # # Upload Route
# # @app.route('/upload', methods=['GET', 'POST'])
# # def upload():
# #     if request.method == 'POST':
# #         file = request.files['file']
# #         if file:
# #             file_path = f'uploads/{file.filename}'
# #             file.save(file_path)
# #             return redirect(url_for('process', filename=file.filename))
# #     return render_template('upload.html')

# # # Process Route
# # @app.route('/process/<filename>', methods=['GET'])
# # def process(filename):
# #     file_path = f'uploads/{filename}'

# #     # Display the PDF content
# #     pdf_content = display_pdf(file_path)

# #     # Extract text chunks from the uploaded file
# #     text_chunks = extract_text_chunks(file_path)

# #     # Named Entity Recognition (NER) using LegalBERT model
# #     entities = extract_entities(text_chunks)

# #     # Clause Identification and Classification
# #     clause_data = identify_clauses(text_chunks)

# #     # Summarization of each text chunk using Facebook BART
# #     summaries = [generate_summary(chunk) for chunk in text_chunks]  # Updated function name
# #     final_summary = ' '.join(summaries)

# #     # Question Answering using DistilBERT SQuAD model
# #     answers = get_answers(text_chunks)

# #     # Contract Analysis (clause analysis) including favorability scoring
# #     analyzed_clauses, favorability = analyze_clauses(text_chunks)

# #     # Render the results on the analysis page
# #     return render_template('analysis.html',
# #                            pdf_content=pdf_content,
# #                            entities=entities,
# #                            clause_data=clause_data,
# #                            summaries=summaries,
# #                            final_summary=final_summary,
# #                            answers=answers,
# #                            analyzed_clauses=analyzed_clauses,
# #                            favorability=favorability)

# # # Error Handling Route
# # @app.errorhandler(404)
# # def page_not_found(e):
# #     return render_template('404.html'), 404

# # # Run the application
# # if __name__ == '__main__':
# #     app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for
# from file_processing import display_pdf, extract_text_chunks
# from nlp import identify_clauses, extract_entities  # Updated to match new function structure
# from summarization import generate_summary  # Ensure this matches your new summarization function name
# from question_answering import get_answers
# from contract_analysis import analyze_clauses

# # Initialize the Flask app
# app = Flask(__name__)

# # Home Route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Upload Route
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             file_path = f'uploads/{file.filename}'
#             file.save(file_path)
#             return redirect(url_for('process', filename=file.filename))
#     return render_template('upload.html')

# # Process Route
# @app.route('/process/<filename>', methods=['GET'])
# def process(filename):
#     file_path = f'uploads/{filename}'

#     # Display the PDF content
#     pdf_content = display_pdf(file_path)

#     # Extract text chunks from the uploaded file
#     text_chunks = extract_text_chunks(file_path)

#     # Named Entity Recognition (NER) using LegalBERT model
#     entities = extract_entities(text_chunks)

#     # Extracting contract details from entities
#     contract_title = ""
#     parties = []
#     contract_type = ""

#     for entity in entities:
#         if entity['label'] == 'TITLE':  # Adjust label according to your NER output
#             contract_title = entity['text']
#         elif entity['label'] == 'PARTY':  # Adjust label according to your NER output
#             parties.append(entity['text'])
#         elif entity['label'] == 'CONTRACT_TYPE':  # Adjust label according to your NER output
#             contract_type = entity['text']

#     # Clause Identification and Classification
#     clause_data = identify_clauses(text_chunks)

#     # Summarization of each text chunk using Facebook BART
#     summaries = [generate_summary(chunk, contract_title, parties, contract_type) for chunk in text_chunks]  # Updated function call
#     final_summary = ' '.join(summaries)

#     # Question Answering using DistilBERT SQuAD model
#     answers = get_answers(text_chunks)

#     # Contract Analysis (clause analysis) including favorability scoring
#     analyzed_clauses, favorability = analyze_clauses(text_chunks)

#     # Render the results on the analysis page
#     return render_template('analysis.html',
#                            pdf_content=pdf_content,
#                            entities=entities,
#                            clause_data=clause_data,
#                            summaries=summaries,
#                            final_summary=final_summary,
#                            answers=answers,
#                            analyzed_clauses=analyzed_clauses,
#                            favorability=favorability)

# # Error Handling Route
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# # Run the application
# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect, url_for
# from file_processing import display_pdf, extract_text_chunks
# from nlp import identify_clauses, extract_entities  # Updated to match new function structure
# from summarization import generate_summary  # Ensure this matches your new summarization function name
# from question_answering import get_answers, get_qa_history  # Added get_qa_history
# from contract_analysis import analyze_clauses

# # Initialize the Flask app
# app = Flask(__name__)

# # Home Route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Upload Route
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             file_path = f'uploads/{file.filename}'
#             file.save(file_path)
#             return redirect(url_for('process', filename=file.filename))
#     return render_template('upload.html')

# # Process Route
# @app.route('/process/<filename>', methods=['GET'])
# def process(filename):
#     file_path = f'uploads/{filename}'

#     # Display the PDF content
#     pdf_content = display_pdf(file_path)

#     # Extract text chunks from the uploaded file
#     text_chunks = extract_text_chunks(file_path)

#     # Named Entity Recognition (NER) using LegalBERT model
#     entities = extract_entities(text_chunks)

#     # Extracting contract details from entities
#     contract_title = ""
#     parties = []
#     contract_type = ""

#     for entity in entities:
#         if entity['label'] == 'TITLE':  # Adjust label according to your NER output
#             contract_title = entity['text']
#         elif entity['label'] == 'PARTY':  # Adjust label according to your NER output
#             parties.append(entity['text'])
#         elif entity['label'] == 'CONTRACT_TYPE':  # Adjust label according to your NER output
#             contract_type = entity['text']

#     # Clause Identification and Classification
#     clause_data = identify_clauses(text_chunks)

#     # Summarization of each text chunk using Facebook BART
#     summaries = [generate_summary(chunk, contract_title, parties, contract_type) for chunk in text_chunks]  # Updated function call
#     final_summary = ' '.join(summaries)

#     # Question Answering using DistilBERT SQuAD model
#     answers = get_answers(text_chunks, '', filename)  # Pass filename as document_id

#     # Retrieve question-answer history for the document
#     qa_history = get_qa_history(filename)  # Get the history for display if needed

#     # Contract Analysis (clause analysis) including favorability scoring
#     analyzed_clauses, favorability = analyze_clauses(text_chunks)

#     # Render the results on the analysis page
#     return render_template('analysis.html',
#                            pdf_content=pdf_content,
#                            entities=entities,
#                            clause_data=clause_data,
#                            summaries=summaries,
#                            final_summary=final_summary,
#                            answers=answers,
#                            qa_history=qa_history,  # Pass QA history to the template
#                            analyzed_clauses=analyzed_clauses,
#                            favorability=favorability)

# # Error Handling Route
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# # Run the application
# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect, url_for
# from file_processing import display_pdf, extract_text_chunks
# from nlp import identify_clauses, extract_entities
# from summarization import generate_summary
# from question_answering import get_answers, get_qa_history
# from contract_analysis import ContractAnalyzer  # Import the ContractAnalyzer class

# # Initialize the Flask app
# app = Flask(__name__)

# # Instantiate the ContractAnalyzer
# contract_analyzer = ContractAnalyzer()

# # Home Route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Upload Route
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             file_path = f'uploads/{file.filename}'
#             file.save(file_path)
#             return redirect(url_for('process', filename=file.filename))
#     return render_template('upload.html')

# # Process Route
# @app.route('/process/<filename>', methods=['GET'])
# def process(filename):
#     file_path = f'uploads/{filename}'

#     # Display the PDF content
#     pdf_content = display_pdf(file_path)

#     # Extract text chunks from the uploaded file
#     text_chunks = extract_text_chunks(file_path)

#     # Named Entity Recognition (NER) using LegalBERT model
#     entities = extract_entities(text_chunks)

#     # Extracting contract details from entities
#     contract_title = ""
#     parties = []
#     contract_type = ""

#     for entity in entities:
#         if entity['label'] == 'TITLE':  # Adjust label according to your NER output
#             contract_title = entity['text']
#         elif entity['label'] == 'PARTY':  # Adjust label according to your NER output
#             parties.append(entity['text'])
#         elif entity['label'] == 'CONTRACT_TYPE':  # Adjust label according to your NER output
#             contract_type = entity['text']

#     # Clause Identification and Classification
#     clause_data = identify_clauses(text_chunks)

#     # Summarization of each text chunk using Facebook BART
#     summaries = [generate_summary(chunk, contract_title, parties, contract_type) for chunk in text_chunks]
#     final_summary = ' '.join(summaries)

#     # Question Answering using DistilBERT SQuAD model
#     answers = get_answers(text_chunks, '', filename)  # Pass filename as document_id

#     # Retrieve question-answer history for the document
#     qa_history = get_qa_history(filename)  # Get the history for display if needed

#     # Contract Analysis (clause analysis) including favorability scoring
#     analysis_results = contract_analyzer.analyze_document(text_chunks)  # Call the analyze_document method

#     # Render the results on the analysis page
#     return render_template('analyze.html',
#                            pdf_content=pdf_content,
#                            entities=entities,
#                            clause_data=clause_data,
#                            summaries=summaries,
#                            final_summary=final_summary,
#                            answers=answers,
#                            qa_history=qa_history,
#                            analyzed_clauses=analysis_results['clause_info'],
#                            favorability=analysis_results['overall_favorability'])  # Update with the correct keys

# # Error Handling Route
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# # Run the application
# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for, jsonify
from file_processing import display_pdf, extract_text_chunks
from nlp import identify_clauses, extract_entities
from summarization import generate_summary
from question_answering import get_answers, get_qa_history
from contract_analysis import ContractAnalyzer  # Import the ContractAnalyzer class

# Initialize the Flask app
app = Flask(__name__)

# Instantiate the ContractAnalyzer
contract_analyzer = ContractAnalyzer()

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Upload Route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = f'uploads/{file.filename}'  # Ensure this folder exists
            file.save(file_path)
            return redirect(url_for('process', filename=file.filename))
    return render_template('upload.html')

# Process Route (for displaying PDF and analyzing)
@app.route('/process/<filename>', methods=['GET'])
def process(filename):
    file_path = f'uploads/{filename}'

    # Display the PDF content
    pdf_content = display_pdf(file_path)

    # Extract text chunks from the uploaded file
    text_chunks = extract_text_chunks(file_path)

    # Named Entity Recognition (NER) using LegalBERT model
    entities = extract_entities(text_chunks)

    # Extracting contract details from entities
    contract_title = ""
    parties = []
    contract_type = ""

    for entity in entities:
        if entity['label'] == 'TITLE':  # Adjust label according to your NER output
            contract_title = entity['text']
        elif entity['label'] == 'PARTY':  # Adjust label according to your NER output
            parties.append(entity['text'])
        elif entity['label'] == 'CONTRACT_TYPE':  # Adjust label according to your NER output
            contract_type = entity['text']

    # Clause Identification and Classification
    clause_data = identify_clauses(text_chunks)

    # Summarization of each text chunk using Facebook BART
    summaries = [generate_summary(chunk, contract_title, parties, contract_type) for chunk in text_chunks]
    final_summary = ' '.join(summaries)

    # Question Answering using DistilBERT SQuAD model
    answers = get_answers(text_chunks, '', filename)  # Pass filename as document_id

    # Retrieve question-answer history for the document
    qa_history = get_qa_history(filename)  # Get the history for display if needed

    # Contract Analysis (clause analysis) including favorability scoring
    analysis_results = contract_analyzer.analyze_document(text_chunks)  # Call the analyze_document method

    # Render the results on the analysis page
    return render_template('analyze.html',
                           pdf_content=pdf_content,
                           entities=entities,
                           clause_data=clause_data,
                           summaries=summaries,
                           final_summary=final_summary,
                           answers=answers,
                           qa_history=qa_history,
                           analyzed_clauses=analysis_results['clause_info'],
                           favorability=analysis_results['overall_favorability'])  # Update with the correct keys

# Analyze Route for AJAX Calls
@app.route('/analyze', methods=['POST'])
def analyze_document():
    data = request.get_json()
    document_id = data.get('documentId')

    # Logic to analyze the document based on document_id
    file_path = f'uploads/{document_id}'  # Adjust based on how you're managing uploads
    text_chunks = extract_text_chunks(file_path)
    
    # Analysis logic here
    analysis_results = contract_analyzer.analyze_document(text_chunks)

    # Return JSON response with results
    return jsonify(analysis_results)

# Error Handling Route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
