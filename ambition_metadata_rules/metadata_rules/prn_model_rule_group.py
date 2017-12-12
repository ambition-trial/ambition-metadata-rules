from ambition_labs import viral_load_panel, cd4_panel, fbc_panel, chemistry_alt_panel
from edc_constants.constants import YES
from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P
from edc_metadata_rules import RequisitionRule, RequisitionRuleGroup

from ..predicates import Predicates

app_label = 'ambition_subject'
pc = Predicates()


@register()
class PrnModelCrfRuleGroup(CrfRuleGroup):

    #     adverse_event = CrfRule(
    #         predicate=P('adverse_event', 'eq', YES),
    #         consequence=REQUIRED,
    #         alternative=NOT_REQUIRED,
    #         target_models=[f'{app_label}.adverseevent'])

    #     adverse_event_tmg = CrfRule(
    #         predicate=P('adverse_event_tmg', 'eq', YES),
    #         consequence=REQUIRED,
    #         alternative=NOT_REQUIRED,
    #         target_models=[f'{app_label}.adverseeventtmg'])
    #
    #     adverse_event_followup = CrfRule(
    #         predicate=P('adverse_event_followup', 'eq', YES),
    #         consequence=REQUIRED,
    #         alternative=NOT_REQUIRED,
    #         target_models=[f'{app_label}.adverseeventfollowup'])

    blood_result = CrfRule(
        predicate=P('blood_result', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.bloodresult'])

    microbiology = CrfRule(
        predicate=P('microbiology', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.microbiology'])

    radiology = CrfRule(
        predicate=P('radiology', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.radiology'])

#     recurrence_symptom = CrfRule(
#         predicate=pc.func_require_recurrence,
#         consequence=REQUIRED,
#         alternative=NOT_REQUIRED,
#         target_models=[f'{app_label}.recurrencesymptom'])
#
#     protocol_deviation = CrfRule(
#         predicate=P('protocol_deviation', 'eq', YES),
#         consequence=REQUIRED,
#         alternative=NOT_REQUIRED,
#         target_models=[f'{app_label}.protocoldeviationviolation'])

    lumbar_puncture = CrfRule(
        predicate=P('lumbar_puncture', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.lumbarpuncturecsf'])

#     death_report = CrfRule(
#         predicate=P('death_report', 'eq', YES),
#         consequence=REQUIRED,
#         alternative=NOT_REQUIRED,
#         target_models=[f'{app_label}.deathreport'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.prnmodel'


@register()
class PrnRequitisionRuleGroup(RequisitionRuleGroup):

    require_vl = RequisitionRule(
        predicate=P('viral_load', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[viral_load_panel])

    require_cd4 = RequisitionRule(
        predicate=P('cd4', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[cd4_panel])

    require_fbc = RequisitionRule(
        predicate=P('fbc', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[fbc_panel])

    require_chemistry = RequisitionRule(
        predicate=P('chemistry', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_panels=[chemistry_alt_panel])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.prnmodel'
        requisition_model = f'{app_label}.subjectrequisition'
