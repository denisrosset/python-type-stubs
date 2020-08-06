import numpy as np
from pandas._libs.indexing import _NDFrameIndexerBase
#from pandas._libs.lib import item_from_zerodim as item_from_zerodim
#from pandas.core.dtypes.common import is_float as is_float, is_integer as is_integer, is_iterator as is_iterator, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_sequence as is_sequence
#from pandas.core.dtypes.concat import concat_compat as concat_compat
##from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries
#from pandas.core.dtypes.missing import isna as isna
#from pandas.core.indexers import check_array_indexer as check_array_indexer, is_list_like_indexer as is_list_like_indexer, length_of_indexer as length_of_indexer
from pandas.core.indexes.api import Index as Index
# , InvalidIndexError as InvalidIndexError
#from pandas.errors import AbstractMethodError as AbstractMethodError
#from pandas.util._decorators import Appender as Appender
from typing import Any, Optional

class _IndexSlice:
    def __getitem__(self, arg: Any): ...

IndexSlice: Any

class IndexingError(Exception): ...

class IndexingMixin:
    @property
    def iloc(self) -> _iLocIndexer: ...
    @property
    def loc(self) -> _LocIndexer: ...
    @property
    def at(self) -> _AtIndexer: ...
    @property
    def iat(self) -> _iAtIndexer: ...

class _NDFrameIndexer(_NDFrameIndexerBase):
    axis: Any = ...
    def __call__(self, axis: Optional[Any] = ...): ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...

class _LocationIndexer(_NDFrameIndexer):
    def __getitem__(self, key: Any): ...

class _LocIndexer(_LocationIndexer): ...
class _iLocIndexer(_LocationIndexer): ...

class _ScalarAccessIndexer(_NDFrameIndexerBase):
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...

class _AtIndexer(_ScalarAccessIndexer): ...
class _iAtIndexer(_ScalarAccessIndexer): ...

def convert_to_index_sliceable(obj: Any, key: Any): ...
def check_bool_indexer(index: Index, key: Any) -> np.ndarray: ...
def convert_missing_indexer(indexer: Any): ...
def convert_from_missing_indexer_tuple(indexer: Any, axes: Any): ...
def maybe_convert_ix(*args: Any): ...
def is_nested_tuple(tup: Any, labels: Any) -> bool: ...
def is_label_like(key: Any) -> bool: ...
def need_slice(obj: Any) -> bool: ...
