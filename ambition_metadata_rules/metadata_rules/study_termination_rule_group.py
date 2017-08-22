from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P

app_label = 'ambition_subject'


@register()
class StudyTerminationConclusionCrfRuleGroup(CrfRuleGroup):

    protocol_deviation_violation = CrfRule(
        predicate=P('termination_reason', 'eq', 'included_in_error'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.protocoldeviationviolation'])

    class Meta:
        source_model = f'{app_label}.studyterminationconclusion'
        app_label = 'ambition_metadata_rules'
