contract_keywords = {
    'Governing Law': {
        'keywords': [
            "governing law", "applicable law", "jurisdiction", "legal framework", 
            "law of the contract", "compliance", "regulatory environment", 
            "law interpretation", "statutory provisions", "legal obligations"
        ],
        'rules': {
            'positive': [
                "This agreement shall be governed by and construed in accordance with the laws of [specified jurisdiction].",
                "All disputes arising from or relating to this agreement shall be subject to the exclusive jurisdiction of the courts of [specified jurisdiction].",
                "Parties consent to the jurisdiction of [specified court] for any legal proceedings.",
                "Any changes or amendments to the governing law must be documented in writing and agreed upon by both parties.",
                "Parties acknowledge that they have read, understood, and agree to comply with all applicable laws and regulations of [specified jurisdiction]."
            ],
            'negative': [
                "Failure to comply with the governing law may result in the invalidation of this agreement.",
                "No claims shall be made or enforced without the prior consent of the governing jurisdiction.",
                "Parties cannot claim ignorance of the governing law or regulations affecting this agreement.",
                "Any disputes not addressed under the governing law shall not be enforceable in any jurisdiction.",
                "No amendments to the governing law shall be recognized unless they are formally executed and agreed to by both parties."
            ]
        }
    },

    'Severability': {
    'keywords': [
        "severability", "severable", "independent", "divisible", 
        "validity", "enforceability", "separation", "non-effect", 
        "invalid", "disentangle"
    ],
    'rules': {
        'positive': [
            "If any provision of this agreement is found to be invalid or unenforceable, the remaining provisions shall continue in full force and effect.",
            "The invalidity of any provision shall not affect the validity of the remaining provisions of this agreement.",
            "In the event that any provision is deemed unenforceable, the parties shall negotiate in good faith to modify the provision to reflect the original intent.",
            "Each clause of this agreement shall be construed independently of all other clauses.",
            "The parties agree that if any part of this agreement is declared invalid, the remainder will remain valid and enforceable."
        ],
        'negative': [
            "If any provision is deemed invalid, it may lead to the entire agreement being unenforceable.",
            "No part of this agreement should be construed as to diminish the enforceability of any remaining provisions.",
            "Parties cannot ignore severability clauses as they are critical to the integrity of the agreement.",
            "The inclusion of a severability clause does not excuse parties from complying with the remaining provisions.",
            "Failure to acknowledge the severability of this agreement may result in legal challenges."
        ]
    }
},

'Indemnification': {
    'keywords': [
        "indemnify", "compensation", "reimbursement", "repayment", 
        "damages", "hold harmless", "liability coverage", "insurance", 
        "risk transfer", "indemnification obligations", "indemnitor", 
        "indemnitee"
    ],
    'rules': {
        'positive': [
            "The indemnifying party agrees to indemnify and hold harmless the indemnified party from any claims, damages, or losses.",
            "Indemnification applies for any liabilities incurred as a result of third-party claims.",
            "The indemnified party shall be entitled to recover all reasonable costs and expenses associated with the indemnification.",
            "This indemnification obligation survives the termination of this agreement.",
            "The indemnifying party will provide a defense against any claims covered by the indemnification."
        ],
        'negative': [
            "Indemnification does not cover claims arising from the indemnified party's gross negligence or willful misconduct.",
            "The indemnifying party is not liable for any indirect, incidental, or consequential damages.",
            "Failure to notify the indemnifying party of a claim may void the indemnification obligation.",
            "Indemnification shall not apply to claims arising from breach of this agreement by the indemnified party.",
            "The indemnifying party is not responsible for claims made after the expiration of the agreement."
        ]
    }
},

'Confidentiality' : {
    'keywords': [
        "confidential", "non-disclosure", "privacy", "secrecy", 
        "restricted", "classified", "sensitive", "private", 
        "proprietary", "discretion", "anonymity", "trade secrets", 
        "information security", "data protection", "secret", 
        "confidential information"
    ],
    'rules': {
        'positive': [
            "All confidential information shall be treated with utmost care.",
            "The receiving party agrees to maintain confidentiality for all disclosed information.",
            "Confidentiality obligations survive the termination of this agreement.",
            "Disclosure of confidential information is permitted only to employees or agents who need to know.",
            "The parties agree not to disclose any confidential information to third parties without prior consent."
        ],
        'negative': [
            "Confidentiality obligations do not apply to information that is publicly known.",
            "The receiving party is not liable for damages if disclosure is required by law.",
            "Confidentiality shall not apply to information independently developed by the receiving party.",
            "The disclosing party's failure to label information as confidential does not waive confidentiality rights.",
            "Confidentiality obligations may be voided if information is disclosed due to gross negligence."
        ]
    }
},

'Termination' : {
    'keywords': [
        "terminate", "end", "cancel", "void", "expiration", 
        "cessation", "discontinue", "revoke", "suspend", 
        "annul", "finish", "conclude", "termination for cause", 
        "termination for convenience"
    ],
    'rules': {
        'positive': [
            "The contract may be terminated upon mutual agreement of both parties.",
            "Termination can occur without cause with a specified notice period.",
            "The contract shall remain effective until terminated in accordance with this clause.",
            "Either party may terminate this agreement if the other party fails to perform any material obligation.",
            "Termination for convenience is allowed with written notice."
        ],
        'negative': [
            "Termination for cause requires a material breach by the other party.",
            "Notice of termination must be provided in writing to be effective.",
            "The party terminating the agreement shall not be liable for any damages resulting from the termination.",
            "Termination does not relieve either party of obligations incurred prior to termination.",
            "The parties agree to resolve any outstanding disputes before termination."
        ]
    }
},

'Liability' : {
    'keywords': [
        "liability", "responsibility", "accountability", "obligation", 
        "culpability", "duty", "responsiveness", "risk", 
        "exposure", "answerability", "blame", "damages", 
        "claims", "indemnification", "exclusions"
    ],
    'rules': {
        'positive': [
            "The liability of each party is limited to direct damages only.",
            "Neither party shall be liable for indirect, incidental, or consequential damages.",
            "The parties agree to indemnify each other for claims arising from their respective breaches.",
            "Liability shall not exceed the total amount paid under this agreement.",
            "Parties shall take reasonable steps to mitigate any potential damages."
        ],
        'negative': [
            "Liability is excluded for events beyond reasonable control.",
            "The party shall not be liable for losses resulting from the negligence of the other party.",
            "Limitations on liability do not apply to gross negligence or willful misconduct.",
            "Liability for certain types of damages may be expressly limited in this agreement.",
            "Failure to provide notice of a claim may result in the waiver of liability."
        ]
    }
},

'Dispute Resolution' : {
    'keywords': [
        "arbitration", "mediation", "dispute resolution", "conflict resolution", 
        "settlement", "negotiation", "conciliation", "resolution process", 
        "settlement agreement", "litigation", "dispute", "panel", 
        "facilitation", "third-party mediation"
    ],
    'rules': {
        'positive': [
            "The parties agree to attempt to resolve disputes through negotiation.",
            "In the event of a dispute, the parties shall engage in mediation before arbitration.",
            "Arbitration shall be conducted in accordance with the rules of a specified arbitration association.",
            "Any disputes not resolved through mediation shall be submitted to binding arbitration.",
            "The costs of mediation or arbitration shall be shared equally by both parties."
        ],
        'negative': [
            "Dispute resolution does not apply to claims for injunctive relief.",
            "The party shall not be liable for any fees incurred by the other party in resolving disputes.",
            "Failure to participate in the mediation process may result in waiver of rights.",
            "Arbitration awards may not be appealed except on limited grounds.",
            "Confidentiality of the dispute resolution process is paramount."
        ]
    }
},

'Force Majeure' : {
    'keywords': [
        "force majeure", "act of God", "unforeseeable circumstances", 
        "extraordinary events", "natural disasters", "supervening impossibility", 
        "unexpected occurrences", "catastrophic events", "war", 
        "terrorism", "strikes", "government actions", 
        "pandemic", "epidemic", "earthquakes"
    ],
    'rules': {
        'positive': [
            "Neither party shall be liable for any delay or failure to perform due to force majeure.",
            "The affected party must notify the other party of the force majeure event within a specified timeframe.",
            "The performance obligation shall be suspended for the duration of the force majeure event.",
            "If the force majeure event continues for a specified period, either party may terminate the agreement.",
            "Parties agree to take reasonable steps to mitigate the impact of the force majeure event."
        ],
        'negative': [
            "Force majeure does not include financial inability to perform.",
            "A party claiming force majeure must prove that the event was beyond its reasonable control.",
            "Force majeure does not relieve a party from its payment obligations.",
            "Events that could have been avoided with reasonable foresight are not considered force majeure.",
            "Notice of the event must be provided in writing, failing which the claim may be waived."
        ]
    }
},

'Intellectual Property' :{
    'keywords': [
        "intellectual property", "patent", "trademark", "copyright", 
        "licensing", "proprietary rights", "inventions", 
        "creative works", "brand", "invention rights", 
        "trade secrets", "rights management", "IP rights", 
        "licensing agreements", "protection", "disclosure"
    ],
    'rules': {
        'positive': [
            "All intellectual property created during the term of this agreement shall be owned by the company.",
            "Licensee shall have a non-exclusive, non-transferable license to use the intellectual property.",
            "The party disclosing intellectual property must notify the recipient of its confidential nature.",
            "Any unauthorized use of the intellectual property shall result in termination of the license.",
            "Parties agree to protect each other’s intellectual property rights."
        ],
        'negative': [
            "The agreement does not grant any ownership rights to the licensee.",
            "Intellectual property rights do not extend to materials developed prior to the agreement.",
            "Use of third-party intellectual property must comply with applicable laws and licensing agreements.",
            "Failure to enforce intellectual property rights shall not constitute a waiver of rights.",
            "The party shall not be liable for any infringement claims arising from the use of the intellectual property."
        ]
    }
},

'Assignment' : {
    'keywords': [
        "assignment", "transfer", "delegation", "conveyance", 
        "handoff", "assignment rights", "substitution", 
        "passing of rights", "rights assignment", "assignment of obligations"
    ],
    'rules': {
        'positive': [
            "Neither party may assign its rights or obligations under this agreement without prior written consent.",
            "The assignee shall assume all rights and obligations of the assignor.",
            "Assignment of rights does not relieve the assignor of its obligations under the agreement.",
            "Consent to assign shall not be unreasonably withheld by either party.",
            "Any permitted assignment shall be binding upon successors and assigns."
        ],
        'negative': [
            "Unauthorized assignment shall be deemed a breach of this agreement.",
            "The agreement does not allow for assignment to third parties without consent.",
            "Assignment does not change the original terms and conditions of the agreement.",
            "Any assignment in violation of this clause is null and void.",
            "In the case of assignment, the party must notify the other party in writing."
        ]
    }
},

'Non-Compete' : {
    'keywords': [
        "non-compete", "restrictive covenant", "competition restriction", 
        "non-competition", "exclusivity", "prohibition", 
        "competitive restriction", "anti-competitive agreement", 
        "market restriction", "business limitation"
    ],
    'rules': {
        'positive': [
            "The party agrees not to engage in any competitive business for a specified duration.",
            "The non-compete clause shall apply within a specified geographical area.",
            "The parties acknowledge that the restrictions are reasonable and necessary to protect legitimate business interests.",
            "The agreement may include provisions for non-solicitation of employees and clients.",
            "Breach of the non-compete clause may result in injunctive relief."
        ],
        'negative': [
            "The non-compete restrictions shall not exceed a reasonable duration and geographical scope.",
            "The non-compete clause is void if not enforceable under applicable law.",
            "Parties may not restrict competition beyond what is necessary to protect their interests.",
            "Violation of the non-compete clause does not necessarily imply financial damages.",
            "The party may challenge the enforceability of the non-compete restrictions."
        ]
    }
},

'Non-Solicitation' : {
    'keywords': [
        "non-solicitation", "solicitation prohibition", 
        "employee poaching", "client solicitation", "restrictions", 
        "prospective client ban", "prohibited contact", 
        "solicitation of employees", "solicitation of customers"
    ],
    'rules': {
        'positive': [
            "The party agrees not to solicit employees or clients of the other party for a specified period.",
            "Non-solicitation obligations shall survive the termination of the agreement.",
            "The parties acknowledge that solicitation harms legitimate business interests.",
            "The agreement may include specific penalties for breach of the non-solicitation clause.",
            "The parties agree to provide notice of any potential solicitation."
        ],
        'negative': [
            "The non-solicitation clause does not prevent hiring employees who respond to public job advertisements.",
            "Solicitation of former employees after a specified duration is permissible.",
            "The non-solicitation clause is void if found to be overly broad or unreasonable.",
            "Non-solicitation restrictions shall not apply to clients with whom the party had no prior relationship.",
            "Violation of the non-solicitation clause must be substantiated with evidence."
        ]
    }
},

'Payment Terms' : {
    'keywords': [
        "payment terms", "consideration", "compensation", 
        "remuneration", "settlement", "fees", 
        "payment conditions", "financial arrangements", 
        "invoicing", "billing", "due dates"
    ],
    'rules': {
        'positive': [
            "Payments shall be made within a specified number of days after receipt of invoice.",
            "The agreed-upon fees are outlined in the attached schedule.",
            "Late payments may incur a specified interest rate.",
            "The client may pay via multiple payment methods as specified.",
            "All payments are non-refundable unless otherwise stated."
        ],
        'negative': [
            "Payments shall not be contingent on the satisfaction of any third party.",
            "The client shall not withhold payments for disputed amounts without proper notice.",
            "Failure to pay may result in termination of services.",
            "Any amendments to payment terms must be agreed upon in writing.",
            "The provider is not responsible for delays due to banking issues or holidays."
        ]
    }
},

'Scope of Work' : {
    'keywords': [
        "scope of work", "project scope", "deliverables", 
        "services provided", "work description", "task list", 
        "project description", "objectives", "requirements", 
        "tasks", "project milestones"
    ],
    'rules': {
        'positive': [
            "The scope of work is defined in the attached document.",
            "Any changes to the scope must be documented and agreed upon.",
            "Deliverables shall be provided according to the specified timeline.",
            "The service provider shall meet the requirements outlined in the scope.",
            "The client may request changes to the scope with reasonable notice."
        ],
        'negative': [
            "Any work outside the agreed scope shall incur additional charges.",
            "The provider shall not be held liable for delays caused by client changes.",
            "Vague descriptions in the scope may lead to misunderstandings.",
            "Failure to adhere to the specified scope may result in contract termination.",
            "Any assumptions made in the scope that are not documented may not be honored."
        ]
    }
},

'Amendments' : {
    'keywords': [
        "amendments", "modifications", "changes", 
        "alterations", "revisions", "updates", 
        "adjustments", "refinements", "addenda", 
        "supplements"
    ],
    'rules': {
        'positive': [
            "Amendments must be made in writing and signed by both parties.",
            "Changes to the contract shall take effect only upon mutual agreement.",
            "The parties may agree to review the contract at specified intervals.",
            "Any amendments shall be documented in an addendum to the contract.",
            "Parties may negotiate amendments based on changing circumstances."
        ],
        'negative': [
            "Verbal amendments shall not be binding.",
            "Unilateral changes without consent are not valid.",
            "Amendments may not exceed the original purpose of the agreement.",
            "Changes that increase liability may require additional consideration.",
            "The parties may not amend the contract to introduce illegal provisions."
        ]
    }
},

'Entire Agreement' :  {
    'keywords': [
        "entire agreement", "complete agreement", "full agreement", 
        "integrated agreement", "whole contract", "entire contract", 
        "comprehensive agreement", "final agreement"
    ],
    'rules': {
        'positive': [
            "This agreement constitutes the entire understanding between the parties.",
            "No other agreements, oral or written, shall be valid or binding.",
            "The parties acknowledge that they have read and understood this agreement.",
            "This contract supersedes all prior negotiations and agreements.",
            "Any amendments must be in writing and signed to be valid."
        ],
        'negative': [
            "Previous negotiations or representations shall not affect the agreement.",
            "Terms or conditions not included in this contract are not enforceable.",
            "No party may rely on any prior discussions not included in this contract.",
            "Changes made without the proper amendment process are void.",
            "Disputes arising from prior agreements shall not impact the validity of this agreement."
        ]
    }
},

'Notices' : {
    'keywords': [
        "notices", "communications", "alerts", 
        "notifications", "announcements", "messages", 
        "correspondence", "service of notice", 
        "written communication"
    ],
    'rules': {
        'positive': [
            "All notices shall be in writing and delivered to the addresses specified.",
            "Notice shall be deemed received on the date of delivery.",
            "Electronic communications may be used for notices if agreed upon.",
            "The parties agree to notify each other of any changes in contact information.",
            "Notices sent by registered mail shall be considered served."
        ],
        'negative': [
            "Failure to provide notice as specified may result in delays or disputes.",
            "Notices sent to incorrect addresses shall be deemed invalid.",
            "Verbal notices are not recognized under this agreement.",
            "Failure to respond to a notice within the specified time may lead to consequences.",
            "Notices not sent in accordance with the agreed method shall be ineffective."
        ]
    }
},

'Governing Language': {
    'keywords': [
        "governing language", "language of the contract", 
        "official language", "interpretation", 
        "contract language", "language of record"
    ],
    'rules': {
        'positive': [
            "This contract is executed in the governing language.",
            "In case of discrepancies, the version in the governing language prevails.",
            "Parties confirm their understanding of the governing language.",
            "Translations may be provided for reference, but the governing language is authoritative.",
            "Any amendments shall also be executed in the governing language."
        ],
        'negative': [
            "Disputes regarding translations shall not affect the governing language.",
            "No reliance on informal translations for interpretation of this contract.",
            "Misinterpretation due to language issues shall not excuse non-compliance.",
            "The governing language shall not be changed without mutual consent.",
            "Parties may not assert lack of understanding due to language barriers."
        ]
    }
},

'Counterparts': {
    'keywords': [
        "counterparts", "duplicate originals", 
        "multiple copies", "facsimile copies", 
        "reproductions", "identical copies"
    ],
    'rules': {
        'positive': [
            "This agreement may be executed in multiple counterparts.",
            "Each counterpart shall be considered an original document.",
            "Counterparts may be exchanged electronically or via facsimile.",
            "All counterparts together shall constitute one agreement.",
            "Signatures may be provided on separate counterparts."
        ],
        'negative': [
            "Counterparts shall not be binding unless all parties have signed.",
            "A party may not rely on unsigned counterparts.",
            "Changes made on one counterpart must be reflected in all counterparts.",
            "Not all counterparts being executed simultaneously does not invalidate the agreement.",
            "Counterparts not signed by all parties shall be deemed incomplete."
        ]
    }
},

'Survival': {
    'keywords': [
        "survival", "continuation", "perpetuation", 
        "enduring obligations", "lasting obligations", 
        "continued effectiveness", "post-termination obligations"
    ],
    'rules': {
        'positive': [
            "Certain obligations shall survive the termination of this agreement.",
            "The survival clause is intended to protect the parties' rights.",
            "Confidentiality obligations shall survive for a specified period after termination.",
            "Indemnification responsibilities may also survive the termination.",
            "Parties agree that liability provisions shall continue post-termination."
        ],
        'negative': [
            "Obligations not expressly stated as surviving shall not continue.",
            "No party shall assume responsibilities after termination without a written agreement.",
            "Survival provisions shall not be construed to extend indefinitely.",
            "Lack of clarity in the survival clause may lead to unenforceability.",
            "Survival clauses do not grant new rights or obligations."
        ]
    }
},

'Insurance' : {
    'keywords': [
        "insurance", "coverage", "policy", 
        "risk management", "protection", "assurance", 
        "safeguarding", "underwriting", "liability coverage"
    ],
    'rules': {
        'positive': [
            "The parties shall maintain appropriate insurance coverage.",
            "Certificates of insurance shall be provided upon request.",
            "Insurance policies must cover specified risks associated with the contract.",
            "The parties agree to name each other as additional insured.",
            "Proof of insurance must be submitted prior to the commencement of services."
        ],
        'negative': [
            "Failure to provide evidence of insurance may result in contract termination.",
            "The agreement does not require coverage for risks not specified.",
            "No party shall be liable for damages not covered by their insurance.",
            "The insurer’s obligations do not extend beyond the terms of the policy.",
            "Parties may not rely on verbal assurances regarding insurance."
        ]
    }
},

'Limitation of Liability': {
    'keywords': [
        "limitation of liability", "liability cap", 
        "liability limitation", "damage caps", 
        "liability constraints", "risk limitation"
    ],
    'rules': {
        'positive': [
            "The liability of each party shall be limited to the total fees paid under this agreement.",
            "No party shall be liable for indirect, consequential, or punitive damages.",
            "Liability shall not exceed a specified dollar amount unless due to gross negligence.",
            "Parties agree to indemnify each other to the extent of their liability.",
            "Limitations of liability shall survive the termination of this agreement."
        ],
        'negative': [
            "Limitations shall not apply to claims of fraud or willful misconduct.",
            "Exclusions of liability may not shield a party from gross negligence.",
            "Limitation of liability clauses may not be enforceable in all jurisdictions.",
            "Parties may not waive limitations of liability without mutual consent.",
            "Liability limitations shall not affect the obligations of indemnification."
        ]
    }
},

'Equitable Relief' : {
    'keywords': [
        "equitable relief", "injunctive relief", "specific performance", 
        "court orders", "judicial remedies", "equitable remedies", 
        "reparative measures", "non-monetary relief"
    ],
    'rules': {
        'positive': [
            "The parties acknowledge that monetary damages may be insufficient.",
            "Injunctive relief may be sought in cases of breach.",
            "Specific performance shall be an available remedy for breach of contract.",
            "Parties may seek equitable relief without the requirement of posting a bond.",
            "The right to seek equitable relief shall not limit other available remedies."
        ],
        'negative': [
            "Equitable relief shall not be available for claims arising from negligence.",
            "Parties may not seek equitable relief for breaches that are easily remedied.",
            "The court may deny equitable relief if it would cause undue hardship.",
            "No party may waive the right to seek equitable remedies in this agreement.",
            "Equitable relief does not substitute for any agreed-upon dispute resolution process."
        ]
    }
},

'Third-Party Beneficiaries' : {
    'keywords': [
        "third-party beneficiaries", "beneficiary rights", 
        "rights of third parties", "outside parties", 
        "third-party interests", "external beneficiaries", 
        "beneficiary claims"
    ],
    'rules': {
        'positive': [
            "This agreement does not confer rights upon any third party.",
            "Parties may designate specific third parties as beneficiaries.",
            "Third-party beneficiaries may enforce their rights under this contract.",
            "The parties acknowledge the interests of identified third-party beneficiaries.",
            "The intention to benefit third parties must be expressly stated."
        ],
        'negative': [
            "No outside party shall have standing to enforce this contract without consent.",
            "The parties may not unilaterally modify third-party rights without agreement.",
            "Third-party beneficiaries may not claim rights without proper identification.",
            "No party shall assert claims on behalf of a third-party beneficiary without authority.",
            "The agreement shall not create any obligations to third parties absent express terms."
        ]
    }
},

'Assignment of Rights' : {
    'keywords': [
        "assignment of rights", "transfer of rights", 
        "delegation of rights", "conveyance of rights", 
        "rights assignment", "rights transfer", 
        "assignment agreement", "delegation agreement"
    ],
    'rules': {
        'positive': [
            "Rights may be assigned with prior written consent of all parties.",
            "Assignments shall not relieve the assignor of obligations under this agreement.",
            "The parties agree that rights may be assigned to affiliated entities.",
            "Notice of assignment must be provided to all parties involved.",
            "Assignments of rights shall be documented in writing."
        ],
        'negative': [
            "No party may assign rights without consent from the other parties.",
            "Assignments made without proper notice shall be deemed invalid.",
            "The assignment of rights shall not alter the original contract terms.",
            "Parties may not assign their rights to competitors without consent.",
            "Unauthorized assignments may result in termination of the agreement."
        ]
    }
},

'Performance Standards' : {
    'keywords': [
        "performance standards", "quality standards", 
        "service levels", "criteria", 
        "performance criteria", "quality benchmarks", 
        "key performance indicators", "KPIs"
    ],
    'rules': {
        'positive': [
            "The parties agree to adhere to established performance standards.",
            "Performance metrics will be reviewed at specified intervals.",
            "Failure to meet performance standards may trigger corrective actions.",
            "Service levels shall be defined in the project schedule.",
            "Regular assessments of performance standards will be conducted."
        ],
        'negative': [
            "Failure to meet performance standards does not excuse contract breaches.",
            "The provider shall not be held liable for performance affected by external factors.",
            "Performance standards must be clearly defined to avoid ambiguity.",
            "Lack of adherence to performance standards may result in penalties.",
            "Parties may not ignore performance deficiencies without addressing them."
        ]
    }
},

'Change of Control': {
    'keywords': [
        "change of control", "control transfer", 
        "ownership change", "equity transfer", 
        "management change", "change in ownership", 
        "shareholder changes", "ownership structure"
    ],
    'rules': {
        'positive': [
            "A change of control shall require prior written notice to all parties.",
            "Parties may agree to additional terms in the event of a change of control.",
            "Rights and obligations shall remain in effect despite a change of control.",
            "Change of control clauses shall be defined in detail within the contract.",
            "Parties may evaluate the impact of control changes on performance obligations."
        ],
        'negative': [
            "Unauthorized changes of control may lead to contract termination.",
            "No party may transfer control without prior consent from other parties.",
            "Changes in control shall not affect any existing rights or liabilities.",
            "Parties may not assume obligations under new ownership without consent.",
            "The contract shall not be automatically assigned upon change of control."
        ]
    }
},

'Conflicts of Interest' : {
    'keywords': [
        "conflicts of interest", "interest conflicts", 
        "bias", "self-interest", 
        "personal interests", "competing interests", 
        "ethical concerns", "undue influence"
    ],
    'rules': {
        'positive': [
            "Parties shall disclose any potential conflicts of interest.",
            "Measures shall be taken to mitigate any identified conflicts.",
            "The parties agree to act in the best interests of the contract.",
            "Training may be provided to avoid conflicts of interest.",
            "Parties may seek independent counsel if conflicts arise."
        ],
        'negative': [
            "Parties shall not engage in actions that create conflicts of interest.",
            "Failure to disclose conflicts may lead to termination of the agreement.",
            "Conflicts of interest may not be used to justify breaches of contract.",
            "Parties may not benefit from undisclosed conflicts in negotiations.",
            "Lack of transparency regarding conflicts shall not be tolerated."
        ]
    }
},

'Execution': {
    'keywords': [
        "execution", "signing", 
        "endorsement", "ratification", 
        "finalization", "consent", 
        "approval", "effective date"
    ],
    'rules': {
        'positive': [
            "This contract shall be executed in counterparts.",
            "Execution of the contract signifies acceptance of all terms.",
            "Parties may execute the agreement electronically if agreed upon.",
            "All parties must sign to validate the contract.",
            "Execution shall occur on or before the effective date specified."
        ],
        'negative': [
            "No party may execute the contract without proper authority.",
            "Execution under duress or coercion shall render the contract void.",
            "Unsigned agreements shall not be binding upon any party.",
            "Amendments made after execution must be properly documented.",
            "The agreement may not be executed by a party lacking legal capacity."
        ]
    }
},

'Compliance':  {
    'keywords': [
        "compliance", "adherence", "conformance", 
        "observance", "regulatory compliance", 
        "following regulations", "legal compliance", 
        "rule following", "standards compliance"
    ],
    'rules': {
        'positive': [
            "Parties agree to comply with all applicable laws and regulations.",
            "Compliance audits may be conducted periodically.",
            "All parties shall maintain documentation for compliance verification.",
            "Compliance with industry standards is mandatory.",
            "The parties will cooperate to ensure compliance with legal obligations."
        ],
        'negative': [
            "Failure to comply may result in contract termination.",
            "Non-compliance shall not excuse performance obligations.",
            "Parties may not ignore compliance requirements.",
            "Liability for non-compliance rests solely with the non-compliant party.",
            "Disregarding compliance guidelines may lead to penalties."
        ]
    }
},

'Mediation': {
    'keywords': [
        "mediation", "mediation process", 
        "mediation agreement", "dispute resolution", 
        "conciliation", "facilitated negotiation", 
        "third-party mediation", "neutral facilitation"
    ],
    'rules': {
        'positive': [
            "Parties agree to mediate disputes prior to arbitration.",
            "The mediation process shall be confidential.",
            "Mediation shall be conducted in good faith by all parties.",
            "The parties will share the costs of mediation equally.",
            "A qualified mediator shall be selected by mutual agreement."
        ],
        'negative': [
            "Failure to participate in mediation may result in legal consequences.",
            "Parties may not disclose mediation discussions without consent.",
            "Mediation shall not delay obligations under the contract.",
            "No party may unilaterally withdraw from mediation once initiated.",
            "Mediation results are not legally binding unless formalized."
        ]
    }
},

'Arbitration': {
    'keywords': [
        "arbitration", "arbitral process", 
        "binding arbitration", "dispute resolution", 
        "panel decision", "arbitration agreement", 
        "arbitrator", "arbitration rules"
    ],
    'rules': {
        'positive': [
            "Disputes shall be resolved through binding arbitration.",
            "Arbitration shall occur in accordance with established rules.",
            "The parties agree to accept the arbitrator's decision as final.",
            "Costs associated with arbitration shall be shared by all parties.",
            "Arbitration proceedings shall remain confidential."
        ],
        'negative': [
            "Parties may not resort to litigation before arbitration is attempted.",
            "Failure to comply with arbitration terms may result in legal action.",
            "Arbitration findings are not subject to appeal unless specified.",
            "The arbitrator's authority shall be limited to the terms of the contract.",
            "No party may unreasonably delay the arbitration process."
        ]
    }
},

'Independent Contractors': {
    'keywords': [
        "independent contractors", "contract labor", 
        "freelancers", "self-employed", 
        "outsourced labor", "contractual workers", 
        "third-party service providers", "external contractors"
    ],
    'rules': {
        'positive': [
            "Independent contractors shall perform services as agreed.",
            "Contractors are responsible for their own tax obligations.",
            "Parties acknowledge the independent status of contractors.",
            "Independent contractors shall provide their own equipment.",
            "The agreement shall outline the scope of work for contractors."
        ],
        'negative': [
            "Independent contractors are not employees of the company.",
            "Parties may not exert control over the contractors' methods.",
            "Contractors may not claim employee benefits or protections.",
            "Misclassification of contractors as employees may result in penalties.",
            "Independent contractors must comply with their contractual obligations."
        ]
    }
},

'Taxation': {
    'keywords': [
        "taxation", "tax obligations", 
        "tax liabilities", "fiscal responsibilities", 
        "tax duties", "levies", 
        "tax compliance", "tax regulations"
    ],
    'rules': {
        'positive': [
            "Each party is responsible for its own tax liabilities.",
            "Tax obligations shall be clearly stated in the agreement.",
            "Parties shall comply with all applicable tax laws.",
            "The agreement shall not exempt parties from tax responsibilities.",
            "All tax-related documents shall be maintained for review."
        ],
        'negative': [
            "Failure to fulfill tax obligations may result in penalties.",
            "No party may evade taxes through contract terms.",
            "Tax obligations shall not be ignored or deferred without agreement.",
            "Parties may not misrepresent tax-related information.",
            "Liability for unpaid taxes shall rest solely with the responsible party."
        ]
    }
},

'Execution and Delivery': {
    'keywords': [
        "execution and delivery", "signing and delivering", 
        "execution", "endorsement", 
        "transfer of possession", "contract delivery", 
        "document execution", "execution process"
    ],
    'rules': {
        'positive': [
            "The contract shall be executed by authorized representatives.",
            "Delivery of the contract must occur by the specified date.",
            "Execution may take place in counterparts as necessary.",
            "Each party shall receive a signed copy of the executed agreement.",
            "Delivery shall be deemed complete upon receipt by the parties."
        ],
        'negative': [
            "Failure to execute the agreement shall nullify its terms.",
            "Delivery shall not be delayed without mutual consent.",
            "Unsigned contracts shall not be enforceable.",
            "Parties may not alter the execution process without agreement.",
            "Late delivery may result in liability for breach of contract."
        ]
    }
},

'Representation and Warranties': {
    'keywords': [
        "representation and warranties", "affirmations", 
        "assurances", "guarantees", 
        "statements of fact", "warranty obligations", 
        "promises", "declarations"
    ],
    'rules': {
        'positive': [
            "Each party makes representations regarding its authority.",
            "Warranties shall be specified within the agreement.",
            "Parties shall ensure that representations are accurate and truthful.",
            "Breach of warranty may result in damages or remedies.",
            "The agreement may specify duration for warranties."
        ],
        'negative': [
            "Parties may not disclaim liability for false representations.",
            "Misrepresentation shall entitle the aggrieved party to remedies.",
            "Warranties shall not be construed to limit the scope of liability.",
            "Failure to uphold warranties may lead to termination of the contract.",
            "Parties may not rely on oral representations not included in the agreement."
        ]
    }
},

'Contract Term': {
    'keywords': [
        "contract term", "duration", 
        "length of contract", "contract period", 
        "term of agreement", "effective period", 
        "contract timeline", "period of performance"
    ],
    'rules': {
        'positive': [
            "The contract term shall be clearly defined.",
            "Renewal options may be included within the contract.",
            "The term may be extended upon mutual agreement.",
            "Termination shall be governed by the specified contract term.",
            "Parties shall review the contract term periodically."
        ],
        'negative': [
            "Failure to adhere to the contract term may result in penalties.",
            "No party may unilaterally extend the contract term without consent.",
            "The contract shall not remain in effect beyond the agreed term.",
            "Parties may not terminate the contract without notice as specified.",
            "Contract obligations shall cease upon expiration unless renewed."
        ]
    }
},

'Force Majeure Events': {
    'keywords': [
        "force majeure events", "unforeseen events", 
        "extraordinary events", "natural disasters", 
        "events beyond control", "act of God", 
        "supply chain disruptions", "external shocks"
    ],
    'rules': {
        'positive': [
            "Parties shall be excused from performance due to force majeure.",
            "Force majeure events must be documented and communicated.",
            "The contract shall define specific force majeure events.",
            "Affected parties may suspend obligations during force majeure.",
            "Notice of force majeure must be provided within a specified time frame."
        ],
        'negative': [
            "Force majeure shall not excuse non-performance due to negligence.",
            "Parties may not claim force majeure without proper evidence.",
            "Failure to notify the other party of force majeure may result in liability.",
            "Force majeure events shall not extend the contract term unless agreed.",
            "Parties may not invoke force majeure for foreseeable events."
        ]
    }
}





































}
