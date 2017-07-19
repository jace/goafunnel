#!/usr/bin/env python

from coaster.manage import init_manager

import funnel
import funnel.models as models
import funnel.forms as forms
import funnel.views as views
from funnel.models import db
from funnel import app


if __name__ == '__main__':
    db.init_app(app)
    manager = init_manager(app, db, funnel=funnel, models=models, forms=forms, views=views)
    manager.run()
