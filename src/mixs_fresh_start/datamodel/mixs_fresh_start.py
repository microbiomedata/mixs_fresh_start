# Auto generated from mixs_fresh_start.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-13T12:41:14
# Schema: mixs_fresh_start
#
# id: https://w3id.org/microbiomedata/mixs_fresh_start
# description: copy from github
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
TEMP = CurieNamespace('TEMP', 'https://example.org/TEMP/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIXS_FRESH_START = CurieNamespace('mixs_fresh_start', 'https://w3id.org/microbiomedata/mixs_fresh_start/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MIXS_FRESH_START


# Types

# Class references



@dataclass
class Biosample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Biosample
    class_class_curie: ClassVar[str] = "TEMP:Biosample"
    class_name: ClassVar[str] = "Biosample"
    class_model_uri: ClassVar[URIRef] = MIXS_FRESH_START.Biosample

    depth: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.depth is not None and not isinstance(self.depth, QuantityValue):
            self.depth = QuantityValue(**as_dict(self.depth))

        super().__post_init__(**kwargs)


@dataclass
class QuantityValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.QuantityValue
    class_class_curie: ClassVar[str] = "TEMP:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = MIXS_FRESH_START.QuantityValue

    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.depth = Slot(uri=TEMP.depth, name="depth", curie=TEMP.curie('depth'),
                   model_uri=MIXS_FRESH_START.depth, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=TEMP.has_raw_value, name="has_raw_value", curie=TEMP.curie('has_raw_value'),
                   model_uri=MIXS_FRESH_START.has_raw_value, domain=None, range=Optional[str])

slots.Biosample_depth = Slot(uri=TEMP.depth, name="Biosample_depth", curie=TEMP.curie('depth'),
                   model_uri=MIXS_FRESH_START.Biosample_depth, domain=Biosample, range=Optional[Union[dict, "QuantityValue"]])

slots.QuantityValue_has_raw_value = Slot(uri=TEMP.has_raw_value, name="QuantityValue_has_raw_value", curie=TEMP.curie('has_raw_value'),
                   model_uri=MIXS_FRESH_START.QuantityValue_has_raw_value, domain=QuantityValue, range=Optional[str])