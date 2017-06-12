from .general import handlers as general_handlers
from .specialty import handlers as specialty_handlers
from .excursion import handlers as excursion_handlers
from .course import handlers as course_handlers
from .openday import handlers as openday_handlers
from .contacts import handlers as contacts_handlers
from .studorganizations import handlers as studorganizations_handlers
from .about import handlers as about_handlers
from .calculator import handlers as calculator_handlers
from .guide import handlers as guide_handlers

handlers = {}
for i in (general_handlers, specialty_handlers, excursion_handlers, course_handlers, openday_handlers,
          contacts_handlers, studorganizations_handlers, about_handlers, calculator_handlers,guide_handlers):
    handlers.update(i)
