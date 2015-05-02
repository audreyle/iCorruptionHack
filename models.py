import re
from blessings import Terminal
from peewee import *
from app import db

import datetime

from flask_peewee.utils import get_dictionary_from_model

from itertools import tee, izip
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

t = Terminal()

class BaseModel(Model):
    class Meta:
        database = db

class File(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null=False)
    years = CharField(null=False)
    sha1 = CharField(null=False)
    updated = DateTimeField(null=False)
    ingested = BooleanField(null=False)

    def __str__(self):
        return self.name

class ContributionBaseModel(BaseModel):
    sub_id = BigIntegerField(null=False)
    cycle = CharField(null=False)
    date = DateField(null=False)

    comittee_id = CharField(null=True, default=None)
    ammendment_id = CharField(null=True, default=None)
    report_type = CharField(null=True, default=None)
    transaction_pgi = CharField(null=True, default=None)
    image_num = CharField(null=True, default=None)
    transaction_tp = CharField(null=True, default=None)
    entity_tp = CharField(null=True, default=None)
    name = CharField(null=True, default=None)
    city = CharField(null=True, default=None)
    state = CharField(null=True, default=None)
    zip_code = CharField(null=True, default=None)
    employer = CharField(null=True, default=None)
    occupation = CharField(null=True, default=None)
    transaction_date = DateTimeField(null=True, default=None)
    transaction_amount = FloatField(null=True, default=None)
    other_id = CharField(null=True, default=None)
    transaction_id = CharField(null=True, default=None)
    file_num = IntegerField(null=True, default=None)
    memo_cd = CharField(null=True, default=None)
    memo_text = CharField(null=True, default=None)

# Most Recent Contributions
class Contribution(ContributionBaseModel):
    id = PrimaryKeyField()

    def get_on_date(self, date):
        if self.date == date:
            return self
        elif self.date < date:
            raise Exception("%s date not found in database. too far in future" % date.strftime("%x"))
        else:
            changes = sorted(self.changes, key=lambda x: x.date, reverse=True)

            if self.date > date and changes[0].date <= date:
                return changes[0]

            for contrib_a, contrib_b in pairwise(changes):
                if contrib_a.date >= date and contrib_b.date <= date:
                    return contrib_a
            else:
                raise Exception("%s date not found in database. too far in past" % date.strftime("%x"))

    class Meta:
        # primary_key = CompositeKey('cycle', 'sub_id')
        indexes = ((('cycle', 'sub_id'), True),)

# ContributionChanges
class ContributionChanges(ContributionBaseModel):
    id = PrimaryKeyField()
    contribution = ForeignKeyField(Contribution, related_name='changes')

    class Meta:
        # primary_key = CompositeKey('date', 'cycle', 'sub_id')
        indexes = ((('date', 'cycle', 'sub_id'), True),)

# ContributionHistory
class ContributionHistory(BaseModel):
    id = PrimaryKeyField()
    contribution = ForeignKeyField(Contribution, related_name='history')

    sub_id = BigIntegerField(null=False)
    cycle = CharField(null=False)
    date = DateField(null=False)

    class Meta:
        # primary_key = CompositeKey('date', 'cycle', 'sub_id')
        indexes = ((('date', 'cycle', 'sub_id'), True),)

