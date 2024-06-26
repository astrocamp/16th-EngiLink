import rules


@rules.predicate
def is_company(custom_user):
    return custom_user.user_type == 2


@rules.predicate
def is_current_company(company_user, company):
    return company_user == company.custom_user


@rules.predicate
def is_job_owner(user, job):
    return user == job.company.custom_user


rules.add_perm("jobs.show_job", is_company)
rules.add_rule("is_current_company", is_current_company)
rules.add_rule("is_job_owner", is_job_owner)
