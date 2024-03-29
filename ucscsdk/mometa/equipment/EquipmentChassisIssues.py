"""This module contains the general information for EquipmentChassisIssues ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class EquipmentChassisIssuesConsts():
    pass


class EquipmentChassisIssues(ManagedObject):
    """This is EquipmentChassisIssues class."""

    consts = EquipmentChassisIssuesConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentChassisIssues", "equipmentChassisIssues", "config-issue", VersionMeta.Version151a, "InputOutput", 0xf, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy"], ['equipmentChassisProfile', 'equipmentInstance'], [], ["Get"])

    prop_meta = {
        "chassis_config_issues": MoPropertyMeta("chassis_config_issues", "chassisConfigIssues", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|chassis-profile-not-supported|migration|firmware-version-mismatch|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|physical-requirement|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|compute-conn-unsupported-cmc-version|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|compute-second-controller-unsupported-cmc-version|insufficient-power-budget),){0,18}(defaultValue|not-applicable|chassis-profile-not-supported|migration|firmware-version-mismatch|non-interrupt-fsm-running|insufficient-resources|compute-conn-invalid-hw-config|physical-requirement|chassis-undiscovered|chassis-feature-capability-mismatch|resource-ownership-conflict|compute-conn-unsupported-cmc-version|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|chassis-feature-capability-mismatch-non-fatal|compute-second-controller-unsupported-cmc-version|insufficient-power-budget){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_warnings": MoPropertyMeta("config_warnings", "configWarnings", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable),){0,1}(defaultValue|not-applicable){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_config_issues": MoPropertyMeta("storage_config_issues", "storageConfigIssues", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|incomplete-drive-security-config|cimc-mgmt-not-configured|multiple-security-policies|sed-unsupported-server|jbod-disk-used-for-luns|no-deployed-key|bmc-certs-absent|flexflash-metadata|unsupported-disk-controller-config|unsupported-expand-to-available|unsupported-use-remaining-disks|unsupported-strip-size-change|zone-capacity|duplicated-lun-name|unsupported-hotspare-change|unsupported-vd-modification|invalid-disk-slot-ownership|disk-role-mismatch|missing-raid-key|orphaned-lun-ref-missing|virtual-drive-access-denied|unsupported-disk-slot-zoning|destructive-local-disk-config|storage-feature-capability-mismatch|insufficient-disks|conflicting-lun-config|unsupported-global-hotspares|drive-cache-not-supported|unsupported-chassis-disk-zoning|flexflash-controller|unsupported-controller|invalid-storage-profile-binding|lun-in-use|disk-sharing-not-supported|incompatible-disk-types|storage-path-configuration-error|disk-type-mismatch|orphaned-lun-ref-access-denied|virtual-drive-deletion-in-progress|unsupported-partial-disk-group-zoning|virtual-drive-hidden-or-transport-ready|unsupported-raid-level|incomplete-lun-config|unsupported-order|embedded-controller-not-supported|unsupported-security-operation|incompatible-number-of-local-disks|flexflash-card|unsupported-destructive-change|invalid-local-lun-disk-policy-reference|set-proper-order|unsupported-chassis-spare-controller|wwnn-assignment|unsupported-orphan-lun-modification|unsupported-lun-map-modification|unsupported-write-cache-policy|invalid-zoning-virtual-drive-state|invalid-zoning-disk-bootable|insufficient-storage-space|order-should-be-unique|virtual-drive-capacity|incompatible-raid-level|invalid-dzp-reference),){0,64}(defaultValue|not-applicable|incomplete-drive-security-config|cimc-mgmt-not-configured|multiple-security-policies|sed-unsupported-server|jbod-disk-used-for-luns|no-deployed-key|bmc-certs-absent|flexflash-metadata|unsupported-disk-controller-config|unsupported-expand-to-available|unsupported-use-remaining-disks|unsupported-strip-size-change|zone-capacity|duplicated-lun-name|unsupported-hotspare-change|unsupported-vd-modification|invalid-disk-slot-ownership|disk-role-mismatch|missing-raid-key|orphaned-lun-ref-missing|virtual-drive-access-denied|unsupported-disk-slot-zoning|destructive-local-disk-config|storage-feature-capability-mismatch|insufficient-disks|conflicting-lun-config|unsupported-global-hotspares|drive-cache-not-supported|unsupported-chassis-disk-zoning|flexflash-controller|unsupported-controller|invalid-storage-profile-binding|lun-in-use|disk-sharing-not-supported|incompatible-disk-types|storage-path-configuration-error|disk-type-mismatch|orphaned-lun-ref-access-denied|virtual-drive-deletion-in-progress|unsupported-partial-disk-group-zoning|virtual-drive-hidden-or-transport-ready|unsupported-raid-level|incomplete-lun-config|unsupported-order|embedded-controller-not-supported|unsupported-security-operation|incompatible-number-of-local-disks|flexflash-card|unsupported-destructive-change|invalid-local-lun-disk-policy-reference|set-proper-order|unsupported-chassis-spare-controller|wwnn-assignment|unsupported-orphan-lun-modification|unsupported-lun-map-modification|unsupported-write-cache-policy|invalid-zoning-virtual-drive-state|invalid-zoning-disk-bootable|insufficient-storage-space|order-should-be-unique|virtual-drive-capacity|incompatible-raid-level|invalid-dzp-reference){0,1}""", [], []), 
    }

    prop_map = {
        "chassisConfigIssues": "chassis_config_issues", 
        "childAction": "child_action", 
        "configWarnings": "config_warnings", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "storageConfigIssues": "storage_config_issues", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.chassis_config_issues = None
        self.child_action = None
        self.config_warnings = None
        self.status = None
        self.storage_config_issues = None

        ManagedObject.__init__(self, "EquipmentChassisIssues", parent_mo_or_dn, **kwargs)