# CampaignAndCommiteeSummary
class CampaignAndComitteeSummary(BaseModel):
    id = PrimaryKeyField() #just added this for now
    com_nam = CharField(null=False)
    lin_ima = CharField(null=False)
    rep_typ = CharField(null=False)
    com_typ = CharField(null=False)
    com_des = CharField(null=False)
    fil_fre = CharField(null=False)
    add = CharField(null=False)
    cit = CharField(null=False)
    sta = CharField(null=False)
    zip = CharField(null=False)
    tre_nam = CharField(null=False)
    com_id = CharField(null=False)
    fec_ele_yea = CharField(null=False)
    ind_ite_con = CharField(null=False)
    ind_uni_con = CharField(null=False)
    ind_con = CharField(null=False)
    ind_ref = CharField(null=False)
    par_com_con = CharField(null=False)
    oth_com_con = CharField(null=False)
    oth_com_ref = CharField(null=False)
    can_con = CharField(null=False)
    tot_con = CharField(null=False)
    tot_con_ref = CharField(null=False)
    can_loa = CharField(null=False)
    can_loa_rep = CharField(null=False)
    oth_loa = CharField(null=False)
    oth_loa_rep = CharField(null=False)
    tot_loa = CharField(null=False)
    tot_loa_rep = CharField(null=False)
    tra_fro_oth_aut_com = CharField(null=False)
    tra_fro_non_fed_acc = CharField(null=False)
    tra_fro_non_fed_lev_acc = CharField(null=False)
    tot_non_fed_tra = CharField(null=False)
    oth_rec = CharField(null=False)
    tot_rec = CharField(null=False)
    tot_fed_rec = CharField(null=False)
    ope_exp = CharField(null=False)
    sha_fed_ope_exp = CharField(null=False)
    sha_non_fed_ope_exp = CharField(null=False)
    tot_ope_exp = CharField(null=False)
    off_to_ope_exp = CharField(null=False)
    fed_sha_of_joi_act = CharField(null=False)
    non_fed_sha_of_joi_act = CharField(null=False)
    non_all_fed_ele_act_par = CharField(null=False)
    tot_fed_ele_act = CharField(null=False)
    fed_can_com_con = CharField(null=False)
    fed_can_con_ref = CharField(null=False)
    ind_exp_mad = CharField(null=False)
    coo_exp_par = CharField(null=False)
    loa_mad = CharField(null=False)
    loa_rep_rec = CharField(null=False)
    tra_to_oth_aut_com = CharField(null=False)
    fun_dis = CharField(null=False)
    off_to_fun_exp_pre = CharField(null=False)
    exe_leg_acc_dis_pre = CharField(null=False)
    off_to_leg_acc_exp_pre = CharField(null=False)
    tot_off_to_ope_exp = CharField(null=False)
    oth_dis = CharField(null=False)
    tot_fed_dis = CharField(null=False)
    tot_dis = CharField(null=False)
    net_con = CharField(null=False)
    net_ope_exp = CharField(null=False)
    cas_on_han_beg_of_per = CharField(null=False)
    cas_on_han_clo_of_per = CharField(null=False)
    deb_owe_by_com = CharField(null=False)
    deb_owe_to_com = CharField(null=False)
    cov_sta_dat = CharField(null=False)
    cov_end_dat = CharField(null=False)
    pol_par_com_ref = CharField(null=False)
    can_id = CharField(null=False)
    cas_on_han_beg_of_yea = CharField(null=False)
    cas_on_han_clo_of_yea = CharField(null=False)
    exp_sub_to_lim_pri_yea_pre = CharField(null=False)
    exp_sub_lim = CharField(null=False)
    fed_fun = CharField(null=False)
    ite_con_exp_con_com = CharField(null=False)
    ite_oth_dis = CharField(null=False)
    ite_oth_inc = CharField(null=False)
    ite_oth_ref_or_reb = CharField(null=False)
    ite_ref_or_reb = CharField(null=False)
    oth_fed_ope_exp = CharField(null=False)
    sub_con_exp = CharField(null=False)
    sub_oth_ref_or_reb = CharField(null=False)
    sub_ref_or_reb = CharField(null=False)
    tot_com_cos = CharField(null=False)
    tot_exp_sub_to_lim_pre = CharField(null=False)
    uni_con_exp = CharField(null=False)
    uni_oth_dis = CharField(null=False)
    uni_oth_inc = CharField(null=False)
    uni_oth_ref_or_reb = CharField(null=False)
    uni_ref_or_reb = CharField(null=False)


# Transaction Type Codes
# http://www.fec.gov/finance/disclosure/metadata/DataDictionaryTransactionTypeCodes.shtml

# Report Type Codes
# http://www.fec.gov/finance/disclosure/metadata/ReportTypeCodes.shtml

# Ammendment ID
# Indicates if the report being filed is new (N), an amendment (A) to a previous report, or a
# termination (T) report.

# Transaction PGI
# This code indicates the election for which the contribution was made. EYYYY (election plus election year)
# P = Primary
# G = General
# O = Other
# C = Convention
# R = Runoff
# S = Special
# E = Recount
