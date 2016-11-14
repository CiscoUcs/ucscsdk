"""This module contains the meta information of OrgGetSubscribedDomains ExternalMethod."""

from ..ucsccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("OrgGetSubscribedDomains", "orgGetSubscribedDomains", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_class_id": MethodPropertyMeta("InClassId", "inClassId", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_domain_group_dn": MethodPropertyMeta("InDomainGroupDn", "inDomainGroupDn", "ReferenceObject", "Version142b", "Input", False),
    "in_subscription_type": MethodPropertyMeta("InSubscriptionType", "inSubscriptionType", "Xs:string", "Version142b", "Input", False),
    "out_subscribed": MethodPropertyMeta("OutSubscribed", "outSubscribed", "ConfigSet", "Version142b", "Output", True),
    "out_unsubscribed": MethodPropertyMeta("OutUnsubscribed", "outUnsubscribed", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inClassId": "in_class_id",
    "inDomainGroupDn": "in_domain_group_dn",
    "inSubscriptionType": "in_subscription_type",
    "outSubscribed": "out_subscribed",
    "outUnsubscribed": "out_unsubscribed",
}

