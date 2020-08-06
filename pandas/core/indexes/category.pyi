import numpy as np
#from pandas._config import get_option as get_option
#from pandas._libs.hashtable import duplicated_int64 as duplicated_int64
from pandas._typing import AnyArrayLike as AnyArrayLike, UU
from pandas.core import accessor as accessor
#from pandas.core.algorithms import take_1d as take_1d
#from pandas.core.arrays.categorical import Categorical as Categorical, contains as contains
#from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_categorical_dtype as is_categorical_dtype, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_scalar as is_scalar
#from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
#from pandas.core.dtypes.generic import ABCCategorical as ABCCategorical, ABCSeries as ABCSeries
#from pandas.core.dtypes.missing import isna as isna
from pandas.core.indexes.base import Index as Index #, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.extension import ExtensionIndex as ExtensionIndex
#from pandas.core.indexes.extension import inherit_names as inherit_names
#from pandas.core.ops import get_op_result_name as get_op_result_name
#from pandas.util._decorators import Appender as Appender, cache_readonly as cache_readonly
from typing import Any, Optional, Type, overload


class CategoricalIndex(ExtensionIndex, accessor.PandasDelegate):
    codes: np.ndarray
    categories: Index
    def __new__(cls, data: Optional[Any] = ..., categories: Optional[Any] = ..., ordered: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ..., name: Optional[Any] = ...): ...
    def equals(self, other: Any): ...
    @property
    def inferred_type(self) -> str: ...
    @property
    def values(self): ...
    def __contains__(self, key: Any) -> bool: ...
    def __array__(self, dtype: Any=...) -> np.ndarray: ...
    @overload
    def astype(self, dtype: Type[UU]) -> Index[UU]: ...
    @overload
    def astype(self, dtype: str) -> Index: ...
    def fillna(self, value: Any, downcast: Optional[Any] = ...): ...
    def is_unique(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def unique(self, level: Optional[Any] = ...): ...
    def duplicated(self, keep: str = ...): ...
    def get_loc(self, key: Any, method: Optional[Any] = ...): ...
    def get_value(self, series: AnyArrayLike, key: Any) -> Any: ...
    def where(self, cond: Any, other: Optional[Any] = ...): ...
    def reindex(self, target: Any, method: Optional[Any] = ..., level: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...): ...
    def get_indexer(self, target: Any, method: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...): ...
    def get_indexer_non_unique(self, target: Any): ...
    def take_nd(self, *args: Any, **kwargs: Any): ...
    def map(self, mapper: Any): ...
    def delete(self, loc: Any): ...
    def insert(self, loc: Any, item: Any): ...
