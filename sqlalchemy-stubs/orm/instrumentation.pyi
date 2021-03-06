from typing import Any, Optional

class ClassManager(dict):
    MANAGER_ATTR: Any = ...
    STATE_ATTR: Any = ...
    deferred_scalar_loader: Any = ...
    original_init: Any = ...
    factory: Any = ...
    class_: Any = ...
    info: Any = ...
    new_init: Any = ...
    local_attrs: Any = ...
    originals: Any = ...
    def __init__(self, class_) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    @property
    def is_mapped(self): ...
    def manage(self): ...
    def dispose(self): ...
    def manager_getter(self): ...
    def state_getter(self): ...
    def dict_getter(self): ...
    def instrument_attribute(self, key, inst, propagated: bool = ...): ...
    def subclass_managers(self, recursive): ...
    def post_configure_attribute(self, key): ...
    def uninstrument_attribute(self, key, propagated: bool = ...): ...
    mapper: Any = ...
    def unregister(self): ...
    def install_descriptor(self, key, inst): ...
    def uninstall_descriptor(self, key): ...
    def install_member(self, key, implementation): ...
    def uninstall_member(self, key): ...
    def instrument_collection_class(self, key, collection_class): ...
    def initialize_collection(self, key, state, factory): ...
    def is_instrumented(self, key, search: bool = ...): ...
    def get_impl(self, key): ...
    @property
    def attributes(self): ...
    def new_instance(self, state: Optional[Any] = ...): ...
    def setup_instance(self, instance, state: Optional[Any] = ...): ...
    def teardown_instance(self, instance): ...
    def has_state(self, instance): ...
    def has_parent(self, state, key, optimistic: bool = ...): ...
    def __bool__(self): ...
    __nonzero__: Any = ...

class InstrumentationFactory(object):
    def create_manager_for_cls(self, class_): ...
    def unregister(self, class_): ...

instance_state: Any = ...
instance_dict: Any = ...
manager_of_class: Any = ...

def register_class(class_): ...
def unregister_class(class_): ...
def is_instrumented(instance, key): ...
