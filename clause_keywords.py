from transformers import AutoTokenizer, AutoModel
import torch
from functools import lru_cache

@lru_cache(maxsize=1)
def load_embedding_model():
    """
    Load the LegalBERT model using caching to reduce loading times.
    :return: The LegalBERT model and tokenizer.
    """
    tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
    model = AutoModel.from_pretrained("nlpaueb/legal-bert-base-uncased")
    return model, tokenizer

def get_keyword_embeddings():
    """
    Generate embeddings for predefined legal clause keywords using the LegalBERT model.
    :return: A dictionary with clause types as keys and their embeddings as values.
    """
    model, tokenizer = load_embedding_model()

    clause_keywords = {
    'Governing Law': ['jurisdiction', 'governing law', 'legal authority', 'venue', 'applicable law', 'statutory law', 'enforceability', 'local laws', 'law of the land', 'legal framework'],
    'Severability': ['severability', 'severable', 'independence', 'divisibility', 'separation', 'disentanglement', 'isolation', 'individuality'],
    'Indemnification': ['indemnify', 'compensation', 'reimbursement', 'repayment', 'restoration', 'damages', 'liability coverage', 'hold harmless', 'insurance', 'risk transfer'],
    'Confidentiality': ['confidential', 'non-disclosure', 'privacy', 'secrecy', 'restricted', 'classified', 'sensitive', 'private', 'proprietary', 'discretion', 'anonymity'],
    'Termination': ['terminate', 'end', 'cancel', 'void', 'expiration', 'cessation', 'discontinue', 'revoke', 'suspend', 'annul', 'finish', 'conclude'],
    'Liability': ['liability', 'responsibility', 'accountability', 'obligation', 'culpability', 'duty', 'responsiveness', 'risk', 'exposure', 'answerability', 'blame'],
    'Dispute Resolution': ['arbitration', 'mediation', 'dispute resolution', 'conflict resolution', 'settlement', 'negotiation', 'conciliation', 'reconciliation', 'resolution process', 'settlement agreement'],
    'Warranties and Representations': ['warranties', 'representations', 'guarantees', 'assurances', 'promises', 'certifications', 'affirmations', 'commitments'],
    'Force Majeure': ['force majeure', 'act of God', 'unforeseeable circumstances', 'extraordinary events', 'natural disasters', 'supervening impossibility', 'unexpected occurrences'],
    'Intellectual Property': ['intellectual property', 'patent', 'trademark', 'copyright', 'licensing', 'proprietary rights', 'inventions', 'creative works', 'brand', 'invention rights'],
    'Assignment': ['assignment', 'transfer', 'delegation', 'conveyance', 'handoff', 'assignment rights', 'substitution', 'passing of rights'],
    'Non-Compete': ['non-compete', 'restrictive covenant', 'competition restriction', 'non-competition', 'exclusivity', 'prohibition', 'competitive restriction', 'anti-competitive agreement'],
    'Non-Solicitation': ['non-solicitation', 'solicitation prohibition', 'employee poaching', 'client solicitation', 'restrictions', 'prospective client ban'],
    'Payment Terms': ['payment terms', 'consideration', 'compensation', 'remuneration', 'settlement', 'fees', 'payment conditions', 'financial arrangements'],
    'Scope of Work': ['scope of work', 'project scope', 'deliverables', 'services provided', 'work description', 'task list', 'project description'],
    'Amendments': ['amendments', 'modifications', 'changes', 'alterations', 'revisions', 'updates', 'adjustments', 'refinements'],
    'Entire Agreement': ['entire agreement', 'complete agreement', 'full agreement', 'integrated agreement', 'whole contract', 'entire contract'],
    'Notices': ['notices', 'communications', 'alerts', 'notifications', 'announcements', 'messages', 'correspondence'],
    'Governing Language': ['governing language', 'language of the contract', 'official language', 'interpretation', 'contract language', 'language of record'],
    'Counterparts': ['counterparts', 'duplicate originals', 'multiple copies', 'facsimile copies', 'reproductions', 'identical copies'],
    'Survival': ['survival', 'continuation', 'perpetuation', 'enduring obligations', 'lasting obligations', 'continued effectiveness'],
    'Insurance': ['insurance', 'coverage', 'policy', 'risk management', 'protection', 'assurance', 'safeguarding', 'underwriting'],
    'Limitation of Liability': ['limitation of liability', 'liability cap', 'liability limitation', 'damage caps', 'liability constraints', 'risk limitation'],
    'Equitable Relief': ['equitable relief', 'injunctive relief', 'specific performance', 'court orders', 'judicial remedies'],
    'Third-Party Beneficiaries': ['third-party beneficiaries', 'beneficiary rights', 'rights of third parties', 'outside parties', 'third-party interests'],
    'Assignment of Rights': ['assignment of rights', 'transfer of rights', 'delegation of rights', 'conveyance of rights', 'rights assignment'],
    'Performance Standards': ['performance standards', 'quality standards', 'service levels', 'criteria', 'performance criteria', 'quality benchmarks'],
    'Change of Control': ['change of control', 'control transfer', 'ownership change', 'equity transfer', 'management change'],
    'Conflicts of Interest': ['conflicts of interest', 'interest conflicts', 'bias', 'self-interest', 'personal interests', 'competing interests'],
    'Execution': ['execution', 'signing', 'endorsement', 'ratification', 'finalization', 'consent', 'approval'],
    'Compliance': ['compliance', 'adherence', 'conformance', 'observance', 'regulatory compliance', 'following regulations'],
    'Mediation': ['mediation', 'mediation process', 'mediation agreement', 'dispute resolution', 'conciliation', 'facilitated negotiation'],
    'Arbitration': ['arbitration', 'arbitral process', 'binding arbitration', 'dispute resolution', 'panel decision'],
    'Independent Contractors': ['independent contractors', 'contract labor', 'freelancers', 'self-employed', 'outsourced labor'],
    'Taxation': ['taxation', 'tax obligations', 'tax liabilities', 'fiscal responsibilities', 'tax duties', 'levies'],
    'Execution and Delivery': ['execution and delivery', 'signing and delivering', 'execution', 'endorsement', 'transfer of possession'],
    'Representation and Warranties': ['representation and warranties', 'affirmations', 'assurances', 'guarantees', 'statements of fact'],
    'Contract Term': ['contract term', 'duration', 'length of contract', 'contract period', 'term of agreement', 'effective period'],
    'Force Majeure Events': ['force majeure events', 'unforeseen events', 'extraordinary events', 'natural disasters', 'events beyond control']
}


    keyword_embeddings = {}

    for clause_type, keywords in clause_keywords.items():
        keyword_embeddings[clause_type] = []
        for keyword in keywords:
            inputs = tokenizer(keyword, return_tensors="pt")
            with torch.no_grad():
                outputs = model(**inputs)
            # Use the [CLS] token's embedding for semantic similarity
            keyword_embeddings[clause_type].append(outputs.last_hidden_state[0][0].numpy())

    return keyword_embeddings
