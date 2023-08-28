def loan_approval_logic(credit_score):
    if credit_score >= 700:
        return "Approved"
    else:
        return "Pending"

# Example usage
applicant_credit_score = 720
approval_status = loan_approval_logic(applicant_credit_score)
print("Approval Status:", approval_status)
